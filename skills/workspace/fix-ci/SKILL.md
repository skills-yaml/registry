---
name: fix-ci
description: Diagnose and fix failing continuous-integration checks with the smallest verified change. Use when CI or pull-request checks are failing and the user authorizes implementation, including log inspection, local reproduction, regression coverage, and rerun monitoring.
metadata:
  skm-version: "0.2.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "fb4aa64a6121f1f8a57d4848b52fa0ec7cefd452"
  skm-source-path: "workspace/instructions/skills/fix-ci"
  skm-source-integrity: "sha256:5eae3fdeb1a944ce33781478ce557beea3a6c7bf2176fd0b74beaf654292b714"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
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
3. Run the focused failing gate and the required wider checks.
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
