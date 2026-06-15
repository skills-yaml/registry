---
name: claude
version: "1.0.0"
description: "Claude Code integration for skm"
compatibilities:
  - ">=1.0.0"
required_skills: []
recommended_skills:
  - software-development/spec
  - system/devops-manager
tags:
  - ai
  - assistant
  - code-generation
---

# Claude Agent Integration

## Overview

Integration configuration for Claude Code agent with skm.

## Configuration

### Default Settings

```yaml
# .claude/skills/config.yaml
skill_paths:
  - ~/.claude/skills
  - ./skills
```

## Compatibility

This agent integration is compatible with:
- Skill API versions: >= 1.0.0
- skm versions: >= 0.1.0

## Supported Features

- [x] Skill discovery and loading
- [x] Symlink resolution
- [x] SKILL.md parsing
- [ ] Auto-update checking
- [ ] Skill health monitoring
