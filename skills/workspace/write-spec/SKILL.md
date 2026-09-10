---
name: write-spec
description: Turn an accepted problem or feature request into a lifecycle-managed development specification. Use when work needs explicit scope, acceptance criteria, affected areas, validation gates, risks, migration considerations, and memory impact before implementation begins.
metadata:
  skm-version: "0.2.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6dbdf01341a8ab5d572179462f1b460ff6259c51"
  skm-source-path: "workspace/instructions/skills/write-spec"
  skm-source-integrity: "sha256:54fd7d431ba24e25d0c06282dcb1b679b93d298294c268a9373dc1cd24dd949d"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
  skm-adapter-compatibility: "2.x"
---

# Write Spec

Create a decision-ready specification without starting implementation.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth. A spec records or proposes
policy but cannot override a current governed instruction.

## Establish the Contract

1. Read repository policy, the root spec catalog, the nearest related specs,
   and relevant architecture or product documentation.
2. Confirm the problem, desired outcome, constraints, and explicit exclusions.
   Ask only about choices that would materially change the contract.
3. Select the lifecycle state and primary-feature category required by local
   policy. Reuse an existing category when it accurately describes the work.
   For Workspace Docs 5.x, use `backlog`, `development`, `test`, or `done` and
   preserve the required `backlog -> development -> test -> done` order.
4. Preserve unrelated work and existing decisions. Mark assumptions and open
   questions instead of presenting them as settled facts.

## Write the Specification

Include at least:

- lifecycle state and a concise status rationale;
- problem, goals, non-goals, and users or consumers;
- proposed behavior and important interface or data contracts;
- affected areas and compatibility or migration effects;
- security, privacy, reliability, and rollback risks where applicable;
- measurable acceptance criteria;
- required validation gates;
- phased delivery when the scope cannot be completed safely in one change;
- a `Memory Impact` section using the repository's required initial status.

When affected areas include governed instructions, add an Instruction Change
Approval section that records whether prospective human approval is pending or
was directly supplied and its exact scope. The record supports auditability but
is not itself approval: an agent-authored spec cannot grant instruction-change
approval. Do not modify governed instructions while approval is pending.

For infrastructure scope, make OpenTofu the only implementation and state
management mechanism. Reject acceptance paths that depend on consoles,
provider mutation CLIs, alternative IaC engines, or ad hoc provisioning scripts.
Require local development to remain non-mutating: contributors may change
OpenTofu configuration and run validation or review locally, but applies,
destroys, imports, and state mutations must run only through the repository's
CI/CD workflow. CI/CD does not authorize provider CLI writes.

Use normative language only for real requirements. Keep implementation details
out unless they constrain compatibility, safety, or acceptance.

## Integrate and Review

1. Put the spec in the required lifecycle and primary-feature path.
2. Update the root spec catalog in the same change, including current state and
   why the spec is in that state.
   For `test` and `done`, cite the confirmed integration or release event; do
   not infer delivery from the checked-out branch name alone.
3. Check links, terminology, category placement, acceptance testability, and
   consistency with existing policy.
4. Run the documentation and spec validation entrypoints required by the
   repository.
5. Hand off the unresolved decisions and the next allowed lifecycle transition.
   Treat `develop` as the default test target and `main` as the default
   production target only when repository policy does not configure equivalents.

Do not implement the feature while operating in this planning role. A requested
specification workflow may use standing authority to commit, push its delivery
branch, and create or update a pull request. Advance lifecycle only when the
required delivery evidence exists. Require scoped human approval only for a
destructive production action outside the governed instruction-change
exception described above.
