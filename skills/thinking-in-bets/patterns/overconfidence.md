---
title: Use Ranges, Not Point Estimates
impact: HIGH
tags: overconfidence, forecasting, estimates, ranges
---

## Use Ranges, Not Point Estimates

Point estimates ("It'll take 3 months") create false precision. You're more uncertain than you think. Using ranges with confidence levels forces you to acknowledge what you don't know.

**Incorrect (point estimates with false precision):**

> **Sprint planning:**
>
> PM: "How long will the checkout redesign take?"
>
> Engineer: "3 weeks."
>
> PM: "Great, I'll tell stakeholders end of month."
>
> [6 weeks later, it's still not done.]
>
> PM: "What happened? You said 3 weeks."
>
> Engineer: "There were complications I didn't anticipate."

A single number implied certainty that didn't exist. Now there's a credibility problem.

**Correct (ranges with confidence levels):**

> **Sprint planning:**
>
> PM: "How long will the checkout redesign take?"
>
> Engineer: "If everything goes right—no surprises, no dependencies, no scope changes—2 weeks. That's my optimistic case. Realistically, 3-4 weeks. If we hit integration issues with the payment provider like last time, could be 6 weeks."
>
> PM: "So you're saying 2-6 weeks range. What are you 80% confident in?"
>
> Engineer: "80% it's done in 4 weeks or less."
>
> PM: "Good. I'll tell stakeholders 4 weeks with a note that it could stretch to 6 if we hit payment integration issues."

Now expectations are calibrated. If it takes 5 weeks, that's within the communicated range—not a failure.

**How to calibrate estimates:**

| Confidence Level | What It Means |
|------------------|---------------|
| 50% | Coin flip. Could go either way. |
| 80% | Pretty confident, but 1-in-5 chance you're wrong. |
| 90% | Very confident, but still 1-in-10 surprise possible. |
| 99% | Almost certain (but "almost" is doing work here). |

Ask: "If I made 10 estimates at this confidence level, how many would I expect to be wrong?"

**Why it matters:**

Overconfidence is one of the most documented cognitive biases. Studies show that when people say they're 90% confident, they're right about 70% of the time. Ranges force humility. They also make it clear what you're betting on—and what could go wrong.
