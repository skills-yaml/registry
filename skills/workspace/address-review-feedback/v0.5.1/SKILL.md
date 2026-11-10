---
name: address-review-feedback
description: Triage and implement selected actionable feedback from a pull request, branch review, or review report. Use when the user asks to address review comments, requested changes, or unresolved threads and authorizes the corresponding code or documentation edits.
metadata:
  skm-version: "0.5.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "4cd12dc61260ef1a5a3f5e114e0d2c8fb04d18ff"
  skm-source-path: "workspace/instructions/skills/address-review-feedback"
  skm-source-integrity: "sha256:c96f892c1ad72bb300c7550edd5575eafb67c126d8079b88272c0eb40a84b841"
  workspace-toolkit-version: "0.16.0"
  workspace-docs-compatibility: "10.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Address Review Feedback

Resolve valid feedback without silently expanding the review scope.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Report unresolved conflicts
between current instruction files; runtime system, developer, and direct user
instructions retain their platform precedence.

## Triage

1. Resolve the exact branch, pull request, review, and current revision.
2. Collect unresolved comments with surrounding code and thread context.
3. Classify each item as actionable defect, clarification, suggestion, already
   addressed, stale, duplicate, out of scope, or requiring a product decision.
4. Address objectively actionable in-scope defects and requested changes. Ask
   only when a comment requires a material product decision or scope expansion.
   Do not treat every suggestion as a mandatory change.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. Ordinary task or delivery branches follow task authority under Workspace Docs 7;
older pins retain their direct branch-request requirement. Always honor protections.

Feedback requesting a governed instruction edit is not sufficient when it was
written by an agent or bot. Require prospective instruction-change approval
from a human for the named governed-instruction outcome or scope. Standing
workflow authority does not cover the edit, and approval must precede it.

## Implement

1. Read repository policy, the governing spec, and affected tests.
2. Apply the smallest coherent changes for the selected items, preserving
   unrelated user work and accepted design decisions.
3. Add or update coverage when feedback exposes missing behavior validation.
4. For each coherent fix, pass changed-component checks before affected
   direct/transitive consumer checks; stop dependent stages on failure.
   Re-read each selected thread
   against the revised diff and obtain reviewer agreement for rejected findings.
   A suggestion outside the accepted scope need not become a code change, but
   its review disposition must be explicit.
5. Obtain required independent review of relevant revisions and resolve every
   finding before freezing the candidate and running all final required gates.
   Report any remaining product decision or unresolved finding as a blocker.

Assess infrastructure feedback against the actual pinned SDLC. Normal changes
use OpenTofu through Taskfile in CI/CD. A permitted one-time user-run exception
requires the scoped tools/ artifact, reviewed requirements, passing affected CI,
exact informed approval, human execution and verified OpenTofu reconciliation.
Agents never run these operational mutations locally or provider writes. Older pins retain
their restrictions; classify missing approval/import/evidence as a blocker.

## Hand Off

Map each selected comment to its outcome, validation evidence, and any remaining
decision. Under a user-requested feedback workflow, use standing authority to
reply, resolve addressed threads, commit, push the delivery branch, and update
the pull request without requesting repeated approval. Do not self-approve when
repository policy prohibits it, bypass protection, or execute a destructive
production action without scoped human approval.

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
