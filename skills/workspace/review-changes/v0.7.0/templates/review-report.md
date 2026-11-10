# Change Review

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
- `review blocked`: the exact candidate or required context could not be reviewed.
- `changes requested`: any open blocking finding.
- `approve with comments`: open major or minor findings or questions only.
- `approve`: no open findings.
Severity: `blocking`, `major` or `minor`. Type: `defect`, `question` or
`residual risk`. Status: `open`, `fixed` or `rejected (agreed)`.
Validation, first match wins: `failed`, `pending`, `not run`, `passed`.
-->

## Summary

- **Result:** <approve | approve with comments | changes requested | review blocked>
- **Observed:** <UTC timestamp>
- **Scope:** <working tree | branch | commit range | PR #n>
- **Revision:** base <short SHA> → head <short SHA>
- **Sources:** <diff, tests, CI, spec, host review data; mark each unavailable source>
- **Findings:** <n> blocking, <n> major, <n> minor (<n> defects, <n> questions, <n> residual risks)
- **Validation:** <passed | pending | failed | not run>

## Findings

| ID | Severity | Type | Location | Failure mode | Why it matters | Remediation direction | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <R1> | <blocking, major or minor> | <defect, question or residual risk> | <path:line> | <concrete failing input or state> | <impact> | <smallest useful fix> | <open, fixed or rejected (agreed)> |

<!--
Order by severity. Write `None observed.` when no actionable defect was found
and state the remaining limits under Coverage Limits.
-->

## Validation Evidence

| Check | Revision | Source | Result | Fresh for head |
| --- | --- | --- | --- | --- |
| <check or job> | <short SHA> | <local or CI> | <passed, failed, pending or not run> | <yes, no or unknown> |

## Lifecycle Readiness

| Stage | Ready | Occurred | Evidence |
| --- | --- | --- | --- |
| <stage> | <ready, not ready or not in scope> | <verified, not yet or unknown> | <PR, revision or check> |

<!--
One row each for: test-target merge, main completion, publication. Readiness
is not evidence that the merge or publication occurred.
-->

## Coverage Limits

- <untested path, missing tool, pending gate or `none`>

## Evidence Gaps

- <unavailable source, query error, truncation, stale comparison or missing tool>

## Next Steps

1. <highest-priority action that follows from the evidence, with owner or target>
