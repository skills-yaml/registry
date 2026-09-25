# Facts

## 2026-09-10 - Workspace toolkit 0.3.0 skills published

- Type: fact
- Source: command
- Confidence: high
- Review: none
- Supersedes: none

Content:

Registry commit `3b6a8cc6a62ce881e10731828cd73bafc8383605`
published 19 packages from Workspace production commit
`fb4aa64a6121f1f8a57d4848b52fa0ec7cefd452`, including seven explicit
`wk-*` lifecycle facades at 0.1.0. Registry CI run `34427475083` passed. The
released SKM 0.4.0 binary cloned that registry revision, installed
`workspace/wk-deliver@0.1.0` plus its eight exact dependencies under Codex's
`.agents/skills/` root, passed `skm check`, and reported all nine links already
installed on a second apply.

## 2026-09-25 - Workspace Bundle Published From Toolkit 0.4.2

- Type: fact
- Source: repo
- Confidence: high
- Review: none
- Supersedes: none

Content:

Workspace source revision `ec01dd7abe4b0a14d40fc1a9ff3ae56f739c115e`
generated toolkit 0.4.2 and 20 exact package versions. Registry PR #19 passed
CI and integrated that release into `develop` at
`65ee895d89362ffd475a236883d51257037f6b51`; PR #20 passed CI and
published it through `main` at
`3cfdaf3d7d0eb2bf0e6c461f8dc4ab8317811df7` on 2026-09-25. The
schema-2 `workspace/all-workspace-skills` bundle has all 20 members and no
synthetic skill package. Released SKM 0.7 previewed and installed the bundle
from the live Registry in a clean project, passed `skm check`, and planned no
additions on repetition. Existing exact versions remain additive and immutable.
