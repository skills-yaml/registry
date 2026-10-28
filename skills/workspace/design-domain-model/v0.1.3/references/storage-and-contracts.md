# Storage, Contracts and Evolution

Read only sections relevant to the selected engine and changed boundaries.
Current project instructions decide the stack. These references are design aids,
not authorization to introduce another database or migrate an application.

## Storage Decisions

Record real access patterns and expected growth before indexes or embeddings.
For each authoritative fact identify its owner, all writes, how duplicates stay
consistent and how deletion/retention propagates. Separate projections/caches
from authoritative records. State what remains consistent within an atomic
operation and what may be stale across records or services.

For a permitted relational engine, start with keys, dependencies and constraints;
justify deliberate denormalization by measured or required access behavior.
Document foreign-key/delete behavior and null/uniqueness semantics. PostgreSQL
row CHECK constraints are not a general cross-row invariant mechanism; concurrent
rules need appropriate constraints/transactions. [PostgreSQL constraints](https://www.postgresql.org/docs/18/ddl-constraints.html),
[transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html).

For document stores, justify embedding versus references from query/update
patterns, bounded document growth and consistency requirements. [MongoDB relationship design](https://www.mongodb.com/docs/manual/data-modeling/schema-design-process/map-relationships/)
illustrates these engine-specific choices; it does not prescribe MongoDB.

For Firestore, document collection/document identity, query indexes, concurrency
and transaction retry behavior. Transaction callbacks may repeat: keep external
side effects outside a retrying callback and explain how any emitted operation
is deduplicated. Do not infer SQL foreign keys or exactly-once processing.
Client Security Rules and server authorization are separate paths; privileged
server libraries bypass those rules and require IAM plus application checks.
[Transactions](https://firebase.google.com/docs/firestore/manage-data/transactions),
[indexes](https://firebase.google.com/docs/firestore/query-data/index-overview),
[Security Rules and server access](https://firebase.google.com/docs/firestore/security/rules-conditions).

## Executable Contracts

Use the repository's established JSON Schema/OpenAPI/AsyncAPI, Avro, Protobuf or
other format and supported tools. Pin a dialect/version; a new standard release
is not proof that validators, generators or every consumer supports it.
[JSON Schema 2020-12](https://json-schema.org/draft/2020-12),
[OpenAPI](https://spec.openapis.org/oas/v3.2.1.html),
[AsyncAPI](https://www.asyncapi.com/docs/reference/specification/v3.1.0).

For changed fields define the distinctions consumers can observe: requiredness,
missing/null/default behavior, mutability, range/precision/units, enum/union
extensibility, timestamp/timezone, unknown properties and size limits. Input,
response and event representations may have different fields and validation.
Do not derive public schemas directly from persistence without a visibility and
conversion review. Authentication and valid IDs alone do not authorize resources.

JSON Schema `format` is annotation by default. Check actual validator settings
and negative examples before claiming date/email or another semantic format is
enforced. A schema default does not automatically populate a missing value.
Closed objects and composition need the selected dialect's actual semantics;
test the intended unknown-field behavior rather than infer it from an example.
[Type/format guidance](https://json-schema.org/understanding-json-schema/reference/type),
[default annotations](https://json-schema.org/understanding-json-schema/reference/annotations),
[object/composition behavior](https://json-schema.org/understanding-json-schema/reference/object).

Run positive, negative, boundary and conversion examples with native tools.
Malformed values, excessive lengths/nesting, unknown enums and null-versus-missing
deserve explicit cases when relevant. Use local pinned schema resources; external
reference fetching can add trust, availability and nondeterminism concerns.

## Compatibility and Recovery

Record what each supported reader accepts from each supported writer, including
historical persisted records/events. Backward, forward and transitive checks
mean different things and vary by format. A schema-only compatibility pass does
not establish semantic compatibility: units, meanings, side effects and error
behavior can change without a structural diff. [Schema evolution](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html).

Use a matrix with producer/consumer version, encoding/schema, supported payload,
expected outcome and test evidence. Include all active versions and retained
history actually supported; do not silently assume compatibility with every
version ever shipped. Verify affected providers/clients with native contract
tests where available. [Consumer contracts](https://docs.pact.io/).

Plan expand, backfill, verify, switch and later contract where appropriate.
Account for concurrent old/new writes, retry/idempotency, traffic switch order,
observability, checkpoints and failure stops. Separate safe application rollback
from forward repair or data restoration. Deleting a field/data or rewriting
historical events requires an explicit retention and recovery decision.
[Evolutionary database design](https://martinfowler.com/articles/evodb.html).

Design these operations and their checks; execute them only through separately
authorized workflows. Never substitute a local provider CLI or console write
for the host's infrastructure policy.
