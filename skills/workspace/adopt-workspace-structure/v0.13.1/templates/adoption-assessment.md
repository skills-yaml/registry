# Workspace Adoption Assessment

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
Use this template for assessment-only requests; mutating modes use the Hand Off
list. Result, first match wins:
- `assessment blocked`: the target version is ambiguous or a required source was
  unavailable, so conformance could not be established.
- `not adopted`: no workspace documentation structure exists.
- `update needed`: an older version or older canonical layout is pinned.
- `repair needed`: the target is declared but incomplete, duplicated or
  inconsistent, or any required finding is open.
- `conformant`: every Structure Conformance and Policy row `conforms` and no
  required finding is open.
Severity: `critical`, `high`, `medium` or `low`. Classification: `required`
(manifest, policy or validation requirement) or `optional`. A kept or deferred
required item remains an explicit deviation; a follow-up spec does not make it
pass.
Conformance status: `conforms`, `missing`, `duplicated` or `inconsistent`.
Proposed changes are proposals only; the user chooses to address, keep or defer.
-->

## Summary

- **Result:** <assessment blocked | not adopted | update needed | repair needed | conformant>
- **Observed:** <UTC timestamp>
- **Scope:** <repository>
- **Revision:** <ref or detached> <short SHA>
- **Sources:** <AGENTS.md, CLAUDE.md, workspace tree, manifests, CI configuration; mark each unavailable source>
- **Versions:** pinned <version or `none`> → target <version>
- **Recommended mode:** <adoption | update | repair | none>
- **Findings:** <n> critical, <n> high, <n> medium, <n> low; <n> required

## Structure Conformance

| Requirement | Expected | Observed | Status |
| --- | --- | --- | --- |
| <required file or directory> | <expected state> | <observed state> | <conforms, missing, duplicated or inconsistent> |

## Policy and Instruction Files

| File | Manual policy present | Generated block state | Pointer valid | Status |
| --- | --- | --- | --- | --- |
| <repository-relative path> | <yes, no or unknown> | <current, stale, missing or not applicable> | <yes, no or not applicable> | <conforms, missing, duplicated or inconsistent> |

## Findings

| ID | Severity | Requirement | Evidence | Classification |
| --- | --- | --- | --- | --- |
| <A1> | <critical, high, medium or low> | <violated requirement> | <repository-relative path> | <required or optional> |

## Migration Map

| Source | Destination | Merge decision |
| --- | --- | --- |
| <repository-relative source> | <repository-relative destination> | <move, merge, keep or remove, with reason> |

## Validation Gaps

- <failing or unavailable validation, or `none`>

## Architecture and Technology Observations

| Area | Observed fact | Basis | Open question |
| --- | --- | --- | --- |
| <area> | <fact> | <observed, documented, inferred or unknown> | <question or `none`> |

## Proposed Changes

| Change | Classification | Effect | Alternatives | Risk |
| --- | --- | --- | --- | --- |
| <proposal> | <required or optional> | <concrete effect> | <keep current approach, other options> | <migration risk> |

## Evidence Gaps

- <unavailable source, query error, truncation, stale comparison or missing tool>

## Next Steps

1. <highest-priority action that follows from the evidence, with owner or target>
