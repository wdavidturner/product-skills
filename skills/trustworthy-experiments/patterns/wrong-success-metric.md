---
title: Choose the Right Success Metric (OEC)
impact: CRITICAL
tags: metrics, oec, lifetime-value, guardrails
---

## Choose the Right Success Metric (OEC)

Optimizing the wrong metric is worse than not running experiments at all. You'll confidently ship changes that hurt your business.

**Incorrect (optimizing short-term revenue):**

> **Email Team OEC:** Revenue attributed to email clicks
>
> **Result:** Team sends more and more emails to drive clicks.
>
> **Six months later:**
>
> - Email revenue up 40%
> - Unsubscribe rate up 300%
> - Customers increasingly annoyed
> - Long-term revenue: down
>
> **PM:** "But every experiment showed positive results!"

Every experiment did improve the metric they were tracking. But the metric was wrong — it didn't account for the long-term cost of annoying customers.

**Correct (optimizing for lifetime value):**

> **Email Team OEC:** Revenue from email clicks MINUS (cost per unsubscribe x unsubscribes)
>
> **Data Science investigation:** What's an unsubscribe worth?
> - Unsubscribed users can't receive future emails
> - Average future value of an email subscriber: $4.50
>
> **New analysis reveals:**
>
> More than half of email campaigns were actually negative when accounting for unsubscribes.
>
> **Result:** Team focuses on high-value, low-annoyance campaigns. Overall email revenue increases AND unsubscribes decrease.
>
> **Bonus insight:** When users unsubscribe, offer "unsubscribe from this campaign type only" as default. Reduces the cost of each unsubscribe, enables more experimentation.

**Why it matters:**

Your OEC must be causally predictive of customer lifetime value. Easy-to-game metrics (clicks, pageviews, time on site) often hurt the things that matter (retention, satisfaction, actual purchases). Always pair success metrics with guardrails that protect what you can't afford to lose.
