---
name: fix-ci
description: Diagnose and fix failing continuous-integration checks with the smallest verified change. Use when CI or pull-request checks are failing and the user authorizes implementation, including log inspection, local reproduction, regression coverage, and rerun monitoring.
metadata:
  skm-version: "0.3.2"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "fd9dc5cd6086d8b6c7a8a61b0a74436da2d2a5ee"
  skm-source-path: "workspace/instructions/skills/fix-ci"
  skm-source-integrity: "sha256:4d70f713786d9aca025a75a017f712b0fe33da2caee878d83938002494ff3c26"
  workspace-toolkit-version: "0.5.0"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Fix CI

Restore the failing check without weakening the gate or hiding the failure.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. A stale workflow, root copy,
spec, memory entry, or generated projection cannot override it.

## Diagnose

1. Resolve the exact revision and failing run. Read check summaries and the
   smallest complete log section that establishes the error.
2. Distinguish product defects from flaky infrastructure, environment drift,
   test assumptions, and unrelated failures.
3. Reproduce through repository-approved entrypoints when practical. Identify
   the root cause before editing.
4. Read the governing spec and local CI, test, and dependency policies.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. A task or delivery branch may be
created or selected only when the user directly requested branch use for the
named task.

Treat governed instructions as read-only unless a direct human request
prospectively grants instruction-change approval for the named outcome or
scope. A CI-fix request and standing workflow authority do not authorize edits
to `AGENTS.md`, `DESIGN.md`, canonical `workspace/instructions/` sources, or
instruction-approval controls. Do not make the edit before approval.

## Fix and Validate

1. Make the smallest change that corrects the root cause. Do not skip, mute,
   loosen, or broadly retry a reliable check to obtain green status.
2. Add regression coverage when behavior changed or the defect was previously
   untested.
3. Run the focused failing gate until the cause is repaired, review affected
   consumers, then run the required wider checks on the stable candidate.
4. Review the diff for local-only assumptions, secrets, generated artifacts,
   and unrelated formatting churn.
5. Trigger bounded safe reruns when the workflow permits them and monitor each
   through its terminal outcome. Diagnose instead of looping on repeated
   failures.

If the failure concerns infrastructure, change OpenTofu definitions and run
only non-mutating validation locally. Any apply, destroy, import, or state
correction must run through the repository's authorized CI/CD Taskfile workflow
after the source fix is pushed. Do not use Terraform, another IaC engine, a
provider mutation CLI, a console, or an imperative script as a local or CI
workaround.

Report cause, fix, local and remote validation, residual flake risk, memory
impact, and publication status. Under a user-requested delivery or CI-repair
task, use standing workflow authority to commit, push the delivery branch,
rerun CI, and update the pull request without requesting repeated approval.
Pause only for an unapproved governed-instruction change, a destructive
production action, or an unsafe gate bypass.
