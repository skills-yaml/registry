---
name: write-spec
description: Write a development specification from an accepted request before implementation. Use when scope, behavior, acceptance criteria, affected areas, validation, risks, versions or unresolved decisions need an explicit contract.
metadata:
  skm-version: "0.7.0"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "2243d16f5e0b457f0eda538832b87bc2931c7b98"
  skm-source-path: "workspace/instructions/skills/write-spec"
  skm-source-integrity: "sha256:dad056bf0da81cd91724544a919c71a915d3985bc4dc4aae2054bd57fee63944"
  workspace-toolkit-version: "0.15.0"
  workspace-docs-compatibility: "10.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
  skm-dependencies: "workspace/design-domain-model@0.1.8"
---

# Write Spec

Create a decision-ready specification. This role writes and delivers planning
artifacts; feature implementation belongs to the implementation workflow.

## 1. Load the Project Contract

Read the consuming repository's policy, `workspace/instructions/tech/sdlc.md`,
Taskfile guidance, spec catalog, nearest related specs, relevant architecture
and product documents, and project memory. These paths resolve from that
repository's root, not this installed package. Missing required instructions
or catalog are prerequisite gaps: report them before dependent writing.

Applicable current sources under `workspace/instructions/` are the source of
truth for repository-controlled conflicts; a spec cannot override governed
instructions. Use the project's actual pin for lifecycle, branch authority,
review, verification and completion. Read its referenced standard when those
rules are not established; never substitute a newer pin's contract.

Identify the accepted outcome, constraints, exclusions, users/consumers,
affected contracts, primary feature and allowed lifecycle state. Preserve
unrelated work and existing decisions. Work on one active task at a time.

## 2. Resolve Inputs

Check the request against every required spec item in step 4. Resolve facts
from the request, repository, catalog, memory and prior answers first. When
required information remains missing, unclear or conflicting, ask a small
focused batch of plain-language questions with options or the default you
would otherwise assume. Use the host question tool when available.

Wait for actual answers before dependent writing; silence is not a choice.
Continue independent read-only discovery while waiting. If an answer cannot
be obtained, label it as an open question or assumption, identify the work it
blocks, and leave that work unready. Never present it as a settled requirement,
version or approval. Established facts and ordinary delivery permission do
not need another question.

## 3. Establish Impact Before Drafting

Read the pinned versioning contract and latest shared release ledger before
choosing a target. Include its per-component Version Impact table: Component,
Impact (major/minor/patch or justified none), Release and Rationale. Register
member specs in `workspace/releases.json`; declare baseline, target, owner,
timing and rationale through the required shared reservation transaction.
Reuse an already-applied shared release. A backlog idea does not apply a
development bump. Recheck occupancy at handoff.

Load only the conditional material triggered by the affected areas:

- **Domain or schema changes:** read [specialized scope](references/specialized-scope.md#domain-and-schema)
  before defining business concepts, invariants, ownership or database/API/event
  contracts; use its proportionate design-mode modeling handoff.
- **Infrastructure:** read [specialized scope](references/specialized-scope.md#infrastructure)
  and the project's infrastructure policy before defining mutation or acceptance paths.
- **Concurrent mutating agents:** invoke `coordinate-multi-agent-development`
  before delegated edits; follow its worktree, claim and WIP requirements.
- **One-time cleanup/maintenance:** read the actual pinned SDLC's user-run
  exception before planning tools/, execution ownership, exact informed approval,
  expected results and recovery; CI verification remains mandatory. For manual
  infrastructure creation, include OpenTofu import/reconciliation feasibility and the normal CI/CD path.
- **Governed instructions:** record prospective instruction-change approval
  as pending or directly supplied, with its exact human-approved scope. An
  agent-authored approval record grants no authority to edit those instructions.

## 4. Draft the Specification

Include:

- lifecycle state, concise status rationale and primary feature;
- problem, goals, non-goals, users/consumers and proposed behavior;
- important interface/data contracts, bounded affected areas and exclusions;
- compatibility/migration effects and applicable security, privacy,
  reliability and rollback risks;
- measurable acceptance criteria, each mapped to validation evidence;
- validation gates grounded in native Taskfile commands: changed-component
  checks, then affected direct/transitive consumer stages gated on success,
  with selection reasons, dependencies and coverage gaps; use the actual pin's
  final verification contract from step 1;
- ordered delivery steps proportionate to the scope;
- Version Impact and applicable approval/modeling records from step 3;
- Memory Impact with the repository's required initial status;
- unresolved questions/assumptions and the dependent work they block.

Assess whether implementation, review and validation fit one focused change.
When distinct deliverables, dependency stages, migrations or risks need separate
evidence, read [large specifications](references/large-specs.md) and split at
those boundaries. Keep small specs concise and tightly coupled invariants safe.

Use normative language for real requirements. Include implementation detail
only when compatibility, safety or acceptance depends on it. Link authoritative
policy instead of copying it into the spec.

## 5. Check Readiness and Hand Off

Save the spec in its required state/primary-feature path and update the root
catalog with the same state and rationale. Synchronize release member paths.
Preserve done history through linked follow-ups. Lifecycle transitions need
the actual pinned integration/completion evidence, never a branch name.

Self-review links, terminology, required contents, acceptance testability and
policy consistency. Each requirement must have supporting repository evidence,
a user decision, or a labeled unresolved input. Every acceptance criterion
needs a planned check, inspection, demonstration or user decision. Report
uncovered criteria as gaps; dependent work stays unready until resolved.

For this planning artifact's delivery, obtain the independent exact-candidate
review required by project risk rules and resolve every finding. After fixes
and records stabilize, freeze the candidate and run the required affected
documentation/spec/package gates through Taskfile using the pinned local/CI
contract. Renew evidence after relevant edits; missing coverage/tools are gaps.

Standing workflow authority covers safe delivery of the requested planning
artifacts, including commits, branch pushes and pull requests as the pin allows.
Substantial scope expansion, unapproved governed instruction changes and
destructive production actions retain prospective scoped human approval.

Hand off the spec path, ready and blocked work, unresolved decisions, review
and validation results, next allowed lifecycle transition, version reservation
and memory classification with rationale. Distinguish planned feature validation
from checks actually run on the planning artifact, and main completion from
separate deployment/publication.
