---
name: fix-ci
description: Diagnose and fix failing continuous-integration checks with the smallest verified change. Use when CI or pull-request checks are failing and the user authorizes implementation, including log inspection, local reproduction, regression coverage, and rerun monitoring.
metadata:
  skm-version: "0.4.2"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3bf955b7b41193e3e124e4b62757b71eac46228e"
  skm-source-path: "workspace/instructions/skills/fix-ci"
  skm-source-integrity: "sha256:51da73b7aa50cd10ef1d40db13bf93cc748f24af34e2b4dc818098edb0b42d64"
  workspace-toolkit-version: "0.7.2"
  workspace-docs-compatibility: "7.x"
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
the primary checkout coordination-only. Ordinary task or delivery branches follow task authority under Workspace Docs 7;
older pins retain their direct branch-request requirement. Always honor protections.

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
3. Run changed-component regression checks until the cause is repaired. Only
   after they pass, run affected direct/transitive consumer checks in dependency
   order; keep native CI requirements intact and report unavailable coverage.
4. Review the diff for local-only assumptions, secrets, generated artifacts,
   and unrelated formatting churn. Obtain required independent exact-candidate
   review, resolve every finding, and rerun affected modules. Once fixes,
   artifacts, and documentation stabilize, freeze the candidate and run all
   required final gates; renew stale evidence for changed combined revisions.
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

## Pinned SDLC Contract

Read the project's pinned SDLC before planning or delivery. For Workspace Docs
7, done means verified merge into main with reconciled acceptance, documentation,
catalog, version records, and memory; deployment/publication is separate.
Blocked records previous stage, kind, reason, and resume condition; resume there
and renew stale evidence. Preserve done history with linked follow-up specs.
Shared test integration is the default; only an explicitly documented direct
route may omit it, preserving all gates. Older pins keep their prior completion
and branch-authority contracts.

For v7, the task request authorizes ordinary task branches and safe delivery.
Security, data integrity, public interfaces, governed instructions, and release
controls always require independent exact-candidate review; other non-trivial
changes require it except small low-risk changes with focused tests.
Resolve every finding by implementation or reviewer-agreed documented rejection.
For v7 development and review fixes, map changed behavior and direct/transitive
consumers, including interfaces, errors, security, timing, side effects,
configuration, dependencies, and generated outputs. Run the smallest meaningful
changed-component tests/checks first; only after they pass, run affected consumer
checks in dependency order through the transitive chain. Failure blocks dependent
stages; missing coverage or tools is a gap, never a pass. Deduplicate overlapping
checks, assess old/new relationships for deletions and renames, and group cycles.
Avoid unrelated aggregate runs; unknown impact requires justified safe fallback.
Keep required contract/integration/end-to-end coverage and native CI protections.
Reuse only proven-fresh evidence after further edits; a flat selection is not
execution order. Read-only skills assess evidence without mutating; planning
skills specify stages without implementing. Reconcile
knowable spec, catalog, and memory records before required review. Finish review,
artifacts, documentation, records, and fixes before freezing the candidate and
running full required checks/tests. Later tracked event/result records renew
affected review and verification; they do not automatically preserve evidence. Reuse only proven-fresh evidence and verify actual
combined integration/main revisions. Each acceptance criterion needs supporting
evidence; subjective product decisions go to the user. Read-only skills remain
read-only and planning skills do not implement changes.
