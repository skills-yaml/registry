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
│   │       ├── SKILL.md
│   │       ├── latest/ -> v1.0.0/  # Symlink to latest
│   │       ├── default/ -> v1.0.0/ # Symlink to default
│   │       └── v1.0.0/    # Pinned version
│   └── system/
│       └── devops-manager/ # System monitoring and management
│           ├── SKILL.md
│           ├── latest/ -> v1.0.0/
│           ├── default/ -> v1.0.0/
│           └── v1.0.0/
└── agents/
    └── claude/         # Agent integration
        └── MANIFEST.md
```

## Skills

### Software Development
- **spec** - Write clear, reviewable software specs with Symphony-style structure

### System
- **devops-manager** - Manage system services, health, security, and updates on Debian/Docker machines

## Adding New Skills

See [SKILL_STRUCTURE.md](./SKILL_STRUCTURE.md) for complete requirements.
See [VERSIONING.md](./VERSIONING.md) for versioning rules.

Quick start:
1. Add your skill directory: `skills/<category>/<skill-name>/`
2. Create `SKILL.md` with version in frontmatter
3. Create version directory: `skills/<category>/<skill-name>/v1.0.0/`
4. Copy skill files into version directory
5. Create symlinks: `latest -> v1.0.0` and `default -> v1.0.0`
6. Update this README with the new skill description
7. Commit and push to GitHub

Example for new skill at v1.0.0:
```bash
mkdir -p skills/my-category/my-skill/v1.0.0
# Create SKILL.md with version: "1.0.0"
cp -r my-files/* skills/my-category/my-skill/v1.0.0/
cd skills/my-category/my-skill
ln -s v1.0.0 latest
ln -s v1.0.0 default
```

## License

All skills are open source and available for use with skm.
