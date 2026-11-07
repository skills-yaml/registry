# Specialized Scope

Read only the branch triggered by the affected areas. These requirements
supplement the consuming repository's authoritative instructions; they grant
no implementation or mutation authority.

## Domain and Schema

For changed business concepts, lifecycle/invariants, ownership or database/API/
event contracts, use `design-domain-model` in design mode. Produce or reuse
proportionate modeling evidence and carry scenario/invariant IDs,
representation mappings, affected consumers and material questions into the
spec. A clear field/CRUD change needs a model delta, not a mandatory DDD
workshop. Keep unresolved business rules explicit; planning does not authorize
application/schema implementation.

## Infrastructure

Read the consuming repository's `workspace/instructions/tech/infrastructure.md`
and actual pinned SDLC before specifying infrastructure work. Normal management
uses OpenTofu through Taskfile/CI/CD; local agent work is non-mutating.
When the actual pin permits a one-time user-run operation, specify tools/ source,
exact targets and effects, preview/recovery, full applicable requirements and
affected CI evidence, informed scoped approval and human execution. Agents never
execute workstation mutations or provider writes. Establish supported import,
configuration/address and state ownership before manual creation, then require
OpenTofu import and a reviewed matching plan. Block incomplete reconciliation;
older pins retain their restrictions.
