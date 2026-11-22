# Subagent Execution Report

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
- `blocked`: a ticket is blocked or awaits a user decision and dependent work
  cannot continue.
- `partial`: not every ticket is integrated and none is blocked.
- `review pending`: every ticket is integrated but whole-change review, gates
  or reconciliation are incomplete.
- `complete`: every ticket is integrated and the implement-spec completion
  steps for the current lifecycle stage are done.
Ticket status uses the ticket plan vocabulary.
-->

## Summary

- **Result:** <blocked | partial | review pending | complete>
- **Observed:** <start UTC> → <end UTC>
- **Scope:** <repository-relative spec path>
- **Revision:** <short SHA of the combined candidate>
- **Sources:** <ticket plan, subagent handoffs, review decisions, validation output>
- **Agents:** <planner / developer / reviewer>

## Tickets

| ID | Status | Revision | Review rounds | Validation | Note |
| --- | --- | --- | --- | --- | --- |
| t1 | <status> | <short SHA or `none`> | <count> | <pass, fail or `unknown`> | <note or `none`> |

## Review Findings

| Ticket | Finding | Resolution |
| --- | --- | --- |
| <ticket ID> | <finding> | <open, fixed or rejected (agreed)> |

## Acceptance Evidence

| Criterion | Tickets | Evidence |
| --- | --- | --- |
| <AC ID> | <ticket IDs> | <evidence or `unknown`> |

## Lifecycle and Records

- **Spec state:** <state and the confirmed event behind it>
- **Catalog:** <updated or `none`>
- **Versions:** <applied release or `none`>
- **Memory impact:** <updated or none, with rationale>

## Evidence Gaps

| Gap | Impact | Next verification |
| --- | --- | --- |
| <gap> | <affected criterion or ticket> | <step> |

## Next Steps

1. <next action and owner>
