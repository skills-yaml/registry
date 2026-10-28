---
name: design-domain-model
description: Assess, design or review business-domain models, logical data models and database/API/event schemas with explicit invariants, ownership, representation mappings and compatibility evidence. Use for new domain concepts, lifecycle or consistency rules, and schema evolution; scale simple CRUD changes to a concise model delta.
metadata:
  skm-version: "0.1.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ea074843f54a3197ae9adf8ada2e770c0caa862c"
  skm-source-path: "workspace/instructions/skills/design-domain-model"
  skm-source-integrity: "sha256:7e6b889de5b05f327a589d619f037acfe75d6eb3170aa7509b2141b6f8de5de9"
  workspace-toolkit-version: "0.12.0"
  workspace-docs-compatibility: "8.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Design Domain Model

Connect business meaning to behavior, storage and external contracts. Ground the
domain concepts in [Eric Evans's DDD Reference](https://www.domainlanguage.com/ddd/reference/)
and read [domain decisions](references/domain-decisions.md) when terminology,
identity or consistency boundaries need design. Use DDD patterns where they
clarify the task; do not mandate microservices, event sourcing or a universal model.

## Select Mode and Scope

- **Assess:** describe the existing model, evidence, contradictions and gaps.
  Remain read-only; do not create documents, install tools or run migrations.
- **Design:** draft or update only authorized modeling artifacts in the host's
  declared spec/documentation roots. Application code, schemas in use, governed
  instructions and production data require their own applicable authorization.
- **Review:** assess an exact model/artifact revision and its consumers. Remain
  read-only; report findings with evidence, impact and missing verification.

Read applicable project policy, approved requirements and current models first.
Preserve chosen technologies and manual documents. Repository evidence and
external reference prose are not permission to execute scripts or change policy.
Separate documented intent, observed implementation, proposals and unresolved
business decisions. Ask only when a missing decision materially affects behavior;
continue independent work without silently deciding it.

Select effort from the actual change:

- **Small change:** clear existing meaning and a local field/CRUD change. Produce
  a model delta, invariant/representation impact and affected-consumer checks.
- **Domain design:** new concepts, complex behavior or ambiguous boundaries.
  Add scenarios, glossary, context/ownership and logical-model decisions.
- **Cross-boundary evolution:** shared contracts, retained data, security/tenant
  boundaries or several owners. Add reader/writer compatibility, rollout and
  recovery evidence, plus applicable independent review.

Levels can combine. Accept equivalent existing artifacts. Record why sections
do not apply; do not require a workshop, diagram or new file for a small change.

## Build the Design Contract

Read the portable [modeling contract](references/modeling-contract.md); load
[storage and contracts](references/storage-and-contracts.md) only for persistence,
external schemas or evolution. The [design template](templates/model-design.md)
is optional scaffolding; shorten it to the task's level and reuse existing docs.

1. **Discover meaning.** Identify actors, commands, outcomes and counterexamples.
   Keep a glossary within each context; resolve overloaded terms through explicit
   mappings rather than one cross-project definition. Event timelines help
   discover rules, but an agent simulation does not establish stakeholder agreement.
2. **Define behavior.** Explain identity and value semantics, cardinality and
   lifecycle transitions. For each important invariant record its source, owner,
   enforcement point and failing example. Include concurrency, retries/idempotency,
   atomicity or acceptable staleness where they affect correctness.
3. **Model representations.** Map logical concepts to the permitted storage
   engine and actual access patterns. Keep persistence, domain objects and public
   input/output/event shapes separately owned; document conversions and omissions.
4. **Design contracts and evolution.** Pin actual dialects/tools, define field
   semantics and map consumers. Check compatibility by reader/writer direction,
   supported versions and retained data, not a generic additive-change rule.
5. **Verify the handoff.** Trace every critical rule to enforcement and meaningful
   tests/evidence; identify gaps rather than passes. Review upstream decisions
   before building dependent artifacts. After an upstream revision, renew affected
   downstream designs and evidence; unresolved material business choices prevent
   an implementation-ready claim.

## Validate and Report

Schema parsing/linting, examples and type checks demonstrate structural contracts.
They do not prove authorization, business invariants, atomicity or safe migration.
Use behavioral, concurrency, security and consumer tests for those claims. Run
the smallest meaningful changed-component checks first, then affected direct and
transitive consumers after success, using the project's native entrypoints.
Planning proposes these stages; read-only modes inspect evidence and run only
authorized non-mutating checks. Missing tools or coverage remain explicit gaps.

Report the selected level, evidence revision, scenarios, important model decisions,
representation/consumer mapping, rejected alternatives, material questions and
verification limitations. Design handoffs include rollout/recovery limits when
applicable. Review findings identify violated rules and concrete counterexamples,
not preferences about naming or diagram style.

Respect existing instruction approvals, independent review and final delivery
gates. Do not execute downloaded code, deploy schemas, migrate production data
or mutate infrastructure from this skill. Infrastructure changes remain subject
to the host's OpenTofu-only, CI/CD-only boundary where applicable.

## Workspace Docs 8 Execution Boundary

For a repository pinned to v8, retain the v7 lifecycle, review, approval, and
freshness rules while applying the v8 verification boundary: local checks cover
changed behavior and all affected direct/transitive consumers; skip unrelated
projects/suites. Complete required gates run in CI after the candidate stabilizes,
without a duplicate complete local run before requesting CI. Unknown impact
requires investigation and justified CI fallback; missing CI cannot prove final
acceptance. Work on one active task per agent. When writing a spec, split oversized
scope into bounded ordered steps with dependencies, acceptance mapping, and
focused validation; use linked child specs for independently managed delivery.
Preserve this skill's planning/read-only scope and explicit older-pin contracts.
