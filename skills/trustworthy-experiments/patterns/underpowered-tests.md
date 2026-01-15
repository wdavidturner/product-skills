---
title: Underpowered Tests Tell You Nothing
impact: CRITICAL
tags: sample-size, power, statistics, planning
---

## Underpowered Tests Tell You Nothing

Running an experiment without enough users is like trying to hear a whisper at a rock concert. Even if there's a real effect, you won't detect it — and "no significant result" doesn't mean "no effect."

**Incorrect (running anyway with too few users):**

> **Startup PM:** "We have 5,000 monthly active users. Let's A/B test the new onboarding flow."
>
> **Two weeks later:**
>
> Results: +8% activation, P = 0.35
>
> PM: "Not significant. Guess the new flow doesn't work. Let's try something else."
>
> **Reality:** The new flow actually improves activation by 8%. But with only 5,000 users split 50/50, the experiment had just 15% power to detect this effect. There was an 85% chance of missing a real improvement.

The team abandoned a winning idea because they couldn't detect the signal.

**Correct (do the math first):**

> **PM:** "We have 5,000 MAU. Can we A/B test the new onboarding?"
>
> **Data Scientist:** "Let me check. To detect a 10% improvement in activation with 80% power, we need about 40,000 users per group. With 5,000 total users, we can only reliably detect effects larger than 25%."
>
> **PM:** "So we'd only catch massive wins or disasters."
>
> **Data Scientist:** "Right. Our options:
> 1. Focus on qualitative research instead
> 2. Run for 8 weeks to accumulate more users
> 3. Only test ideas we expect to have huge impact"
>
> **PM:** "Let's do user interviews and wait until we have more traffic."

**Why it matters:**

Underpowered experiments don't just waste time — they cause you to abandon good ideas and keep bad ones. Kohavi's rule: you need 200,000+ users for experimentation to really work. Below that, only test big bets and accept you'll miss smaller improvements.
