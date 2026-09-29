# Spec: Open A Docs Review For Each Upstream Release

Status: Development

Purpose: Make every production release of skm or Workspace open a tracking
issue in this registry, so the registry and site documentation are reviewed
against what users can install.

## 1. Problem Statement

The registry README, `VERSIONING.md`, `SKILL_STRUCTURE.md`,
`docs/namespaces/` and the skills-yaml.tech site describe skm commands and
Workspace packages. Both ship independently, and nothing tells this
repository when they change. On 2026-09-25 the site still documented removed
commands (`skm search --add`, `skm workspace`) and a flag that never existed
(`skm add --version`); on 2026-09-26 skm 0.8.0 and Workspace toolkit 0.5.0
were both released without any documentation follow-up.

## 2. Goals and Non-Goals

### Goals

- One issue per skm production version and per Workspace toolkit version,
  labeled `docs-review`, with a checklist of the documents to review.
- For skm, show exactly what changed: a diff of the complete `--help` tree of
  the released binary against the last reviewed snapshot.
- For Workspace, list the toolkit version change and every package version
  change.
- Idempotent: repeated triggers never open a second issue for a version.

### Non-Goals

- Editing documentation automatically. A person reviews and updates it.
- Reacting to skm `development` pre-releases or Workspace source commits that
  are not published here.
- Changing how either upstream builds or publishes.

## 3. Design

`.github/workflows/upstream-release.yml`, backed by
`scripts/upstream_release.py`:

- **skm.** Runs on a `skm-released` `repository_dispatch` sent by skm's
  release workflow after a production release, hourly as a fallback, and on
  manual dispatch. The payload is only a wake-up: the job reads
  `skm-release.json` from `prod-latest`, requires `channel: prod`, verifies the
  Linux archive's SHA-256 and the binary's `--version`, and skips if an issue
  titled `Docs review: skm <version>` exists in any state. Otherwise it
  captures every help page with the update notice suppressed, uploads it as
  the `skm-cli.txt` artifact, and opens the issue with a unified diff against
  `docs/upstream/skm-cli.txt` (truncated at 400 lines).
- **Workspace.** Runs on pushes to `main` that change
  `skills/workspace/manifest.yaml`, which is when a Workspace release becomes
  installable. It compares the manifest before and after the push and opens
  `Docs review: Workspace toolkit <version>` only when `toolkit_version`
  changed.
- **Snapshot.** `docs/upstream/skm-cli.txt` records the help of the skm
  version the docs were last reviewed against. Closing a review includes
  replacing it with the artifact from the issue's run. The initial snapshot is
  skm 0.7.0, built from `44a502a`, because the docs were last reviewed
  against 0.7.0.

The job uses only the workflow's own token with `issues: write`. skm needs the
`workspace-registry-publisher` GitHub App credentials to send the dispatch;
without them the hourly fallback still opens the issue.

## 4. Verification and Acceptance Criteria

- [x] The help capture is complete, depth-first, deterministic, and excludes
      `help` pages and the update notice (fake-binary tests).
- [x] Against the published 0.8.0 binary and the 0.7.0 snapshot, the rendered
      issue shows the changed `--yes` help for `add` and `install`.
- [x] Against the registry's real 0.4.2 → 0.5.0 manifest change, the Workspace
      issue lists the version change and each changed package; an unchanged
      toolkit version renders nothing.
- [x] Invalid versions and commit hashes are rejected before rendering.
- [x] The release-reading step runs against the live `prod-latest` release,
      verifying checksum and version.
- [x] `actionlint`, `task check` and `task test` pass.
- [ ] After merge to `main`, a manual run opens `Docs review: skm 0.8.0` and a
      second run opens nothing.
- [ ] skm sends `skm-released` after its next production release.

## 5. Integration And Release

Pending.

## 6. Risks and Mitigations

- *Risk*: The dispatch from skm is never configured or fails.
  *Mitigation*: The hourly poll opens the same issue within an hour.
- *Risk*: The snapshot is not refreshed, so later diffs include changes that
  were already reviewed.
  *Mitigation*: The issue checklist includes refreshing it, and the snapshot
  header names the version it describes.
- *Risk*: The first Workspace push to `main` after this merges reports a
  version that was already reviewed.
  *Mitigation*: Close it as a duplicate; issues are keyed by version.
