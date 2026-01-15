# Advanced Product Management Skills for AI Agents

 A collection of AI agent skills inspired from the guests on Lenny's Podcast.

## Purpose

This project generates reusable [Agent Skills](https://agentskills.io/) that capture product management wisdom, frameworks, and methodologies shared by industry experts.

Each skill transforms podcast insights into actionable, on-demand guidance for AI agents helping with product decisions, strategy, and execution.

## What Are Agent Skills?

Agent Skills are an [open format](https://agentskills.io/) for extending AI agent capabilities. They package:

- **Instructions** - Workflows, best practices, and domain-specific guidance
- **Resources** - Reference materials, templates, and examples
- **Scripts** - Executable utilities for deterministic operations

Skills load on-demand when relevant to a task, enabling agents to act as specialists without consuming context upfront.

## What's Included

20 frameworks from leading product thinkers:

| Skill | Creator | What It Does |
|-------|---------|--------------|
| [Design Sprint](skills/design-sprint/) | Jake Knapp | Go from problem to tested prototype in 5 days |
| [Growth Loops](skills/growth-loops/) | Brian Balfour, Elena Verna | Build compounding growth systems, not funnels |
| [Hierarchy of Engagement](skills/hierarchy-of-engagement/) | Sarah Tavel | Design retention through accruing benefits |
| [Hierarchy of Marketplaces](skills/hierarchy-of-marketplaces/) | Sarah Tavel | Build defensible marketplace businesses |
| [Hooked Model](skills/hooked-model/) | Nir Eyal | Create habit-forming products |
| [Jobs to be Done](skills/jobs-to-be-done/) | Clayton Christensen, Bob Moesta | Discover why customers hire and fire products |
| [Monetizing Innovation](skills/monetizing-innovation/) | Madhavan Ramanujam | Design pricing before building features |
| [OKRs](skills/okrs/) | Andy Grove, Christina Wodtke | Focus teams with objectives and key results |
| [Opportunity Solution Trees](skills/opportunity-solution-trees/) | Teresa Torres | Connect outcomes to customer opportunities |
| [PMF Survey](skills/pmf-survey/) | Sean Ellis, Rahul Vohra | Measure and improve product-market fit |
| [Positioning Canvas](skills/positioning-canvas/) | April Dunford | Make your product's value obvious |
| [Product-Led Growth](skills/product-led-growth/) | Elena Verna, Hila Qu | Let the product drive acquisition and monetization |
| [Product-Led SEO](skills/product-led-seo/) | Eli Schwartz | Treat SEO as a product, not marketing |
| [Radical Candor](skills/radical-candor/) | Kim Scott | Give feedback that cares and challenges |
| [Seven Powers](skills/seven-powers/) | Hamilton Helmer | Identify durable competitive advantages |
| [Shape Up](skills/shape-up/) | Ryan Singer | Ship meaningful work in fixed cycles |
| [Strategic Narrative](skills/strategic-narrative/) | Andy Raskin | Craft stories about change, not features |
| [Thinking in Bets](skills/thinking-in-bets/) | Annie Duke | Make better decisions under uncertainty |
| [Trustworthy Experiments](skills/trustworthy-experiments/) | Ronny Kohavi | Run A/B tests that produce reliable results |
| [Working Backwards](skills/working-backwards/) | Amazon | Start with the customer, work backward |

## Installation

Install skills using [add-skill](https://github.com/vercel-labs/add-skill):

```bash
# Install all skills
npx add-skill wdavidturner/product-skills

# List available skills
npx add-skill wdavidturner/product-skills --list

# Install a specific skill
npx add-skill wdavidturner/product-skills --skill jobs-to-be-done

# Install globally (available across all projects)
npx add-skill wdavidturner/product-skills --global
```

## Skill Structure

Each skill follows this format:

```
skill-name/
├── SKILL.md          # Framework overview + patterns index
├── patterns/         # Bad/good examples for each concept
│   ├── _template.md  # Template for new patterns
│   └── *.md          # Individual pattern files
├── references/       # Optional supporting materials
└── scripts/          # Optional automation scripts
```

The `SKILL.md` file requires:

```yaml
---
name: Jobs to be Done (JTBD)
description: Use when asked to "understand why customers churn", "prep for customer interviews", or "figure out what to build". The Jobs to be Done framework (created by Clayton Christensen and Bob Moesta) reveals why customers "hire" and "fire" products.
---

# Jobs to be Done (JTBD)

## When to Use It
[Specific triggers]

## Patterns
[Index of bad/good examples organized by impact level]

## The Framework
[Core concepts, methodology, checklists]

## Resources
[Books, links]
```

**Key principle:** Skills teach through **patterns** — concrete bad/good examples showing how to apply the framework correctly. The SKILL.md provides overview; the patterns show application. Favor **progressive disclosure**: keep SKILL.md focused on the minimum needed to orient and index, and push tactical detail into patterns or references.

## Source Material

Skills in this repository are generated from transcripts of product management podcast episodes. The wisdom, frameworks, and methodologies captured here come from conversations with industry experts.

### Inspiration & Attribution

This project was inspired by [Lenny's Newsletter](https://www.lennysnewsletter.com/), a leading resource for product management, growth, and career advice created by Lenny Rachitsky. It's great, promise.

Transcripts were [shared publicly by Lenny](https://x.com/lennysan/status/2011243567340298651) for the community to explore and build upon.

**Related resources:**
- [Lenny's Product Pass](https://www.lennysnewsletter.com/p/productpass) — The Product Pass gives his subscribers access to a ton of valuable tools for product managers, many of which I've personally found super useful.
- [Lennybot](https://www.lennybot.com/) — An AI chatbot that answers questions based on the entire content of Lenny's Newsletter and podcast episodes. It provides interactive access to practical insights on product, growth, and careers.


### Topics Covered

The podcast episodes cover:
- Product strategy and roadmapping
- Growth and experimentation
- Team building and leadership
- User research and discovery
- Metrics and measurement
- Go-to-market strategies

## Creating Skills

This project follows the [Agent Skills specification](https://agentskills.io/). See the [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) for methodology.

## Usage

The easiest way to install skills is with `npx add-skill` (see [Installation](#installation)).

Skills are compatible with multiple coding agents:

- **Claude Code** - `~/.claude/skills/` (global) or `.claude/skills/` (project)
- **Cursor** - `.cursor/skills/`
- **Codex** - `.codex/skills/`
- **OpenCode** - `.opencode/skill/`

## License

MIT License. See [LICENSE](LICENSE) for details.
