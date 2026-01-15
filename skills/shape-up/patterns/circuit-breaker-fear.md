---
title: Stop Building and Return to Shaping
impact: MEDIUM
tags: circuit-breaker, failure, reshaping, courage
---

## Stop Building and Return to Shaping

When a project is off the rails, the answer isn't "throw more time at it." The answer is to stop building and return to shaping.

**Incorrect (sunk cost escalation):**

> *Week 4 of a 6-week project...*
>
> **PM:** "How's the project going?"
>
> **Engineer:** "It's... complicated. We keep finding new problems. The whole approach might be wrong."
>
> **PM:** "But we've invested 4 weeks already! Let's push through."
>
> **Engineer:** "I don't think we can finish in 2 weeks."
>
> **PM:** "Okay, let's extend it. 2 more weeks."
>
> *2 weeks later...*
>
> **PM:** "Still not done?"
>
> **Engineer:** "The approach is fundamentally broken. We should have stopped earlier."
>
> **PM:** "But now we've spent 8 weeks..."

The sunk cost fallacy kept them throwing time at something that wasn't working. They never stopped to ask "is this shaped well?"

**Correct (circuit breaker):**

> *Week 4 of a 6-week project...*
>
> **PM:** "How's the project going?"
>
> **Engineer:** "We're stuck. The approach we shaped isn't working. The data model can't support what we need."
>
> **PM:** "Show me. Where's the scope on the hill chart?"
>
> **Engineer:** "It's been stuck on the left side — in 'figuring it out' — for 2 weeks."
>
> **PM:** "That's a shaping failure. Let's stop building and bring this back to shaping."
>
> *Back in shaping session...*
>
> **Senior Engineer (different person):** "Oh, I see the problem. You needed to use the events table, not the tasks table. That changes everything."
>
> **PM:** "Okay. We reshape around the events table. This is actually simpler. 3-week scope now."

The circuit breaker saved time by stopping the bleeding. The project was reshaped and shipped in the next cycle.

**Why it matters:**

A circuit breaker isn't about canceling projects — it's about admitting when the shaping was wrong. Keeping a poorly-shaped project in build mode just burns time. Pull it back to shaping, figure out what was missed, and try again with clarity.
