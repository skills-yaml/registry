# Repository Status

<!--
Fixed response contract. Every agent emits these sections, labels, columns and
vocabulary in this order so reports stay comparable across agents and runs.
Never rename, reorder or drop a heading, summary label or table column, and
emit none of the text inside these comments.

Markers, used exactly:
- `None observed.` is the whole body of an in-scope section with nothing to show.
- `Not in scope for this request.` is the whole body of an excluded section.
- `none` fills a summary value, list item or table cell with nothing to show.
- `unknown` fills a value that could not be established. Never leave it blank.

Overall, first match wins:
- `stale`: a relevant HEAD, status or live branch head moved during observation
  and was not re-read.
- `partial`: a requested source was unavailable, failed or was truncated.
- `current`: every requested source was observed and stayed unchanged.
-->

## Summary

- **Overall:** <current | partial | stale> — <primary blocker or `none`>
- **Observed:** <UTC timestamp>
- **Scope:** <full repository | project | specs: ids | work items: labels>
- **Revisions:** HEAD <short SHA> (<ref or detached>); <target> <short SHA> (<live | cached | unknown>)
- **Sources:** <local Git, live remotes, spec catalog, coordination board, host API; mark each unavailable source>
- **Work items:** <n> total — <n> merge eligible, <n> keep/finish, <n> keep/verify, <n> discard candidate
- **Specs:** <n> backlog, <n> development, <n> test, <n> blocked, <n> done; <n> mismatches
- **Top blockers:**
  1. <most consequential blocker or `none`>

## Work Items and Worktrees

| Item / worktree | Ref / HEAD / file state | Change group | Spec / association | Target | Recommendation | Blocker / next step |
| --- | --- | --- | --- | --- | --- | --- |
| <stable label> | <branch or detached>, <short SHA>, <clean, staged, unstaged, untracked or conflicted> | <repository-relative paths or unique commits> | <spec link>; <strong, candidate, ambiguous, conflicting, unassociated or unknown> | <explicit target> | <merge eligible, keep/finish, keep/verify or discard candidate> | <reason and smallest next action> |

<!--
One row per work item, including unavailable, locked and prunable worktrees.
Note relevant stash/ignored work and preservation limits in the Blocker / next
step cell without exposing contents or absolute locations.
-->

## Spec Status

| Spec | Feature | Catalog state | File state | Consistency | Delivery evidence | Open acceptance / gates | Linked work | Next step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <repository-relative spec link> | <primary feature> | <catalog state> | <directory and recorded State> | <consistent, mismatch or unverified> | <test integration, main merge and publication each as verified, recorded only or none> | <unmet criteria, review, CI, version or memory gaps; blocked kind, reason and resume condition; or `none`> | <work item labels, PRs or `none`> | <smallest next lifecycle action or `none`> |

<!--
One row per backlog, development, test and blocked spec in scope. Add a done
spec only when it is requested, linked to current work or a mismatch; otherwise
it is counted only in the summary. Include legacy specs only when requested.
-->

## Branches and Remotes

| Local branch / upstream | Local HEAD | Live remote head | Cached ref | Relationship to named target | Status / gap |
| --- | --- | --- | --- | --- | --- |
| <project ref or consistent alias> | <short SHA> | <short SHA, unavailable or not configured> | <short SHA, marked cached> | <ahead/behind, ancestor, not ancestor or unknown> | <missing object/upstream, conflict, other limitation or `none`> |

<!--
Include live remote-only branches and local branches without an upstream.
-->

## Next Steps

1. <highest-priority action, owning work item or spec, and target>

<!--
Order by priority. Keep test-target readiness, main completion and publication
as separate steps. The report recommends actions only; it performs no merges,
discards, cleanup or spec changes.
-->

## Evidence Gaps

- <unavailable source, query error, truncation or stale comparison>
