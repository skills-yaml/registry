# AI, Memory and Tool Boundaries

Load this guide when untrusted content reaches model context, durable memory,
MCP metadata or a model-driven capability. Keep ordinary file, network, injection
and access-control checks; the model adds another trust handoff.

## Map Authority Separately from Content

Identify who can write each retrieved document, message, memory record, tool
description or response; whose session consumes it; and which identity executes
the resulting action. Treat model output and external context as untrusted data.
Look for deterministic resource-scoped authorization and isolation at the sink.
A prompt telling a model to behave is not an enforced security boundary.

Prompt-injection text alone is not a confirmed vulnerability. Establish a concrete
cross-boundary outcome: another principal's data/context, unintended use of an
affected user's authority, an unauthorized tool action or unsafe output handling.
An intentional direct request using the requester's allowed authority does not
become a delegation defect simply because a model carries it out.

## Trace Context and Durable Memory

- Follow retrieval, embeddings, prompt caches and conversation history keys to
  tenant/session/resource filters, including batch and retry paths.
- Trace every memory writer, summarizer, merge and later privileged reader.
  Check provenance and whether low-trust observations become durable policy.
- Examine prompt/history serialization for role or provenance confusion. Confirm
  which trust decision or capability can change, not merely whether text looks
  like a higher-priority instruction.
- Follow model output into rendering, links, file writes, command arguments and
  other sinks. Apply the destination's real validation and encoding contract.

## Bind Approval to the Final Action

Authorization and user intent are separate checks. A tool can hold valid user
credentials while performing an action that the user never requested or approved.
Trace the final principal, operation, resource, destination and arguments from
approval through dispatch and every side effect. Check queued, resumed, delegated
and retried actions for changes after approval and before use.

Inspect whether a sub-agent or MCP call inherits broader credentials, filesystem
access or tools than required. Verify server/tool identity and schema-to-dispatch
agreement. Descriptions and tool responses must not grant policy authority; a
schema declaration alone does not prove that runtime arguments are constrained.

Check cancellation, retry and recursive delegation limits when actions consume
shared resources or paid quota. Do not invoke real accounts, external APIs or
paid operations to demonstrate a failure.

## Validate the Actual Boundary

State the attacker-controlled source, affected principal, executing identity,
exact resource/action, intended authorization/approval control and demonstrated
result. Seek the strongest deterministic control that refutes the claim. Use
dummy identities and mocked tools under the skill's execution safeguards.
Unknown provider/model behavior stays a named validation blocker; do not assume
the model follows an injection or that a persuasive prompt defeats a control.
Require independent verification before confirmation and keep policy/hardening
observations distinct from demonstrated vulnerabilities.
