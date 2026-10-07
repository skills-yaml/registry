---
name: fix-bug
description: Reproduce, isolate, and fix a reported software defect with regression coverage. Use when observed behavior differs from a requirement or established contract and the user authorizes a focused implementation change.
metadata:
  skm-version: "0.4.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "e205b8c9e4f092adb9b20aaa129e644d858a25ca"
  skm-source-path: "workspace/instructions/skills/fix-bug"
  skm-source-integrity: "sha256:7cc9180adad34a2ad03f05c5f883d290479faf1a8d9ade24530c46cdc6d9208e"
  workspace-toolkit-version: "0.8.0"
  workspace-docs-compatibility: "7.x"
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
under standing workflow authority. Ordinary branch creation and pushing follow the pinned SDLC authority. Pause only for an
unapproved governed-instruction change, a destructive production action, or a
material missing product decision. Do not fold unrelated cleanup or speculative
hardening into the bug fix.

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
For v7 development and review fixes, map changed behavior and direct/transitive
consumers, including interfaces, errors, security, timing, side effects,
configuration, dependencies, and generated outputs. Run the smallest meaningful
changed-component tests/checks first; only after they pass, run affected consumer
checks in dependency order through the transitive chain. Failure blocks dependent
stages; missing coverage or tools is a gap, never a pass. Deduplicate overlapping
checks, assess old/new relationships for deletions and renames, and group cycles.
Avoid unrelated aggregate runs; unknown impact requires justified safe fallback.
Keep required contract/integration/end-to-end coverage and native CI protections.
Reuse only proven-fresh evidence after further edits; a flat selection is not
execution order. Read-only skills assess evidence without mutating; planning
skills specify stages without implementing. Reconcile
knowable spec, catalog, and memory records before required review. Finish review,
artifacts, documentation, records, and fixes before freezing the candidate and
running full required checks/tests. Later tracked event/result records renew
affected review and verification; they do not automatically preserve evidence. Reuse only proven-fresh evidence and verify actual
combined integration/main revisions. Each acceptance criterion needs supporting
evidence; subjective product decisions go to the user. Read-only skills remain
read-only and planning skills do not implement changes.
