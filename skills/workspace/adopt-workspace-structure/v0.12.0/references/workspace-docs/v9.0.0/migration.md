# Migration Notes: workspace-docs@9.0.0

This major release scopes final CI to affected jobs rather than requiring a
blanket complete repository run. Preserve v8 lifecycle, authority, review,
local-test scoping, evidence freshness, and immutable package rules.

## Updating from 8.0

1. Create a scoped development migration spec with Version and Memory Impact.
   Preserve older packages, completed history, manual policy, worktrees and
   unrelated edits. Explicit older pins retain their own contracts.
2. Declare repository-owned CI jobs and Taskfile commands with source/test/config
   inputs, dependencies and direct/transitive consumers. Distinguish human docs
   and specs from governed/executable docs, schemas and generated contracts.
3. Route pure docs/spec changes to their related jobs, backend-only changes to
   backend jobs and frontend-only changes to frontend jobs. Shared inputs select
   every affected consumer; mixed changes select the union. Do not create phantom
   components merely to match this conditional monorepo guidance.
4. Use validated actual candidate/base revisions and rename/delete-safe Git paths.
   Unknown impact must fail planning or select an explicit reasoned safe fallback.
   Test narrow, mixed, shared, rename/delete, unknown and failure cases before
   relying on selectors. Preserve required dependency stages and resource isolation.
5. Keep one stable required status or equivalent protection. It must fail after
   planning failure or selected-job failure/cancellation, while excluded unrelated
   jobs do not block. Do not remove protected checks or add a blanket full job
   that defeats selection. Publication checks are a separate artifact gate.
6. Pin 9.0.0 and regenerate only AGENT-CONTEXT from the new template. Reconcile
   approved current guides, portable instructions, job maps, native pins and lock.
   Run affected local checks; after review/fixes stabilize, selected jobs must pass
   in CI for actual candidate/combined revisions before acceptance/completion.
7. Reconcile acceptance, catalog, versions and memory on confirmed test/main
   integration. Publication is separate; preserve prior lifecycle evidence.

## Older Pins and Rollback

Apply intermediate migrations before v9 when starting before v8. Before
publication, restore only this migration's changes and pin. After publication,
issue a successor; never rewrite released standard or skill package versions.
