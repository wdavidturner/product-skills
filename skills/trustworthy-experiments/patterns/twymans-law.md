---
title: If Results Look Amazing, Investigate First
impact: CRITICAL
tags: twymans-law, debugging, validation, false-positives
---

## If Results Look Amazing, Investigate First

Twyman's Law: "Any figure that looks interesting or different is usually wrong." When experiment results seem too good to be true, they usually are.

**Incorrect (celebrating immediately):**

> **Normal experiment impact:** 0.1% to 0.5%
>
> **This experiment:** +12% revenue
>
> PM: "Holy shit! This is the biggest win in company history! Let's ship immediately and tell the CEO!"
>
> **Three weeks after launch:**
>
> Finance: "Why hasn't our revenue increased? The experiment said +12%."
>
> **Investigation finally happens:**
>
> A logging bug was double-counting treatment revenue.

The team celebrated, shipped, and embarrassed themselves because they didn't question an implausible result.

**Correct (investigating first):**

> **Normal experiment impact:** 0.1% to 0.5%
>
> **This experiment:** +12% revenue
>
> PM: "Wow, that's way outside our normal range. Twyman's Law. Let's investigate before we celebrate."
>
> **Investigation checklist:**
> - [ ] Sample ratio mismatch? → Clean
> - [ ] Logging parity between variants? → Clean
> - [ ] Data pipeline issues? → Clean
> - [ ] Bot contamination? → Clean
> - [ ] Replicate the result? → Replicated
>
> Data Scientist: "I've checked everything. The result is real."
>
> PM: "Let's replicate one more time with fresh users."
>
> **Second replication:** +11.5% revenue
>
> PM: "Okay, NOW we can celebrate. And we should understand WHY this worked so we can find more ideas like it."

**Why it matters:**

At Bing, about 9 out of 10 "too good to be true" results had bugs. The tenth was a genuine breakthrough — like the ad title change that added $100M in annual revenue. Twyman's Law doesn't mean dismiss surprising results; it means verify them before acting. The celebration can wait a few days.
