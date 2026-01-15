---
title: Adjust Detail Based on Who's Building
impact: MEDIUM
tags: shaping, junior, senior, detail, coaching
---

## Adjust Detail Based on Who's Building

The amount of detail in shaping should match who's on the build team. Senior engineers need less; junior engineers need more.

**Incorrect (one-size-fits-all shaping):**

> **PM (to junior engineer):** "Here's the shaped project. It's a dot grid calendar with agenda view. Go build it."
>
> **Junior Engineer:** "Okay... where do I start?"
>
> **PM:** "That's your job to figure out. We shaped at the right level of abstraction."
>
> *Week 2...*
>
> **Junior Engineer (internally):** "I don't want to look stupid by asking questions. I'll just try something."
>
> *Week 4...*
>
> **PM:** "How's it going?"
>
> **Junior Engineer:** "I built the grid but... it's not connected to anything. I'm not sure how the data model should work."

The shaping was appropriate for a senior engineer who would know how to approach it. The junior engineer needed more guidance.

**Correct (detail dial adjusted):**

> **Senior Engineer (in shaping):** "Who's building this?"
>
> **PM:** "Marcus — he joined 6 months ago. First time leading a feature."
>
> **Senior Engineer:** "Okay, let's add more detail. Marcus, for the data model, I'd suggest using our existing Event schema but adding a recurrence_rule field. Here's how we've done similar things..."
>
> *In the pitch document:*
> - Data model: "Use Event schema, add recurrence_rule (nullable), see /models/event.rb for pattern"
> - Rendering approach: "Use our grid component from /components/grid — it handles the month layout"
> - Suggested order: "Start with static grid, then wire up data, then add interactions"
>
> **Marcus (at kickoff):** "This is clear. I know where to start and I can see how it connects."

The shaping was dialed up for a junior builder. He learns from the embedded guidance and succeeds.

**Why it matters:**

Shaping isn't about finding the "right" level of abstraction universally. It's about giving teams what they need to succeed. A senior engineer might be insulted by too much detail. A junior engineer might drown without it. Dial accordingly.
