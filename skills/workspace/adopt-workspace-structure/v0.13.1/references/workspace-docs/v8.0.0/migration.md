# Migration Notes: workspace-docs@8.0.0

This major release changes the required development/verification workflow while
preserving v7 lifecycle, approval, review, memory, version, and protection rules.
Read [SDLC](./sdlc.md), [process](./process.md), and [audit](./audit-checklist.md).

## Updating from 7.0

1. Create a scoped development migration spec; record Version and Memory Impact.
   Preserve released packages, completed specs, manual policy, unrelated work,
   existing worktrees, and unique commits. Older pins retain their own contract.
2. Require one active task per agent, with explicit completion or blocked/deferred
   handoff before switching. Split oversized specs into ordered task-sized steps
   with bounded outcomes, dependencies, acceptance mapping, and focused validation.
   Use linked child specs only for independently managed delivery/lifecycle.
3. Map changed behavior and affected direct/transitive consumers. Run only their
   smallest meaningful Taskfile checks locally, changed component before dependent
   consumers; skip unrelated projects/suites. Missing coverage is not a pass.
4. Configure complete required candidate and integration/main verification in CI,
   using Taskfile entrypoints and existing protections. Publication-only CI cannot
   replace pre-merge checks. Unknown impact requires investigation and justified
   aggregate fallback in CI. Missing CI blocks acceptance, not submission for CI.
5. Finish review, fixes, artifacts, and documentation before full CI gates on the
   stable candidate. Do not require a duplicate complete local run. Renew evidence
   after relevant edits or moving integration inputs; record run and revision.
6. Pin 8.0.0, replace only generated AGENT-CONTEXT from the new template, reconcile
   approved current guidance/skills and native integrity records, and run affected
   local checks. Preserve manual policy unless its reconciliation was approved.
7. Verify actual shared-test integration before test and main merge before done;
   reconcile acceptance, catalog, version reservations and memory. Publication is
   separate. Preserve historical evidence and explicitly document unresolved gaps.

## Older Pins and Rollback

For a pin older than v7, apply each intermediate migration in order. Before
release, restore the previous pin and only this migration's changes. After
release, issue a successor; never rewrite published standard or skill packages.
