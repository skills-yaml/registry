# Security Review

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
- `vulnerabilities confirmed`: at least one confirmed vulnerability.
- `control-integrity failure`: an open policy/control finding breaks control
  integrity, such as a governed instruction change without prospective human
  approval.
- `no confirmed vulnerabilities`: a valid result; still report limits.
Severity applies only to confirmed vulnerabilities: `critical`, `high`,
`medium` or `low`. Confidence is separate: `high`, `medium` or `low`.
Coverage outcome: `reviewed`, `candidate`, `blocked`, `deferred` or
`out_of_scope`, as defined in references/evidence-and-coverage.md; report the
coverage record even when findings exist.
IDs are stable root-cause identifiers; combine duplicate paths without hiding
different preconditions. A disproved claim belongs in Rejected Claims.
-->

## Summary

- **Result:** <review blocked | vulnerabilities confirmed | control-integrity failure | no confirmed vulnerabilities>
- **Observed:** <UTC timestamp>
- **Scope:** <code, configuration, dependencies or change under review>
- **Revision:** <base and head short SHAs> (dirty changes included: <yes | no>)
- **Sources:** <source, configuration, dependency data, local proofs, host data; mark each unavailable source>
- **Counts:** <n> confirmed (<n> critical, <n> high, <n> medium, <n> low), <n> needs-validation, <n> unverified, <n> rejected, <n> policy/control

## Threat Context

| Asset | Trust boundary | Untrusted input | Actor | In scope |
| --- | --- | --- | --- | --- |
| <asset> | <boundary> | <input> | <actor> | <yes or no> |

## Confirmed Vulnerabilities

| ID | Severity | Confidence | Confidence rationale | Location | Trust boundary | Preconditions | Demonstrated impact | Source trace | Preventing controls | Verification | Remediation and regression case |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <S1> | <critical, high, medium or low> | <high, medium or low> | <why> | <path:line> | <boundary> | <attacker preconditions> | <impact actually demonstrated> | <source to sink> | <controls checked> | <independent verifier scope and result, or pending gap> | <smallest effective fix and test> |

## Coverage

| Surface / boundary | Reviewed paths and controls | Evidence / check | Outcome | Gap / next step |
| --- | --- | --- | --- | --- |
| <surface and boundary> | <paths and controls> | <source trace or bounded check and result> | <reviewed, candidate, blocked, deferred or out_of_scope> | <exact missing fact or `none`> |

## Needs-Validation Leads

| ID | Location | Hypothesis | Blocker | Validation plan |
| --- | --- | --- | --- | --- |
| <L1> | <path:line> | <source-grounded hypothesis> | <exact blocker> | <plan> |

## Unverified Candidates

| ID | Location | Concern | Why unverified |
| --- | --- | --- | --- |
| <U1> | <path:line> | <concern> | <reason> |

## Rejected Claims

| ID | Claim | Disproving evidence |
| --- | --- | --- |
| <X1> | <claim> | <evidence> |

## Policy and Control Findings

| ID | Control | Gap | Recommendation |
| --- | --- | --- | --- |
| <P1> | <control> | <gap> | <recommendation> |

## Hardening Advice

- <optional defense-in-depth advice or `none`>

## Coverage and Threat-Model Limits

- <unreviewed boundary, assumption, missing tool or `none`>

## Evidence Gaps

- <unavailable source, query error, truncation, stale comparison or missing tool>

## Next Steps

1. <highest-priority action that follows from the evidence, with owner or target>
