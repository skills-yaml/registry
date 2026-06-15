# Registry

Central registry of skills and agents for the skm project.

## Structure

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

1. Add your skill directory under the appropriate category in `skills/`
2. Include a `SKILL.md` file with proper metadata
3. Update this README with the new skill description
4. Commit and push to GitHub

## License

All skills are open source and available for use with skm.
