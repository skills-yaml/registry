---
name: implement-spec
description: Implement an approved development specification through validated, reviewable changes. Use when a spec is active in development and the request authorizes code or documentation changes, including required tests, compatibility work, lifecycle reconciliation, and memory-impact completion.
metadata:
  skm-version: "0.3.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ec01dd7abe4b0a14d40fc1a9ff3ae56f739c115e"
  skm-source-path: "workspace/instructions/skills/implement-spec"
  skm-source-integrity: "sha256:6da89647a847f5ab49640ab51b74f1d4ddfb16abcc6a16c2bdec0a5422601c8d"
  workspace-toolkit-version: "0.4.2"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
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
the primary checkout coordination-only. A task or delivery branch may be
created or selected only when the user directly requested branch use for the
named task.

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

1. Run the narrowest repository-owned focused gates while iterating. Format
   changed files and regenerate affected artifacts before their checks.
2. Self-review the complete diff against each acceptance criterion and inspect
   edge cases, regressions, error messages, and rollback behavior.
3. Reconcile documentation and memory knowable before integration, stabilize
   the candidate, then run every required final gate. Reuse evidence only when
   the repository's native freshness contract proves every relevant input is
   unchanged; unknown scope or dependencies require the aggregate gates.
4. Resolve memory impact according to local policy and update durable memory
   only for stable decisions, facts, preferences, or open questions.
5. Keep the spec in development after local implementation and validation.
   Move it to test only after confirmed merge or deployment to the configured
   test target, conventionally `develop`. Move it from test to done only after
   confirmed production release, conventionally through `main`. Do not infer
   either event from the checked-out branch name alone.
6. Update the root catalog in the same lifecycle change and record the actual
   integration or release evidence in its rationale.
7. Report the outcome, validation evidence, memory classification, remaining
   risks, and publication status.

After a user requests delivery, continue under standing workflow authority
through commits, pull-request creation or updates, bounded CI fixes and reruns,
test integration, and non-destructive releases. Create or push a task or
delivery branch only after the direct branch request required above. Do not
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
