# Domain, Data Model and Schema Design Contract

This guide defines the shared modeling artifact contract. Apply it only when
modeling is relevant and within the host's approved scope. Preserve its chosen
technology and governance. The design-domain-model skill supplies the procedure;
its portable modeling-contract reference is a checked copy of this guide.

## Evidence and Proportion

Identify scope, owner, input/artifact revisions and sources. Distinguish observed
behavior, requirements, proposals and hypotheses. Reuse equivalent project docs.
A small field/CRUD change needs a model delta; new domain behavior needs scenarios
and logical-model decisions; cross-boundary evolution additionally needs consumer,
migration and recovery evidence. Explain omissions rather than creating empty
documents. Diagrams illustrate decisions without becoming another source of truth.

## Connected Representations

| Layer | Meaning to establish |
| --- | --- |
| Domain | Language/context, actors, commands/outcomes, identity, rules and lifecycle. |
| Logical model | Entities/values, relationships, cardinality, optionality and ownership. |
| Storage | Permitted engine, keys, access patterns, constraints/indexes and consistency. |
| Contracts | Public input/output/events, field semantics, versions and visibility. |
| Evolution | Supported readers/writers, retained data, rollout, validation and recovery limits. |

One business concept may have different storage and external representations.
Assign an authoritative source to each contract and document conversions,
omissions and derived fields. Do not expose internal secrets just to align shapes.
Keep canonical definitions within their context; do not force one global model.

Use a concise traceability table with source/scenario, concept/context, invariant,
representation, enforcement, consumer, test/evidence and omission rationale.
Equivalent existing mappings are acceptable. Every critical rule has an owner,
enforcement location and a concrete failure example; unknown evidence is a gap.

## Behavior and Integrity

Specify identity versus descriptive equality, cardinality/uniqueness, time/units,
allowed lifecycle transitions and deletion/history semantics where relevant.
Account for concurrent writes, retries, idempotency, atomicity and acceptable
staleness. State which rules belong to storage constraints, application behavior
or an authorization boundary; a valid payload is not proof of a valid operation.

Model tenant isolation and resource authorization across the actual read/write
paths. Separate trusted server-derived context from client claims. Identify
sensitive fields, purpose, exposure and retention/deletion propagation. Use
synthetic examples without secrets or personal data. Storage/security mechanisms
depend on the selected engine and client/server access path, not a diagram label.

## Schema Semantics and Evolution

Pin the actual format/dialect and tools. Distinguish missing, null and defaults;
define range/precision/units, timestamp interpretation, enums/unions, unknown
fields, collection limits and error behavior where applicable. Verify converter
behavior and field visibility across storage, domain and external boundaries.

Assess compatibility by supported old/new readers and writers, retained data,
encoding and actual consumers. Adding a field or enum value is not universally
compatible. Record affected direct/transitive consumers and deployment order.
For migrations include backfill/concurrent writes, checkpoints, stop conditions,
verification and recovery limits. Application rollback and data restoration are
separate claims; a down migration may destroy rather than restore information.

## Verification and Handoff

Check the changed representation first; only after success check its affected
consumers in dependency order. Keep required native integration/end-to-end and
final gates. Parsing, schema examples and static types demonstrate structure;
business/security/concurrency and migration claims need corresponding evidence.
Missing tools or coverage cannot be reported as passes.

Upstream model changes invalidate affected downstream decisions and checks.
Independent review applies under the host's risk rules. Implementation-ready
handoffs identify decisions, rejected alternatives, mappings, consumer impact,
validation and rollout/recovery limits, with no unresolved material business rule.
Assessment/review remain read-only; designs change only authorized artifacts.
No modeling request by itself grants production migration or infrastructure
mutation authority. Respect prospective instruction approval and the applicable
OpenTofu/CI/CD boundary.
