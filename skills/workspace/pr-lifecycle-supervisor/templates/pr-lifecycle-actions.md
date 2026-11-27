# PR Lifecycle Supervisor Action Messages

<!--
Select the one matching block. Apply the shared output contract in
pr-lifecycle-report.md, including empty and unknown markers, full SHAs,
evidence links, privacy, and unfinished-work requirements. Preserve headings,
labels, and order. Do not emit text inside comments.
-->

## Interim Update

`[HH:MM:SS UTC] <PR link> @ <full head or merge SHA>: <old stage> → <new stage>; <action and reason>; evidence: <report, comment or check link>; owner: <agent>`

## PR Finding Comment

**Finding <ID> — reviewed head `<full SHA>`**

- **Reviewer:** <agent>
- **Location or check:** <repository-relative path:line or check link>
- **Failure and impact:** <concrete behavior and consequence>
- **Evidence:** <short reproduction, test or run link>
- **Requested correction:** <smallest in-scope fix>

## Merged PR Finding Comment

**Post-merge finding <ID> — merge revision `<full SHA>`**

- **Reviewer:** <agent>
- **Failure and impact:** <concrete behavior and consequence>
- **Evidence and attribution:** <run/report link and reason this merge caused the failure>
- **Requested correction:** <bounded fix in a new linked PR; never rewrite the merge>

## Developer Handoff

- **PR and input head:** <PR link, full SHA or merged PR link and full merge SHA>
- **Developer owner:** <assigned agent>
- **Findings:** <IDs and comment links>
- **Task:** <bounded fix; use address-review-feedback, fix-ci, implement-spec or fix-bug as applicable>
- **Validation:** <affected Taskfile groups and required checks>
- **Return contract:** <assigned reviewer; require the new full head SHA, validation results and remaining gaps after the fix>

## Return to Reviewer

- **PR and new head:** <PR link, full SHA>
- **Developer and reviewer:** <returning developer and assigned reviewer>
- **Fixes:** <finding IDs addressed and unresolved items>
- **Validation:** <Taskfile/check results tied to the new head>
- **Requested review:** <full base/head SHAs and affected behavior>

## Merge Decision

- **PR and reviewed head/base:** <PR link and full SHAs>
- **Reviewer owner:** <agent>
- **Review and acceptance:** <decision, findings resolution and criterion evidence>
- **Required checks and protection:** <run links and results>
- **Decision:** <merged, waiting or held; reason>
- **Merge revision:** <full SHA or `none`>

## Post-Merge Escalation

- **Merged PR and revision:** <PR link, full merge SHA>
- **Observer and reviewer owners:** <observer agent and assigned reviewer>
- **Observed failure:** <check/run or regression report link, short symptom>
- **Attribution:** <confirmed, unrelated or unknown, with evidence>
- **Reviewer task:** <triage the exact merge revision and report the finding>
- **Correction path:** <new linked PR if an in-scope repository fix is confirmed; otherwise hold and owner>
