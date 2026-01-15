---
title: Shaping Requires Engineering
impact: CRITICAL
tags: shaping, engineering, collaboration, rabbit-holes
---

## Shaping Requires Engineering

Shaping without a senior engineer is like designing a kitchen remodel without checking if there's electricity in the walls. You'll discover the real costs in week 4, not before you commit.

**Incorrect (product and design shape alone):**

> **PM:** "Design and I shaped the new checkout flow. We've got wireframes and user stories. Let's kick off the build."
>
> **Engineer (in week 2):** "Uh, this payment provider integration you've designed? We don't support that. It's a 4-week project just to add it."
>
> **PM:** "But it's core to the feature! Can we find a workaround?"
>
> **Engineer:** "We can use the old provider, but then half these screens don't make sense."
>
> **PM:** "We're 2 weeks into a 4-week project and we're basically starting over."

The shaping happened in a vacuum. Technical rabbit holes weren't discovered until the build.

**Correct (engineer in the shaping room):**

> **PM:** "Let's shape the new checkout flow. Marcus, can you join? You know our payment systems best."
>
> *In the session...*
>
> **Designer:** "What if we let users save multiple payment methods?"
>
> **Engineer:** "Our current provider has a vault feature, but it's a compliance nightmare. We'd need a security review."
>
> **PM:** "Is there a simpler version?"
>
> **Engineer:** "We could just let them toggle 'remember this card' for their default method. That's basically free — we already store tokens."
>
> **Designer:** "That covers 80% of the use case. Let's do that."
>
> **Engineer (opening code):** "Let me check one thing... Yeah, this integration point exists. We're good."

The engineer caught the rabbit hole before commitment. The team found a simpler version that actually ships.

**Why it matters:**

Ryan Singer calls it the "grumpy old plumber" test — you need someone who insists on opening up the walls before giving a quote. That senior engineer knows where the bodies are buried. Without them, you're shaping a fantasy.
