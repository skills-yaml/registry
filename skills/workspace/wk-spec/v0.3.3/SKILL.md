---
name: wk-spec
description: Run the wk.spec lifecycle facade to turn an accepted request into a complete, categorized, lifecycle-managed development specification. Invoke explicitly when implementation needs scope, acceptance criteria, affected areas, validation, risks, and memory impact.
metadata:
  skm-version: "0.3.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "e205b8c9e4f092adb9b20aaa129e644d858a25ca"
  skm-source-path: "workspace/instructions/skills/wk-spec"
  skm-source-integrity: "sha256:ae31c5b3ad406ecaf0d7d288e3052dce684981e9d19e7d985da841088b4e1bd3"
  workspace-toolkit-version: "0.8.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/write-spec@0.4.3"
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

## Pinned Workflow Routing

Have validation criteria specify changed-component checks followed by affected
direct/transitive consumer stages gated on success, with selection reasons and
coverage gaps. Preserve full final verification and planning-only boundaries.

Use the pinned states and completion definition through write-spec. For v7,
include blocked metadata when applicable, preserve done history with linked
follow-ups, and plan independent review before full final verification. Keep
specification work separate from implementation.
