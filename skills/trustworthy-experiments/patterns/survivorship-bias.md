---
title: Survivorship Bias — Don't Ignore Who Left
impact: HIGH
tags: survivorship, attrition, bias, analysis
---

## Survivorship Bias — Don't Ignore Who Left

If your treatment causes some users to leave before being measured, you're comparing apples to oranges. The remaining treatment users aren't representative.

**Incorrect (analyzing only who stayed):**

> **Experiment:** New aggressive upsell modal on checkout
>
> **Results:**
> - Control: 100,000 users reached checkout, 3% conversion
> - Treatment: 95,000 users reached checkout, 3.5% conversion
> - "Treatment wins! +17% conversion!"
>
> **What actually happened:**
>
> 5,000 treatment users bounced immediately when they saw the upsell modal. The users who stayed were more committed buyers. The "lift" is just measuring more committed users, not a better checkout flow.

**Correct (accounting for attrition):**

> **Experiment:** New aggressive upsell modal on checkout
>
> **Analysis:**
> - Control: 100,000 users reached checkout
> - Treatment: 95,000 users reached checkout
> - Sample Ratio Mismatch detected: Where did 5% of treatment users go?
>
> **Investigation:**
> - 5,000 users bounced at the upsell modal
> - These were real potential customers we lost
>
> **Correct calculation:**
> - Control: 100,000 users → 3,000 purchases (3.0%)
> - Treatment: 100,000 users assigned → 3,325 purchases (3.3%)... but wait
> - Treatment: Actually 95,000 reached checkout × 3.5% = 3,325 purchases
> - But per 100,000 assigned: 3.3% conversion
>
> **Conclusion:** The modal increases conversion among those who see it, but drives away users. Net effect is smaller than it appeared, and we're annoying customers.

**Why it matters:**

Whenever treatment and control have different numbers of users reaching a measurement point, you have differential attrition. This is a form of sample ratio mismatch. Always analyze from the point of randomization (when users were assigned), not just users who made it through.
