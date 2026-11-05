---
name: fix-bug
description: Reproduce, isolate, and fix a reported software defect with regression coverage. Use when observed behavior differs from a requirement or established contract and the user authorizes a focused implementation change.
metadata:
  skm-version: "0.4.9"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6392e044b7d98e5735966ad106a4eedeaf41da5f"
  skm-source-path: "workspace/instructions/skills/fix-bug"
  skm-source-integrity: "sha256:51ebe227491d3674766433cfa336c77c8b7478d3c1bb7bb50e7a1e02c77a8650"
  workspace-toolkit-version: "0.13.1"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Fix Bug

Correct the root cause while preserving unrelated behavior.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Report unresolved conflicts
between current instruction files rather than guessing.

## Reproduce and Isolate

1. Read repository policy, the relevant spec or contract, and the bug report.
2. Establish expected versus actual behavior, affected versions or inputs, and
   a deterministic reproduction when practical.
3. Trace the smallest relevant execution path and identify the root cause.
   Distinguish it from symptoms, environmental failures, and nearby issues.
4. Inspect branch and worktree state and preserve unrelated user changes.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. Ordinary task or delivery branches follow task authority under Workspace Docs 7;
older pins retain their direct branch-request requirement. Always honor protections.

Treat governed instructions as read-only unless a direct human request
prospectively grants instruction-change approval for the named outcome or
scope. A general bug-fix request and standing workflow authority do not include
that permission. Do not edit governed instructions and seek approval
retroactively.

## Fix and Prove

1. Add a regression test that fails for the confirmed defect where feasible.
2. Implement the smallest coherent correction using established patterns.
3. Test boundary inputs, error paths, compatibility, and adjacent behavior.
4. Run the narrowest repository-owned focused checks until the reproduction and
   representative failure paths pass. Regenerate affected artifacts first.
5. Self-review the complete diff against the reproduction, expected contract,
   affected consumers, and relevant security or persistence boundaries.
6. Reconcile knowable documentation, spec acceptance, catalog, and memory before
   independent exact-candidate review under the pinned risk rules. Resolve every
   finding through a fix or reviewer-agreed rejection; rerun affected modules
   and renew review for relevant edits. Freeze the reviewed candidate and run
   all required final gates. Reuse only proven-fresh native evidence.
7. Keep the spec in development until confirmed test integration, then in test
   until the pinned completion event (verified main merge with reconciled
   acceptance and records in v7). Documented direct routes preserve every gate.
   Later tracked result/integration records require affected review and gate
   reconciliation; report final results at handoff without assuming record
   writes preserve the candidate.

For infrastructure defects, change OpenTofu configuration and run non-mutating
validation locally. Apply, destroy, import, and state correction must run only
through the repository's CI/CD Taskfile workflow. Any proposed local, direct,
provider-CLI, or alternative-engine mutation path is a blocker, not a fallback.

Report the reproduction, cause, change, regression evidence, remaining risk,
memory classification, and publication status. Continue through ordinary
commit, pull-request, CI, test-integration, and non-destructive release steps
under standing workflow authority. Ordinary branch creation and pushing follow the pinned SDLC authority. Pause for a substantial scope expansion, an
unapproved governed-instruction change, a destructive production action, or a
material missing product decision. Do not fold unrelated cleanup or speculative
hardening into the bug fix.

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
