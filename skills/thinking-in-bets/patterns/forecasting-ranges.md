---
title: Replace Certainty with Calibrated Probability Ranges
impact: MEDIUM
tags: forecasting, probability, calibration, uncertainty
---

## Replace Certainty with Calibrated Probability Ranges

"I think this will work" or "This will fail" are useless statements. They sound like predictions but carry no information about confidence level. Replace certainty language with probabilities you can track and calibrate.

**Incorrect (binary certainty language):**

> **Feature prioritization meeting:**
>
> PM 1: "I think customers will love the new onboarding flow."
>
> PM 2: "I think it's risky. They might not adopt it."
>
> VP: "Well, which is it?"
>
> [Both PMs dig in. No resolution. Decision made by whoever argues loudest.]

Neither PM has said anything actionable. "Love" and "risky" aren't falsifiable.

**Correct (calibrated probabilities):**

> **Feature prioritization meeting:**
>
> PM 1: "I'm 70% confident the new onboarding flow will improve Day-7 retention by at least 5 percentage points."
>
> PM 2: "I'm at 40% on the same outcome. My concern is that the flow is longer, and we've seen drop-off on longer flows before."
>
> VP: "Interesting spread. PM1, you're at 70%, PM2 is at 40%. Let's discuss what would have to be true for each of you to move 20 points."
>
> PM 1: "If we saw significant drop-off at step 3 in testing, I'd drop to 50%."
>
> PM 2: "If we got qualitative feedback that the added steps feel 'worth it,' I'd move to 60%."
>
> VP: "Good. Let's run a small test for both signals before full rollout."

Now the disagreement is quantified, the assumptions are explicit, and there's a path to resolution.

**How to calibrate your forecasts:**

1. **Start tracking your predictions.** Write them down with probabilities.
2. **Check calibration over time.** Of predictions you said were 70% likely, did 70% come true?
3. **Adjust based on evidence.** Most people are overconfident—you probably need to widen your ranges.
4. **Use reference classes.** "Of similar projects, how many hit their timelines?"

**Common calibration errors:**

| You Say | Reality | Fix |
|---------|---------|-----|
| "90% sure" | Right 70% of the time | You're overconfident. Say 70%. |
| "50/50" | Means "I don't know" | Do the work to form an actual view. |
| "I'm sure" (100%) | Almost never actually 100% | Even highly certain beliefs have some uncertainty. |

**Why it matters:**

Probabilities create accountability. "I said 70% and was wrong" is learnable. "I said it would work and it didn't" teaches nothing. Over time, calibrated forecasters get much better at predicting outcomes—and at knowing what they don't know.
