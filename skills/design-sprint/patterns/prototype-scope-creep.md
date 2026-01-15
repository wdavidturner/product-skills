---
title: Prototype the Critical Path, Not the Whole Product
impact: HIGH
tags: thursday, prototype, scope, focus
---

## Prototype the Critical Path, Not the Whole Product

Thursday has one job: build just enough to test Friday's hypothesis. Scope creep turns a focused prototype into an unfinished product.

**Incorrect (full product prototype):**

> **Thursday 9am:** Team starts on the storyboard flow.
>
> **Thursday 11am:**
> "What if they click the settings icon?"
> "We should show the login screen."
> "What about error states?"
> "Can we add the admin dashboard?"
>
> **Thursday 3pm:** Team is building screens that aren't in the storyboard.
>
> **Thursday 6pm:** Core flow is 70% done. Settings, login, admin are 30% done each.
>
> **Friday:** Customers can't complete the core flow. The extra screens are confusing dead ends.
>
> *Result:* Nothing is testable. Week wasted on scope creep.

**Correct (critical path only):**

> **Thursday 9am:** Facilitator posts the storyboard. "We're building frames 1-13. Nothing else."
>
> **Thursday 11am:**
> "What if they click the settings icon?" → "We'll put a fake icon that does nothing."
> "Should we show the login screen?" → "Prototype starts at the dashboard. Assume they're already logged in."
> "What about error states?" → "We'll guide customers through the happy path."
>
> **Thursday 3pm:** Core flow is complete. Team does a trial run.
>
> **Thursday 5pm:** Core flow is polished. Realistic data, smooth transitions.
>
> **Friday:** Customers complete the entire critical path. Clear feedback on the core experience.
>
> *Result:* Complete, testable prototype. Clear signal on the hypothesis.

**Why it matters:**

The prototype is not the product. It's a facade to test a specific hypothesis. Every screen you build outside the storyboard is a screen that:
- Takes time away from the critical path
- Creates potential dead ends for Friday customers
- Reduces the quality of what you're actually testing

**Scope control techniques:**
- "Can we click this?" → "No, just the highlighted buttons."
- "What if they go back?" → "We'll guide them forward."
- "Should we show [edge case]?" → "Only if it's in the storyboard."
