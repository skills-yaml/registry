---
name: implement-spec
description: Implement an approved development specification through validated, reviewable changes. Use when a spec is active in development and the request authorizes code or documentation changes, including required tests, compatibility work, lifecycle reconciliation, and memory-impact completion.
metadata:
  skm-version: "0.5.6"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "b3d3173635d9a8c2896f4d45a17bcdd41e6155a5"
  skm-source-path: "workspace/instructions/skills/implement-spec"
  skm-source-integrity: "sha256:88c04103dae8baa74823d22a7868ed7b2bc54fa6285715660e5806d6a5e062ac"
  workspace-toolkit-version: "0.14.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.1.6"
---

# Implement Spec

Deliver the active specification without expanding its authority or scope.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Report unresolved conflicts
between current instruction files; runtime system, developer, and direct user
instructions retain their platform precedence.

## Prepare

1. Read repository instructions, the active spec, related architecture, tests,
   and durable memory required by local policy.
2. Verify that scope, acceptance criteria, affected areas, validation gates, and
   memory impact are present. Resolve material ambiguity before implementation.
3. Inspect branch and worktree state. Preserve unrelated user changes.
4. Create or update an ordered plan for non-trivial work and keep the active
   step visible while work proceeds.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. Ordinary task or delivery branches follow task authority under Workspace Docs 7;
older pins retain their direct branch-request requirement. Always honor protections.

Before editing governed instructions (`AGENTS.md`, `DESIGN.md`, canonical files
under `workspace/instructions/`, or instruction-approval controls), verify
prospective instruction-change approval from a direct human request naming the
outcome or scope. Standing authority and an agent-authored spec do not provide
that approval. Do not edit first and request approval afterward; once the human
has directly approved the scope, do not ask again for the same change.

## Implement

1. Make the smallest coherent change that advances the approved contract.
2. Follow local patterns and preserve compatibility unless the spec explicitly
   authorizes a break or migration.
3. Add or update tests for success and representative failure paths with each
   behavior change.
4. Treat security, privacy, destructive production operations, and data
   migrations as explicit safety boundaries. Ordinary delivery actions are
   covered by standing workflow authority; do not expand product scope.
5. Review intermediate diffs for accidental scope growth and generated or
   machine-local information.

Never mutate cloud infrastructure from local development. Locally, change only
OpenTofu configuration and run non-mutating validation or review. OpenTofu
applies, destroys, imports, and state mutations must run only through the
repository's CI/CD Taskfile workflow. Non-destructive operations proceed after
required gates; destructive production operations require scoped human
approval.
Never substitute Terraform, another IaC engine, a provider mutation CLI, a
cloud console, or an ad hoc provisioning script; CI/CD does not authorize those
alternatives. Stop as blocked if the requested change cannot comply.

## Validate and Reconcile

1. Map changed behavior and affected consumers before each coherent change's
   verification. Run changed-component tests/checks first; after they pass, run
   affected direct/transitive consumer tests in dependency order. Stop dependent
   stages on failure. Format changed files and regenerate affected artifacts
   before their checks; explain selected, deferred, and fallback checks.
2. Self-review the complete diff against each acceptance criterion and inspect
   edge cases, regressions, error messages, and rollback behavior.
3. Reconcile documentation, spec acceptance records, and memory knowable before
   integration. Classify memory as updated or none with rationale and persist
   stable decisions, facts, preferences, or open questions under local policy.
4. Obtain independent exact-candidate review under the pinned risk rules, fix
   every finding or record reviewer-agreed rejection, and rerun affected modules.
   After records, review, artifacts, and fixes stabilize, freeze the candidate
   and run every required final gate. Reuse evidence only when native tooling
   proves relevant inputs unchanged; unknown scope or freshness uses aggregate
   fallback. Report final results at handoff. Later tracked result or integration
   records renew affected review and verification; never assume they preserve
   the frozen candidate.
5. Keep the spec in development after local implementation and validation.
   Move it to test only after confirmed merge or deployment to the configured
   test target, conventionally `develop`. Move it to done only after the pinned completion event: verified main merge
   with reconciled acceptance and records in v7; production release in older pins. Do not infer
   either event from the checked-out branch name alone.
6. Update the root catalog in the same lifecycle change and record the actual
   integration, main merge, or separate publication evidence in its rationale.
7. Report the outcome, validation evidence, memory classification, remaining
   risks, and publication status.

After a user requests delivery, continue under standing workflow authority
through commits, pull-request creation or updates, bounded CI fixes and reruns,
test integration, and non-destructive releases. Ordinary branch creation and pushing follow the pinned SDLC authority. Do not
request repeated approval for the remaining ordinary steps. Pause before a
destructive production action and present its exact target, effect, rollback,
evidence, and workflow for scoped human approval.

## Version Application

Before implementation, check the latest shared release reservation and version
source. Apply a development-start bump once through its designated owner; for
merge timing, require the owner to apply it before integration artifacts are
built. Reuse an already-applied shared reservation. Recheck occupancy and
baseline at handoff, run `task versions:check`, and reconcile member paths and
release evidence with lifecycle changes.

## Implement Modeling Decisions

For domain/schema scope, use $design-domain-model to inspect the approved model
or its delta before changing representations. Preserve invariant ownership,
trusted tenant context, conversions and supported consumer behavior. Update
affected mappings and tests with implementation; missing/material design choices
return to planning rather than being silently inferred. Storage, public schemas
and internal objects may differ deliberately. Execute migrations only within the
existing authorization and deployment boundaries.

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
