# Symphony Spec Writing Checklist

Use this checklist while drafting or reviewing a spec modeled on `openai/symphony/SPEC.md`.

## 1. Framing
- [ ] Title is specific
- [ ] Status is explicit
- [ ] Purpose fits in one sentence
- [ ] Normative language is explained once

## 2. Scope
- [ ] Problem statement names the operational problem
- [ ] Goals are testable
- [ ] Non-goals are explicit
- [ ] Boundaries and trust assumptions are stated

## 3. Architecture
- [ ] Main components are enumerated
- [ ] Each component has a clear responsibility
- [ ] Layering is described (policy/config/coordination/execution/integration/observability)

## 4. Domain and Config
- [ ] Entities are named and typed
- [ ] Required vs optional fields are clear
- [ ] Defaults are listed
- [ ] Validation and reload behavior are documented
- [ ] Environment variable indirection is described where applicable

## 5. Lifecycle
- [ ] States are defined
- [ ] Transitions have triggers
- [ ] Restart behavior is documented
- [ ] Retry and backoff are explicit
- [ ] Cancellation and cleanup are covered

## 6. Safety
- [ ] Invariants are written as MUST statements
- [ ] Workspace/path or data-boundary rules are explicit
- [ ] Failure semantics are split by phase (startup / running / cleanup)

## 7. Observability
- [ ] Logs are specified
- [ ] Status surfaces or metrics are specified if needed
- [ ] Operators can see what happened and why

## 8. Review Test
- [ ] A second implementer could build the same system without guessing
- [ ] Ambiguous adjectives were replaced with concrete requirements
- [ ] Every major runtime behavior has a documented failure mode
