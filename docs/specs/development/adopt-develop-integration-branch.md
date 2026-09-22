# Spec: Adopt `develop` As The Integration Branch

Status: Development

Purpose: Give the registry a two-stage branch flow, so a change can be
integrated and validated before it becomes the published state consumers
resolve against.

## 1. Problem Statement

Every change has landed directly on `main`. For a registry that is different
from an ordinary repository: `main` is not just the trunk, it is the published
artifact. `skm` resolves skills from it, `latest` and `default` point into it,
and released-version immutability is enforced against it.

So merging to `main` publishes. There has been no place to integrate a change,
run the gates against the combined result, and look at it before consumers can
install it. The sibling repositories already have this: `skm` integrates on
`development`, `workspace` on `develop`.

The spec lifecycle also has no way to distinguish the two events. `done`
currently means merged, which conflates "integrated" with "released".

## 2. Goals and Non-Goals

### Goals

- Add `develop` as the integration branch, branched from `main`.
- Keep `main` as the production branch and the published registry state.
- Validate pushes to `develop` in CI, not only to `main`.
- Record the branch model where contributors and agents will read it.
- State that `done` requires release through `main`, not merge to `develop`.

### Non-Goals

- Adopting a fourth spec state. This repository follows `workspace-docs@1.0.0`,
  whose states are `backlog`, `development` and `done`. Adding a `test/` state
  is a standard migration, not a branch change, and is out of scope.
- Changing the immutability rule. It stays anchored to `origin/main`, which is
  what makes it meaningful: a version becomes immutable when it is published,
  not when it is integrated.
- Branch protection settings, which are repository administration.

## 3. Proposed Design

1. Create `develop` from `main`.
2. Extend the CI `push` trigger to cover `develop`, so integration is validated
   and not only pull requests.
3. Record the model in `AGENTS.md` under project-owned Local Rules, outside the
   generated `AGENT-CONTEXT` block, since it is repository-specific and not part
   of the workspace-docs standard.
4. Record the configured targets in `docs/specs/README.md` alongside the
   transitions, so the lifecycle and the branches are described together.

Immutability needs no change and is the reason the anchor matters. Comparing
against `origin/main` means a version already integrated on `develop` can still
be corrected before publication; once it reaches `main`, it is frozen and can
only be withdrawn under `WITHDRAWN.yaml`.

## 4. Verification and Acceptance Criteria

- [ ] `develop` exists and matches `main` at creation.
- [ ] CI runs on pushes to `develop` and passes.
- [ ] `AGENTS.md` and `docs/specs/README.md` describe the model consistently.
- [ ] A pull request targeting `develop` runs the gates and can be merged.
- [ ] `task check` and `task test` pass on `develop`.
- [ ] This spec moves to `done` only after `develop` is merged to `main`.

## 5. Risks and Mitigations

- *Risk*: `develop` and `main` drift, and the published state stops matching
  what was validated together.
  *Mitigation*: Release by merging `develop` into `main` rather than
  cherry-picking, so `main` is always a prefix of validated integration work.
- *Risk*: A contributor reads `develop` as released and pins a skill from it.
  *Mitigation*: The Local Rules state plainly that integration is not release
  and that a consumer resolves against `main`.
- *Risk*: The extra stage is ignored, and changes keep going straight to `main`.
  *Mitigation*: The rule is written where agents working in this repository read
  it. Enforcement through branch protection is available but deliberately not
  part of this change.
