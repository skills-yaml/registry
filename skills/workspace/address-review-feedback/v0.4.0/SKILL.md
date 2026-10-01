---
name: address-review-feedback
description: Triage and implement selected actionable feedback from a pull request, branch review, or review report. Use when the user asks to address review comments, requested changes, or unresolved threads and authorizes the corresponding code or documentation edits.
metadata:
  skm-version: "0.4.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bdedc37407589cce10ce4f4db4c5c15ab1c33dce"
  skm-source-path: "workspace/instructions/skills/address-review-feedback"
  skm-source-integrity: "sha256:c40156cfde4628759755232c2de930fbe181f44dafbc296525198ef1f84b0068"
  workspace-toolkit-version: "0.7.0"
  workspace-docs-compatibility: "7.x"
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
4. Run affected modules for each coherent fix. Re-read each selected thread
   against the revised diff and obtain reviewer agreement for rejected findings.
   A suggestion outside the accepted scope need not become a code change, but
   its review disposition must be explicit.
5. Obtain required independent review of relevant revisions and resolve every
   finding before freezing the candidate and running all final required gates.
   Report any remaining product decision or unresolved finding as a blocker.

Do not accept feedback that introduces infrastructure mutation outside
OpenTofu and repository Taskfile entrypoints or asks for local infrastructure
mutation. Classify it as a policy conflict and request a source-only local
OpenTofu change whose apply, destroy, import, or state mutation runs through
the authorized CI/CD workflow. Provider CLI writes remain prohibited there.

## Hand Off

Map each selected comment to its outcome, validation evidence, and any remaining
decision. Under a user-requested feedback workflow, use standing authority to
reply, resolve addressed threads, commit, push the delivery branch, and update
the pull request without requesting repeated approval. Do not self-approve when
repository policy prohibits it, bypass protection, or execute a destructive
production action without scoped human approval.

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
