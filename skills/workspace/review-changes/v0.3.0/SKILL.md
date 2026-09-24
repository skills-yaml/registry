---
name: review-changes
description: Review a working tree, branch, commit range, or pull request for correctness, regressions, and missing validation. Use when the user asks for a code review, branch review, pull-request review, or an evidence-backed assessment of proposed changes without implementation.
metadata:
  skm-version: "0.3.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bd958c01249e1cb1e1fbbcf91ba70e83abec8d5f"
  skm-source-path: "workspace/instructions/skills/review-changes"
  skm-source-integrity: "sha256:8c1459fd3c2d599f8d72a59ac3c4c00e35f6c682a13dea2016e24303e9620cbc"
  workspace-toolkit-version: "0.4.0"
  workspace-docs-compatibility: "6.x"
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
- a spec state or catalog rationale that claims test integration or production
  release without evidence from the configured delivery target;
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
test target from evidence that the merge occurred, and distinguish production
release readiness from evidence that the release occurred.
