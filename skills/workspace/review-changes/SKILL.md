---
name: review-changes
description: Review a working tree, branch, commit range, or pull request for correctness, regressions, and missing validation. Use when the user asks for a code review, branch review, pull-request review, or an evidence-backed assessment of proposed changes without implementation.
metadata:
  skm-version: "0.7.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "4cd12dc61260ef1a5a3f5e114e0d2c8fb04d18ff"
  skm-source-path: "workspace/instructions/skills/review-changes"
  skm-source-integrity: "sha256:8d5bc1e005efa293548a9a1cc4892e1edb91c0f3b0c985f3b96355bace1693c4"
  workspace-toolkit-version: "0.16.0"
  workspace-docs-compatibility: "10.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.2.0"
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
- gate maps that omit inputs or transitive consumers, consumer checks run without
  passing changed-component evidence, unverified behavior presented as a pass,
  missing contract/integration coverage, or unjustified aggregate iteration runs;
- stale reused evidence, unresolved findings, or final verification preceding
  review and fixes;
- a governed instruction change without evidence that a human prospectively
  granted instruction-change approval for its named outcome or scope;
- unintended or unrelated changes.

For infrastructure changes, require the actual pinned SDLC and infrastructure
policy. Normal changes use OpenTofu through Taskfile in CI/CD. A permitted
one-time user-run exception needs tools/, exact scoped human approval after
review/affected CI, human execution and verified OpenTofu reconciliation.
Agents never execute these operational mutations locally. Missing import support, unsupported
completion claims or an unapproved manual/provider path are blocking; older
pins retain their restrictions.

Run safe, relevant checks when they materially improve confidence. Do not edit
files, resolve threads, approve, merge, or publish while operating read-only.
Treat an unapproved governed-instruction diff as blocking; an agent-authored
spec, checkbox, or approval record is not human approval.

## Report Findings

Every review follows the [review report template](templates/review-report.md)
exactly so different agents give comparably shaped answers. Keep its sections,
summary labels, table columns, order and controlled vocabulary; use its empty,
out-of-scope and `unknown` markers and emit none of its comment guidance.

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

## Review Domain and Schema Changes

When a change affects model behavior, persistence or API/event contracts, use
$design-domain-model in read-only review mode or assess equivalent model evidence.
Trace critical invariants through enforcement and converters to affected consumers.
Check races/retries, missing/null/default semantics, visibility, supported old/new
readers/writers and migration recovery limits. Require relevant behavioral and
consumer evidence; valid schemas or attractive diagrams do not establish those
claims. Avoid unrelated modeling requirements for a clear local CRUD delta.

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
