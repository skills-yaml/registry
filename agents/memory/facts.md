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
