---
name: wk-plan
description: Run the wk.plan lifecycle facade to validate or create an active specification and produce an executable implementation plan. Invoke explicitly when approved work needs ordered steps, affected files, migration handling, validation, rollback, and completion gates.
metadata:
  skm-version: "0.3.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "f867573bc91b5560d12cebd304ba3dd98aed7435"
  skm-source-path: "workspace/instructions/skills/wk-plan"
  skm-source-integrity: "sha256:e49f7f44f92d51fca18c07a14d3e442d058afc249ea640ca02c07f43b1c1ba7b"
  workspace-toolkit-version: "0.7.1"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.4.1, workspace/plan-implementation@0.4.1"
---

# wk.plan

Compose `write-spec` and `plan-implementation`.

1. Require both focused dependencies and stop with an actionable installation
   or compatibility error when either is unavailable.
2. Locate the active specification. If none adequately covers a user-requested
   plan, use `write-spec` first without starting implementation.
3. Stop when the spec is ambiguous, incomplete, not in an implementable state,
   lacks required authority, or conflicts with current authoritative
   instructions.
4. Otherwise use `plan-implementation` to produce dependency-ordered,
   reviewable steps with concrete affected areas, compatibility and migration
   handling, per-step validation, rollback, and completion gates.
5. Report assumptions, blockers, and the exact implementation handoff.

Do not edit product code or treat planning as authority to deliver changes.

## Pinned Workflow Routing

Have the focused plan declare module inputs, dependencies, consumers,
resources, freshness, review/finding resolution, and full final gates. Under v7,
plan main completion separately from deployment/publication and include blocked
resume conditions where needed. Planning does not start deferred implementation.
