---
name: spec
description: "Write clear, reviewable software specs with a Symphony-style structure: problem, goals, non-goals, design, alternatives, rollout, risks, and open questions. Use this when drafting a spec, RFC, design doc, or implementation plan that should be easy for humans and agents to review."
---

# Spec Writing

Write specs that make the decision and the reasoning obvious. Favor a crisp structure, explicit tradeoffs, and a narrow scope.

## When to use

Use this skill when you need to:

- draft a new feature spec or RFC
- turn an idea into an implementation-ready plan
- review an existing proposal for gaps, ambiguity, or missing risks
- convert a rough conversation into a reusable document
- rewrite an existing process, architecture, or policy doc into a cleaner spec-style format
- turn a Linear ticket into a crisp spec, especially when the ticket is incomplete and needs a structured list of missing details

If you're rewriting docs, favor concise section headings, explicit scope boundaries, and consistent terminology across related files.

## Core principles

- Start with the decision, not the story.
- Separate *what* from *how*.
- Make scope boundaries explicit.
- Surface assumptions early.
- Prefer concrete acceptance criteria over vague intent.
- Keep the document readable in one pass.
- If a detail is only useful for one session, move it to `references/` instead of creating a narrower skill.

## Recommended spec shape

1. **Title and summary**
   - One-sentence description of the change.
   - State the intended outcome.

2. **Problem statement**
   - What is broken, missing, or costly today?
   - Who is affected and how?

3. **Goals**
   - What the spec must accomplish.
   - Keep them measurable when possible.

4. **Non-goals**
   - What is explicitly out of scope.
   - Prevents scope creep and accidental assumptions.

5. **Proposed design**
   - The recommended approach.
   - Break into components, flows, or phases.

6. **Alternatives considered**
   - Short comparison of plausible options.
   - Explain why the chosen path wins.

7. **Risks and tradeoffs**
   - Technical, operational, and user-facing risks.
   - Include mitigations where possible.

8. **Rollout plan**
   - Migration, feature flags, backward compatibility, or staged release notes.

9. **Validation and acceptance criteria**
   - How we know the work is done.
   - Prefer testable statements.

10. **Open questions**
    - Items that still need input or investigation.

## Writing process

1. Identify the audience.
   - Decide whether the doc is for implementers, reviewers, or stakeholders.

2. Collect the minimum facts.
   - Gather only enough context to make the proposal concrete.

3. Write the rough outline first.
   - Fill all major sections before polishing prose.

4. Tighten scope.
   - Remove anything that does not support a decision or implementation.

5. Check for missing decisions.
   - If the reader would still ask "which option?", the spec is incomplete.

6. Add review aids.
   - Tables are not supported in Telegram delivery, so prefer bullets and labeled fields.
   - Use concise headings and short paragraphs.

## Quality bar

A good spec lets a reader answer these questions quickly:

- What problem are we solving?
- Why this approach?
- What is out of scope?
- What could go wrong?
- How will we know it worked?

## Support files

- `references/rewrite-pattern.md` — concise rewrite pattern for converting existing docs into spec-style documents.

## Style tips

- Prefer plain language over jargon.
- Use short sections and explicit labels.
- Avoid hidden requirements.
- Name invariants and constraints directly.
- If a section is empty, either remove it or explain why it is intentionally empty.

## Practical guardrails

- Do not create a new skill for each one-off spec topic.
- Keep this as the umbrella skill for spec writing.
- Put session-specific examples, edge cases, and research excerpts in `references/`.
- Put reusable scaffolding in `templates/`.
- Put deterministic checks or generation helpers in `scripts/`.
