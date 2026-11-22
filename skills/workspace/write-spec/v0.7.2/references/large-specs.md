# Large Specifications

Use when scope needs separate implementation, review or validation boundaries.
Split by deliverables, dependencies, migrations and risk, rather than page
length, fixed step count or an arbitrary time estimate.

For each ordered step assign a stable ID and define:

- one concrete outcome, bounded affected areas and exclusions;
- prerequisites, earlier-step dependencies and unresolved decisions;
- measurable acceptance criteria mapped to overall spec criteria;
- the smallest meaningful changed-component and affected-consumer checks,
  selection reasons and evidence required for completion.

Split again if a step still combines independently reviewable tasks. Plan one
ready step at a time per agent and require passing acceptance evidence before
dependent steps begin. Unresolved decisions block dependent work while
established independent steps may still be planned. Keep edits and tests within
the step's scope.

Preserve cross-step contracts, compatibility, migration/rollback safety,
integration checks and the pinned final gates. Passing isolated steps does not
establish overall feature acceptance. Never split tightly coupled invariants
into unsafe intermediate states.

Use one spec when steps share a delivery and lifecycle. Use linked child specs
for independently deliverable/lifecycle-managed parts: the parent records the
overall outcome, dependencies and acceptance mapping; children link back and
each follow feature, catalog, lifecycle, version, approval and memory rules.
The parent remains incomplete until overall acceptance and pinned completion
requirements are met. Preserve completed specs with linked follow-ups.
