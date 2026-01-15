---
title: Hill Charts Show Real Progress
impact: HIGH
tags: hill-charts, progress, tracking, honesty
---

## Hill Charts Show Real Progress

Hill charts force honesty about where work actually stands. They're not for status theater — they're for revealing problems early.

**Incorrect (status theater):**

> **PM:** "Let's update the hill chart for standup."
>
> **Engineer (moving dots):** "I'll put the API scope at 60% up the hill."
>
> **PM:** "What does that mean?"
>
> **Engineer:** "I've written some code. It's kind of working."
>
> **PM:** "Great, progress!"
>
> *Week 3...*
>
> **Engineer:** "Actually, the API scope has a fundamental problem. I need to rewrite it."
>
> **PM:** "But you said it was 60% done!"
>
> **Engineer:** "I meant 60% of the code was written. I didn't mean it was going to work."

The hill chart became a meaningless number, just like a percentage in a status report.

**Correct (honest progress on unknowns):**

> **PM:** "Where's the API scope on the hill?"
>
> **Engineer:** "Still on the left side, pretty low. I've written code, but I'm stuck. The approach might not work."
>
> **PM:** "That's the uphill part — figuring it out. What's blocking you?"
>
> **Engineer:** "I don't know if our database can handle the query pattern this requires."
>
> **PM:** "Can you test that today? If it doesn't work, we need to know now — we might need to reshape that scope."
>
> *Next day...*
>
> **Engineer:** "Good news. Did a spike. The query works. Moving the dot over the hill — now it's just execution."

The hill chart revealed a problem in week 1, not week 3. The team could have reshaped if needed.

**Why it matters:**

The hill isn't about percentage complete. The left side (uphill) means "I'm figuring it out — there are unknowns." The right side (downhill) means "I know what to do — just making it happen." A scope that won't climb the hill is a red flag that shaping missed something.
