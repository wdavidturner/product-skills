# Trustworthy Experiments Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Humbling Reality: Most Ideas Fail

Before designing your experiment, internalize this truth:

| Organization | Failure Rate |
|--------------|--------------|
| Microsoft (overall) | ~66% |
| Bing (mature product) | ~85% |
| Airbnb Search | ~92% |
| Google Ads, Booking | 80-90% |

**Only 8-34% of ideas actually improve the metrics you're trying to move.**

This isn't because teams are bad — it's because predicting user behavior is genuinely hard. The value of experimentation isn't proving you're right; it's preventing you from shipping things that hurt your product.

## The Overall Evaluation Criterion (OEC)

The most important decision in experimentation: **What are you optimizing for?**

### The Wrong Way

> "We're optimizing for revenue."

This leads to bad outcomes. You can always increase short-term revenue by:
- Showing more ads (hurts user experience)
- Adding dark patterns (destroys trust)
- Reducing quality to cut costs (increases churn)

### The Right Way: Lifetime Value

Your OEC should be **causally predictive of customer lifetime value**. This means balancing:

1. **Success metrics** — What you want to improve (revenue, conversion, engagement)
2. **Guardrail metrics** — What you can't afford to hurt (user experience, retention, page speed)

```
                     ┌──────────────────────────┐
                     │                          │
  SUCCESS METRICS    │   SHIP DECISION          │   GUARDRAIL METRICS
  (what we want)     │                          │   (what we protect)
                     │                          │
       ▲             └──────────────────────────┘             ▲
       │                                                      │
  ┌────┴────┐                                           ┌─────┴────┐
  │ Revenue │                                           │ Churn    │
  │ Conv.   │                                           │ Load     │
  │ Engage  │                                           │ NPS      │
  └─────────┘                                           └──────────┘
```

### Constraint Optimization Approach

One powerful framing: **Maximize success metric within a fixed budget of user experience impact.**

Example from Bing Ads:
> "You can show as many ads as you want, but the total vertical pixels of ad real estate is capped. If you can make more money within the same footprint, ship it."

This forces the team to find genuinely better solutions, not just more aggressive monetization.

## Sample Size and Runtime

### The Math You Need

Two critical numbers:

1. **Statistical Power (1 - Beta)** — Probability of detecting a real effect. Aim for 80%.
2. **Significance Level (Alpha)** — False positive rate. Standard is 0.05 (5%).

### Practical Defaults

| Users Available | What You Can Detect | Recommendation |
|----------------|---------------------|----------------|
| < 10,000 | Only massive effects (>20%) | Focus on qualitative research |
| 10,000 - 50,000 | Large effects (10-20%) | Test big bets only |
| 50,000 - 200,000 | Medium effects (5-10%) | Starting to work |
| 200,000+ | Small effects (<5%) | Full experimentation capability |

**Kohavi's rule of thumb:** You need ~200,000 users before experimentation really works.

### Runtime Guidelines

| Factor | Minimum Runtime |
|--------|-----------------|
| Weekly cycles | At least 1 full week (capture weekend behavior) |
| Novelty effects | 2-4 weeks to let effects stabilize |
| Low-traffic features | Until you reach required sample size |
| Business cycles | Cover any relevant seasonality |

**Never stop an experiment early because the P-value looks good.** This inflates your false positive rate from 5% to potentially 30%+.

## P-Values: What They Actually Mean

### The Common Misconception

Most people think: "P-value of 0.02 means 98% probability treatment is better."

**This is wrong.**

### What P-Value Actually Means

P-value is the probability of seeing this data **assuming there's no real effect**. It's NOT the probability that your treatment works.

To get the probability you actually want (is treatment better than control?), you need:
1. The P-value
2. The **prior probability** that your idea would succeed

### The False Positive Risk

Given typical base rates:

| Base Success Rate | P-value < 0.05 | Actual False Positive Risk |
|-------------------|----------------|---------------------------|
| 33% (Microsoft) | Significant! | ~15% |
| 15% (Bing) | Significant! | ~20% |
| 8% (Airbnb Search) | Significant! | ~26% |

**When 92% of ideas fail, a "significant" P-value of 0.05 still means 1-in-4 chance you're wrong.**

### What To Do About It

1. **Use lower P-value thresholds** — Consider 0.01 instead of 0.05
2. **Replicate surprising results** — Run the experiment again
3. **Combine experiments** — Use Fisher's or Stouffer's method for joint P-values
4. **Be especially skeptical of surprising wins** — Twyman's Law applies

## Validity Threats

### Sample Ratio Mismatch (SRM)

The single most important validity check.

**What it is:** Your 50/50 split isn't actually 50/50.

**Why it matters:** Any deviation larger than expected by chance indicates a bug in your experiment. The results cannot be trusted.

**How to detect:** Statistical test on observed vs. expected split.

| Expected | Observed | Users | Probability by Chance |
|----------|----------|-------|----------------------|
| 50% | 50.2% | 1,000,000 | 1 in 500,000 |

**If the probability is tiny, something is wrong.**

Common causes of SRM:
- Bots hitting control/treatment differently
- Data pipeline issues
- Starting experiment mid-session
- Redirect failures
- Performance differences causing user drop-off

**At Microsoft, 8% of experiments had SRM.** Always check.

### Other Validity Threats

| Threat | What Goes Wrong | How to Detect |
|--------|-----------------|---------------|
| **Novelty Effect** | Users react to "new," not "better" | Run longer, compare early vs. late |
| **Primacy Effect** | Users prefer familiar (opposite of novelty) | Run longer, segment by prior exposure |
| **Survivorship Bias** | Only analyzing users who stayed | Check for differential attrition |
| **Instrumentation** | Logging differs between variants | Validate logging parity |
| **Network Effects** | Treatment affects control users | Use proper isolation |

## Twyman's Law

> "Any figure that looks interesting or different is usually wrong."

**If results look too good to be true, investigate before celebrating.**

### The Process

1. Normal experiment improvement: < 1%
2. You see: 10% improvement
3. **First reaction:** Hold the celebratory dinner
4. **Check for:**
   - Sample ratio mismatch
   - Logging bugs
   - Data pipeline issues
   - Bot contamination
   - Segmentation errors

**Nine times out of ten**, surprisingly good results have a bug.

The tenth time? You have a genuine breakthrough. But verify first.

### Real Example: The $100M Bug

At Bing, a simple change (moving ad title text to be larger) showed +12% revenue. The alarm system fired.

Everyone assumed bug. They checked:
- Logging: correct
- Pipeline: correct
- Sample ratio: correct
- Replicated multiple times

**It was real.** The biggest revenue improvement in Bing's history from a change that languished in the backlog as "meh."

The lesson: Twyman's Law tells you to investigate, not to dismiss.

## Building Experimentation Culture

### Start Small

1. Find a team that ships frequently (weekly, not quarterly)
2. Build/buy basic infrastructure
3. Run experiments, share surprising results
4. Let success spread organically

### The Flywheel

```
Run experiments → Share surprising results → Build trust → More experiments
       ↑                                                          │
       └──────────────────────────────────────────────────────────┘
```

### Quarterly Learnings

Host quarterly meetings focused on **most surprising experiments**:

- Expected positive, was flat → Learning
- Expected small, was huge → Learning
- Expected small, was very negative → Learning

**Surprising = |Expected - Actual| is large.** Share these, not just wins.

### Institutional Memory

Without documentation, you'll repeat the same mistakes.

- Searchable database of all experiments
- Tagged by keywords, features, metrics
- Include what you learned, not just what happened
- New team members can search: "Has anyone tested X?"

**At Microsoft in 2019:** 20,000-25,000 experiments per year. ~100 new treatments every working day.

## Application Checklists

### Before You Start

- [ ] Do we have enough users? (tens of thousands minimum, 200k ideal)
- [ ] Is the metric clearly defined and measurable?
- [ ] Do we have guardrail metrics to protect?
- [ ] Is the experiment duration long enough (1-2 weeks minimum)?
- [ ] Is the expected effect size realistic?

### Experiment Design

- [ ] What is the hypothesis?
- [ ] What is the primary success metric (OEC)?
- [ ] What are the guardrail metrics?
- [ ] What sample size do we need for 80% power?
- [ ] How long must we run to reach that sample size?
- [ ] How are users randomized? (ensure proper isolation)

### During the Experiment

- [ ] Check sample ratio daily — abort if SRM detected
- [ ] Monitor guardrails for egregious violations
- [ ] Do NOT peek at primary metrics daily
- [ ] Do NOT stop early because P-value looks good

### Analyzing Results

- [ ] Check sample ratio mismatch first
- [ ] Was required sample size reached?
- [ ] Did experiment run full planned duration?
- [ ] If "significant," is the effect size meaningful?
- [ ] Are guardrail metrics acceptable?
- [ ] Does Twyman's Law apply? (results surprisingly good)

### Ship Decision

- [ ] Primary metric improved with P < threshold?
- [ ] No guardrail metric violations?
- [ ] Effect replicated (if surprising)?
- [ ] Document what we learned
- [ ] If flat: do NOT ship (adds maintenance cost with no value)

### After Shipping

- [ ] Monitor metrics post-launch
- [ ] Update institutional memory
- [ ] If it was a big win/loss, share learnings
- [ ] Consider follow-on experiments

## Variance Reduction Techniques

Want results faster without losing validity? These techniques reduce the variance of your metrics:

### 1. Metric Capping

If revenue is highly skewed (few users spend a lot), cap the metric.

> "If someone books more than 30 nights, count it as 30."

This reduces variance from outliers while keeping the signal.

### 2. Pre-Experiment Adjustment (CUPED)

Use pre-experiment data to adjust results. If users who spent a lot before the experiment also spend a lot during, you can factor this out.

**Result:** Same unbiased estimate, lower variance, faster results.

### 3. Stratified Sampling

If you know certain user segments have different behavior, stratify your randomization to ensure balance.

## Common Mistakes Summary

| Mistake | Why It Happens | Consequence |
|---------|----------------|-------------|
| Peeking at P-values | Impatience | 5% error becomes 30%+ |
| Ignoring SRM | Don't know to check | Invalid results |
| Underpowered tests | Want fast results | Meaningless conclusions |
| Wrong OEC | Short-term thinking | Harm long-term value |
| Shipping flat results | Sunk cost fallacy | Complexity with no value |
| Big redesigns without testing | Hubris | 80% chance of failure |
| No guardrails | Focus on success only | Win metric, hurt business |

## Quick Reference

**The core idea:** Most experiments fail. The value is avoiding bad ships, not proving wins.

**Sample size:** Need 200,000+ users for mature experimentation. Tens of thousands to start.

**Runtime:** Minimum 1 week. 2-4 weeks if novelty effects possible. Never stop early.

**P-values:** 0.05 is NOT 95% confidence. With high failure rates, false positive risk is 15-26%.

**SRM:** If your 50/50 split is off, stop. Find the bug. Results are invalid.

**Twyman's Law:** Surprisingly good = probably wrong. Investigate first, celebrate second.

**Ship decision:** Positive effect + no guardrail violations + replicated if surprising.

---

