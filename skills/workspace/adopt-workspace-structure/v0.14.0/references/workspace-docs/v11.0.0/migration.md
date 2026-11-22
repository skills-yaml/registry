# Migration to Workspace Docs 11.0.0

This major release adds the [Unfinished Work Notice](./sdlc.md#unfinished-work-notice).
When a task ends before its requested outcome is fully delivered, the agent's
final hand-off opens with `**Not finished:**` and explains, in plain language,
what was done, why it stopped, numbered possible fixes with who must act and a
recommendation, and where the work is preserved. Lifecycle states, approval
boundaries, review rules and CI selection are unchanged, and older released
packages keep their own contracts.

Update the generated context from agents-template.md, preserving manual rules,
and pin `workspace-docs@11.0.0` in the project selection and lock. Add the
notice to current SDLC guidance, skills and role profiles. A toolkit that
carries the rule declares Workspace Docs 11 compatibility. Update any
enforcement and tests, and regenerate native profiles.

From older pins, apply the relevant earlier migration notes first, including
the [v10 operations boundary](../v10.0.0/migration.md).
