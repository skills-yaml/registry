---
name: plan-implementation
description: Build an ordered, evidence-backed implementation plan from an approved development specification. Use when a feature, migration, or refactor has an active spec and needs dependency ordering, concrete file areas, validation strategy, compatibility handling, and completion gates before code changes begin.
metadata:
  skm-version: "0.4.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "f867573bc91b5560d12cebd304ba3dd98aed7435"
  skm-source-path: "workspace/instructions/skills/plan-implementation"
  skm-source-integrity: "sha256:e358c66a3252940d58dc9784e89052a17ddc21c5c287ba4e2e8e4ae4bf23f020"
  workspace-toolkit-version: "0.7.1"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Plan Implementation

Translate an active specification into executable work while keeping the plan
grounded in the current repository.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. Report unresolved conflicts
between current instruction files instead of planning from a conflicting copy.

## Plan the Work

1. Verify that the spec is in the locally required development state and has
   scope, acceptance criteria, affected areas, validation gates, and
   memory impact initialized as pending or resolved with a valid rationale.
2. Read the governing instructions and inspect the actual entrypoints, data
   flows, tests, and closest implementation precedents.
3. Identify dependencies, externally visible contracts, migration boundaries,
   collision risks, and the smallest safe delivery slices.
4. Resolve facts from the repository. Label assumptions and stop on missing
   decisions that would materially change behavior or data.

## Produce an Executable Plan

For each ordered step state:

- the outcome, not just the activity;
- the files or components likely to change;
- dependencies on earlier steps;
- validation for success and representative failure cases;
- rollback, compatibility, or migration considerations;
- the acceptance criteria the step advances.

Design gate modules from actual inputs, dependencies, consumers, Taskfile
commands, resources, pass conditions, and freshness rules. Include affected
iteration gates, artifact generation, self-review and required independent
exact-candidate review, finding resolution, a frozen-candidate boundary, full
required gates, spec lifecycle reconciliation,
and memory-impact classification. Include ordinary commit, push, pull-request,
CI, test-integration, and non-destructive release steps under standing workflow
authority. Model a separate human approval gate only for destructive production
actions outside governed instruction changes. When governed instructions are
affected, plan a prospective instruction-change approval gate before their
first edit. A direct human request naming the instruction outcome already
satisfies that gate; general standing authority and an agent-authored spec do
not.
Plan the lifecycle handoffs separately: local implementation remains in
development, confirmed integration into the configured test target moves the
spec to test, and the confirmed pinned completion event moves it to done
(verified main merge plus reconciled acceptance and records in v7). Use `develop`
and `main` only as defaults when local policy does not name equivalent targets.

If infrastructure is affected, plan every resource mutation through OpenTofu
and repository Taskfile entrypoints in CI/CD. Keep local steps limited to
OpenTofu source changes and non-mutating validation or review. Never plan a
local apply, destroy, import, or state mutation. Treat any other execution
environment or mutation mechanism as a blocker, including cloud consoles,
provider CLIs, and alternative IaC engines. CI/CD does not authorize those
alternative mechanisms.

## Hand Off

Call out critical-path decisions, parallel-safe work, known risks, and any
acceptance criterion not covered by a planned validation. Persist the plan only
when requested or required by repository policy. Do not modify implementation
files while operating in a planning-only role.

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
