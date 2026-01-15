# Skill Eval Harness

Test whether skills trigger correctly and provide useful responses. This harness helps you evaluate skill quality across different models.

## Structure

```
evals/
├── prompts/skill-prompts.yaml   # 3 prompts per skill (minimal, scenario, application)
├── templates/feedback.md        # Template for recording feedback
├── run_claude.py                # Runner for Claude models
├── run_codex.py                 # Runner for Codex models
└── runs/                        # Output directory (gitignored)
```

**Note:** The `runs/` directory is excluded from version control. Create it locally when running evals.

Output layout:

```
evals/runs/<skill-id>/<agent>/<model>/<date>.md
```

Example:

```
evals/runs/growth-loops/claude/claude-opus-4-5-20251101/2026-01-15.md
evals/runs/growth-loops/codex/gpt-5.2/2026-01-15.md
```

## How to Run

1. Pick a skill in `evals/prompts/skill-prompts.yaml`.
2. Run its prompts in a clean context for your target model.
3. Save output using the feedback template in `evals/templates/feedback.md`.
4. Record whether the skill triggered, whether the response felt useful, and whether the SKILL.md had too much or too little context.

## CLI Runners

Each runner executes every prompt in a separate process (clean context) and captures only the final assistant response. Provide a command template that accepts `{model}` and `{prompt}`.

- **Claude runner** parses JSON output; include `--print --output-format json --no-session-persistence --tools ""` so only the `result` field is used.
- **Codex runner** automatically adds `--output-last-message <tempfile>`, so your template should not include that flag (it’s handled internally).

Example commands:

```bash
export CLAUDE_CMD='claude --print --output-format json --no-session-persistence --tools "" --model {model} {prompt}'
python3 evals/run_claude.py --model claude-opus-4-5-20251101

export CODEX_CMD='codex exec --full-auto --color never --model {model} {prompt}'
python3 evals/run_codex.py --model gpt-5.2
```

Optional filters:

```bash
python3 evals/run_claude.py --model claude-opus-4-5-20251101 --skill growth-loops --skill okrs
```

## Prompt Types

Each skill has 3 prompts testing different trigger scenarios:

| Type | Purpose | Example |
|------|---------|---------|
| **minimal** | Direct ask with clear intent | "Explain growth loops and how they differ from funnels." |
| **scenario** | Realistic PM problem (implicit trigger) | "We're spending $50k/month on paid acquisition but growth flatlines whenever we pause ads." |
| **application** | User actively applying the framework | "Help me design a growth loop for our B2B SaaS product." |

## Tips

- If a skill doesn't trigger for `minimal`, add the missing phrase to the frontmatter description.
- If `scenario` doesn't trigger, the description may need more problem-oriented language.
- If responses feel generic, add sharper patterns or a "How to Apply" section to SKILL.md.
