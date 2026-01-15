# Hierarchy of Marketplaces Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Core Insight: Happy GMV > Raw GMV

Most marketplace founders obsess over hitting GMV milestones. But not all GMV is created equal.

**The race to $1M GMV creates perverse incentives:**

| GMV-Focused Approach | Happiness-Focused Approach |
|---------------------|---------------------------|
| Spread across cities to capture more volume | Focus on one city until it tips |
| Go after the biggest market for easy wins | Go after the market with least competition |
| Count every transaction | Count retained transactions |
| Optimize for number of sellers | Optimize for seller quality |

**Example: Food Delivery**

Postmates went after big cities (LA, NYC, SF) and multiple categories (restaurants, retail, Apple products). They spread thin.

DoorDash went after suburbs where no one else was competing. They lost money initially but dominated those markets. Their focused approach let them:
- Make customers genuinely happy (no alternatives)
- Make restaurants happy (dedicated attention)
- Build a playbook they could repeat
- Tip each market before expanding

The suburbs seemed like a small opportunity. They became the foundation of a dominant company.

## The Three Levels

### Level 1: Focus (The Thimble)

**Goal:** Achieve minimum viable happiness in a constrained market.

Your market should be so focused that it feels uncomfortably small. Sarah Tavel calls this the "thimble" - a tiny vessel you can actually heat to boiling, versus trying to warm an ocean.

```
CONSTRAINTS TO EMBRACE:

Geography         "Just this city" or "just these suburbs"
                  Not multiple cities at once

Category          "Just restaurants" or "just handmade goods"
                  Not everything that could transact

Customer Type     "Just serious campers" or "just suburban families"
                  Not everyone who might use you
```

**Why focus works:**

1. **Capital is scarce** - You can't raise hundreds of millions at the start
2. **Attention is scarce** - Founders can only execute well on limited fronts
3. **Tipping requires saturation** - You can't tip a market you haven't penetrated

**Signs you've achieved Level 1:**

- Customers text/email you about great experiences
- Both sides retain after their first transaction
- 40%+ would be "very disappointed" if you disappeared (Sean Ellis test)
- You feel pull, not just push

**What "minimum viable happiness" means:**

You're not making everyone happy. You're making a core persona so happy they can't imagine going back. That white-hot center will expand outward.

### Level 2: Tip (Reach Saturation)

**Goal:** Reach a saturation point where the market tips in your favor.

Tipping is the moment when things shift from pushing to pulling. The market starts coming to you. Your cost of acquisition drops. Cohorts improve. Growth becomes organic.

**How tipping happens:**

The REKKI example illustrates this perfectly:

1. **Before tipping:** Sales team knocks on restaurant doors. High cost of sales. Every customer acquired manually.

2. **Tipping moment:** Suppliers receiving orders via REKKI start requesting their other customers join. They hand REKKI lists of restaurants to onboard.

3. **After tipping:** Supply brings demand. Demand brings supply. The flywheel spins on its own.

**Two types of loops to identify and maximize:**

**Growth Loops** - How usage creates more users:
- Buyer invites buyer (camping trip invitations)
- Seller invites seller (driver referral bonuses)
- Seller invites buyer (business cards with marketplace links)
- Buyer invites seller (requesting restaurants join)

**Happiness Loops** - How usage improves quality:
- Search ranking rewards good suppliers
- Reviews surface quality, sink poor performers
- Repeat transactions concentrate on best matches
- Bad suppliers naturally churn

**Conditions required for tipping:**

Not all markets can tip. Check for:

| Condition | Why It Matters |
|-----------|---------------|
| Fragmented supply | Concentrated supply won't compete for your marketplace |
| Heterogeneous supply | Homogeneous supply means no differentiation from more supply |
| Low switching costs | High switching costs mean incumbents are protected |
| No dominant incumbent | Existing dominant player blocks tipping |
| Repeated transactions | One-time purchases don't build relationships |
| Definable market boundary | You need a market you can saturate |

### Level 3: Dominate (Expand from Strength)

**Goal:** Replicate your playbook across adjacent markets to achieve dominant market share.

Only after tipping your initial market should you expand. Now you have:
- A proven playbook
- Contribution profit to reinvest
- Evidence that raises more capital
- Confidence in what makes both sides happy

**Three vectors of growth:**

1. **Deepen existing market**
   - Uber: Black cars → UberX → UberPool
   - More use cases in markets you already dominate

2. **Adjacent geographies**
   - Take your playbook to similar markets
   - Go from strength to strength, not random expansion

3. **Adjacent categories**
   - Expand what you offer in markets you dominate
   - Only after you've earned the right

**The dominance imperative:**

Marketplace economics favor dominant players dramatically:

```
Market Position          Profitability
─────────────────────────────────────
Dominant (#1 by far)     Highly profitable
#1 but barely            Marginally profitable
Middle of pack           Barely surviving
Laggard                  Losing money
```

This is why blitz-scaling makes sense *after* you've proven the model. One focused competitor putting all resources into your market will beat you if you're spread across ten.

## The Whac-A-Mole Problem

From Ramesh Johari's research: Marketplace management is inherently about moving attention and inventory around. Many consequential changes create winners and losers.

**Example:**
- New supply having bad experiences? Route them to experienced buyers.
- Now experienced buyers have worse selection? Route them to better supply.
- Now existing sellers get less attention? The metrics keep moving.

**The key question:** Are the winners you've created more important to your business than the losers?

This is why happiness metrics matter more than volume metrics. You need to measure whether your allocation decisions are net positive for the marketplace, not just whether GMV increased.

## Data Science in Marketplaces

Marketplaces depend on data to reduce friction. The three core problems:

### 1. Finding Matches
How do buyers find potential sellers? How do sellers find buyers?
- Search algorithms
- Recommendation systems
- Notifications and surfacing

### 2. Making Matches
Once found, how do they evaluate and commit?
- Ranking and sorting
- Information display
- Trust signals

### 3. Learning from Matches
What happened? How do we improve?
- Rating systems
- Passive data collection
- Feedback loops

**Critical insight:** Prediction is not decision-making.

Machine learning predicts patterns from past data. But decisions are about causation, not correlation.

| Prediction Question | Decision Question |
|--------------------|-------------------|
| "Who is likely to be hired?" | "Who will be hired *because* we ranked them higher?" |
| "What's their lifetime value?" | "How much *more* will they spend because of this promotion?" |
| "What will they click?" | "What ranking leads to better matches overall?" |

The difference between these questions is the difference between correlation and causation. Data scientists building marketplaces must think causally.

## Rating System Design

Ratings drive happiness loops but have inherent challenges:

### Rating Inflation
Over time, median ratings drift upward. A 4-star rating becomes devastating.

**Causes:**
- Reciprocity ("please rate me well")
- Norming (everyone gives 5 stars so you do too)
- Fear of retaliation

**Solutions:**
- Ask comparative questions ("better or worse than your last experience?")
- Frame as expectations ("did this exceed your expectations?")
- Separate dimensions ("rate speed separately from quality")

### The Averaging Problem
New sellers are devastated by one bad review. Established sellers are immune.

**Solutions:**
- Don't show ratings until minimum threshold
- Use Bayesian priors (assume average until proven otherwise)
- Weight recent ratings more heavily

### Sound of Silence
The ratings NOT left contain signal. People who had bad experiences often just leave.

**Solution:** Track "effective percent positive" including non-respondents.

## Applying the Hierarchy: Checklists

### For Launching a Marketplace

**Level 1 Readiness:**
- [ ] Have you defined your thimble? (geography + category + customer type)
- [ ] Is it uncomfortably small? (it should feel constraining)
- [ ] Can you measure happiness, not just transactions?
- [ ] Do you have a hypothesis for what makes both sides happy?
- [ ] Are you prepared to do things that don't scale?

### For Diagnosing Stalled Growth

**Check against the hierarchy:**
- [ ] Are you measuring GMV or Happy GMV?
- [ ] What's the retention rate for both sides?
- [ ] Have you reached saturation in any market?
- [ ] Are you spread too thin across markets?
- [ ] Do you have any markets showing signs of tipping?

### For Deciding When to Expand

**Level 2 → Level 3 checklist:**
- [ ] Is your core market tipping? (organic growth, improving cohorts)
- [ ] Do you have a playbook that can be repeated?
- [ ] Is there contribution profit to reinvest?
- [ ] Is the adjacent market similar enough for your playbook?
- [ ] Can you maintain focus on your tipping market while expanding?
- [ ] Is a competitor threatening to dominate the new market first?

### For Evaluating Tipping Potential

**Can this market tip?**
- [ ] Is supply fragmented? (no dominant supplier)
- [ ] Is supply heterogeneous? (variety matters to buyers)
- [ ] Are transactions repeated? (not one-time purchases)
- [ ] Is there low switching cost? (buyers can move to you)
- [ ] Is there no dominant incumbent? (market is contestable)
- [ ] Is there a clear market boundary? (something to saturate)

### For Building Growth & Happiness Loops

**Growth loops to find:**
- [ ] How can buyers invite buyers?
- [ ] How can sellers invite sellers?
- [ ] How can sellers bring buyers?
- [ ] How can buyers bring sellers?
- [ ] What creates SEO/organic discovery?

**Happiness loops to build:**
- [ ] How does search reward good suppliers?
- [ ] How does the rating system surface quality?
- [ ] How do bad suppliers naturally churn?
- [ ] How does each transaction improve the next?

## Common Mistakes

### 1. Racing to $1M GMV
The milestone of $1M GMV became a Series A benchmark. But GMV concentrated in one market is worth more than GMV spread across ten. The race to hit numbers creates incentives to spread thin.

### 2. Going after the biggest market
Big markets are competitive. You need fragmentation to tip a market. The suburbs that DoorDash targeted seemed small but were uncontested.

### 3. Treating both sides equally at all times
In the beginning, aggregate supply. As you grow, corner demand. The relative importance shifts over the lifecycle. Airbnb started supply-constrained, eventually needed demand focus.

### 4. Optimizing for transactions, not matches
A marketplace's value is reducing friction. If you optimize for volume, you may sacrifice match quality. Happy matches retain; mere transactions don't.

### 5. Expanding before tipping
If you haven't tipped your first market, you don't have a playbook. Expansion will just spread your unproven model across more places to fail.

### 6. Ignoring disintermediation risk
Long-term relationships eventually route around you. The Thumbtack delivery guy gives you his business card. Pricing and value must evolve as relationships mature.

## Quick Reference

**The core hierarchy:**
1. **Focus** → Pick a thimble, achieve minimum viable happiness
2. **Tip** → Saturate until the market tips to you
3. **Dominate** → Expand from strength with your proven playbook

**What to measure:**
- Happy GMV (retained transactions), not raw GMV
- Both sides' retention rates
- Organic growth percentage
- Cohort improvement over time
- Sean Ellis test (40%+ "very disappointed")

**Key questions:**
- "Is our market uncomfortably focused?"
- "Are we making both sides genuinely happy?"
- "Is the market starting to come to us?"
- "Can this market actually tip?"

---

