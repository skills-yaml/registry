#!/usr/bin/env python3
"""Tests for the namespace manifest generator."""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_manifests  # noqa: E402
from validate_registry import RegistryValidator  # noqa: E402


class GenerateManifestsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "skills").mkdir()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def package(self, namespace: str, skill_id: str, version: str = "1.0.0") -> None:
        content = (
            f"---\nname: {skill_id}\n"
            f"description: Exercise the {skill_id} fixture.\n"
            f'metadata:\n  skm-version: "{version}"\n---\n\n# {skill_id}\n'
        )
        package = self.root / "skills" / namespace / skill_id
        (package / f"v{version}").mkdir(parents=True)
        (package / f"v{version}" / "SKILL.md").write_text(content, encoding="utf-8")
        (package / "SKILL.md").write_text(content, encoding="utf-8")
        (package / "latest").symlink_to(f"v{version}")
        (package / "default").symlink_to(f"v{version}")

    def manifest(self, namespace: str) -> Path:
        return self.root / "skills" / namespace / "manifest.yaml"

    def run_generator(self, *args: str) -> tuple[int, str]:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = generate_manifests.main(["--root", str(self.root), *args])
        return code, out.getvalue() + err.getvalue()

    def test_fills_packages_from_latest_aliases(self) -> None:
        self.package("tools", "beta", "0.2.0")
        self.package("tools", "alpha", "1.3.0")
        self.manifest("tools").write_text(
            "bundles:\n  pair:\n    packages: [beta, alpha]\n", encoding="utf-8"
        )
        code, _ = self.run_generator()
        self.assertEqual(code, 0)
        text = self.manifest("tools").read_text(encoding="utf-8")
        self.assertIn('packages:\n  alpha: "1.3.0"\n  beta: "0.2.0"\n', text)
        self.assertIn("      - alpha\n      - beta\n", text)

    def test_generated_manifest_passes_the_validator(self) -> None:
        self.package("tools", "alpha")
        self.package("tools", "beta")
        self.manifest("tools").write_text(
            "bundles:\n  pair:\n    packages: [alpha, beta]\n", encoding="utf-8"
        )
        self.run_generator()
        errors = RegistryValidator(self.root).validate()
        self.assertEqual(errors, [])

    def test_is_idempotent_and_check_reports_stale_files(self) -> None:
        self.package("tools", "alpha")
        self.manifest("tools").write_text("bundles:\n  one:\n    packages: [alpha]\n", encoding="utf-8")
        code, output = self.run_generator("--check")
        self.assertEqual(code, 1)
        self.assertIn("stale: skills/tools/manifest.yaml", output)
        self.run_generator()
        before = self.manifest("tools").read_text(encoding="utf-8")
        code, _ = self.run_generator("--check")
        self.assertEqual(code, 0)
        self.run_generator()
        self.assertEqual(self.manifest("tools").read_text(encoding="utf-8"), before)

    def test_updates_the_inventory_after_a_new_release(self) -> None:
        self.package("tools", "alpha", "1.0.0")
        self.manifest("tools").write_text("bundles:\n  one:\n    packages: [alpha]\n", encoding="utf-8")
        self.run_generator()
        package = self.root / "skills" / "tools" / "alpha"
        (package / "v1.1.0").mkdir()
        (package / "v1.1.0" / "SKILL.md").write_text(
            (package / "v1.0.0" / "SKILL.md").read_text(encoding="utf-8").replace("1.0.0", "1.1.0"),
            encoding="utf-8",
        )
        (package / "latest").unlink()
        (package / "latest").symlink_to("v1.1.0")
        self.run_generator()
        self.assertIn('alpha: "1.1.0"', self.manifest("tools").read_text(encoding="utf-8"))

    def test_rejects_a_bundle_member_that_is_not_published(self) -> None:
        self.package("tools", "alpha")
        original = "bundles:\n  one:\n    packages: [alpha, ghost]\n"
        self.manifest("tools").write_text(original, encoding="utf-8")
        code, output = self.run_generator()
        self.assertEqual(code, 2)
        self.assertIn("not published: ghost", output)
        self.assertEqual(self.manifest("tools").read_text(encoding="utf-8"), original)

    def test_rejects_unknown_fields(self) -> None:
        self.package("tools", "alpha")
        self.manifest("tools").write_text("toolkit_version: '1.0.0'\n", encoding="utf-8")
        code, output = self.run_generator()
        self.assertEqual(code, 2)
        self.assertIn("unknown fields: toolkit_version", output)

    def test_leaves_workspace_and_namespaces_without_a_manifest_alone(self) -> None:
        self.package("workspace", "alpha")
        self.package("tools", "beta")
        original = "schema_version: 1\nnamespace: workspace\npackages:\n  alpha: 1.0.0\n"
        self.manifest("workspace").write_text(original, encoding="utf-8")
        code, _ = self.run_generator()
        self.assertEqual(code, 0)
        self.assertEqual(self.manifest("workspace").read_text(encoding="utf-8"), original)
        self.assertFalse(self.manifest("tools").exists())


if __name__ == "__main__":
    unittest.main()
