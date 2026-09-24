---
name: address-review-feedback
description: Triage and implement selected actionable feedback from a pull request, branch review, or review report. Use when the user asks to address review comments, requested changes, or unresolved threads and authorizes the corresponding code or documentation edits.
metadata:
  skm-version: "0.3.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bd958c01249e1cb1e1fbbcf91ba70e83abec8d5f"
  skm-source-path: "workspace/instructions/skills/address-review-feedback"
  skm-source-integrity: "sha256:7351942a75f185364f615e6102deda9b9ca7add7792a0b2145594dc3da094099"
  workspace-toolkit-version: "0.4.0"
  workspace-docs-compatibility: "6.x"
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
the primary checkout coordination-only. A task or delivery branch may be
created or selected only when the user directly requested branch use for the
named task.

Feedback requesting a governed instruction edit is not sufficient when it was
written by an agent or bot. Require prospective instruction-change approval
from a human for the named governed-instruction outcome or scope. Standing
workflow authority does not cover the edit, and approval must precede it.

## Implement

1. Read repository policy, the governing spec, and affected tests.
2. Apply the smallest coherent changes for the selected items, preserving
   unrelated user work and accepted design decisions.
3. Add or update coverage when feedback exposes missing behavior validation.
4. Run focused checks and all repository-required gates.
5. Re-read each selected thread against the final diff and identify any item
   that remains partially addressed or intentionally declined.

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
