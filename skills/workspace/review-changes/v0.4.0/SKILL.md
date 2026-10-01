---
name: review-changes
description: Review a working tree, branch, commit range, or pull request for correctness, regressions, and missing validation. Use when the user asks for a code review, branch review, pull-request review, or an evidence-backed assessment of proposed changes without implementation.
metadata:
  skm-version: "0.4.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bdedc37407589cce10ce4f4db4c5c15ab1c33dce"
  skm-source-path: "workspace/instructions/skills/review-changes"
  skm-source-integrity: "sha256:7a344efccd672c21845edd35a42a7e81bac17ba1d58f4adb972aeb66ec02b4d7"
  workspace-toolkit-version: "0.7.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Review Changes

Perform a read-only, defect-focused review of the requested change set.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Report conflicting root,
documentation, spec, memory, or generated copies as findings.

## Establish the Review Range

1. Identify the exact working tree, base, head, commit range, or pull request.
2. Read repository policy, the governing spec, and affected architecture and
   tests before judging the diff.
3. Inspect complete changed files and relevant callers, consumers, schemas, and
   validation paths. Do not review isolated hunks without their context.

## Evaluate

Check for:

- behavior that contradicts requirements or established contracts;
- regressions, edge cases, incorrect state transitions, and data loss;
- compatibility, migration, concurrency, retry, and error-handling failures;
- security or privacy boundary violations;
- missing, weak, or misleading tests and documentation;
- a spec state or catalog rationale that claims shared-test integration, pinned
  completion, or publication without actual event and acceptance evidence;
- missing blocked metadata, stale resume evidence, or reopening done history;
- gate maps that omit inputs or transitive consumers, stale reused evidence,
  unresolved findings, or final verification preceding review and fixes;
- a governed instruction change without evidence that a human prospectively
  granted instruction-change approval for its named outcome or scope;
- unintended or unrelated changes.

For infrastructure changes, report any local mutation path, any mutation
outside the repository's CI/CD workflow, or any mutation mechanism outside
OpenTofu and Taskfile as a blocking policy violation. This includes local
applies, destroys, imports, state changes, and provider CLI writes even when
they are described as emergency or functionally equivalent steps.

Run safe, relevant checks when they materially improve confidence. Do not edit
files, resolve threads, approve, merge, or publish while operating read-only.
Treat an unapproved governed-instruction diff as blocking; an agent-authored
spec, checkbox, or approval record is not human approval.

## Report Findings

Lead with actionable findings ordered by severity. For each finding include the
affected location, concrete failure mode, why it matters, and the smallest
useful remediation direction. Distinguish confirmed defects from questions or
residual risk. If no actionable defect is found, say so and state the remaining
test or coverage limitations.
When lifecycle readiness is in scope, distinguish readiness to merge into the
test target from evidence that the merge occurred, verified main completion
from a merely ready candidate, and separate publication readiness from actual
publication. Final full gates may still be pending during review; report them
as pending rather than require premature broad runs. Relevant edits invalidate
affected review; rejected findings require reviewer agreement.

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
Run affected modular gates during implementation and review fixes. Reconcile
knowable spec, catalog, and memory records before required review. Finish review,
artifacts, documentation, records, and fixes before freezing the candidate and
running full required checks/tests. Later tracked event/result records renew
affected review and verification; they do not automatically preserve evidence. Reuse only proven-fresh evidence and verify actual
combined integration/main revisions. Each acceptance criterion needs supporting
evidence; subjective product decisions go to the user. Read-only skills remain
read-only and planning skills do not implement changes.
