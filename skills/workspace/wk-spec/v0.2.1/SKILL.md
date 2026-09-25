---
name: wk-spec
description: Run the wk.spec lifecycle facade to turn an accepted request into a complete, categorized, lifecycle-managed development specification. Invoke explicitly when implementation needs scope, acceptance criteria, affected areas, validation, risks, and memory impact.
metadata:
  skm-version: "0.2.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ec01dd7abe4b0a14d40fc1a9ff3ae56f739c115e"
  skm-source-path: "workspace/instructions/skills/wk-spec"
  skm-source-integrity: "sha256:e034f10d1e49f9a11dca69d920987a1565ab789c91467940cc2e0fc3627fceee"
  workspace-toolkit-version: "0.4.2"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.3.1"
---

# wk.spec

Route the request through `write-spec`.

1. Require the focused dependency and stop with an actionable installation or
   compatibility error when it is unavailable.
2. Preserve the user's accepted problem and use repository evidence plus
   reasonable assumptions. Ask only for a missing decision that materially
   changes behavior or data.
3. Let the focused workflow detect conflicts with authoritative instructions,
   select the single valid feature and lifecycle path, write the complete spec,
   update its canonical catalog, and run repository-native gates.
4. Record governed-instruction approval status accurately. A spec cannot grant
   that approval.
5. Report unresolved decisions and the next allowed transition without starting
   implementation.

Do not duplicate the focused skill's specification template or lifecycle rules.
