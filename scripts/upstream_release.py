#!/usr/bin/env python3
"""Turn an upstream release into a documentation review issue.

skm and Workspace ship independently of this registry, but the registry
README, VERSIONING.md, SKILL_STRUCTURE.md, docs/namespaces/ and the
skills-yaml.tech site describe their commands and packages. This script
prepares the tracking issue the `Upstream Release` workflow opens when either
one publishes a production release.

  skm-cli      capture the complete `--help` tree of an skm binary
  skm-issue    render the issue for an skm release, with a help diff against
               the reviewed snapshot in docs/upstream/skm-cli.txt
  workspace    compare two Workspace manifests; print nothing when the
               toolkit version is unchanged, otherwise render the issue

Output is a JSON object {"title": ..., "body": ...} on stdout, so the workflow
never has to assemble Markdown in shell.
"""

import argparse
import difflib
import json
import os
import re
import subprocess
import sys

SNAPSHOT = "docs/upstream/skm-cli.txt"
COMMAND_LINE = re.compile(r"^  ([a-z][a-z0-9-]*)\s{2,}\S")
MAX_DIFF_LINES = 400

SKM_DOCS = (
    "registry `README.md` (bundles, search, adding skills)",
    "registry `VERSIONING.md` (version management with skm)",
    "registry `SKILL_STRUCTURE.md` (testing a skill locally)",
    "registry `docs/namespaces/*.md`",
    "site `index.html` command table and its skm version caption",
    "site `guide.html` commands and the skm version it is written for",
)
WORKSPACE_DOCS = (
    "registry `docs/namespaces/workspace.md` (package count, facades, examples)",
    "registry `README.md` Workspace entry and Bundles section",
    "site `guide.html` notes on the `workspace` namespace",
)


def run_help(binary, path):
    env = dict(os.environ, SKM_NO_UPDATE_CHECK="1", NO_COLOR="1", COLUMNS="100", TERM="dumb")
    result = subprocess.run(
        [binary, *path, "--help"],
        capture_output=True,
        text=True,
        env=env,
        stdin=subprocess.DEVNULL,
        timeout=30,
        check=False,
    )
    if result.returncode != 0:
        sys.exit(f"`skm {' '.join(path)} --help` exited with {result.returncode}: {result.stderr.strip()}")
    return "\n".join(line.rstrip() for line in result.stdout.strip().splitlines())


def subcommands(help_text):
    names, inside = [], False
    for line in help_text.splitlines():
        if line.rstrip() == "Commands:":
            inside = True
            continue
        if inside:
            if not line.strip():
                break
            match = COMMAND_LINE.match(line)
            if match and match.group(1) != "help":
                names.append(match.group(1))
    return names


def capture_cli(binary):
    """Return every help page, depth first, as one stable text document."""
    version = subprocess.run(
        [binary, "--version"], capture_output=True, text=True, check=True, timeout=30,
        env=dict(os.environ, SKM_NO_UPDATE_CHECK="1"), stdin=subprocess.DEVNULL,
    ).stdout.strip()
    sections, queue = [], [[]]
    while queue:
        path = queue.pop(0)
        text = run_help(binary, path)
        sections.append(f"## skm {' '.join(path)}".rstrip() + f"\n\n{text}\n")
        queue[0:0] = [path + [name] for name in subcommands(text)]
    return f"# {version}\n\n" + "\n".join(sections)


def help_diff(old, new):
    diff = list(difflib.unified_diff(
        old.splitlines(), new.splitlines(), "reviewed", "released", lineterm="", n=2,
    ))
    if len(diff) > MAX_DIFF_LINES:
        omitted = len(diff) - MAX_DIFF_LINES
        diff = diff[:MAX_DIFF_LINES] + [f"... {omitted} more lines; run the snapshot command below to see all of them"]
    return "\n".join(diff)


def checklist(items):
    return "\n".join(f"- [ ] {item}" for item in items)


def skm_issue(version, commit, release_url, snapshot, captured, run_url):
    reviewed = snapshot.splitlines()[0].removeprefix("# ").strip() if snapshot else "none"
    diff = help_diff(snapshot, captured)
    changes = (
        f"Command help changed since the reviewed snapshot ({reviewed}):\n\n```diff\n{diff}\n```"
        if diff
        else f"Command help is unchanged since the reviewed snapshot ({reviewed}). Check the release for behavior changes that help text does not show."
    )
    body = f"""skm {version} was published to the production channel.

- Release: {release_url}
- Commit: `{commit}`

{changes}

### Update the documentation

{checklist(SKM_DOCS)}
- [ ] Replace `{SNAPSHOT}` with the `skm-cli.txt` artifact of {run_url}, so the
      next release diffs against this one. It was captured from the released binary.

Close this issue when the registry change is released through `main` and the site is deployed.
"""
    return {"title": f"Docs review: skm {version}", "body": body}


def parse_manifest(text):
    """Read the scalar fields and `packages` map of a namespace manifest."""
    fields, packages, section = {}, {}, None
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            key, _, value = line.partition(":")
            section = key.strip()
            if value.strip():
                fields[section] = value.strip().strip("\"'")
        elif section == "packages" and line.startswith("  ") and not line.startswith("   "):
            name, _, value = line.strip().partition(":")
            packages[name.strip()] = value.strip().strip("\"'")
    return fields, packages


def workspace_issue(old_text, new_text, commit, repository):
    old_fields, old_packages = parse_manifest(old_text)
    new_fields, new_packages = parse_manifest(new_text)
    old_version = old_fields.get("toolkit_version", "none")
    new_version = new_fields.get("toolkit_version")
    if not new_version or new_version == old_version:
        return None
    rows = []
    for name in sorted(set(old_packages) | set(new_packages)):
        before, after = old_packages.get(name, "—"), new_packages.get(name, "removed")
        if before != after:
            rows.append(f"| `workspace/{name}` | {before} | {after} |")
    table = "\n".join(["| Package | Before | After |", "| --- | --- | --- |", *rows]) if rows else "No package versions changed."
    body = f"""Workspace toolkit {new_version} was published to this registry's `main` branch (previously {old_version}).

- Registry commit: https://github.com/{repository}/commit/{commit}
- Source revision: `{new_fields.get('source_revision', 'unknown')}`
- Minimum skm: {new_fields.get('minimum_skm_version', 'unknown')}
- Workspace Docs compatibility: {new_fields.get('workspace_docs_compatibility', 'unknown')}
- Packages: {len(old_packages)} → {len(new_packages)}

{table}

### Update the documentation

{checklist(WORKSPACE_DOCS)}

Close this issue when the registry change is released through `main` and the site is deployed.
"""
    return {"title": f"Docs review: Workspace toolkit {new_version}", "body": body}


def read(path):
    if not path or not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)

    cli = commands.add_parser("skm-cli")
    cli.add_argument("--binary", required=True)

    skm = commands.add_parser("skm-issue")
    skm.add_argument("--version", required=True)
    skm.add_argument("--commit", required=True)
    skm.add_argument("--release-url", required=True)
    skm.add_argument("--captured", required=True, help="output of skm-cli for the released binary")
    skm.add_argument("--snapshot", default=SNAPSHOT)
    skm.add_argument("--run-url", required=True, help="workflow run that captured the help")

    workspace = commands.add_parser("workspace")
    workspace.add_argument("--old", required=True, help="manifest before the push; may be missing")
    workspace.add_argument("--new", required=True)
    workspace.add_argument("--commit", required=True)
    workspace.add_argument("--repository", default="skills-yaml/registry")

    args = parser.parse_args()
    if args.command == "skm-cli":
        sys.stdout.write(capture_cli(args.binary))
        return
    if args.command == "skm-issue":
        if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", args.version):
            sys.exit(f"not a release version: {args.version!r}")
        if not re.fullmatch(r"[0-9a-f]{40}", args.commit):
            sys.exit(f"not a full commit hash: {args.commit!r}")
        issue = skm_issue(args.version, args.commit, args.release_url, read(args.snapshot), read(args.captured), args.run_url)
    else:
        issue = workspace_issue(read(args.old), read(args.new), args.commit, args.repository)
    if issue:
        json.dump(issue, sys.stdout)


if __name__ == "__main__":
    main()
