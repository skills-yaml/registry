---
name: fix-ci
description: Diagnose and fix failing continuous-integration checks with the smallest verified change. Use when CI or pull-request checks are failing and the user authorizes implementation, including log inspection, local reproduction, regression coverage, and rerun monitoring.
metadata:
  skm-version: "0.5.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "4cd12dc61260ef1a5a3f5e114e0d2c8fb04d18ff"
  skm-source-path: "workspace/instructions/skills/fix-ci"
  skm-source-integrity: "sha256:b9b1e1c76fbd4a1dfd1caca29700d74ec0427d29d1170788aa61ac7a8efbb23c"
  workspace-toolkit-version: "0.16.0"
  workspace-docs-compatibility: "10.x"
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

## Repair Scope

A delivery request authorizes a bounded repair of an observed failing operation,
not speculative pipeline improvement. Record the failing run/command and error,
connect the defect to the requested outcome and use the smallest fix within
existing tasks/workflows. Report optional improvements without implementing them.
If the required repair introduces a new pipeline, workflow, infrastructure or
architectural redesign, explain the concrete blocker and smallest proposal and
obtain approval for substantial scope expansion before editing. Resume the same
release/artifact after repair; retain all protections and approval boundaries.

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

Normal infrastructure fixes use OpenTofu through Taskfile/CI/CD, with local
agent work limited to source changes and non-mutating validation. For a one-time
user-run operation explicitly allowed by the actual pinned SDLC, prepare tools/,
review applicable specs, pass affected CI, explain the exact operation/result
and obtain scoped approval, then ask the user to execute and verify/reconcile.
Agents never run these operational mutations locally or provider writes. Older pins retain
their restrictions; missing approval, failed gates or missing OpenTofu import/
ownership evidence blocks the exceptional path.

Report cause, fix, local and remote validation, residual flake risk, memory
impact, and publication status. Under a user-requested delivery or CI-repair
task, use standing workflow authority to commit, push the delivery branch,
rerun CI, and update the pull request without requesting repeated approval.
Pause for a substantial scope expansion, an unapproved governed-instruction change, a destructive
production action, or an unsafe gate bypass.

## Pinned SDLC Contract

Read the repository's pinned SDLC; this skill does not override its authority
or this skill's read-only/planning boundary. Deliver the requested scope using
existing patterns. Report optional improvements separately and leave them
unimplemented. Before substantial scope expansion, identify the concrete
blocker, propose the smallest solution and obtain approval. Standing workflow
authority never grants unrelated work or governed instruction changes.

For v7 and later, ordinary task branches and safe delivery follow task authority.
Done means verified main merge with acceptance, documentation, catalog, versions
and memory reconciled; publication is separate. Preserve done history with
linked follow-ups. Blocked work records previous stage, kind, reason and resume
condition; resume that stage with renewed evidence. Shared test integration is
the default; a documented direct route preserves the same gates.

Security, data integrity, public interfaces, governed instructions and release
controls require independent exact-candidate review. Other non-trivial changes
require it except small low-risk changes with focused tests. Resolve findings
by a fix or reviewer-agreed documented rejection; optional suggestions remain
outside scope. Finish relevant review, fixes, artifacts and knowable records
before final verification. Later edits renew affected evidence. Verify actual
combined integration/main revisions, record acceptance evidence and preserve
host protections; missing coverage/tools are gaps, never a pass.

Use the verification contract for the actual pin:

- v9 and later: changed behavior and all affected direct/transitive consumers locally;
  every required affected CI job on the stable candidate. Docs/spec, backend
  and frontend changes skip unrelated jobs. Preserve required status names,
  validated selection and dependency stages. No blanket full-repository run.
- v8: the same affected local boundary, then complete required gates in CI.
  Neither v8 nor v9/v10 requires a duplicate full local run before CI. Missing CI
  cannot establish final acceptance; unknown impact needs investigation and
  justified CI fallback.
- v7: affected modules during iteration, then full required final-candidate
  checks/tests after review and fixes. Earlier pins retain their own contract.

During development and review fixes, pass changed-component checks before
consumer checks in dependency order. Include interfaces, errors, security,
timing, side effects, configuration, dependencies and generated outputs in
impact analysis. Failures block dependent stages; deduplicate checks, assess
old/new relationships for moves/deletions and group cycles. Reuse only proven-
fresh evidence. Read-only work assesses this evidence; planning specifies it.
Work on one active task per agent. Split oversized specs into bounded ordered
steps with prerequisites, acceptance mapping and focused validation; use linked
child specs for independently deliverable work and preserve overall acceptance.
