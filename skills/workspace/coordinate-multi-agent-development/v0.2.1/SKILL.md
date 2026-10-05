---
name: coordinate-multi-agent-development
description: Let peer agents coordinate on one machine through atomic task and version claims, self-created detached worktrees, shared file scopes, independent review, serialized integration, and lossless recovery. No coordinator agent is required.
metadata:
  skm-version: "0.2.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "f867573bc91b5560d12cebd304ba3dd98aed7435"
  skm-source-path: "workspace/instructions/skills/coordinate-multi-agent-development"
  skm-source-integrity: "sha256:1b251ba31f97239ec09c521d5c765f486b8d9a986c55b1a6b6716db35c21f828"
  workspace-toolkit-version: "0.7.1"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Coordinate Multi-Agent Development

Peers coordinate through a shared local runtime, without a leader agent. This
skill does not grant authority to spawn agents, change governed instructions,
create branches, publish changes, or perform destructive actions. Follow the
applicable current instructions under `workspace/instructions/`.

## Establish the Environment

Use this workflow when two or more agents may modify one repository. The first
implementation requires one machine, a local filesystem, and one Git common
directory. Python 3, Git, and operating-system file locking are required.
Separate clones or machines do not share the board. Do not place its runtime
directory on a network share.

The portable runtime is `scripts/peer_runtime.py` in this skill package and is
invoked directly from the installed package. An optional Taskfile wrapper may
expose the same CLI, but Task is not a runtime dependency. Repositories
register explicit validation argument arrays from their authorized policy.

Any peer can initialize once from a reviewed committed base:

```sh
task peers -- init --base HEAD
```

Initialization never copies uncommitted changes. Save and validate intended
work through the normal workflow before selecting its base. The runtime stores
its atomic JSON board and file lock under `.git/workspace-peers/` in the Git
common directory. New environments store worktrees externally, under the
user-home `worktrees` directory by default. Set `WORKSPACE_WORKTREE_ROOT` before
initialization to choose another absolute, persistent local directory separate from
the primary checkout and its parent directory. Do not use temporary directories, caches,
or network shares. The namespace combines the primary project name with a
digest of the Git common directory, isolating repositories with the same name.
Agent paths use `agents/<task-id>/<agent-id>`; staging and recovery paths use
`integration/<agent-id>` and `archives/<archive-id>` under that namespace.

Initialization records the resolved namespace in the untracked board. Every
peer discovers that board through Git and uses its recorded location even if
its environment differs. Never create manual worktrees beside the project or
directly in its parent directory; use the same external-root policy. Atomic replacement
prevents partial board writes.
Operational state remains untracked; never copy it into project memory or logs.

New environments use board schema 3, which older runtimes reject. Schema-2
boards retain their existing Git-metadata paths without moving or deleting any
worktree. Do not reinitialize a lost board over existing worktrees or change its
storage settings by hand. Migration of an existing environment requires a
separate explicit recovery plan preserving ownership, dirty files, and commits.

## Register the Spec and Task Plan

Register the reviewed spec revision, stable acceptance IDs, and a repository
validation configuration whose commands are JSON argument arrays:

```sh
python3 <installed-skill>/scripts/peer_runtime.py spec-register \
  --spec workspace/specs/development/example/feature.md \
  --criterion AC-1 --criterion AC-2 \
  --validation-config workspace/validation/peer-commands.json
python3 <installed-skill>/scripts/peer_runtime.py plan \
  --task api-change --kind implementation --scope backend/api \
  --criterion AC-1 --expected-plan-revision 0
```

Every plan amendment supplies the last observed plan revision. Invalid
dependencies and cycles fail atomically. A material spec or validation change
requires the current contract revision, marks existing evidence stale, and
preserves commits and worktrees until each affected task is reconciled.

## Self-Claim a Task and Create a Worktree

Each peer independently runs:

```sh
task peers -- ready
task peers -- claim --agent worker-api --task api-change
task peers -- join --agent worker-ui --task ui-support --scope frontend/app
task peers -- status
```

`claim` atomically claims a published unique task and agent identity, checks dependencies,
and creates that peer's detached worktree. Its response includes a worktree
path relative to the invoking checkout. Continue inside that worktree for all
actor operations. No coordinator allocates or approves the claim. Published
scope and dependencies come from the plan; prerequisites must be integrated.

`join` is a compatibility shortcut for unplanned supporting work. Spec-driven
delivery uses `ready` and `claim`; task definitions bind the accepted contract,
criteria, dependencies, scope, validation revision, and status history.
For `join`, repeat `--scope` for multiple paths and use `--depends-on` for
prerequisite task IDs. It cannot override an existing published task plan.

Peers may ALWAYS claim overlapping files, including parent/child directory
scopes. Each worktree isolates its own edits. Scope limits what a peer may
change; it does not grant exclusive file ownership. Semantic and textual
conflicts are resolved during integration. Task identity and version allocation
remain atomic. Claim scopes are fixed for this task; finish it before starting
a new task with a different scope.

Keep the primary checkout coordination-only during concurrent mutation. The
runtime creates no task branches. Outside this detached workflow, ordinary task branches follow the pinned
SDLC authority: v7 task requests suffice; older pins retain direct requests.
Read-only peers remain exempt until they mutate project files.

## Maintain Work Records

`claim` creates a task index and the joining peer's WIP record under
`workspace/docs/work/multi-agent/<task-id>/`. These retain schema version 1,
base revision, scopes, statuses, timestamps, and the required Assignment,
Actions, Validation, Blockers and Dependencies, Next Step, and Handoff sections.
The joining peer owns its task index; there is no coordinator-owned global file.

Update your own record after meaningful edits, validation, blockers, and before
interruption or handoff. Include it in checkpoint commits. Never edit another
peer's working files or record directly. The integration operation projects
completion status into the reviewed task's records in its staging worktree.

Use the runtime's `status` command for live shared progress; private WIP copies
are not a live task board. Records must contain no secrets, credentials, absolute
paths, usernames, hostnames, or raw command transcripts.

## Peer Review and Integration

After local gates pass, commit the task and publish a clean handoff:

```sh
task peers -- handoff --agent worker-api
```

The runtime checks claimed scope, committed WIP records, a detached worktree,
and a clean status, then preserves the exact commit in an internal checkpoint
ref. Another registered peer inspects that commit and records a decision from
its own worktree:

```sh
task peers -- review --agent worker-ui --subject worker-api --revision <commit> --decision approve
task peers -- land --agent worker-ui --subject worker-api
```

Self-review is rejected. Review applies to one exact handoff revision. A new
handoff invalidates older approvals, and any unresolved rejection blocks land.
Any peer may land approved work; no permanent integrator role is required.

`land` serializes integration in a separate detached staging worktree, merges
against the latest internal integration ref, projects record completion, and
runs the registered project validation argument arrays. Only successful, clean results advance the
ref with compare-and-swap and complete the task. Busy callers retry later;
there is no automatic lease expiry or claim stealing.

The internal ref is `refs/workspace-peers/integration`. It is not a task branch
or evidence of shared-test integration, verified main merge, or publication. Normal review,
branch protection, instruction approval, and release policies still apply to
promotion into the configured delivery targets.

After all required planned tasks are current and integrated, one peer records
acceptance coverage for every current criterion on the combined revision and a
different peer reviews that exact report with `accept-review`. Missing coverage,
stale contracts, self-review, and changed combined revisions are rejected.

## Conflicts and Recovery

A conflict or failed gate preserves the staging worktree, checkpoint refs, and
active task claim. Inspect the staged result, then preserve it with:

```sh
task peers -- archive --agent worker-ui --subject worker-api
```

This moves the failed staging worktree into runtime archives without deleting
its dirty files and pins its commit. The author merges the latest internal
integration ref into its OWN worktree, resolves conflicts, reruns gates, commits,
and publishes a new handoff for peer review. Retry land after that approval.
A clean interrupted land can be retried; stale staging bases require archive
first. Archives are retained for explicit recovery, not automatically deleted.

Repeated identical joins return the existing claim. A partially created,
unregistered worktree is preserved and blocks that identity; stop peers and
inspect it before manual recovery. Missing or damaged board state must not be
silently recreated. Quiesce affected processes before resuming an interrupted
identity; the runtime does not stop arbitrary filesystem writers.

After verified integration, a different peer may run:

```sh
task peers -- cleanup --agent worker-ui --subject worker-api
```

Cleanup requires clean detached worktrees whose commits are reachable from the
internal integration ref. Never force-remove a dirty worktree. Verify that
no unique work would be lost; do not delete peer records or runtime archives.

## Version Reservations

Before choosing a version, any peer calls the shared transaction service:

```sh
task peers -- reserve --agent worker-api --component example-api --release example-next --baseline 1.2.3 --impact minor
```

Same-release claims reuse the target and aggregate the highest SemVer impact;
conflicting releases fail. The runtime checks integrated release metadata when
present. Record the reservation in the spec, WIP record, and release ledger;
apply it at the selected lifecycle boundary. Files remain shareable, but any
combined ledger and manifest changes must pass `task versions:check` and match
runtime reservations before integration. Offline claims do not prove remote
published-version availability. No release or version owner gains authority
over other peers or bypasses the governed-instruction approval boundary.

## Hand Off

Report tasks, peer identities, reviewed and integrated revisions, validation,
remaining conflicts, retained worktrees, and recovery state. Reconcile spec
lifecycle only on actual delivery evidence and separately classify memory impact.

## Pinned SDLC Contract

Read the project's pinned SDLC before planning or delivery. For Workspace Docs
7, done means verified merge into main with reconciled acceptance, documentation,
catalog, version records, and memory; deployment/publication is separate.
Blocked records previous stage, kind, reason, and resume condition; resume there
and renew stale evidence. Preserve done history with linked follow-up specs.
Shared test integration is the default; only an explicitly documented direct
route may omit it, preserving all gates. Older pins keep their prior completion
and branch-authority contracts.

For v7, the task request authorizes ordinary task branches and safe delivery.
Security, data integrity, public interfaces, governed instructions, and release
controls always require independent exact-candidate review; other non-trivial
changes require it except small low-risk changes with focused tests.
Resolve every finding by implementation or reviewer-agreed documented rejection.
Run affected modular gates during implementation and review fixes. Reconcile
knowable spec, catalog, and memory records before required review. Finish review,
artifacts, documentation, records, and fixes before freezing the candidate and
running full required checks/tests. Later tracked event/result records renew
affected review and verification; they do not automatically preserve evidence. Reuse only proven-fresh evidence and verify actual
combined integration/main revisions. Each acceptance criterion needs supporting
evidence; subjective product decisions go to the user. Read-only skills remain
read-only and planning skills do not implement changes.
