---
title: Builders Must Map Implementation Scopes
impact: HIGH
tags: kickoff, scopes, implementation, planning
---

## Builders Must Map Implementation Scopes

At kickoff, the build team translates shaped work into implementation scopes. If they can't fit it into 9 or fewer boxes, there's too much scope.

**Incorrect (skipping the translation):**

> **PM:** "Here's the shaped pitch. You have 6 weeks. Go build!"
>
> **Engineer:** "Okay... I'll just start with the first thing that seems important."
>
> *Week 4...*
>
> **Engineer:** "I've been working on the API layer for 3 weeks. It's bigger than I thought."
>
> **PM:** "What about the UI? What about the other features in the pitch?"
>
> **Engineer:** "I haven't gotten to those. I'm still in the API."
>
> **PM:** "But we only have 2 weeks left!"

Without mapping implementation scopes, the team lost track of the whole. They went deep on one part without seeing how it fit.

**Correct (9-box kickoff exercise):**

> **PM:** "Before we start building, let's do the 9-box exercise. Can you map the shaped work into 9 or fewer implementation scopes?"
>
> **Team (drawing a 3x3 grid):**
> 1. Data model + migrations
> 2. List view component
> 3. Detail view component
> 4. Create flow
> 5. Edit flow
> 6. Search + filtering
> 7. Permissions layer
> 8. Mobile layout
> 9. Loading states + error handling
>
> **PM:** "That's 9. With 30 business days, that's about 4 days per scope. Does that feel right?"
>
> **Engineer:** "Permissions might be bigger. Can we simplify? What if only admins can edit for now?"
>
> **PM:** "That works. Simpler permissions. Now it fits."

The team discovered a scope problem at kickoff, not in week 4. They made a trade-off before starting.

**Why it matters:**

The 9-box rule (based on the 7+/-2 cognitive limit) forces the team to see the whole project. If they can't fit it in 9 boxes, the shaping wasn't tight enough. If a single box seems huge, that's a flag to simplify or re-shape.
