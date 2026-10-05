---
name: analyze-repository
description: Analyze a repository without modifying it, producing an evidence-backed account of its purpose, structure, technology stack, development lifecycle, policies, documentation state, active work, risks, and evidence gaps. Use when a repository needs assessment, onboarding context, or current-state discovery before planning work.
metadata:
  skm-version: "0.3.1"
  skm-source-repository: "https://github.com/skills-yaml/workspace.git"
  skm-source-revision: "f867573bc91b5560d12cebd304ba3dd98aed7435"
  skm-source-path: "workspace/instructions/skills/analyze-repository"
  skm-source-integrity: "sha256:4ba680e6beb1a6f423b6c60aaaa0f7d833436931be0b9871d9fff66317a64493"
  workspace-toolkit-version: "0.7.1"
  workspace-docs-compatibility: "7.x"
  minimum-skm-version: "0.7.0"
  skm-adapter-compatibility: "2.x"
---

# Analyze Repository

Build a current-state report from repository evidence. Remain read-only.

## Establish Scope

1. Read the repository's agent policy and its required documentation before
   inspecting implementation details.
2. Confirm the repository root and requested analysis scope. Inspect only the
   current project; do not inventory sibling projects or machine-local state.
3. Preserve the distinction between observed facts, documented intent,
   reasonable inferences, and unresolved evidence gaps.

## Analyze

Inspect the smallest sufficient set of sources to establish:

- repository purpose, major components, and ownership boundaries;
- languages, frameworks, package managers, runtime requirements, and generated
  artifacts;
- canonical build, test, lint, validation, and task-runner entrypoints;
- Workspace standard version, applicable instructions, active specifications,
  documentation state, and durable memory state when present;
- source-control, CI/CD, release, migration, and rollback conventions;
- security-sensitive boundaries, untrusted inputs, secrets handling, and
  dependency or supply-chain exposure; and
- inconsistencies, stale documentation, missing evidence, and material risks.

Use repository-native, read-only commands. Do not install dependencies, execute
untrusted project resources, mutate infrastructure, or infer delivery status
from a branch name alone.

## Report

Lead with the repository's current status and the most consequential findings.
Include concise evidence using repository-relative paths, identify commands
that were actually run, and state limitations. Recommend next actions only
when they follow directly from the evidence. Do not edit files, create specs,
or persist memory while operating in this skill.

## Pinned Lifecycle Assessment

Assess the actual pinned contract. For v7, distinguish local implementation,
confirmed shared-test integration, verified main completion with reconciled
acceptance/records, and separate deployment/publication. Inspect blocked reason,
kind, prior stage, and resume condition without changing lifecycle states.
Check whether modular gate inputs, dependencies, consumers, resource constraints,
and freshness justify affected iteration and full final coverage after review.
Identify missing evidence without inventing completion or measured speedups.
Older pins retain their contracts; analysis remains read-only.
