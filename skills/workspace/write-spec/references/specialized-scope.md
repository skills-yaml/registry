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

Read `workspace/instructions/tech/infrastructure.md` from the consuming
repository before specifying infrastructure work. OpenTofu is the only
implementation and state-management mechanism. Local work is limited to
configuration changes and non-mutating validation/review through Taskfile.
Applies, destroys, imports and state mutations run only through repository
CI/CD. Acceptance paths using consoles, provider mutation CLIs, alternative
IaC engines or ad hoc provisioning scripts are invalid; CI/CD does not
authorize provider CLI writes. Record incompatible requested paths as blockers.
