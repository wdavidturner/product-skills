---
title: Get Results Faster Without Losing Validity
impact: MEDIUM
tags: variance-reduction, cuped, capping, efficiency
---

## Get Results Faster Without Losing Validity

You can get trustworthy results with fewer users by reducing metric variance. This doesn't mean cutting corners — these are statistically valid techniques that make your data more efficient.

**Incorrect (just running shorter):**

> PM: "We don't have time for a 2-week experiment. Let's just run for 3 days."
>
> Data Scientist: "But we won't reach statistical power—"
>
> PM: "It's fine, we'll just look at the directional trend."
>
> **Result:** Meaningless data that could point in either direction by chance.

Running shorter without addressing variance just gives you noise.

**Correct (using variance reduction techniques):**

> **Technique 1: Metric Capping**
>
> Problem: Revenue metric has huge variance because 0.1% of users spend 100x more than average.
>
> Solution: Cap the metric. "If anyone spends more than $500, count it as $500."
>
> Result: Variance drops 40%, need 40% fewer users for same power.
>
> **Example at Airbnb:**
> - Nights booked varies wildly (some agencies book hundreds)
> - Capping at 30 nights/month dramatically reduces variance
> - Same statistical power with fewer users

---

> **Technique 2: CUPED (Pre-Experiment Adjustment)**
>
> Problem: Users who spent a lot before the experiment also spend a lot during, creating noise.
>
> Solution: Use pre-experiment behavior to adjust post-experiment metrics. "Subtract out" the predictable variation.
>
> Result: Unbiased estimate with lower variance. Papers show 20-50% variance reduction in some cases.
>
> **How it works:**
> - User spent $100 before experiment (control period)
> - User spent $120 during experiment
> - Adjusted metric accounts for their baseline, isolating the treatment effect

---

> **Technique 3: Stratified Randomization**
>
> Problem: Treatment group happens to get more high-spenders by chance.
>
> Solution: Stratify randomization by known high-variance segments.
>
> Result: Groups are balanced on important dimensions, reducing variance from random imbalance.

**Why it matters:**

These techniques are mathematically valid ways to increase experiment efficiency. They don't sacrifice correctness — they reduce noise so the signal is clearer. The CUPED paper from Microsoft shows significant speedups without losing validity.
