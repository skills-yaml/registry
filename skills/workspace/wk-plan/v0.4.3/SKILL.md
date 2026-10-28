---
name: wk-plan
description: Run the wk.plan lifecycle facade to validate or create an active specification and produce an executable implementation plan. Invoke explicitly when approved work needs ordered steps, affected files, migration handling, validation, rollback, and completion gates.
metadata:
  skm-version: "0.4.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ea074843f54a3197ae9adf8ada2e770c0caa862c"
  skm-source-path: "workspace/instructions/skills/wk-plan"
  skm-source-integrity: "sha256:188d949ec573aa0b35bc6f0e32b0ac3a790b4d8acc1dcb0075244d34ebf61ee6"
  workspace-toolkit-version: "0.12.0"
  workspace-docs-compatibility: "8.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.6.1, workspace/plan-implementation@0.5.3"
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
resources, freshness, review/finding resolution, and full final gates. Plan
changed-component checks first, then affected direct/transitive consumer stages
gated on upstream success, with selection reasons, fallback, and coverage gaps.
Under v7,
plan main completion separately from deployment/publication and include blocked
resume conditions where needed. Planning does not start deferred implementation.

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
