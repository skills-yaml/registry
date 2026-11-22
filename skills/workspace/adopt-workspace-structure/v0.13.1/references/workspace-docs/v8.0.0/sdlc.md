# Spec-Driven SDLC (`workspace-docs@8.0.0`)

## Development Workflow

Work on one active task at a time per agent. Complete it or record an explicit
blocked/deferred handoff before switching. Keep edits and tests within task scope.
Split oversized specifications into ordered steps with stable IDs, one bounded
outcome, prerequisites, acceptance criteria mapped to the overall spec, and focused
validation. Keep small specs concise; use linked child specs only when independent
delivery or lifecycle tracking is needed. Preserve cross-step invariants and
whole-feature acceptance; passing individual steps is not final acceptance.

Non-trivial work has one categorized specification under
`workspace/specs/<state>/<primary-feature>/<spec>.md`. The default route is:

```text
backlog -> development -> test -> done
```

Use `develop` or the documented shared test target for integration and `main`
for completion. A project may explicitly document a direct-to-main route,
including urgent fixes, preserving every review, verification, acceptance,
and approval requirement. Branch names alone never prove a transition.
Deployment and package publication are separate release events.

Before implementation, a non-trivial spec defines scope, acceptance criteria,
affected areas, an implementation plan, validation gates, risks, Version
Impact, and Memory Impact initialized to `pending`. A clear user task request
approves its scope; ask only for material missing product decisions or a
required governed instruction approval. Small low-risk changes may proceed
without a spec.

## Standing Workflow Authority

A task request authorizes ordinary task-branch creation, selection, and pushing,
commits, pull-request updates, safe CI repairs, shared-test integration, merge
into main, and non-destructive release. Do not request repeated human approval
for these steps. Proceed automatically once all required gates pass.
Standing workflow authority does not include permission to modify governed
instructions. Governed instructions need prospective human approval for their named scope; a direct request naming the instruction change is sufficient. Destructive production actions also need scoped human approval exposing target, effect, recovery, and workflow.
Repository-host, branch, environment, and credential protections are
never bypassed. Silence or elapsed time is not approval.

## Spec States

The pinned [Workspace standard](../README.md) defines
versioned behavior. This project's successor contract is Workspace Docs 8.

| State | Meaning and transition evidence |
| --- | --- |
| `backlog` | Accepted inactive work awaiting implementation. |
| `development` | Implementation, review, and final-candidate verification are active. Local completion does not itself advance the state. |
| `test` | Confirmed integration into the configured shared test branch or environment; verify the actual combined revision and acceptance criteria. |
| `blocked` | Work cannot proceed or is deliberately deferred; record the previous stage, reason, kind, and resume condition. |
| `done` | Verified work merged into main, with acceptance, documentation, catalog, version records, and memory reconciled. Deployment or publication may still be pending. |

Normal transitions are `backlog -> development -> test -> done`.
A documented direct route permits `development -> done` only after the same
required gates and confirmed main merge. Block from backlog, development, or
test; resume at that recorded stage and renew stale review, verification, and
acceptance evidence. Use these fields in a blocked specification:

```text
State: blocked
Previous State: development
Block Kind: impediment
Block Reason: Required dependency is unavailable.
Resume Condition: Dependency becomes available and affected evidence is renewed.
```

`Block Kind` is `impediment` or `deferred`. Preserve blocked work and unique
commits. Gate failures alone do not require a blocked transition: repair and
rerun safely while development continues. Block only when a missing decision,
dependency, external action, or deliberate deferral prevents progress.
Done history is preserved; defects and enhancements create linked follow-up
specs rather than reopening completed work. No existing spec becomes done
solely because the completion definition changed.

Every current spec has one primary feature and exactly one catalog row with
its path, feature, state, and rationale. Update the spec, catalog, and release
member paths together. Record actual integration or main-merge evidence.

## Review Gate

Every change receives author self-review. Small low-risk behavior changes
with focused tests may use self-review alone. Other non-trivial changes need
independent agent or human review of the exact candidate revision. Changes to
security, data integrity, public interfaces, governed instructions, or release
controls always require independent review regardless of size. Repository
protections may require a human reviewer in addition.

Resolve every finding before integration: implement it or obtain the
reviewer's agreement to a documented rejection. Style and optional suggestions
also require resolution; no unresolved findings remain. Record the candidate,
reviewer, outcome, and finding resolutions. Relevant edits renew affected
review and acceptance evidence. Complete review and fixes before freezing the
candidate and running final verification.

## Modular Quality Gates

The system designs project-specific modules from repository evidence. Every
gate declares its purpose, Taskfile command, relevant source/test/configuration
and generated inputs, dependencies and downstream consumers, resource
constraints, pass condition, and freshness rules. Validate selectors with
positive and representative negative cases before relying on them. Gates must
fail loudly when required tools or dependencies are missing.

### Staged Testing During Development

Agents MUST test only changed code and behavior demonstrably affected by the
change. For each selected test group, state which changed behavior or affected
contract it verifies. An unchanged component requires tests only when impact
evidence connects it to the change. Do not run unrelated tests for reassurance
or merely because they are available. Do not broaden the task to fix unrelated
failures discovered by mandatory gates; report them separately and preserve the
failed gate as a delivery blocker until it is resolved through authorized work.

In a monorepo, local development MUST cover changed code and all demonstrably
affected direct and transitive consumers, while skipping unrelated projects
and test suites. Run the complete required gates in CI when the final candidate
is ready. A full local run is not required before pushing a candidate for CI.

During development, select only gates affected by each coherent change,
including transitive consumers. For each change or review fix, run only strictly
necessary tests and checks covering affected behavior. Select the
smallest meaningful repository-owned test group; do not replace required
contract, integration, or end-to-end coverage with weaker unit tests. Do not
repeatedly execute unrelated aggregate gates during iteration.

1. **Map impact before testing.** Identify changed source, tests, interfaces,
   configuration, dependencies, and generated outputs. Use evidence from imports,
   callers, schemas, events, manifests, build rules, and runtime data flows to
   identify direct and transitive consumers. Include behavior, errors, security,
   timing, and side effects; an unchanged schema alone does not prove no impact.
2. **Verify the changed component first.** Run its smallest meaningful behavior
   tests and relevant checks through Taskfile entrypoints. A failed, missing,
   interrupted, or unavailable required check blocks dependent stages. Correct
   the failure and rerun affected checks before proceeding; absence of tests is
   a coverage gap, never a pass.
3. **Verify affected consumers after success.** Once changed-component checks
   pass, run only consumer tests exercising affected behavior or contracts.
   Order consumer stages by dependencies, continuing through the affected
   transitive chain. Passing one consumer does not eliminate downstream impact.
   Stop dependent stages on failure; unrelated stages may continue only when
   their independence is demonstrated. Record a reason when no consumer applies.
4. **Renew only invalidated evidence during iteration.** Further edits rerun
   checks whose source, tests, dependencies, contracts, tools, configuration, or
   execution conditions changed. Reuse passing evidence only when freshness is
   proven; do not treat a prior pass as evidence for changed inputs.

Deduplicate checks when changes overlap. Assess deletions and renames using both
old and new dependency relationships. Test cyclic components as one coherent
group where separate ordering is impossible. Generated contracts are classified
by behavior and consumers, not directory name. Independent modules may run
concurrently only with demonstrated isolation; shared mutable resources require
serialization or explicit isolation.

Unknown scope or dependencies require impact investigation and select the safe
aggregate fallback in CI with an explicit reason; never invent a narrow scope
to avoid testing or run unrelated suites locally merely because a selector
returns aggregate commands. Missing tools, untested
behavior, or unavailable external consumers remain documented gaps and block
acceptance when required by the contract. Native CI checks and protections are
not suppressed by local focused results. A flat selector is an affected-test
inventory, not execution order: derive stages from repository evidence and run
the declared Taskfile commands manually unless native tooling enforces staging.

| Changed area | Verify first | Verify after success |
| --- | --- | --- |
| Shared library | Changed library behavior and relevant checks | Affected importing libraries, services, and frontends, including transitive consumers. |
| Backend behavior | Changed handler/service and relevant backend integration | Consumers exercising changed results, errors, authorization, timing, or side effects; affected frontend/backend flows. |
| API, schema, or generated client | Producer behavior, schema/contract, and generation checks | Client compatibility, generated SDK builds/tests, and affected frontend/backend integration flows. |
| Frontend component or state | Changed component/state behavior | Affected screens, callers, and user journeys; backend tests only when a backend contract is affected. |
| Database migration or query | Migration, affected queries, and upgrade compatibility | Services and jobs using affected data, then affected integration flows. |
| Event or background job | Changed producer/worker, event contract, retry and ordering behavior | Affected subscribers, jobs, and downstream side effects. |
| Shared configuration, dependency, or build tool | Relevant configuration/build/tool behavior | Components consuming the changed setting, dependency, artifact, or deployment assumption. |
| Documentation only | Relevant Markdown/link and documentation checks | Executable examples or generated outputs when affected; no unrelated application tests. |

These technology cases are conditional guidance for downstream repositories,
not claims that this documentation repository contains those stacks.

### Final Candidate Verification

After implementation, artifact generation, documentation reconciliation,
review, and all fixes finish, freeze the candidate and run `task check`,
`task test`, and every applicable project-specific gate in CI. One complete final run
is the normal target, not a cap on necessary reruns after defects or changes.

CI MUST cover the complete required gate set, including projects excluded from
focused local testing when they belong to that required set. Do not require a
duplicate full local run before submitting the candidate for CI. A local
handoff may report focused checks passing and CI pending; it is not final
acceptance. Missing or unavailable candidate CI is a delivery blocker, not
permission to replace CI with local results or to waive required coverage.

Full required coverage is mandatory for every final candidate, including small
changes. Reuse a passing result only when deterministic native tooling proves
all relevant inputs, locks, gate definitions, tools, and non-sensitive
execution conditions unchanged. Missing, failed, interrupted, or stale evidence
requires rerunning the affected gate; unknown freshness requires full fallback.
A gate result never proves inputs changed during its execution. Record concise
candidate-bound results, reuse reasons, and final coverage without raw logs.
Record the CI run, exact tested revision, and result. Protected CI may
independently require fresh execution.

## Integration and Acceptance Gates

Verify the actual combined shared-test revision in CI; contributor-only results
cannot prove a different merged revision. Before main merge, verify the
resulting revision in CI whenever relevant inputs differ from the tested candidate.
Required coverage may use proven-fresh evidence; repository protections remain
authoritative. A moving integration base invalidates affected evidence.

Every acceptance criterion has a recorded result and supporting test,
inspection, demonstration, or user-decision evidence. Agents may establish
objective acceptance. Subjective or materially ambiguous product decisions go
to the user. All required gates and acceptance criteria must pass before main
merge; failures are repaired, never waived to gain speed.

## Completion and Release Tracking

Done requires confirmed merge into main and reconciled acceptance criteria,
verification, documentation, catalog, version records, and memory impact.
Handoffs record the exact candidate, review and finding resolutions, gate
results or valid reused evidence, acceptance results, shared integration,
main merge, and remaining release status. Keep secrets, machine-local
information, and raw logs out of tracked evidence.

Deployment and package publication are tracked separately with their own
artifact identity, checks, release evidence, and recovery plan. An applied
version or main merge is not a published artifact. Non-destructive production
releases proceed automatically after required release gates and protections;
destructive production actions retain the scoped human approval boundary.

## Memory Impact Completion Gate

Every completed user-directed task or bounded work item classifies memory
impact as `updated` or `none`, with a rationale in the final handoff and spec
where applicable. Internal commands are not separate memory actions.
Use `updated` for durable decisions, facts, preferences, or consequential open
questions; append both the category entry and `workspace/agents/memory/changelog.md`.
Use `none` when no durable context changes and explain why. Pending memory may
remain only while genuinely unresolved; done requires a resolved classification.

## Spec Version Impact

Follow the [version reservation contract](./versioning.md)
and `workspace/releases.json`. Reserve before implementation; one owner applies
one bump at development start or merge before integration artifacts are built.
Check latest shared reservations before choosing targets and at handoff.
Require applied versions before test or done; publication separately marks
reservations released. Reuse already-applied shared versions without another
bump. Run `task versions:check` as part of complete final verification.

## Repository Automation and Commits

Configure repository-native CI to run the required `task check`, `task test`,
and relevant project gates for the actual candidate and integration revisions.
Shared-test and main merges obey configured host protections. If publication
uses a separate workflow, its checks do not establish automatic PR validation.
Document the repository-specific pipelines and environments in the CI guide.

Iterative checkpoint commits may rely on affected modules and do not establish
final acceptance. A PR may request CI with focused local evidence and CI pending. Complete
passing CI evidence is required before acceptance or completion. Use conventional commit messages:
`type(scope): description`.
