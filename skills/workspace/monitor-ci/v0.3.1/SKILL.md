---
name: monitor-ci
description: Monitor a continuous-integration run or pull-request checks through a terminal outcome and report meaningful transitions. Use when the user asks to watch, babysit, follow, or wait for CI without changing code or workflow configuration.
metadata:
  skm-version: "0.3.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "ec01dd7abe4b0a14d40fc1a9ff3ae56f739c115e"
  skm-source-path: "workspace/instructions/skills/monitor-ci"
  skm-source-integrity: "sha256:956a53296e3c54832e5489587550f4caced66d8637974ba509cad8fb79a950cc"
  workspace-toolkit-version: "0.4.2"
  workspace-docs-compatibility: "6.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Monitor CI

Track the requested run until it succeeds, fails, is cancelled, or reaches an
explicit monitoring deadline.

For repository-controlled conflicts, use the applicable current source under
`workspace/instructions/` as the source of truth and report stale conflicting
CI documentation or generated guidance.
Monitoring remains read-only and cannot supply instruction-change approval for
any governed instruction edit.

## Monitor

1. Identify the repository, branch or pull request, workflow, and run to watch.
   Prefer the newest relevant run only when the target is otherwise unambiguous.
2. Record the initial checks, statuses, URLs or identifiers, and commit revision.
3. Poll with bounded intervals and provide concise updates when state changes or
   at least once per minute during active work.
4. Detect replacement, cancellation, rerun, stale revision, or authorization
   failure instead of silently following the wrong run.
5. Stop at a terminal outcome or the user-defined deadline.

Report an infrastructure job that mutates state outside OpenTofu and repository
Taskfile entrypoints as a policy failure. Also report any infrastructure
mutation performed outside the trusted CI/CD workflow or through a provider CLI
such as `gcloud`. Monitoring remains read-only and does not authorize a local or
manual remediation path.

## Hand Off

Report the final outcome, failed or incomplete checks, relevant revision, and
the most useful next diagnostic step. A monitoring-only request remains
read-only. Within a broader delivery task, hand a failure directly to the
authorized CI-fix workflow without asking for repeated human approval; bounded
safe reruns, fixes, test integration, and non-destructive releases are covered
by standing workflow authority.
