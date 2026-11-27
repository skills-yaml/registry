# PR Lifecycle Supervisor Reporting

<!--
Fixed output contract for this skill's controller and action messages. Select
the one block matching the message; do not emit every block together or any
text inside comments. Preserve its headings, labels, columns and order.

Use `none` for an empty value, `unknown` for an unverified value, and
`None observed.` as the entire body of an empty in-scope table section.
Use `Not in scope for this run.` for an excluded section. Never leave a required
field blank. Include links to PR comments and checks when available. Use
repository-relative paths; omit secrets, credentials, credential-bearing URLs,
absolute local paths, machine identities and raw logs.
Use full commit SHAs for handoffs and action messages. In controller tables, a
short SHA must link to the full commit. If a requested setup or bounded run is
unfinished, prepend the required `**Not finished:**` sentence, list numbered
possible fixes with an owner and one recommendation under Next Steps, and name
the preserved work in Summary.

The reviewer still uses the review-changes fixed report during read-only review;
the post-merge observer still uses the monitor-ci fixed report. The companion action-message template covers their action messages; this file
covers the controller's synthesis of those reports.

Controller result, first match wins: `blocked` when no safe action can proceed
and an external decision or capability is needed; `partial` when some work was
done but eligible PR work remains queued, pending or held; `complete` when the
requested setup or bounded run finished; `idle` when a scheduled run found no
new action; `unknown` when the run or schedule cannot be verified.
Schedule state: `proposed`, `active`, `paused`, `not configured`, or `unknown`.
PR stage: `review`, `developer fix`, `waiting for checks`, `merge`,
`post-merge`, `held`, or `complete`.
-->

## Controller Report

### Summary

- **Result:** <blocked | partial | complete | idle | unknown>
- **Observed:** <start UTC> → <end UTC>
- **Scope:** <repository allowlist>
- **Controller owner:** <agent or accountable owner>
- **Schedule:** <scheduler identifier or `none`>
- **Schedule state:** <proposed | active | paused | not configured | unknown>
- **Schedule evidence:** <creation/activation receipt or scheduler state link; `none` if not configured>
- **Run:** <run identifier or `not run`>
- **Sources:** <PR API, review reports, CI/build runs, scheduler state; mark unavailable sources>
- **Work preserved:** <scheduler state or repository-relative record; `none` if no unfinished work>

### Configuration

| Repository | Cadence | Post-merge window | Action authority | Controller state |
| --- | --- | --- | --- | --- |
| <repository> | <cadence or `unknown`> | <duration or `unknown`> | <comment, push, merge scope or `unknown`> | <active, paused, proposed, not configured or unknown> |

### PR Activity

| PR | Base → head or merge revision | Stage | Review | Checks/build | Action and owner |
| --- | --- | --- | --- | --- | --- |
| <PR link> | <linked base SHA → linked head SHA or linked merge SHA> | <PR stage> | <decision and linked reviewed SHA or `none`> | <status and run link or `unknown`> | <action and responsible agent or `none`> |

### Findings and Comments

| PR | Finding | Evidence | Comment | Developer handoff |
| --- | --- | --- | --- | --- |
| <PR link> | <finding ID and severity> | <repository path:line or check link> | <comment link or `none`> | <agent and linked head or `none`> |

### Repair and Review Returns

| PR | Input head | Developer output | Validation | Reviewer return |
| --- | --- | --- | --- | --- |
| <PR link> | <linked head SHA> | <linked new head or corrective PR> | <Taskfile/check result and linked revision or `unknown`> | <reviewer and linked revision or `pending`> |

### Merge Decisions

| PR | Reviewed head/base | Required checks | Protection | Decision | Merge revision |
| --- | --- | --- | --- | --- | --- |
| <PR link> | <linked head/base SHAs> | <passing, pending, failed or unknown; run link> | <passed, blocked or unknown> | <merged, waiting or held; reviewer> | <linked SHA or `none`> |

### Post-Merge Observation

| PR | Merge revision | Check or report | Outcome | Attribution | Review restart or corrective PR |
| --- | --- | --- | --- | --- | --- |
| <PR link> | <linked SHA> | <run/report link> | <pass, fail, pending or unknown> | <confirmed, unrelated or unknown> | <reviewer handoff or PR link and owner; or `none`> |

### Holds and Evidence Gaps

| PR or schedule | Reason | Needed evidence or decision | Owner |
| --- | --- | --- | --- |
| <PR link or schedule ID> | <plain-language reason> | <specific next evidence/decision> | <agent or user> |

### Next Steps

1. <highest-priority next action, owner and target; use `None.` when the bounded run is complete>
