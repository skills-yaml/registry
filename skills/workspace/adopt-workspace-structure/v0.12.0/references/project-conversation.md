# Project Conversation and Deferred Improvements

Read for mutating adoption or updates to project-specific guidance. Scale the
conversation to the project; ask only questions that can affect the plan. This
is design discovery, not another permission checkpoint for authorized delivery.

## Explain the Current Situation

Summarize the observed components, their responsibilities/data flow, deployment
boundaries and existing technical policies using repository-relative evidence.
Identify what is uncertain. For a new repository there may be no architecture
or stack yet; say that rather than importing example directories or technologies.
Confirm intent as well as inventory: a dependency manifest does not explain why
it was chosen or whether the user wants it retained.

Useful questions depend on what remains unknown:

- What does this project need to accomplish, and who uses or maintains it?
- Which existing architecture/technology choices are intentional constraints?
- What matters for this decision: simplicity, delivery effort, reliability,
  scale, privacy, hosting limits, team familiarity or migration cost?
- Which observed problem should be addressed during adoption, and which should
  stay as documented follow-up work?

Do not ask the user to repeat supplied answers or choose nonexistent components.
Explain unfamiliar options before requesting a decision. Group closely related
choices into a concise conversation, then follow up only on material gaps.
If material choices are unresolved, pause dependent writes and wait for answers;
absence of a reply is never acceptance. If choices are already fully specified,
explain the resulting plan and proceed within existing authority. Routine
commits, testing and safe delivery need no fresh approval.

## Guide a Decision

For each evidenced concern, distinguish a required adoption defect, a project
problem, and an optional improvement. Explain the current effect, desired
outcome, evidence and uncertainty. Compare viable options proportionately,
including retaining a suitable existing approach. Describe relevant benefits,
operating/migration costs, compatibility and recovery limits. Recommend an
option for this project's goals; do not equate unfamiliar or older technology
with an incorrect architecture. Verify version-sensitive technical claims
against primary sources when available; otherwise qualify the recommendation.

A useful decision record fits in a small table:

| Concern and evidence | Options and recommendation | User choice and reason | Adoption effect / follow-up |
| --- | --- | --- | --- |
| Repository-relative evidence and concrete effect. | Proportionate alternatives, tradeoffs and uncertainties. | Address now, retain, defer, or unresolved. | In-scope doc action, required gap, or linked future spec. |

Do not label recommendations as approved design or facts. "Address now" covers
only authorized work: a documentation adoption does not implicitly approve a
database move, application rewrite, production migration or infrastructure change.
Record any needed additional scope before such implementation. Preserve manual
policy outside the approved migration; an alternative that contradicts it needs
an explicit scope-bound user decision before governed edits.

## Turn Deferral into Work That Can Be Resumed

After the user chooses deferral, reuse a matching open spec when its scope and
acceptance fit; otherwise create a separate coherent backlog spec and catalog
row using the pinned project's templates and lifecycle. Do not reopen done
history, create duplicate follow-ups, or make already-active work look unstarted.
Where an active spec must enter blocked, preserve its previous stage, deferred
reason, resume condition and evidence-renewal needs under the local contract.
On fresh adoption, establish the minimum migration spec/catalog bootstrap first.

Each follow-up must tell the next person what to do:

- Current behavior/problem and repository-relative evidence, including what is
  unknown; link the adoption spec and relevant decisions.
- User's deferral reason and a proposed outcome or decision to resolve; keep
  technology alternatives open when the user has not selected one.
- Bounded scope, non-goals and affected components/docs/consumers.
- Ordered concrete actions: discover remaining facts, choose a design if needed,
  implement only after activation/authority, handle compatibility/data migration,
  update consumers/docs, and verify the result. Include only applicable steps.
- Observable acceptance criteria, meaningful staged validation and tools/coverage
  gaps. Define success, not merely "improve architecture" or copied prose.
- Dependencies, operational/rollback risks and a practical resume trigger or
  prerequisite. Record an owner or date only when actually supplied.
- The pinned contract's Version Impact and Memory Impact. A planning-only spec
  may justify no immediate version change; reserve/apply a concrete release when
  implementation becomes active under local versioning policy. Do not invent a
  version or mark an unresolved durable result complete.

Cross-link migration and follow-up, update the catalog state/rationale, and
report the retained current behavior while work is deferred. A backlog spec is
an agreed work item, not permission to execute it during adoption.

Required conformance and safety gates cannot be converted into optional backlog
work to claim success. If the user defers a required gate or unresolved collision,
explain that full adoption remains incomplete and retain the required deviation
or blocked record. An optional architecture improvement does not itself make an
otherwise conformant adoption fail. Assessment stays read-only: provide proposed
spec content/next steps in chat and explain that persistence needs write scope.
