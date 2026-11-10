# Repository Analysis

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
- `critical risks`: any critical finding.
- `concerns`: any high or medium finding.
- `sound`: only low findings or none.
Basis values: `observed` (seen in the repository), `documented` (stated intent),
`inferred` (reasoned from evidence) or `unknown`.
Severity values: `critical`, `high`, `medium`, `low`.
-->

## Summary

- **Result:** <sound | concerns | critical risks> — <most consequential finding or `none`>
- **Observed:** <UTC timestamp>
- **Scope:** <repository | repository-relative paths>
- **Revision:** <ref or detached> <short SHA>
- **Sources:** <docs, manifests, Git, CI configuration, specs, memory; mark each unavailable source>
- **Workspace standard:** <pinned version or `none`>
- **Findings:** <n> critical, <n> high, <n> medium, <n> low

## Purpose and Components

| Component | Path | Purpose | Boundary / owner | Basis |
| --- | --- | --- | --- | --- |
| <name> | <repository-relative path> | <purpose> | <ownership boundary> | <observed, documented, inferred or unknown> |

## Stack and Entrypoints

| Area | Technology or command | Evidence | Basis |
| --- | --- | --- | --- |
| <language, framework, package manager, runtime, build, test, lint, validation or generated artifact> | <value> | <repository-relative path> | <observed, documented, inferred or unknown> |

## Lifecycle and Delivery

| Aspect | Current practice | Evidence | Gap |
| --- | --- | --- | --- |
| <aspect> | <practice> | <repository-relative path> | <gap or `none`> |

<!--
One row each for: branching, CI/CD, release, migration, rollback, pinned SDLC
and spec lifecycle.
-->

## Active Work

| Work item | Spec / branch / PR | State | Evidence |
| --- | --- | --- | --- |
| <work item> | <link or `none`> | <state as recorded and as observed> | <repository-relative path or revision> |

## Documentation, Specs and Memory

| Item | State | Evidence | Gap |
| --- | --- | --- | --- |
| <document, spec group or memory file> | <current, stale, missing or inconsistent> | <repository-relative path> | <gap or `none`> |

## Security and Supply Chain

| Boundary or exposure | Current control | Evidence | Gap |
| --- | --- | --- | --- |
| <untrusted input, secret handling, dependency or execution boundary> | <control or `none`> | <repository-relative path> | <gap or `none`> |

## Findings

| ID | Severity | Category | Finding | Evidence | Basis | Next action |
| --- | --- | --- | --- | --- | --- | --- |
| <F1> | <critical, high, medium or low> | <category> | <finding> | <repository-relative path> | <observed, documented, inferred or unknown> | <action that follows from the evidence> |

<!--
Order by severity. Report optional improvements separately from defects.
-->

## Optional Improvements

- <optional improvement kept separate from defects, or `none`>

## Commands Run

| Command | Purpose | Result |
| --- | --- | --- |
| <read-only command> | <purpose> | <passed, failed or output summary> |

## Evidence Gaps

- <unavailable source, query error, truncation, stale comparison or missing tool>

## Next Steps

1. <highest-priority action that follows from the evidence, with owner or target>
