---
name: monitor-ci
description: Monitor a continuous-integration run or pull-request checks through a terminal outcome and report meaningful transitions. Use when the user asks to watch, babysit, follow, or wait for CI without changing code or workflow configuration.
metadata:
  skm-version: "0.4.8"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/monitor-ci"
  skm-source-integrity: "sha256:e76fdb34ce16a20320fef8f1dd5cfe97b72c539eb1090acf50bd92363f20870d"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Monitor CI

Track the requested run until it succeeds, fails, is cancelled, or reaches an
explicit monitoring deadline.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth and report stale conflicting
CI documentation or generated guidance.
Monitoring remains read-only and cannot supply instruction-change approval for
any governed instruction edit.

## Monitor

1. Identify the repository, branch or pull request, workflow, and run to watch.
   Prefer the newest relevant run only when the target is otherwise unambiguous.
2. Record the initial checks, statuses, URLs or identifiers, and commit revision.
3. Poll with bounded intervals and provide concise updates when state changes or
   at least once per minute during active work.
4. Detect replacement, cancellation, rerun, stale revision, or authorization
   failure instead of silently following the wrong run.
5. Stop at a terminal outcome or the user-defined deadline.

Report an infrastructure job that mutates state outside OpenTofu and repository
Taskfile entrypoints as a policy failure. Also report any infrastructure
mutation performed outside the trusted CI/CD workflow or through a provider CLI
such as `gcloud`. Monitoring remains read-only and does not authorize a local or
manual remediation path.

## Hand Off

Report the final outcome, failed or incomplete checks, relevant revision, and
the most useful next diagnostic step. A monitoring-only request remains
read-only. Within a broader delivery task, hand a failure directly to the
authorized CI-fix workflow without asking for repeated human approval; bounded
safe reruns, fixes, test integration, and non-destructive releases are covered
by standing workflow authority.

## Pinned Lifecycle Evidence

Read the pinned SDLC when reporting delivery readiness. Under v7, passing CI
alone does not prove done: verify actual main merge and reconciliation of
acceptance and records. Deployment/publication remain separate events. Report
missing, failed, interrupted, or stale gate evidence against the exact revision;
a contributor run cannot prove coverage of a changed combined revision. Report
blocked metadata or resume needs without editing specs. Keep monitoring read-only;
older pins retain their lifecycle contract.

## Workspace Docs 8 Execution Boundary

For a repository pinned to v8, retain the v7 lifecycle, review, approval, and
freshness rules while applying the v8 verification boundary: local checks cover
changed behavior and all affected direct/transitive consumers; skip unrelated
projects/suites. Complete required gates run in CI after the candidate stabilizes,
without a duplicate complete local run before requesting CI. Unknown impact
requires investigation and justified CI fallback; missing CI cannot prove final
acceptance. Work on one active task per agent. When writing a spec, split oversized
scope into bounded ordered steps with dependencies, acceptance mapping, and
focused validation; use linked child specs for independently managed delivery.
Preserve this skill's planning/read-only scope and explicit older-pin contracts.

## Workspace Docs 9 Affected CI

For a v9 pin, complete final verification means every required affected CI job,
not every project/job in the repository. Docs/spec-only changes run related jobs;
backend-only and frontend-only changes run their own jobs. Shared inputs include
all proven direct/transitive consumers. Use validated job selection and preserve
required status/protections, dependency stages, and this skill's authority.
Unknown scope needs investigation and a justified fallback. Do not restore a
blanket full-repository CI run for known narrow scope. Older pins retain their
contracts; publication checks remain separate from ordinary change validation.
