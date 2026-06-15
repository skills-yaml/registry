# Shared installation for reusable skills

Use this pattern when you want a skill to be discoverable by other agents in the shared library:

1. Keep the canonical skill directory under the shared skills root for this runtime.
2. Ensure the agent config scans that shared root via `skills.external_dirs`.
3. Put reusable starters in `templates/`.
4. Put session-specific notes, quirks, and condensed research in `references/`.
5. Put deterministic probes or validation helpers in `scripts/`.

For this environment, the shared root used in the session was `~/.agents/skills`, and Hermes was configured to include it in `skills.external_dirs`.

Avoid making a new skill for a one-off session artifact. Add a reference note instead and keep the umbrella skill broad.