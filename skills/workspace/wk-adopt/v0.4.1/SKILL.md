---
name: wk-adopt
description: Run the wk.adopt lifecycle facade to assess, adopt, repair, or upgrade a repository's Workspace structure through the focused adoption workflow. Invoke explicitly when the user requests Workspace adoption or migration.
metadata:
  skm-version: "0.4.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "5d12491288a6f28ebfcfc23b3b288bbcecd85732"
  skm-source-path: "workspace/instructions/skills/wk-adopt"
  skm-source-integrity: "sha256:423899fe5255aa03ed456aa476dcdfc4beb97819af69dfc9fb0373143a87c600"
  workspace-toolkit-version: "0.11.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/adopt-workspace-structure@0.9.0"
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
