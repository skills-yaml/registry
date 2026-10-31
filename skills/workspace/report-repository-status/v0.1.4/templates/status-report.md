# Repository Status

Observed: <UTC time>. Scope: <project/spec/work items>. Sources: <local Git,
live remote queries, catalog, coordination and host APIs>. Overall: <current or
partial, primary blocker>. Observation revisions: <HEAD and named targets>.

## Work Items and Worktrees

| Item / worktree | Ref / HEAD / file state | Change group | Spec / association evidence | Spec state and remaining work | Target | Recommendation / blocker / next step |
| --- | --- | --- | --- | --- | --- | --- |
| <stable label> | <branch or detached, short SHA, staged/unstaged/untracked/conflicted> | <repository-relative paths or unique commits> | <spec link and strong/candidate/unknown/ambiguous/conflicting> | <recorded state versus confirmed delivery, acceptance/review gaps> | <explicit target> | <merge eligible, keep/finish, keep/verify or discard candidate with reason> |

Include unavailable, locked and prunable worktrees; show relevant stash/ignored
work and preservation limits without exposing contents or absolute locations.

## Branches and Remotes

| Local branch / upstream | Local HEAD | Live remote head | Cached ref | Ahead / behind / preservation against named target | Status / gap |
| --- | --- | --- | --- | --- | --- |
| <project ref or consistent alias> | <SHA> | <remote/ref SHA or unavailable/not configured> | <SHA clearly marked cached> | <verified relationship or unknown> | <missing object/upstream, conflict or other limitation> |

Include live remote-only branches and local branches without an upstream.
State query errors, pagination/truncation, stale comparisons and observation limits.

## Next Steps

Prioritize blockers and list the evidence/action needed for each work item.
Separate test-target readiness, main completion and publication. This report
recommends actions; it performs no merges, discards, cleanup or spec changes.
