# Publish Workspace Toolkit 0.9.0

State: `done`

## Scope and Source

Publish the upstream-approved coordinated Workspace 0.9.0 release through
Registry develop then main. Generate all 22 packages with the existing verified
Workspace publisher; do not hand-edit package contents or released versions.
New packages are design-domain-model and report-repository-status, both 0.1.0.
The user requested production and Registry delivery. Upstream modeling first
release accepts correctness with comparative improvement explicitly unproven;
Registry publication never establishes an improvement claim.

Affected: generated skills/workspace release, this spec/catalog and the human
namespace package count. No validator, workflow, instruction or unrelated
namespace changes. All prior published exact-version contents remain immutable.

## Acceptance Criteria

1. Namespace manifest identifies exact upstream main revision, toolkit 0.9.0,
   all 22 exact pins and complete all-workspace-skills bundle.
2. Generated root/exact packages, resources, integrity, modes and dependency
   closure match canonical source; every prior production exact tree is unchanged.
3. Independent exact candidate review, native task check/test and required PR,
   develop and production CI pass; proposed and actual trees match reviewed source.
4. Confirm actual develop integration and main publication. Live released SKM
   installation/check/repeat plan and website refresh are verified in the
   companion upstream publication records.

## Plan and Validation

Prepare this spec before staging the generated release. Review the publisher
proposal and canonical-byte/immutability evidence, then run native Registry
checks/tests after review on the stable candidate. Retarget publisher PR to
integration develop and release develop through main after passing CI. Record
confirmed integration/main events; move this spec to done only after main.
Update human package count and catalog without altering generated provenance.
Event-only completion records retain review and CI under the same branch model.

## Versions, Risks and Memory

Reuse upstream applied 0.9.0 exact pins; no independent Registry component bump.
Failed candidates remain preserved; never force-push production or rewrite
published packages. Correct future defects with a successor version. No external
schema/database/production modeling correctness is claimed.
Memory impact: none for Registry-local policy; canonical release facts and the
user acceptance decision are maintained in the companion Workspace records.

## Delivery Evidence

Workspace PR #91 confirmed source main
76bbf51eeb27c663755d5494649b2a2b8b5dd0c5 with the reviewed/tested source tree.
Publisher run 38091413165 succeeded and opened Registry PR #50; it is retargeted
to develop before integration. Generated manifest pins the exact source main
revision and 22 package versions. Independent review, final native gates,
actual develop/main integration and live verification remain pending.

## Confirmed Production and Acceptance

Independent exact review approved candidate
d2b050905d8135c915a527b72827a7b9a1c7dfd6 and renewed approval for production
head da868a9cd4518570914fe6cce6d249dcef7f170f. All 22 packages and 140 canonical
files match upstream source, metadata, dependencies, integrity and modes; all
184 previously published exact trees are unchanged. Eighteen inherited EOF
warnings are accepted only for historical reference bytes identical to canonical
source and published adoption 0.7.0; new documentation has no such exception.
The 110 unchanged support files were checked against published bytes rather
than exhaustively re-audited; no payload was executed during safety review.

Final native task check/test passed with 27 packages, 206 exact releases and
41 tests. PR CI 38091571139 passed. PR #50 integrated develop at
da868a9cd4518570914fe6cce6d249dcef7f170f with proposed/actual tree equal to
approved 81f785dcbe1c46366960fb67324c5baa0e6adbab. Renewed exact review,
develop CI 38091721068 and production PR CI 38091741086 passed. PR #51 released
main ef215c1e80ee006a8034b74f2bd87fda641f7bd8 on 2026-10-10 with the same
approved tree. Production CI 38091816374 passed.

The live manifest selects toolkit 0.9.0 and exact canonical source main
76bbf51eeb27c663755d5494649b2a2b8b5dd0c5. Released SKM 0.9.0 binary/source and
asset checksum were verified; it installed all 22 exact pins, passed check,
matched 140 installed payload files and created 44 Codex/Cursor links. Its
repeat plan reports zero actions. An initial origin mismatch stopped safely
before installation; a fresh project-local registry alias resolved the test
setup without clearing or modifying the existing registry cache.

Website deployment 38091817509 passed from unchanged website source. Live JSON,
catalog, homepage and both metapackage pages show all 22 Workspace pins; all
27 catalog, six preview and 24 member GitHub links resolve to released paths.
Stable GitHub release workspace-toolkit-v0.9.0 points to the exact canonical
Workspace main revision. Comparative modeling improvement remains unproven;
installation/resource correctness does not establish native agent execution,
deployed schemas or universal performance gains. All acceptance criteria pass
within these stated bounds. Memory impact: none for Registry policy; companion
Workspace records preserve verified release facts and the user's decision.

These record-only completion changes follow the normal develop/main branch
model with independent exact review and native gates/CI before delivery; they
never change published package bytes or canonical provenance.
