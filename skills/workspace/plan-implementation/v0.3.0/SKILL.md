---
name: plan-implementation
description: Build an ordered, evidence-backed implementation plan from an approved development specification. Use when a feature, migration, or refactor has an active spec and needs dependency ordering, concrete file areas, validation strategy, compatibility handling, and completion gates before code changes begin.
metadata:
  skm-version: "0.3.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bd958c01249e1cb1e1fbbcf91ba70e83abec8d5f"
  skm-source-path: "workspace/instructions/skills/plan-implementation"
  skm-source-integrity: "sha256:1aafe7bc1cab590384b2386c7421d31ff74241013b1d0a1fa56e2c1b1277b6fb"
  workspace-toolkit-version: "0.4.0"
  workspace-docs-compatibility: "6.x"
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
   scope, acceptance criteria, affected areas, validation gates, and unresolved
   memory impact.
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

Include focused iterative gates, artifact generation, final self-review, a
stable-candidate boundary, full required gates, spec lifecycle reconciliation,
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
spec to test, and confirmed production release moves it to done. Use `develop`
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
