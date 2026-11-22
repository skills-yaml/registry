# Migration to Workspace Docs 9.0.1

This patch corrects contradictory scope/approval wording in v9.0.0. It retains
v9 lifecycle, affected CI, review, protection and version contracts. No new
workflow, schema or gate is required. From older pins, first apply the relevant
migration notes through [v9.0.0](../v9.0.0/migration.md).

Update the generated agent block from this version's agents-template.md,
preserving manual rules outside the approved scope. Reconcile current delivery
instructions with [scope and proportionality](./sdlc.md#scope-and-proportionality):
bounded repairs need observed failures, and release requests reuse established
artifacts/workflows. Substantial expansion needs prospective approval.
Refresh installed role profiles through the existing installer and verify their
actual instructions against canonical sources; lock metadata alone is insufficient.
Validate affected instructions and consumers using existing gates. Preserve all
older released packages and historical evidence.
