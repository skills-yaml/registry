# Evidence and Coverage

Use this guide for review records and candidate verification. It supplements
the skill's execution, scope and pinned SDLC rules; it does not grant additional
authority. Keep the record in the configured review response unless the user
requests a saved artifact.

## Bound the Review

Record the exact revision/range and included working-tree changes. Identify the
protected asset, actor capability, relevant entrypoints, strongest controls and
unknown runtime/deployment facts. A diff review includes reachable affected
callers and alternate paths; it does not imply a repository-wide audit.

## Track What Was Actually Checked

Use one row per meaningful surface/boundary. Scale rows to the requested scope;
do not enumerate a Cartesian product of every risk category.

| Surface / boundary | Reviewed paths and controls | Evidence / check | Outcome | Gap / next step |
| --- | --- | --- | --- | --- |
| Example: export / tenant ownership | Source path and exact authorization scope | Source trace or bounded check and result | reviewed / candidate / blocked / deferred / out_of_scope | Exact missing fact, or none |

- `reviewed`: the stated invariant was examined with identified source/checks;
  no surviving candidate or decisive gap remains for that row. This is bounded
  evidence, never proof of general safety.
- `candidate`: a concrete claim is being evaluated; link its root-cause ID and
  current disposition. A resolved candidate keeps its evidence and verdict.
- `blocked`: partial review identifies a decisive missing capability or fact.
- `deferred`: work in scope was not completed; give the reason.
- `out_of_scope`: discovered work is outside the authorized boundary.

Do not mark failed/absent tests, skipped paths, tool failures or budget-exhausted
work reviewed. Retain the evidence of partial work and describe the remaining
gap. Report this record even when there are confirmed findings. If a budget is
set, reserve time for validation and disclose unfinished work when it expires.

## Use Distinct Dispositions

| Disposition | Required support | Reporting |
| --- | --- | --- |
| confirmed | Complete reachable trace, prerequisites, bounded demonstrated result and independent verification | Severity and confidence with separate reasons, narrow fix and regression case |
| needs_validation | Source-supported boundary hypothesis with one or more decisive unknown facts | Exact blockers and safe local or owner-observed plan; no severity |
| unverified | A concrete candidate has not received required independent verification | State verification pending; no severity or confirmation claim |
| rejected | A preventing control, impossible prerequisite, absent boundary/impact or contradictory evidence refutes the claim | Record the reason; keep out of the vulnerability list |
| hardening / policy | Defense-in-depth or repository-control observation | Separate category; do not assign vulnerability severity without a demonstrated security boundary failure |

An absent secondary control does not create a vulnerability if the primary
control prevents the claimed effect. A same-principal action permitted by design
is not privilege escalation. A crash does not establish code execution. A
dependency advisory does not establish exploitability of this application.

## Falsify Before Confirming

For every candidate, ask:

1. Can this actor reach this entrypoint under the exact stated configuration?
2. What validation, framework, identity, authorization, normalization or lifecycle
   control most strongly prevents the claimed result? Inspect callers and sinks.
3. Does each transformation preserve the guarantee the next component assumes?
   Check parallel paths, canonicalization, retries and current versus stale state.
4. Is every prerequisite established, including the final affected principal,
   resource and observable result? What counterexample would disprove it?
5. Does a qualifying bounded check or proven-fresh existing result establish the
   effect? Follow execution safeguards; absence of a sandbox is not permission.
6. Does the smallest proposed fix enforce the invariant at the trusted decision
   point, and what regression case distinguishes the failure from allowed use?

Have an independent reviewer repeat this assessment for proposed confirmations.
It must re-read source, not merely agree with a summary. Reproduce decisive
behavior independently when safe and feasible; if an unobserved fact remains
decisive, downgrade to needs_validation. Missing reviewer capacity leaves the
candidate unverified, distinct from a known runtime/deployment blocker.
Changed source, root cause, prerequisites, result or impact renew affected review.

## Compact Finding Record

Use these fields in prose for ordinary reviews; the same fields may become
structured records when a larger audit is explicitly requested:

- Stable root-cause ID, title, disposition and reviewed revision.
- Actor capability, intended invariant, affected principal/resource.
- Ordered repository-relative entrypoint, propagation and sink file:line trace.
- Strongest preventing controls considered and why they do or do not apply.
- Exact prerequisites and minimum check/input/result, or exact blocker and plan.
- Independent verifier's scope/result or pending verification gap.
- For confirmed findings: demonstrated impact, likelihood, severity, separate
  confidence rationale, smallest source fix and discriminating regression case.

Do not include secrets or machine-local paths. Validate references and merge
duplicate root causes without suppressing distinct affected paths. Prior rejected
claims suppress only the same disproved claim while its evidence is unchanged;
they do not establish coverage. Recheck relevant source and conditions before
carrying earlier results forward. Derive summaries from the final records so
prose never silently strengthens a verdict or impact.

Methodology informed by Cloudflare's
[security-audit skill at c1c8a8c](https://github.com/cloudflare/security-audit-skill/tree/c1c8a8c/skills/security-audit).
This guide is an original adaptation for bounded Workspace reviews; it does not
bundle their code or assert comparative detection performance.
