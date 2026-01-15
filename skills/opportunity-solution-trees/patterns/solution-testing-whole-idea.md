---
title: Test Assumptions, Not Whole Ideas
impact: HIGH
tags: experiments, assumptions, testing
---

## Test Assumptions, Not Whole Ideas

Teams often run experiments that test an entire solution at once. This takes too long, costs too much, and doesn't tell you what went wrong if it fails. Break solutions into assumptions and test the riskiest ones first.

**Incorrect (testing the whole idea):**

> **Solution:** Add personalized "why you'll like this" explanations for content
>
> **Team's Approach:**
> "Let's build it and run an A/B test for 4 weeks to see if it increases engagement."
>
> **4 weeks later:**
> "Engagement was flat. Guess that idea didn't work. Let's try something else."
>
> *Result:* You spent 6+ weeks (build + test) and learned nothing about *why* it failed. Was the concept wrong? Was the execution bad? Did users not notice? Did it feel creepy? You can't improve because you don't know what broke.

**Correct (testing assumptions individually):**

> **Solution:** Add personalized "why you'll like this" explanations for content
>
> **Underlying Assumptions:**
>
> | Assumption | Type | Risk | Test |
> |------------|------|------|------|
> | Users struggle to evaluate content | Desirability | Medium | Review interview data |
> | Users will notice/read explanations | Usability | High | Prototype with eye tracking |
> | Personalization feels helpful, not creepy | Desirability | High | Interview with mockups |
> | We can generate accurate explanations | Feasibility | High | Technical spike |
> | Explanations increase viewing intent | Viability | Medium | Landing page test with fake explanations |
>
> **Testing sequence:** Start with "personalization feels helpful, not creepy" — if users find it invasive, nothing else matters.
>
> **Week 1 result:** Users loved the concept but found specific phrasing ("We know you watched...") uncomfortable.
>
> *Result:* You learned the core concept works but execution needs adjustment — in 1 week, not 6.

**Why it matters:**

Assumption testing is what makes continuous discovery sustainable. Teams stuck in "big experiment" mode can barely test one idea per quarter. Teams testing assumptions run half a dozen tests per week across multiple solutions. Speed of learning determines speed of progress.
