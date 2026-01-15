# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This repository generates skills for AI agents from podcast transcripts. Skills capture product management wisdom, frameworks, and methodologies from industry experts in a portable, reusable format.

## Skill Creation

Skills follow the [Agent Skills specification](https://agentskills.io/) — an open format for extending AI agent capabilities. See the [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) for methodology.

### Required Skill Structure

```
skill-name/
├── SKILL.md          # Main file with YAML frontmatter + overview
├── patterns/         # Concrete examples showing how to apply the framework
│   ├── _template.md  # Template for creating new patterns
│   └── *.md          # Individual pattern files (bad/good examples)
├── references/       # Optional supporting materials
└── scripts/          # Optional automation scripts
```

### SKILL.md Format

```yaml
---
name: skill-name          # lowercase, hyphens only, max 64 chars
description: What this skill does and when to use it (max 1024 chars)
---

# Skill Name

[Instructions, workflows, and guidance for AI agents to follow]
```

**Naming constraints**: No XML tags, no reserved words (avoid agent-specific brand names).

## Source Material

### Lenny's Newsletter

The transcripts in this repository are sourced from [Lenny's Newsletter](https://www.lennysnewsletter.com/), a leading resource for product management, growth, and career advice. Transcripts were [shared publicly by Lenny](https://x.com/lennysan/status/2011243567340298651) for the community to explore and build upon.

**Related resources:**
- [Lennybot](https://www.lennybot.com/) — An AI chatbot that answers questions based on the entire content of Lenny's Newsletter and podcast episodes. It provides interactive access to practical insights on product, growth, and careers.
- [Lenny's Newsletter](https://www.lennysnewsletter.com/) — The original newsletter and podcast

### Transcript Format

Transcripts are in `lennys-transcripts/` as `.txt` files named by guest (e.g., `Brian Chesky.txt`). Format is speaker-timestamped dialogue:

```
Speaker Name (HH:MM:SS):
[Content]
```

## Workflow

1. Read transcript(s) from `lennys-transcripts/`
2. Extract actionable frameworks, methodologies, or advice
3. Create skill directory in `skills/` (e.g., `skills/jobs-to-be-done/`)
4. Write `SKILL.md` with overview, patterns index, framework details, and checklists
5. Create `patterns/` folder with `_template.md` and 10-15 pattern files
6. Each pattern shows bad/good examples for one concept
7. Add `references/` if the skill benefits from supporting materials

## Skill Creation Checklist

### Frontmatter Description

The description determines when the skill gets triggered. Write it for **matching user intent**, not explaining the framework.

- [ ] **Start with active language**: "Use when you need to..." or "Helps with..."
- [ ] **Include literal trigger phrases in quotes** - the exact words someone might type
  - Example: `Use when asked to "understand why customers churn", "prep for customer interviews", or "figure out what to build"`
- [ ] **List specific trigger scenarios** in the user's language (not academic terms)
  - Bad: "Understand customer motivation through demand-side analysis"
  - Good: "Use when you need to understand why customers buy, churn, or choose competitors"
- [ ] **Avoid overly broad triggers** that would fire on generic PM questions (e.g., "what should we build" without a domain qualifier)
- [ ] **Spell out the full name** + abbreviation if applicable (e.g., "Jobs to be Done (JTBD)")
- [ ] **Credit the creator** if well-known (helps trigger on name recognition)
- [ ] **Add `argument-hint`** if the skill takes input (e.g., `argument-hint: <file-or-url>`)

### Skill Content (SKILL.md sections)

- [ ] **What It Is**: Brief explanation of the core insight (1-2 paragraphs)
- [ ] **When to Use It**: Specific situations where this applies
- [ ] **When NOT to Use It**: Prevent misapplication
- [ ] **Patterns**: Index table linking to all patterns, organized by impact level (Critical → High → Medium)
- [ ] **Core Framework**: The methodology itself — concepts, models, diagrams
- [ ] **How to Apply It**: Step-by-step process
- [ ] **Common Mistakes**: Pitfalls to avoid (brief — details go in patterns)
- [ ] **Application Checklists**: Quick reference for different contexts (product, marketing, sales, etc.)
- [ ] **Resources**: Books, links for deeper learning

### Progressive Disclosure (Selective Loading)

Skills should be helpful **without** dumping everything at once. Keep the SKILL.md lean and let patterns carry the depth.

- [ ] **SKILL.md is orientation + index** — enough to understand the framework and find patterns fast
- [ ] **Move tactical detail into patterns** — examples teach better than long exposition
- [ ] **Use references for deep dives** — only link what the agent needs when it opts in
- [ ] **Avoid redundant examples** — don’t repeat full pattern content in SKILL.md

### Do/Don't Examples (Scope + Disclosure)

**Frontmatter description**

**Do:**
```
description: Use when asked to "map customer needs to outcomes", "structure discovery around opportunities", or "Teresa Torres". Helps teams connect outcomes to customer opportunities using Opportunity Solution Trees (created by Teresa Torres).
```

**Don't:**
```
description: Use when asked "what should we build" or "make a roadmap". Helps with product strategy.
```

**SKILL.md content**

**Do:**
- Short "What It Is"
- Clear index to patterns
- One concise checklist

**Don't:**
- Full interview scripts or long case studies in SKILL.md (put in patterns or references)
- Repeating complete pattern examples in the overview

### Quality Check

- [ ] Would a PM actually say the words in your description when they need this?
- [ ] Can someone apply this framework after reading the skill (not just understand it)?
- [ ] Are the steps concrete enough to follow, not just conceptual?
- [ ] Did you include what makes this framework different from adjacent ones?

## Patterns: Show Don't Tell

The `patterns/` folder contains concrete examples that demonstrate how to apply the framework. **Examples are the content** — don't explain abstractly, show bad vs good.

### Pattern File Structure

Each pattern file follows this template:

```markdown
---
title: Pattern Title
impact: HIGH
tags: relevant, tags, here
---

## Pattern Title

Brief explanation of why this matters (1-2 sentences max).

**Incorrect (what's wrong with this approach):**

[Bad example - a realistic scenario showing the wrong way]

**Correct (what makes this better):**

[Good example - the same scenario done right]

**Why it matters:**

Optional 1-2 sentences on the consequence of getting this wrong.
```

### Impact Levels

- `CRITICAL` - Core to the framework, get this wrong and you've wasted your time
- `HIGH` - Significant impact on quality of output
- `MEDIUM` - Improves results but not fatal if missed
- `LOW` - Nice to have, refinement

### Pattern Writing Guidelines

1. **Use realistic scenarios** - Not toy examples. Show real PM situations.
2. **Make the bad example tempting** - It should look reasonable at first glance
3. **Keep examples concise** - Just enough to show the contrast
4. **Name patterns by what they teach** - `interview-asking-why.md` not `pattern-1.md`
5. **One concept per pattern** - Don't bundle multiple lessons

### Pattern Count Guidance

Aim for **10-15 patterns per skill**:
- 3-5 CRITICAL patterns (core mistakes that waste the entire effort)
- 5-7 HIGH patterns (significant quality impact)
- 2-3 MEDIUM patterns (refinements)

### Reference Implementation: JTBD

The `skills/jobs-to-be-done/` skill has 14 patterns as a reference:

**Critical:**
- `interview-asking-why.md` — Don't ask "why" — ask "walk me through what happened"
- `job-statement-too-broad.md` — "Save time" is useless — needs context + outcome
- `missing-forces.md` — Analyze all four forces, not just Push and Pull
- `interviewing-prospects.md` — Only interview people who already switched
- `conference-room-jtbd.md` — Can't hypothesize jobs without customers

**High:**
- `wrong-competitors.md` — Real competitors are what customers do *instead*
- `clustering-vs-segmenting.md` — Find pathways, don't segment demographics
- `complaints-arent-jobs.md` — "Bitching ain't switching"
- `reducing-friction.md` — Lower anxiety often beats adding features
- `context-changes-everything.md` — Same person + different context = different job
- `getting-past-pablum.md` — Push 2-3 questions past the first answer
- `milkshake-story.md` — The classic example: same product, multiple jobs

**Medium:**
- `three-energies.md` — Functional, Emotional, Social all matter
- `following-power-users.md` — Power users lead away from what scales
