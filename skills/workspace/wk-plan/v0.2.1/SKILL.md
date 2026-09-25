---
name: wk-plan
description: Run the wk.plan lifecycle facade to validate or create an active specification and produce an executable implementation plan. Invoke explicitly when approved work needs ordered steps, affected files, migration handling, validation, rollback, and completion gates.
metadata:
  skm-version: "0.2.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ec01dd7abe4b0a14d40fc1a9ff3ae56f739c115e"
  skm-source-path: "workspace/instructions/skills/wk-plan"
  skm-source-integrity: "sha256:9049a15bd6760c893c3546f95b59ad169dabe5f562d301723bd004d06e8cd375"
  workspace-toolkit-version: "0.4.2"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.3.1, workspace/plan-implementation@0.3.1"
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
