---
title: Document Learnings or Repeat Mistakes
impact: MEDIUM
tags: documentation, learning, institutional-memory, process
---

## Document Learnings or Repeat Mistakes

Organizations forget. Without systematic documentation, teams repeat the same failed experiments and miss opportunities to build on past wins.

**Incorrect (no documentation):**

> **Year 1:** Team tests "open link in new tab" — big win, ships.
>
> **Year 2:** Original team members leave.
>
> **Year 3:** New PM: "What if we opened search results in a new tab?"
>
> Senior Engineer: "Hmm, I feel like we tried that? But I can't find anything about it."
>
> **Outcome:** Team either:
> - Wastes time re-running the same experiment
> - Misses applying the pattern to new features
> - Argues about whether it was tested without data

At Airbnb, the "open in new tab" pattern was implemented once, forgotten, and had to be rediscovered years later when Kohavi joined and asked about it.

**Correct (systematic documentation):**

> **After every experiment:**
>
> 1. Results logged in searchable database
> 2. Tagged with keywords: "new tab," "search results," "navigation"
> 3. Key learnings summarized: "Opening listings in new tab increased engagement because users could compare multiple options without losing their place"
>
> **Quarterly meeting:** Review most surprising experiments
> - Expected positive, was flat → What did we learn?
> - Expected small, was huge → Why? What can we apply elsewhere?
> - Expected small, was very negative → What went wrong?
>
> **Year 3:** New PM searches "new tab" → Finds past experiment, understands why it worked, applies pattern to new feature.

**Why it matters:**

Microsoft ran 20,000+ experiments per year. Without searchable documentation, that knowledge is lost. Searchable experiment history lets new team members learn from thousands of past tests. The quarterly "surprising experiments" meeting builds shared understanding and prevents repeated mistakes.
