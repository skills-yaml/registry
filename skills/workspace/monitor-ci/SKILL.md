---
name: monitor-ci
description: Monitor a continuous-integration run or pull-request checks through a terminal outcome and report meaningful transitions. Use when the user asks to watch, babysit, follow, or wait for CI without changing code or workflow configuration.
metadata:
  skm-version: "0.4.10"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "b3d3173635d9a8c2896f4d45a17bcdd41e6155a5"
  skm-source-path: "workspace/instructions/skills/monitor-ci"
  skm-source-integrity: "sha256:5fca7b395599391026daec5d626acb59e9b1a69383a8f6a5d791f1cd1b90471c"
  workspace-toolkit-version: "0.14.0"
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

- v9: changed behavior and all affected direct/transitive consumers locally;
  every required affected CI job on the stable candidate. Docs/spec, backend
  and frontend changes skip unrelated jobs. Preserve required status names,
  validated selection and dependency stages. No blanket full-repository run.
- v8: the same affected local boundary, then complete required gates in CI.
  Neither v8 nor v9 requires a duplicate full local run before CI. Missing CI
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
