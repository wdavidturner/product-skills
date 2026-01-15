---
title: Don't Peek at P-Values — Let Experiments Run
impact: CRITICAL
tags: statistics, p-value, early-stopping, false-positives
---

## Don't Peek at P-Values — Let Experiments Run

Checking P-values daily and stopping when they look "significant" dramatically inflates your false positive rate. What looks like 5% error becomes 30%+ error.

**Incorrect (peeking and stopping early):**

> **Day 3 of planned 14-day experiment:**
>
> PM: "I checked the dashboard and we hit P < 0.05! The new checkout flow is +4.2% conversion. Let's ship it!"
>
> Data Scientist: "Great, we can stop the experiment and launch."
>
> **Two months later:**
>
> PM: "Our conversion rate hasn't improved at all since launch. What happened?"

The team thought they had a 5% chance of being wrong. In reality, by checking repeatedly and stopping at the first "significant" result, their false positive rate was over 30%.

**Correct (pre-commit to runtime):**

> **Day 3 of planned 14-day experiment:**
>
> PM: "I saw P < 0.05 on the dashboard. Should we ship early?"
>
> Data Scientist: "No. We committed to 14 days because that's what our power calculation required. Looking now is just seeing noise fluctuate. Let's check again at Day 14."
>
> **Day 14:**
>
> Data Scientist: "Experiment complete. P = 0.12. No significant effect."
>
> PM: "Good thing we didn't ship. What we saw on Day 3 was random fluctuation."

**Why it matters:**

P-values bounce around during an experiment. If you check 10 times and stop at any "significant" reading, you're running 10 tests, not one. Each check is a chance to be fooled by noise. Pre-commit to your runtime and check only when complete.
