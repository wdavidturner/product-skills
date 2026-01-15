---
title: Always Monitor What You Might Be Hurting
impact: HIGH
tags: guardrails, tradeoffs, metrics, user-experience
---

## Always Monitor What You Might Be Hurting

It's easy to improve one metric by hurting another. Without guardrail metrics, you'll optimize yourself into a corner.

**Incorrect (only watching the success metric):**

> **Experiment:** Add interstitial ad after search
>
> **Primary metric:** Ad revenue
>
> **Results:** +8% ad revenue, P < 0.01
>
> PM: "Ship it!"
>
> **Three months later:**
>
> - Search usage down 15%
> - User complaints up
> - Competitors gaining share
>
> PM: "But we ran an experiment!"

They did run an experiment. They just didn't measure what they were trading away.

**Correct (watching what you might hurt):**

> **Experiment:** Add interstitial ad after search
>
> **Primary metric:** Ad revenue
>
> **Guardrail metrics:**
> - Time to first successful click (user experience)
> - Session success rate (task completion)
> - 7-day return rate (retention)
> - Page load time (performance)
>
> **Results:**
> - Ad revenue: +8% (P < 0.01)
> - Time to first click: +1.2 seconds (P < 0.01)
> - Session success: -4% (P < 0.05)
> - Return rate: -2% (P = 0.08)
>
> PM: "The guardrails are failing. We're making money by hurting users."
>
> Data Scientist: "That -2% return rate would compound. In a year, we'd have significantly fewer users. Let's find a way to monetize without degrading experience."

**Why it matters:**

Any metric can be gamed. Guardrails protect what matters long-term. Common guardrails: page load time, error rates, user success metrics, retention, customer satisfaction proxies. Set acceptable thresholds before the experiment. "We'll ship if primary metric improves AND guardrails stay within bounds."
