# Resources

What has been measured, the philosophy, and how this repo is laid out.
Open this when you are checking a claim, extending the pack, or running the validator.
Back to [jon-skills](../../README.md).

## What is verified where

Only Claude Code has been measured, and `evals/RESULTS.md` records what was tested, what was not, and what failed. Three things carry over:

- **A model-invoked skill was never reached for on its own** across eleven runs, on two models. The pack works around this three ways: wiring the important gates into skills that do fire, offering to write a verification rule into the repo's `AGENTS.md`, and offering a routing block in the same file that maps the recurring moments of a task to the skill that owns each. The first has eval evidence behind it. The second and third rest on the same reasoning (a file read every turn reaches the model, a description does not) and neither has been measured yet.
- **Cross-skill chaining** (`Call the Skill tool with "..."`) is Claude Code phrasing. Whether another harness acts on it is untested, so elsewhere treat each skill as self-contained.
- **Nothing in `design/`, and no frontend skill, has an eval.** Eight skills now cover that territory on reasoning alone. `design-review` is the only one whose output is structured enough to score objectively, so it is the one to measure first.

User-invoked skills (`setup-skills`, `align-first` aside, plus `investigate-product`, `plan-delivery`, `retro`) rely on `disable-model-invocation`, a Claude Code key, plus `policy.allow_implicit_invocation: false` for OpenAI-style hosts. A harness honouring neither may reach for them on its own, which matters most for `investigate-product`, since it is forbidden from proposing a solution and would derail a coding task.

## Philosophy

Detect before you decide. Recommend before you impose. Ask before you assume. Prove before you claim.

Small, composable skills that defer to the project in front of them, so they stay useful across personal and company codebases instead of fighting whatever is already there.

## Repo layout

- `skills/` grouped into `foundation/`, `engineering/`, `design/` and `process/`. `docs/<bucket>/` holds human-facing pages for user-invoked skills. `docs/pack/` holds the longer pages linked from the README.
- `evals/` the test harness and its findings. `RESULTS.md` records what has and has not been measured, including what failed.
- `scripts/validate.py` the checks: frontmatter parses, names match folders, guardrails present, cross-references and relative links resolve, manifests in sync, no undeclared external skill, and markdown style holds. `.githooks/pre-commit` runs it before a commit; `.github/workflows/validate.yml` runs it on push and pull request plus a weekly link check.
- `.agents/conventions.md` how to write and extend a skill here. `AGENTS.md` instructions for an agent working on this repo, not for consumers.
- `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/` (marketplace) plus `plugins/jon/` (Cursor plugin), `gemini-extension.json` one manifest per harness, kept in sync by the validator. `GEMINI.md` is the context file the Gemini extension loads.

```bash
pip install pyyaml
git config core.hooksPath .githooks   # once per clone
python3 scripts/validate.py           # offline, fast
python3 scripts/validate.py --links   # also resolves external URLs
```

Skip the hook for one commit with `git commit --no-verify`. Without pyyaml the validator still runs, reports that frontmatter is only partially checked, and CI covers the rest.

No Node toolchain here on purpose, and no markdown formatter: the repo is markdown, YAML and two scripts, so there is no JavaScript to lint, and a formatter was measured against it and rejected (384 lines changed across 24 files while every measurable axis was already uniform). The style is checked instead of rewritten; the reasoning is in [`.agents/conventions.md`](../../.agents/conventions.md).
