# Migration to Workspace Docs 10.0.0

This major release adds an explicitly approved human-run one-time operations
exception to the former absolute local infrastructure boundary. Preserve all
older released packages and their pinned restrictions. CI remains mandatory
for final verification, and normal infrastructure management stays in OpenTofu
through Taskfile/CI. No agent receives local mutation authority.

Update the generated context from agents-template.md, preserving manual rules.
Reconcile current SDLC/infrastructure/task guidance, skills and roles with
[the one-time operation contract](./sdlc.md#one-time-user-run-operations).
Tools live under tools/<operation>/ and require exact reviewed inputs/targets,
CI, informed approval, human execution and outcome evidence. For infrastructure,
prove import/ownership feasibility and plan configuration/state reconciliation
before manual creation. Older blanket rules must not silently override or widen
this scoped exception. Update enforcement/tests and regenerate native profiles.

From older pins, apply the relevant earlier migration notes first. Adoption
of this policy does not approve any particular operation or execute a tool.
