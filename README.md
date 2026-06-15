# Registry

Central registry of skills and agents for the skm project.

## Structure

For the complete skill structure specification, see [SKILL_STRUCTURE.md](./SKILL_STRUCTURE.md).

## Versioning

For versioning rules and best practices for skills and agents, see [VERSIONING.md](./VERSIONING.md).

```
registry/
├── skills/
│   ├── software-development/
│   │   └── spec/          # Spec writing skill
│   └── system/
│       └── devops-manager/ # System monitoring and management
└── agents/
    └── (future agents)
```

## Skills

### Software Development
- **spec** - Write clear, reviewable software specs with Symphony-style structure

### System
- **devops-manager** - Manage system services, health, security, and updates on Debian/Docker machines

## Adding New Skills

See [SKILL_STRUCTURE.md](./SKILL_STRUCTURE.md) for complete requirements.

Quick start:
1. Add your skill directory under the appropriate category in `skills/`
2. Include a `SKILL.md` file with proper metadata (frontmatter required)
3. Follow the structure: `skills/<category>/<skill-name>/SKILL.md`
4. Update this README with the new skill description
5. Commit and push to GitHub

## License

All skills are open source and available for use with skm.
