---
title: Data Scale Economies Flatten Fast
impact: HIGH
tags: scale-economies, data, common-mistake
---

## Data Scale Economies Flatten Fast

"We have more data than competitors" is one of the most common — and most overrated — power claims. Data advantages often don't create scale economies because the benefit curve flattens quickly. Having 10x more data rarely means 10x better outcomes.

**Incorrect (assuming data creates power):**

> **Strategy Presentation:**
>
> "Our scale economies in data are unassailable:
> - 50M user interactions per day vs competitor's 10M
> - 5 years of historical data vs their 2 years
> - This data advantage compounds — we get smarter while they fall behind
>
> Our data moat makes us impossible to catch."

**Correct (testing the data advantage curve):**

> **Strategy Presentation:**
>
> "Let's rigorously test our data advantage:
>
> **The claim:** More data = better model = competitive advantage
>
> **Testing the curve:**
> - At 1M training examples: Model accuracy 78%
> - At 10M training examples: Model accuracy 89%
> - At 50M training examples: Model accuracy 91%
> - At 500M training examples: Model accuracy 92%
>
> **Finding:** The curve flattens dramatically. Our 5x data advantage over the nearest competitor translates to ~2% accuracy improvement.
>
> **Is 2% material?**
> - Does it justify higher prices? Unlikely.
> - Does it justify lower costs? Marginally.
> - Can competitors reach 'good enough' with less data? Yes.
>
> **Conclusion:** We have data, but we don't have data-based power. The advantage exists but isn't material enough to sustain differential returns. Our actual power (if any) must come from elsewhere."

**Why curves flatten:**

Most machine learning and statistical models follow diminishing returns curves. The first million data points teach you a lot. The next million teach you less. Eventually, more data barely moves the needle.

```
Performance
    │
    │                    ┌─────────────────────
    │               ┌────┘
    │          ┌────┘
    │     ┌────┘
    │ ┌───┘
    └─┴───────────────────────────────────────► Data Volume
       Small competitor   You
       (good enough)      (marginal improvement)
```

**When data DOES create power:**

- Network effects from data (my data improves YOUR experience) — rare
- Unique data that can't be replicated (proprietary, exclusive access)
- Data creates switching costs (customer's data is locked in)

**Why it matters:**

Hamilton Helmer specifically warns about this: "People often think that they get scale economies through data. And I'd say that that's possible, but it's rare... the range of scale that existing competitors have are often large enough to put them in shouting distance of each other."

Don't confuse having more data with having power. Test the curve.
