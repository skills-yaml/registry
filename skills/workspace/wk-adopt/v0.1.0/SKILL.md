---
name: wk-adopt
description: Run the wk.adopt lifecycle facade to assess, adopt, repair, or upgrade a repository's Workspace structure through the focused adoption workflow. Invoke explicitly when the user requests Workspace adoption or migration.
metadata:
  skm-version: "0.1.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "6dbdf01341a8ab5d572179462f1b460ff6259c51"
  skm-source-path: "workspace/instructions/skills/wk-adopt"
  skm-source-integrity: "sha256:1642df00c2738c5d7e5b82b45e1c4c225c4d64f5e0fee78772bb05459ed6c2d4"
  workspace-toolkit-version: "0.3.0"
  workspace-docs-compatibility: "5.x"
  minimum-skm-version: "0.4.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/adopt-workspace-structure@0.2.0"
---

# wk.adopt

Route the request through `adopt-workspace-structure`.

1. Require the focused dependency and stop with an actionable installation or
   compatibility error when it is unavailable.
2. Preserve the user's requested mode: assessment, fresh adoption, upgrade, or
   repair. Skill invocation by itself grants no write authority.
3. Let the focused workflow collect project-local evidence, resolve a complete
   pinned standard, preserve manual policy, validate the migration, and
   reconcile lifecycle and memory state.
4. Stop before governed instruction writes unless the human request explicitly
   authorizes the named adoption or migration scope.
5. Report the adopted version, validation evidence, unresolved compatibility
   gaps, and next lifecycle transition.

Do not reproduce or weaken the focused skill's migration and safety rules.
