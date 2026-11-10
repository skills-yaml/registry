# Model Assessment

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
Use this template for assess and review modes; design mode uses
model-design.md. Result, first match wins:
- `blocked`: the requested assessment could not be performed.
- `issues found`: any violated invariant, contradiction or review finding.
- `consistent`: no issues found within the stated limits.
Status values: `holds`, `violated`, `untested` or `unknown`.
Findings name a violated rule and a concrete counterexample, never naming or
diagram-style preferences. In assess mode, Findings lists contradictions only.
-->

## Summary

- **Result:** <consistent | issues found | blocked>
- **Observed:** <UTC timestamp>
- **Scope:** <contexts, models, schemas or artifacts>
- **Revision:** <short SHA>
- **Sources:** <models, schemas, migrations, code, consumers; mark each unavailable source>
- **Mode:** <assess | review>
- **Level:** <small change | domain design | cross-boundary evolution; combinations allowed>

## Scenarios

| Scenario | Expected behavior | Evidence | Status |
| --- | --- | --- | --- |
| <scenario> | <behavior> | <repository-relative path or test> | <holds, violated, untested or unknown> |

## Invariants and Decisions

| Invariant or decision | Source / owner | Enforcement point | Failing example | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| <rule> | <source and owner> | <where it is enforced> | <input that would violate it> | <repository-relative path or test> | <holds, violated, untested or unknown> |

## Representation and Consumer Mapping

| Concept | Storage | API / event | Consumers | Old/new reader-writer compatibility |
| --- | --- | --- | --- | --- |
| <concept> | <table or field> | <contract> | <consumers> | <compatible, incompatible or unknown> |

## Findings

| ID | Severity | Violated rule | Counterexample | Location | Remediation |
| --- | --- | --- | --- | --- | --- |
| <M1> | <blocking, major or minor> | <rule> | <concrete counterexample> | <path:line> | <smallest fix> |

## Material Questions

| Question | Blocks | Owner |
| --- | --- | --- |
| <unresolved business decision> | <dependent work> | <decision owner> |

## Verification Limits

- <missing behavioral, concurrency, security or consumer evidence, or `none`>

## Evidence Gaps

- <unavailable source, query error, truncation, stale comparison or missing tool>

## Next Steps

1. <highest-priority action that follows from the evidence, with owner or target>
