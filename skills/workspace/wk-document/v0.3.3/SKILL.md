---
name: wk-document
description: Run the wk.document lifecycle facade to create or maintain human-facing project documentation within repository ownership boundaries. Invoke explicitly when documentation must be reconciled with current behavior and validated.
metadata:
  skm-version: "0.3.3"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "e205b8c9e4f092adb9b20aaa129e644d858a25ca"
  skm-source-path: "workspace/instructions/skills/wk-document"
  skm-source-integrity: "sha256:83b21c394d7d485d969bf47cef799cf24c33fa83b259e43bcd3dce8167b6c279"
  workspace-toolkit-version: "0.8.0"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/maintain-project-docs@0.3.3"
---

# wk.document

Route the request through `maintain-project-docs`.

1. Require the focused dependency and stop with an actionable installation or
   compatibility error when it is unavailable.
2. Confirm that the user's request authorizes the requested documentation
   writes; invocation alone is not write authority.
3. Let the focused workflow use current code, specs, and authoritative policy
   as evidence, update only declared human-facing documentation roots, reconcile
   affected references, and run repository-native gates.
4. Keep governed instructions out of scope unless the human request names that
   exact instruction change.
5. Report changed documents, validation, memory impact, and deferred gaps.

Do not turn documentation maintenance into an undocumented policy migration.

## Pinned Workflow Routing

Use affected documentation modules during edits. Let the focused workflow
resolve required review before freezing the candidate and running full final
gates. Reconcile the pinned lifecycle without claiming completion or publication
from documentation changes alone.
