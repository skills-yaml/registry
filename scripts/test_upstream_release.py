import json
import os
import stat
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import upstream_release  # noqa: E402

SCRIPT = Path(__file__).resolve().parent / "upstream_release.py"

FAKE_SKM = textwrap.dedent('''\
    #!/usr/bin/env python3
    import os, sys
    if os.environ.get("SKM_NO_UPDATE_CHECK") != "1":
        print("update available", file=sys.stderr)
    args = [a for a in sys.argv[1:] if a != "--help"]
    if sys.argv[1:] == ["--version"]:
        print("skm 9.9.9"); sys.exit(0)
    pages = {
        (): "Usage: skm <COMMAND>\\n\\nCommands:\\n  add    Add a skill\\n  dev    Local skills\\n  help   Print help\\n\\nOptions:\\n  -h, --help  Print help   ",
        ("add",): "Usage: skm add <NAME>\\n\\nOptions:\\n  --yes  Apply",
        ("dev",): "Usage: skm dev <COMMAND>\\n\\nCommands:\\n  link   Link a folder\\n  help   Print help",
        ("dev", "link"): "Usage: skm dev link <PATH>",
    }
    if tuple(args) not in pages:
        sys.exit(2)
    print(pages[tuple(args)])
''')

MANIFEST = textwrap.dedent('''\
    schema_version: 2
    namespace: workspace
    toolkit_version: "{toolkit}"
    source_revision: "abc"
    minimum_skm_version: "0.7.0"
    workspace_docs_compatibility: "6.x"
    packages:
      wk-spec: "{spec}"
      write-spec: "0.3.0"
    bundles:
      all-workspace-skills:
        packages:
          - wk-spec
          - write-spec
''')


class CaptureTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.binary = Path(self.directory.name) / "skm"
        self.binary.write_text(FAKE_SKM, encoding="utf-8")
        self.binary.chmod(self.binary.stat().st_mode | stat.S_IEXEC)

    def tearDown(self):
        self.directory.cleanup()

    def test_captures_every_page_depth_first_without_help_or_trailing_spaces(self):
        text = upstream_release.capture_cli(str(self.binary))
        headings = [line for line in text.splitlines() if line.startswith("#")]
        self.assertEqual(headings, ["# skm 9.9.9", "## skm", "## skm add", "## skm dev", "## skm dev link"])
        self.assertNotIn("skm help", text)
        self.assertFalse(any(line != line.rstrip() for line in text.splitlines()))

    def test_capture_is_deterministic(self):
        self.assertEqual(
            upstream_release.capture_cli(str(self.binary)),
            upstream_release.capture_cli(str(self.binary)),
        )


class SkmIssueTest(unittest.TestCase):
    ARGS = ("1.2.0", "a" * 40, "https://example.test/release")

    def test_diff_against_the_reviewed_snapshot(self):
        issue = upstream_release.skm_issue(*self.ARGS, "# skm 1.1.0\n\nold flag\n", "# skm 1.2.0\n\nnew flag\n", "RUN")
        self.assertEqual(issue["title"], "Docs review: skm 1.2.0")
        self.assertIn("reviewed snapshot (skm 1.1.0)", issue["body"])
        self.assertIn("-old flag", issue["body"])
        self.assertIn("+new flag", issue["body"])
        self.assertIn("artifact of RUN", issue["body"])

    def test_unchanged_help_still_asks_for_a_review(self):
        issue = upstream_release.skm_issue(*self.ARGS, "same\n", "same\n", "RUN")
        self.assertIn("unchanged", issue["body"])
        self.assertIn("- [ ] registry `VERSIONING.md`", issue["body"])

    def test_long_diffs_are_truncated(self):
        old = "\n".join(f"old {n}" for n in range(1000))
        new = "\n".join(f"new {n}" for n in range(1000))
        body = upstream_release.skm_issue(*self.ARGS, old, new, "RUN")["body"]
        self.assertIn("more lines", body)
        self.assertLess(len(body), 60000)

    def test_rejects_unexpected_versions_and_commits(self):
        for version, commit in (("latest", "a" * 40), ("1.2.0", "abc"), ("1.2.0; rm -rf /", "a" * 40)):
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), "skm-issue", "--version", version, "--commit", commit,
                 "--release-url", "u", "--captured", "/dev/null", "--run-url", "r"],
                capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0, (version, commit))
            self.assertEqual(result.stdout, "")


class WorkspaceIssueTest(unittest.TestCase):
    def test_toolkit_bump_lists_changed_packages(self):
        issue = upstream_release.workspace_issue(
            MANIFEST.format(toolkit="0.4.0", spec="0.2.0"),
            MANIFEST.format(toolkit="0.5.0", spec="0.2.1"),
            "c" * 40, "skills-yaml/registry",
        )
        self.assertEqual(issue["title"], "Docs review: Workspace toolkit 0.5.0")
        self.assertIn("previously 0.4.0", issue["body"])
        self.assertIn("| `workspace/wk-spec` | 0.2.0 | 0.2.1 |", issue["body"])
        self.assertNotIn("write-spec` |", issue["body"])
        self.assertIn("Packages: 2 → 2", issue["body"])

    def test_same_toolkit_version_opens_nothing(self):
        text = MANIFEST.format(toolkit="0.5.0", spec="0.2.1")
        self.assertIsNone(upstream_release.workspace_issue(text, text, "c" * 40, "r"))

    def test_first_publication_has_no_previous_version(self):
        issue = upstream_release.workspace_issue("", MANIFEST.format(toolkit="0.1.0", spec="0.1.0"), "c" * 40, "r")
        self.assertIn("previously none", issue["body"])

    def test_cli_prints_nothing_when_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.yaml"
            path.write_text(MANIFEST.format(toolkit="0.5.0", spec="0.2.1"), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), "workspace", "--old", str(path), "--new", str(path), "--commit", "c" * 40],
                capture_output=True, text=True, check=True,
            )
            self.assertEqual(result.stdout, "")

    def test_cli_emits_json(self):
        with tempfile.TemporaryDirectory() as directory:
            old, new = Path(directory) / "old.yaml", Path(directory) / "new.yaml"
            old.write_text(MANIFEST.format(toolkit="0.4.0", spec="0.2.0"), encoding="utf-8")
            new.write_text(MANIFEST.format(toolkit="0.5.0", spec="0.2.1"), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-B", str(SCRIPT), "workspace", "--old", str(old), "--new", str(new), "--commit", "c" * 40],
                capture_output=True, text=True, check=True,
            )
            self.assertEqual(json.loads(result.stdout)["title"], "Docs review: Workspace toolkit 0.5.0")


if __name__ == "__main__":
    unittest.main()
