# Publish Workspace Toolkit 0.9.0

State: `development`

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
