# Contributing

Thanks for your interest in improving these PM skills! Here's how you can help.

## Ways to Contribute

### 1. Improve Existing Skills

**Fix a pattern that's unclear or wrong:**
- Each skill has a `patterns/` folder with bad/good examples
- If an example doesn't resonate or is misleading, open a PR with a fix
- Keep the Incorrect/Correct format — show don't tell

**Add a missing pattern:**
- Use `patterns/_template.md` as your starting point
- Assign an impact level: CRITICAL, HIGH, or MEDIUM
- Focus on common mistakes PMs actually make

**Improve trigger phrases:**
- If a skill doesn't activate when you expect it to, the frontmatter description may need work
- Add literal phrases in quotes that match how PMs actually ask for help

### 2. Suggest New Frameworks

Open an issue with:
- Framework name and creator (if applicable)
- When a PM would use it (specific scenarios)
- Why it's actionable (not just conceptual)
- Source material (books, talks, articles)

Good candidates:
- Have clear methodology (steps, checklists, decisions)
- Solve recurring PM problems
- Can be taught through bad/good examples

### 3. Report Issues

- Skill didn't trigger when expected
- Pattern example was confusing or wrong
- Framework explanation missing key concept
- Broken links or typos

## Skill Structure

Each skill follows this format:

```
skill-name/
├── SKILL.md              # Framework overview + patterns index
├── patterns/
│   ├── _template.md      # Template for new patterns
│   └── *.md              # Individual pattern files
└── references/           # Optional supporting materials
```

See `CLAUDE.md` for detailed guidance on writing skills.

## Pull Request Process

1. Fork the repo
2. Create a branch (`git checkout -b improve-jtbd-patterns`)
3. Make your changes
4. Test that patterns render correctly in markdown
5. Submit a PR with a clear description of what you changed and why

## Code of Conduct

Be helpful, be specific, be kind. We're all here to make better PM tools.
