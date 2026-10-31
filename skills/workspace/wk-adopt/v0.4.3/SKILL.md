---
name: wk-adopt
description: Run the wk.adopt lifecycle facade to assess, adopt, repair, or upgrade a repository's Workspace structure through the focused adoption workflow. Invoke explicitly when the user requests Workspace adoption or migration.
metadata:
  skm-version: "0.4.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "3fae5b83a7a8324e871d7e707f1c73498b02bb1f"
  skm-source-path: "workspace/instructions/skills/wk-adopt"
  skm-source-integrity: "sha256:6559e279c5c9bbc270925b160fa7c497b12e914567fde06da627b69f9b5e6595"
  workspace-toolkit-version: "0.13.0"
  workspace-docs-compatibility: "9.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/adopt-workspace-structure@0.11.0"
---

# wk.adopt

Route the request through `adopt-workspace-structure`.

1. Require the focused dependency and stop with an actionable installation or
   compatibility error when it is unavailable.
2. Preserve the user's requested mode: assessment, fresh adoption, upgrade, or
   repair. Skill invocation by itself grants no write authority.
3. Let the focused workflow collect project-local evidence, ask the user about
   missing, unclear, or conflicting information, and involve the user
   in material architecture/technology choices, including explained alternatives
   and actionable specs for agreed deferred improvements. Delegate its complete
   pinned-standard resolution, manual-policy preservation, required conformance,
   validation, lifecycle and memory handling without skipping the conversation.
4. Stop before governed instruction writes unless the human request explicitly
   authorizes the named adoption or migration scope.
5. Report the adopted version, validation evidence, unresolved compatibility
   gaps, and next lifecycle transition.

Do not reproduce or weaken the focused skill's migration and safety rules.

## Pinned Workflow Routing

Resolve the concrete target standard through the focused skill. For v7,
include blocked metadata and main-based completion in the migration map;
preserve historical done specs and older pinned contracts. Governed migration
changes require independent review before full final verification.

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

## Workspace Docs 9 Affected CI

For a v9 pin, complete final verification means every required affected CI job,
not every project/job in the repository. Docs/spec-only changes run related jobs;
backend-only and frontend-only changes run their own jobs. Shared inputs include
all proven direct/transitive consumers. Use validated job selection and preserve
required status/protections, dependency stages, and this skill's authority.
Unknown scope needs investigation and a justified fallback. Do not restore a
blanket full-repository CI run for known narrow scope. Older pins retain their
contracts; publication checks remain separate from ordinary change validation.
