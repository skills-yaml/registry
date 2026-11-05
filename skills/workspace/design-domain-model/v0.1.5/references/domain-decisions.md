# Domain Decisions

## DDD Vocabulary

Eric Evans's [DDD Reference: Definitions and Pattern Summaries](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
(2015) supplies the foundation. These are brief original paraphrases; the
reference is guidance, not a formal compliance standard or project authority.

| Concept | Design question |
| --- | --- |
| Ubiquitous language | Which terms do domain experts and implementation share within this context? |
| Bounded context | Where does this model and its meaning apply, and who owns it? |
| Entity | What identity persists when attributes or representations change? |
| Value object | Is equality defined by descriptive values rather than independent identity? |
| Aggregate | Which related state must preserve business invariants as one consistency boundary? |
| Domain service | Which domain operation does not belong naturally to a single entity/value? |
| Domain event | Which meaningful domain occurrence has happened? |

For complementary author explanations see [bounded contexts](https://martinfowler.com/bliki/BoundedContext.html)
and [aggregates](https://martinfowler.com/bliki/DDD_Aggregate.html). A context is
not automatically a deployed service. A table, REST resource or object graph
does not by itself determine an aggregate boundary.

## Questions That Change the Design

Start with a successful scenario and a plausible failure, then ask what must
remain true after either. Identify rule sources and ambiguities before choosing
classes. State differences between requirements and observed behavior.

- If two records describe the same party, who decides they are the same entity?
  Do not merge identities based solely on a mutable email address or display name.
- If ownership changes, does identity remain stable? Which history must survive?
- Can two commands race, and which outcome is permitted? Distinguish validation
  before a write from enforcement at the actual atomicity boundary.
- Does the same term mean different things to different owners? Record the
  mapping, version/ownership boundary and translation responsibility.
- Which operations are legal in each lifecycle state? Define repeated calls,
  retries, invalid transitions and partial failures where relevant.

Prefer the smallest useful behavior model. A CRUD catalog with no rich rules can
use a simple logical model and constraints; a complex lifecycle may warrant
entities, value objects, aggregates and services. Justify choices by scenarios,
not a target number of patterns. Do not introduce CQRS/event sourcing just to
produce domain events or separate a public schema from storage.

## Example: Evidence Versus Assumption

Synthetic requirement: a confirmed reservation consumes one unit of capacity;
the same tenant/request key must not consume capacity twice. A request schema
can validate a positive quantity, but two individually valid concurrent requests
can still exceed available capacity. The design must identify the owner and
atomic enforcement of the capacity rule, plus retry-safe request identity.
Whether pending reservations consume capacity is a business question unless a
requirement answers it. Do not invent that answer from field names.

Use [EventStorming](https://www.eventstorming.com/) when collaborative process
discovery is useful. Mark an agent-authored timeline as a hypothesis and retain
unresolved disagreements; it is not evidence that a workshop took place.
