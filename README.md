# skills

36 skills for JavaScript, TypeScript, React, and React Native, installed from [skilldeck](https://github.com/jonathanjuliani/skilldeck).
They read the repo before they pick a stack.

Detect before you decide. Recommend before you impose. Ask before you assume. Prove before you claim.

## Do this

Pick one install. Both at once installs every skill twice.

1. Any agent, choose which skills: `npx skills add jonathanjuliani/skills`
2. All 36, as a plugin from skilldeck. In Claude Code, pick marketplace or npm. Codex uses the marketplace. Cursor and Gemini: [Install and remove](docs/pack/install.md).

Marketplace, in Claude Code:

```text
/plugin marketplace add jonathanjuliani/skilldeck
/plugin install skills@skilldeck
```

npm, in Claude Code:

```bash
npm i -g @jonathanjuliani/skilldeck
skilldeck install skills
```

Codex:

```bash
codex plugin marketplace add jonathanjuliani/skilldeck
codex plugin add skills@skilldeck
```

Start a new session after a plugin install. Then once per repo:

- `/setup-skills`
- `/skilldeck:setup-skills`

It asks whether to write `.skilldeck-skills/config.yaml`. It asks again before it edits anything else.

## The pack

- **foundation** (3) — detect conventions, set up, write agent instructions
- **engineering** (22) — build, test, and ship
- **design** (6) — decide the surface before building it
- **process** (5) — align, investigate, plan, diagram, retro

One line per skill: [skills](docs/pack/skills.md).

## How a choice is made

1. **Project.** What the repo already uses. This wins.
2. **Company.** A standard the repo carries.
3. **Personal.** Your tiebreaker, only if the two above are silent.
4. **Community.** Greenfield only. Offered with a reason, confirmed first.

## Read next

- [Install and remove](docs/pack/install.md)
- [Skills](docs/pack/skills.md) — full breakdown
- [Coverage](docs/pack/coverage.md) — what the pack does and does not cover
- [Inspirations](docs/pack/inspirations.md) — prior art and companions
- [Resources](docs/pack/resources.md) — layout, checks, what was measured
