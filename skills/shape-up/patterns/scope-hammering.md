---
title: Cut Scope Before You Start
impact: HIGH
tags: scope, trade-offs, shaping, constraints
---

## Cut Scope Before You Start

Scope cutting happens in shaping, not during the build. If you're cutting scope in week 5 of a 6-week project, you've already failed.

**Incorrect (scope cutting at the end):**

> *Week 1:* "We're building a full reporting dashboard with 8 charts, filters, and export to CSV."
>
> *Week 3:* "This is taking longer than expected. Let's cut it to 6 charts."
>
> *Week 5:* "We're not going to make it. Let's ship with 3 charts and no filters."
>
> *Week 6:* "We shipped something but... it doesn't really solve the problem anymore. Users still can't get the insights they needed."
>
> **Team:** "That was brutal. We feel like we failed."

Last-minute scope cutting demoralizes the team and often produces something that doesn't actually work.

**Correct (scope negotiation in shaping):**

> *In shaping session...*
>
> **PM:** "Stakeholders want a full reporting dashboard. Our appetite is 6 weeks."
>
> **Engineer:** "8 charts plus filters plus export? That's probably 10 weeks minimum."
>
> **PM:** "What's the core value?"
>
> **Engineer:** "Honestly, if we nail the revenue trend chart with weekly filtering, that answers 80% of their questions."
>
> **PM:** "What about the other charts?"
>
> **Designer:** "We could show 3 key metrics as simple numbers, not full charts. That's fast."
>
> **PM:** "So the shape is: 1 main chart with filters, 3 metric cards. Export comes in a future bet. Everyone aligned?"
>
> **Team (at kickoff):** "This is what we're building. It's tight but doable."

The team knows upfront what they're shipping. No surprises. No last-minute compromises.

**Why it matters:**

Scope cutting during the build means the shaping failed. You didn't find the right version of the project. In Shape Up, the hard trade-offs happen before commitment, when you still have options — not in week 5, when you're just trying to survive.
