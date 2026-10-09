# Contributing

How to add a skill to the one skilldeck plugin.
Open this before creating a folder. The authoring rules are in [`.agents/conventions.md`](.agents/conventions.md).
Back to [skilldeck](README.md).

`foundation/`, `engineering/`, `design/`, and `process/` are folders inside one plugin. They are not four plugins.

## Where a skill goes

```text
plugins/skilldeck/skills/<bucket>/<name>/SKILL.md
```

`plugins/skilldeck/skills/engineering/debug/` is the example. The folder name is the skill name.

Required frontmatter:

```yaml
---
name: debug
description: One line that says when to run it, and when not to.
---
```

`name` matches the folder. Anything else the validator requires is in the conventions.

## Before you open a pull request

```bash
python3 scripts/validate.py
```

Add a line under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

Issues for a new skill use the Skill template: name, bucket, and when it should run. The label `good first skill` is for a new skill inside this plugin that a new contributor can finish.
