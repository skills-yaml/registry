# CI Outcome

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

Use repository-relative paths; never include secrets, credentials, credential-bearing
URLs, absolute local paths or personal identifiers.
-->

<!--
Result, first match wins:
- `unknown`: the run could not be identified, or authorization failed or the
  run became unobservable and no failed required check was observed.
- `superseded`: a newer run or revision replaced the watched one.
- `failure`: any required check failed.
- `cancelled`: the run was cancelled without a newer replacement.
- `deadline reached`: checks were still pending at the monitoring deadline.
- `success`: every required check succeeded.
Check status: `success`, `failure`, `cancelled`, `skipped` or `pending`.
Transition event: `started`, `rerun`, `replaced`, `stale revision`,
`authorization failure`, `cancelled`, `failed` or `completed`. Error excerpts are at most three redacted lines.
While monitoring, send each interim update as one line:
`[HH:MM:SS UTC] <check>: <old status> → <new status>`.
-->

## Summary

- **Result:** <unknown | superseded | failure | cancelled | deadline reached | success>
- **Observed:** <start UTC> → <end UTC>
- **Scope:** <repository, branch or PR #n, workflow>
- **Revision:** <short SHA> (<current head | stale>)
- **Sources:** <host API, run logs; mark each unavailable source>
- **Run:** <run identifier and link>

## Checks

| Check | Status | Duration | Link | Note |
| --- | --- | --- | --- | --- |
| <check> | <success, failure, cancelled, skipped or pending> | <duration> | <link> | <note or `none`> |

## Transitions

| Time (UTC) | Event | Detail |
| --- | --- | --- |
| <HH:MM:SS> | <started, rerun, replaced, stale revision, authorization failure, cancelled, failed or completed> | <detail> |

## Failures

| Check | Failing step | Error excerpt | Likely cause | Next diagnostic step |
| --- | --- | --- | --- | --- |
| <check> | <step> | <at most three redacted lines> | <cause or `unknown`> | <step> |

## Lifecycle Evidence

| Stage | Evidence | Status |
| --- | --- | --- |
| <stage> | <PR, revision or run> | <verified, pending or not in scope> |

<!--
One row each for: test-target merge, main completion, publication. Passing CI
alone does not prove done.
-->

## Evidence Gaps

- <unavailable source, query error, truncation, stale comparison or missing tool>

## Next Steps

1. <highest-priority action that follows from the evidence, with owner or target>
