# Spec rewrite pattern

Use this when converting an existing process or architecture doc into a clearer spec-style document.

## Rewrite goals
- Reduce repetition.
- Put the decision and scope first.
- Add explicit problem / goals / non-goals sections.
- Use short headings and bullets instead of long prose blocks.
- Keep the document readable in one pass.

## Suggested structure for rewrites
1. Summary
2. Problem
3. Goals
4. Non-goals
5. Main content / design / process
6. Risks and tradeoffs
7. Validation or acceptance criteria
8. Open questions

## Practical notes
- When a document is mainly process-oriented, rewrite it into a concise operating guide rather than a narrative essay.
- When a document is mainly architecture-oriented, keep the repository map and workflow together so contributors know both the layout and the sequence of changes.
- When rewriting multiple docs in the same area, align wording across them so terms like "quality gates", "validation", and "workflow" mean the same thing everywhere.
- Prefer stable labels like "Summary" and "Non-goals" over creative section names.

## Example targets from this session
- SDLC / process docs: rewrite toward clear phases, responsibilities, quality gates, and acceptance criteria.
- Architecture docs: rewrite toward repository layout, system surfaces, operating principles, and validation.
- Index docs: rewrite toward a short entrypoint that points readers to the canonical docs.
