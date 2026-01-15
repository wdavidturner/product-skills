---
title: Flat Results Mean Don't Ship
impact: HIGH
tags: ship-decision, flat-results, sunk-cost, complexity
---

## Flat Results Mean Don't Ship

"No significant difference" doesn't mean "good enough to ship." It means the change added no value. Shipping it adds code complexity and maintenance cost for zero benefit.

**Incorrect (shipping flat results):**

> **Experiment Results:**
> - Conversion: +0.3% (P = 0.42, not significant)
>
> PM: "Well, it's not hurting anything. The team worked hard on it. Let's ship."
>
> **Arguments used:**
> - "We already built it"
> - "The team will be demotivated if we don't ship"
> - "It's slightly positive, maybe it's real"
> - "Users in interviews liked it"
>
> **Reality:**
> - Code complexity increased
> - Maintenance burden increased
> - Future changes are harder
> - Zero user value delivered

The team shipped complexity without benefit, making everything else harder.

**Correct (not shipping flat):**

> **Experiment Results:**
> - Conversion: +0.3% (P = 0.42, not significant)
>
> PM: "Not significant. We don't ship."
>
> Engineer: "But we spent two months on this!"
>
> PM: "I know. That's a sunk cost. Shipping something that adds no value means:
> - More code to maintain
> - Harder to make future changes
> - Same user experience, more complexity
>
> We learned something: this approach doesn't work. Let's document why and try a different angle."
>
> **Exception:** Legal or compliance requirements. If legal says "you must do X," you ship even if flat or negative. But you still experiment to find the least harmful implementation.

**Why it matters:**

Every feature shipped has ongoing costs: bugs to fix, edge cases to handle, code that makes other changes harder. A flat result is the experiment telling you this feature doesn't earn its maintenance burden. Listen to the data, not the sunk cost fallacy.
