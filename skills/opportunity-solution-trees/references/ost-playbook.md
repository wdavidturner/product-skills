# Opportunity Solution Trees Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## Table of Contents

- Tree structure deep dive
- Experience maps and opportunity framing
- Interviewing for opportunities
- Evaluating solutions and assumptions
- Collaboration model
- Checklists

## Tree Structure Deep Dive

The tree connects outcomes to opportunities, then to solutions and experiments.

- **Outcome**: measurable business result (customer behavior change)
- **Opportunities**: customer needs or pains (not solutions)
- **Solutions**: multiple ideas that address one opportunity
- **Experiments**: tests for the riskiest assumptions

Example outcomes:
- Increase 30-day retention from 25% to 35%
- Reduce time-to-first-value from 7 days to 1 day

Non-outcomes (outputs):
- Launch the new onboarding flow
- Ship 12 features this quarter

## Experience Maps and Opportunity Framing

Organize opportunities around the customer journey, not your org chart.

Example experience map for streaming:
1. Trigger (decide to watch)
2. Platform selection
3. Content discovery
4. Evaluation
5. Viewing
6. Post-viewing

Each step becomes a top-level branch. Capture the specific needs under each branch.

### Vertical Decomposition

Break broad opportunities into specific, solvable moments.

Example:
```
Outcome: Increase engagement
  Opportunity: Hard to decide what to watch
    Opportunity: Too many options
      Opportunity: I keep scrolling and cannot commit
    Opportunity: I cannot tell if a show is good
      Opportunity: Thumbnails do not explain the show
```

## Interviewing for Opportunities

Collect stories, not preferences. Ask about specific moments.

Good prompts:
- "Tell me about the last time you watched something."
- "Set the scene. Where were you? What time was it?"
- "Walk me through what happened next."

Signals to listen for:
- "I usually just..." (workaround)
- "It took a while to..." (friction)
- "I wish I could..." (desire)
- "I gave up and..." (abandoned task)

## Evaluating Solutions and Assumptions

Compare multiple solutions for the same opportunity using simple criteria:

| Criteria | Solution A | Solution B | Solution C |
|----------|------------|------------|------------|
| Addresses the opportunity | Strong | Medium | Medium |
| Effort to build | High | Low | Medium |
| Risk level | Medium | Low | High |
| Dependencies | None | Design | Backend |

Break each solution into assumptions and test the riskiest first.

Example solution: add "why you'll like this" explanations

| Assumption | Type | Risk | Test |
|------------|------|------|------|
| Users struggle to evaluate content | Desirability | Medium | Review interview data |
| Users will notice explanations | Usability | High | Prototype test |
| Personalization feels helpful | Desirability | High | Interview with mockups |
| We can generate explanations | Feasibility | High | Technical spike |
| Explanations increase intent | Viability | Medium | Landing page test |

## Collaboration Model

Share the tree with the product trio to align decisions:

- Product: owns outcome and prioritization
- Design: shapes solutions and usability tests
- Engineering: assesses feasibility and risks

## Checklists

### Roadmap Planning
- Define the outcome for the period.
- Identify the top opportunities that drive the outcome.
- Ensure multiple solutions per opportunity.
- Identify and test the riskiest assumptions.

### Feature Prioritization
- Name the opportunity the feature addresses.
- Verify the opportunity comes from research.
- List alternative solutions.
- Confirm how it ladders to the outcome.

### Stakeholder Alignment
- Show the path from outcome to opportunity to solution.
- Make trade-offs visible in the tree.
- Surface assumptions for debate.
