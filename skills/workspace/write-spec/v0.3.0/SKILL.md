---
name: write-spec
description: Turn an accepted problem or feature request into a lifecycle-managed development specification. Use when work needs explicit scope, acceptance criteria, affected areas, validation gates, risks, migration considerations, and memory impact before implementation begins.
metadata:
  skm-version: "0.3.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "bd958c01249e1cb1e1fbbcf91ba70e83abec8d5f"
  skm-source-path: "workspace/instructions/skills/write-spec"
  skm-source-integrity: "sha256:f9ae8a7a155662b27de876f4e12ad23686b984aef46c72011aff47bfe2ed193a"
  workspace-toolkit-version: "0.4.0"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
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
   For Workspace Docs 6.x, use `backlog`, `development`, `test`, or `done` and
   preserve the required `backlog -> development -> test -> done` order.
4. Preserve unrelated work and existing decisions. Mark assumptions and open
   questions instead of presenting them as settled facts.

If two or more agents may mutate the repository concurrently, invoke
`coordinate-multi-agent-development` before delegated edits. Give each
mutating agent a dedicated detached worktree and repository WIP record; keep
the primary checkout coordination-only. A task or delivery branch may be
created or selected only when the user directly requested branch use for the
named task.

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

## Version Impact

Before implementation, include the per-component Version Impact table required
by the pinned standard and register member specs in `workspace/releases.json`.
Classify major, minor, patch, or justified none; declare a shared reservation
with baseline, target, owner, timing, and rationale. Check occupied versions
before proposing a target. Do not apply a development bump to a backlog idea.
