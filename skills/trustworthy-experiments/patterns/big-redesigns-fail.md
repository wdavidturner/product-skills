---
title: Big Redesigns Usually Fail — Ship Incrementally
impact: HIGH
tags: redesign, incremental, risk, portfolio
---

## Big Redesigns Usually Fail — Ship Incrementally

When you bundle 17 changes into one big redesign, you're betting they all work together. History says you'll lose that bet 80% of the time.

**Incorrect (big bang redesign):**

> **Project:** Complete checkout redesign
> - New visual design
> - Reordered steps
> - New payment flow
> - Added upsells
> - Changed copy
> - New animations
> - Mobile-first layout
>
> **Timeline:** 6 months of work
>
> **Experiment Results:** -12% conversion, P < 0.01
>
> PM: "But we did extensive user research! Everyone loved the mocks!"
>
> **Outcome:** Team spends 3 more months trying to "fix" it, eventually abandons most changes.

Six months of work, negative result. Some individual changes were probably good, but they can't tell which ones.

**Correct (incremental testing):**

> **Approach:** Same goal, incremental execution
>
> **Month 1:** Test new visual design (existing flow)
> - Result: +2% conversion → Ship
>
> **Month 2:** Test reordered steps
> - Result: -3% conversion → Don't ship, investigate why
>
> **Month 3:** Test new payment flow
> - Result: +1.5% conversion → Ship
>
> **Month 4:** Test upsells
> - Result: +0.5% conversion → Ship
>
> **Month 5:** Test new copy
> - Result: Flat → Don't ship (adds complexity with no value)
>
> **Month 6:** Test mobile-first layout
> - Result: +3% on mobile, flat on desktop → Ship for mobile
>
> **Net result:** +5% conversion from the changes that worked. Didn't waste effort on the ones that failed.

**Why it matters:**

Kohavi's data: 66-92% of ideas fail. Bundling them makes debugging impossible. One Factor at a Time (OFAT) lets you learn what works, abandon what doesn't, and compound wins. The incremental approach often delivers more improvement than the "big bet" because you course-correct along the way.
