# Model Design or Model Delta

Use only applicable sections; record why an omitted layer does not apply.
Reuse equivalent existing documents. Replace guidance with concrete evidence.

## Scope and Evidence

- Mode, effort level and selection rationale:
- Owner, requirements and current/proposed artifact revisions:
- Observed behavior, intended behavior and change:
- Governing technologies, constraints and unaffected boundaries:
- Material questions and explicit hypotheses:

## Scenarios and Language

| ID | Actor/command | Preconditions | Outcome | Failing/counterexample case | Source |
| --- | --- | --- | --- | --- | --- |

| Term/concept | Meaning and context | Identity or value equality | Owner | Evidence |
| --- | --- | --- | --- | --- |

## Behavior and Logical Model

Relationships/cardinality, optionality, lifecycle transitions and history.
Atomic consistency boundaries, concurrency/retries and acceptable staleness.
State/relationship diagrams only if they clarify a decision.

| Invariant ID | Rule and source | Owner | Enforcement point | Counterexample | Test/evidence or gap |
| --- | --- | --- | --- | --- | --- |

## Representation and Consumer Mapping

| Scenario/invariant | Concept/context | Storage field/key | API/event field | Conversion/omission | Direct/transitive consumers | Verification |
| --- | --- | --- | --- | --- | --- | --- |

Access patterns, indexes, constraints and growth limits for the permitted engine.
Separate authoritative data from projections, public contracts and internal data.
Tenant/authorization paths, trusted context, sensitive fields and deletion/retention.

## Schema Semantics

Actual schema dialect, serializer/generator and validator versions/settings.
Required versus missing/null/default; ranges/units/precision, timestamps,
enum/union and unknown-field behavior, errors and limits where relevant.
Positive/negative examples and behavioral claims that require separate evidence.

## Evolution and Recovery

| Supported writer | Supported reader | Stored/wire schema | Expected behavior | Evidence/gap |
| --- | --- | --- | --- | --- |

Retained history, affected owners, rollout order and old/new concurrent writes.
Backfill/checkpoints/stop conditions and verification. Distinguish application
rollback, forward repair and restored data; record irreversible effects.

## Decisions and Verification

Chosen and rejected alternatives with scenario-based rationale.
Changed-component checks, then affected consumers after success; native final
gates and independent review. Evidence revision, actual results and missing tools.
Implementation handoff readiness, unresolved decisions and recovery limits.
