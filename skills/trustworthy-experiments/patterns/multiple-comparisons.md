---
title: Testing Many Metrics Inflates False Positives
impact: HIGH
tags: multiple-comparisons, false-positives, metrics, bonferroni
---

## Testing Many Metrics Inflates False Positives

If you test 20 metrics at P < 0.05, you expect one "significant" result by pure chance, even if nothing changed. Cherry-picking the significant one is lying with statistics.

**Incorrect (fishing for significance):**

> **Experiment:** New recommendation algorithm
>
> **Primary metric (revenue):** No significant change
>
> PM: "Let me check the other metrics..."
>
> **Secondary metrics checked:**
> - Click-through rate: not significant
> - Time on site: not significant
> - Pages per session: not significant
> - Add to cart rate: not significant
> - Mobile conversion: not significant
> - Desktop conversion: not significant
> - New user engagement: not significant
> - Return user engagement: not significant
> - Category A views: not significant
> - **Category B views: P = 0.04**
>
> PM: "The algorithm improves Category B views! Let's ship it."

With 10 metrics tested, there's roughly a 40% chance of finding at least one "significant" result by chance. The PM found noise, not signal.

**Correct (pre-specifying metrics and adjusting):**

> **Experiment Design:**
> - Primary metric: Revenue (ship decision)
> - Secondary metrics: CTR, conversion, add-to-cart
> - Exploratory metrics: Everything else (hypothesis generation only)
>
> **Analysis:**
> - Primary metric (revenue): P = 0.15, not significant → Do not ship
> - Secondary metrics: None significant → Confirms no-ship decision
> - Exploratory: Category B views up (P = 0.04)
>
> PM: "The exploratory finding is interesting but not actionable. We won't ship based on it. We could design a follow-up experiment specifically testing Category B impact."
>
> Data Scientist: "Right. If we wanted to ship based on secondary metrics, we'd need to apply Bonferroni correction — dividing our threshold by the number of tests. With 4 secondary metrics, we'd need P < 0.0125, not 0.05."

**Why it matters:**

Pre-specify your primary metric. Be clear which metrics are for shipping decisions vs. learning. If testing multiple metrics for ship decisions, adjust your threshold (Bonferroni: divide alpha by number of tests). Exploratory findings are hypotheses for future experiments, not reasons to ship.
