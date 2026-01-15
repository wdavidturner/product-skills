# PMF Survey (Product-Market Fit Survey) Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Core Framework

### The Magic Question

The survey asks one core question:

> "How would you feel if you could no longer use [product]?"
> - Very disappointed
> - Somewhat disappointed
> - Not disappointed

This question works because it measures **dependence**, not satisfaction. Users can be satisfied but not dependent. Dependence predicts retention and word-of-mouth.

### The 40% Benchmark

Sean Ellis benchmarked this question across hundreds of companies:

| PMF Score | What It Means |
|-----------|---------------|
| **40%+** very disappointed | Strong PMF - focus on growth |
| **25-40%** very disappointed | Promising - focus on increasing PMF before scaling |
| **<25%** very disappointed | Weak PMF - consider pivoting or major changes |

**Important:** 40% is a threshold, not a target. Getting to 39.9% doesn't mean you failed. Getting to 41% doesn't mean you're done. The number tells you where you are in the journey.

### Why This Question Works

Traditional satisfaction metrics fail because:

- **NPS** measures recommendation intent, not actual behavior
- **CSAT** measures satisfaction with individual interactions, not the product
- **Usage metrics** measure habit, not value

The disappointment question cuts through this. If users would be "very disappointed" without you, they're getting real value that they can't easily replace. That's product-market fit.

## The Superhuman PMF Engine

Rahul Vohra expanded Sean Ellis's framework into an algorithm that writes your roadmap. Here's how it works:

### Step 1: Run the Survey

Ask these four questions:

1. **How would you feel if you could no longer use [product]?**
   - Very disappointed / Somewhat disappointed / Not disappointed

2. **What type of people do you think would most benefit from [product]?**
   - Free text response

3. **What is the main benefit you receive from [product]?**
   - Free text response

4. **How can we improve [product] for you?**
   - Free text response

### Step 2: Segment Your Responses

Divide respondents into three groups:

```
┌─────────────────────────────────────────────────────────┐
│                    ALL RESPONSES                        │
├─────────────────┬─────────────────┬─────────────────────┤
│ Very            │ Somewhat        │ Not                 │
│ Disappointed    │ Disappointed    │ Disappointed        │
│                 │                 │                     │
│ LOVERS          │ FENCE-SITTERS   │ NOT YOUR USERS      │
│ Learn from them │ Convert them    │ Politely ignore     │
└─────────────────┴─────────────────┴─────────────────────┘
```

### Step 3: Identify Your High-Expectation Customers (HXC)

From the "Very Disappointed" group, analyze Question 2 (who benefits most). These descriptions reveal your ideal customer profile.

Look for patterns:
- Job titles / roles
- Use cases
- Contexts
- Pain points they mention

**Your HXC** is the intersection of:
- Who loves you (very disappointed)
- Who they say would benefit

### Step 4: Understand What They Love

From the "Very Disappointed" group, analyze Question 3 (main benefit). Code responses into themes.

This is your **core value proposition** - what you must never break.

### Step 5: Segment the "Somewhat Disappointed" Users

This is the key insight. Split "Somewhat Disappointed" into two groups:

**Group A: Main benefit resonates**
- They mention the same core benefit as the "Very Disappointed" users
- Something small is holding them back
- These users can be converted

**Group B: Main benefit doesn't resonate**
- They like your product for different reasons
- Converting them would pull you away from your core
- Politely ignore their feedback

### Step 6: Build the Roadmap

From Group A (somewhat disappointed, main benefit resonates), analyze Question 4 (how to improve).

These are your roadmap items - the things that will convert fence-sitters into lovers.

**The Algorithm:**

```
FOR EACH sprint/quarter:
  - 50% of effort: Double down on what "Very Disappointed" users love
  - 50% of effort: Fix what's holding back Group A "Somewhat Disappointed" users

IGNORE:
  - Feedback from "Not Disappointed" users
  - Feedback from "Somewhat Disappointed" users where main benefit doesn't resonate
```

### Step 7: Repeat and Track

Run the survey quarterly. Track your PMF score over time.

**If score increases:** Your roadmap is working. Continue.
**If score plateaus:** You may have saturated your current segment. Time to expand.
**If score decreases:** Something broke. Investigate immediately.

## Who to Survey

### Include

- Users who have experienced your core value (not just signed up)
- Users from the past 2-4 weeks (recent enough to remember)
- A representative mix of user types

### Exclude

- Users who signed up but never activated
- Users from 6+ months ago (they've forgotten or context changed)
- Users who were assigned the product (no choice = no signal)
- Trial users who haven't hit the "aha moment"

### Sample Size

| Sample | Reliability |
|--------|-------------|
| 30 responses | Minimum viable - directionally useful |
| 40-50 responses | Good - confident in segment patterns |
| 100+ responses | Great for sub-segment analysis |

**Don't wait for statistical perfection.** You're looking for patterns, not p-values. 40 responses showing 25% very disappointed tells you something important even if the confidence interval is wide.

## Common Mistakes

### 1. Surveying too early
Users need time to experience value. Survey after the "aha moment," not after signup.

### 2. Trying to please everyone
If you build everything the "Not Disappointed" users ask for, you'll dilute what the "Very Disappointed" users love.

### 3. Ignoring the segment filter
Not all "Somewhat Disappointed" users are convertible. Only act on feedback from those whose main benefit matches your core.

### 4. Treating 40% as a finish line
40% means you have permission to grow. It doesn't mean you're done improving.

### 5. Changing the question wording
The benchmark only works with the exact wording. "Would you recommend this product?" is a different question with different benchmarks.

### 6. Running it once
PMF isn't binary. Run the survey quarterly to track progress and catch regressions.

## Applying PMF Survey: Checklists

### Before Running the Survey

- [ ] Do we have enough active users? (minimum 30-40 who've experienced core value)
- [ ] Have users had enough time to experience value?
- [ ] Are we using the exact standard question wording?
- [ ] Do we have follow-up questions to understand why?

### Analyzing Results

- [ ] What's our overall PMF score (% very disappointed)?
- [ ] Who are our "Very Disappointed" users? (demographics, use cases)
- [ ] What main benefit do they cite?
- [ ] Who are the "Somewhat Disappointed" users where main benefit resonates?
- [ ] What's holding Group A back?

### Building the Roadmap

- [ ] Are we allocating ~50% to doubling down on loved features?
- [ ] Are we allocating ~50% to converting fence-sitters?
- [ ] Are we explicitly ignoring feedback from wrong segments?
- [ ] Do we have a plan to re-run the survey and measure impact?

### For Pivot Decisions

- [ ] Is our PMF score below 25%?
- [ ] Have we tried the segment-and-focus approach first?
- [ ] Is there a sub-segment with 40%+ (even if small)?
- [ ] If we pivot, what's our hypothesis for why the new direction will score higher?

## Quick Reference

**The core question:** "How would you feel if you could no longer use this product?"

**The benchmark:** 40%+ "very disappointed" = strong PMF

**Who to survey:** Users who experienced your core value in the past 2-4 weeks

**Sample size:** 40-50 is enough for actionable patterns

**The algorithm:** 50% double down on loved features + 50% fix objections from convertible fence-sitters

**Key insight:** Ignore feedback from users who don't love your core value proposition - they'll pull you in the wrong direction

---

