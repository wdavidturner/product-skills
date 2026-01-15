---
title: First Opinions Contaminate Everyone Else
impact: HIGH
tags: anchoring, groups, meetings, independence
---

## First Opinions Contaminate Everyone Else

When opinions are shared in a group, the first one spoken anchors everyone else. Subsequent opinions shift toward the anchor—especially if the first speaker is senior, confident, or respected.

**Incorrect (anchoring in action):**

> **Estimation meeting:**
>
> CTO (speaks first): "I think this integration will take about 3 weeks."
>
> Senior Engineer: "Yeah, sounds about right. Maybe 3-4."
>
> Junior Engineer: "I was thinking... yeah, 3 weeks seems reasonable."
>
> PM: "Great, I'll put down 3 weeks."

The junior engineer was actually thinking 6 weeks but didn't want to contradict the CTO. The senior engineer was thinking 5 weeks but anchored down. Nobody knows the true spread of estimates.

**Correct (collecting opinions independently before discussion):**

> **Before the meeting:**
>
> PM emails: "How long do you think this integration will take? Reply to me only with your estimate and reasoning. Don't discuss with others."
>
> **Responses:**
> - CTO: 3 weeks (assuming no API issues)
> - Senior Engineer: 5 weeks (we always underestimate auth complexity)
> - Junior Engineer: 6 weeks (similar project took this long last year)
>
> **In the meeting:**
>
> PM: "Here's the spread: 3, 5, and 6 weeks. Let's discuss. Sarah, you said 6 weeks—tell us more about the project comparison."
>
> [Discussion reveals the junior engineer has relevant experience the CTO didn't know about. Final estimate: 5 weeks with 6-week contingency.]

The true spread was 3 to 6 weeks. Without independent collection, it would have looked like "everyone agreed on 3."

**How to prevent anchoring:**

1. **Collect opinions in writing before meetings** (email, form, Slack DM to facilitator)
2. **If opinions must be shared live**, have people write their answer on paper first, then reveal simultaneously
3. **Call on junior people first** if you must go around the room
4. **Share ranges, not point estimates** ("I'm thinking 2-4 weeks" is less anchoring than "2 weeks")

**Why it matters:**

Anchoring is one of the most robust cognitive biases—it affects everyone, even experts who know about it. The only reliable defense is process: collect opinions before they can contaminate each other. You're not smarter than the bias; you need structural protection.
