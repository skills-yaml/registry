---
name: implement-spec
description: Implement an approved development specification through validated, reviewable changes. Use when a spec is active in development and the request authorizes code or documentation changes, including required tests, compatibility work, lifecycle reconciliation, and memory-impact completion.
metadata:
  skm-version: "0.5.4"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/implement-spec"
  skm-source-integrity: "sha256:cdf2f1d5a6d3cfb1279ccf346943c01f2e888ee5fc58841b72aca39440263a3c"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.1.4"
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

## Workspace Docs 8 Execution Boundary

For a repository pinned to v8, retain the v7 lifecycle, review, approval, and
freshness rules while applying the v8 verification boundary: local checks cover
changed behavior and all affected direct/transitive consumers; skip unrelated
projects/suites. Complete required gates run in CI after the candidate stabilizes,
without a duplicate complete local run before requesting CI. Unknown impact
requires investigation and justified CI fallback; missing CI cannot prove final
acceptance. Work on one active task per agent. When writing a spec, split oversized
scope into bounded ordered steps with dependencies, acceptance mapping, and
focused validation; use linked child specs for independently managed delivery.
Preserve this skill's planning/read-only scope and explicit older-pin contracts.

## Workspace Docs 9 Affected CI

For a v9 pin, complete final verification means every required affected CI job,
not every project/job in the repository. Docs/spec-only changes run related jobs;
backend-only and frontend-only changes run their own jobs. Shared inputs include
all proven direct/transitive consumers. Use validated job selection and preserve
required status/protections, dependency stages, and this skill's authority.
Unknown scope needs investigation and a justified fallback. Do not restore a
blanket full-repository CI run for known narrow scope. Older pins retain their
contracts; publication checks remain separate from ordinary change validation.
