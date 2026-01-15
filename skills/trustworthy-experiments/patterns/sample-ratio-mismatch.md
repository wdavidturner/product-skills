---
title: Check Sample Ratio First — Off-Balance Means Invalid
impact: CRITICAL
tags: srm, validity, randomization, debugging
---

## Check Sample Ratio First — Off-Balance Means Invalid

If your 50/50 experiment split isn't actually 50/50, something is broken. The results cannot be trusted regardless of what they show.

**Incorrect (ignoring the split):**

> **Experiment Results:**
> - Control: 498,000 users
> - Treatment: 502,000 users
> - Conversion lift: +3.2% (P < 0.01)
>
> PM: "Great results! Let's ship."
>
> Data Scientist: "The numbers look good to me."

With 1 million users, a 50.2% vs 49.8% split would only happen by chance about 1 in 500,000 times. This wasn't random — something is systematically different between groups, and that difference could be causing the "lift."

**Correct (checking SRM first):**

> **Experiment Results:**
> - Control: 498,000 users
> - Treatment: 502,000 users
> - Sample Ratio Mismatch test: P < 0.0001
>
> Data Scientist: "Stop. We have sample ratio mismatch. These results are invalid. We need to find the bug."
>
> **Investigation reveals:**
> - Treatment page loads 200ms slower
> - Impatient users abandon treatment before being logged
> - The "lift" was survivorship bias — we were comparing engaged control users to only the most patient treatment users
>
> PM: "So the treatment is actually hurting us?"
>
> Data Scientist: "We don't know yet. Fix the performance bug, re-run the experiment with proper measurement."

**Why it matters:**

At Microsoft, 8% of experiments had sample ratio mismatch. Common causes: bots, performance differences, logging bugs, redirect failures. SRM is the single most important validity check — do it first, before looking at any results.
