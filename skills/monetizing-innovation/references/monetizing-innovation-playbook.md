# Monetizing Innovation Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Core Framework

### Price Before Product

The central thesis: Don't build a product and then figure out how to monetize it. Instead, validate willingness to pay first, then design the product around that information.

**Why this matters:**
- 72% of innovations fail from a monetization perspective
- Most failures are preventable with earlier pricing conversations
- You cannot prioritize a roadmap without willingness to pay data
- 20% of what you build drives 80% of willingness to pay

**The shift:**
```
WRONG: Idea → Build → Launch → Figure out pricing
RIGHT: Idea → Test WTP → Design around WTP → Build → Launch with confidence
```

### Willingness to Pay Research

The goal is to understand whether people will actually pay for your innovation, and how much, BEFORE you build it.

#### Who to Talk To

- **B2B:** Talk to 20-30 accounts representing your target market
- **B2C:** Get 1,000-2,000 survey responses for statistical significance
- **Pattern recognition:** After 10-20 conversations, you'll hear themes repeat

#### How to Ask (The Methods)

**Never ask:** "What should I charge for this?" — you'll get garbage.

**Instead, use these techniques:**

**1. Relative Pricing**
Frame questions comparatively:
> "If Salesforce is indexed at 100 for value, where would you rate us?"
> "If Salesforce is indexed at 100 for price, where should we be?"

People are "absolutely meaningless, relatively super smart."

**2. Acceptable/Expensive/Prohibitive**
After pitching your value, ask three questions:
- "What would be an **acceptable** price?" (they love price + product)
- "What would be an **expensive** price?" (neutral — would pay but not thrilled)
- "What would be **prohibitively expensive**?" (laughed out of room)

This reveals psychological thresholds where demand drops sharply.

**3. Purchase Probability**
On a scale of 1-5, would you buy this?
- 5 = 30-50% will actually buy
- 4 = 10-20% will actually buy
- 3 or below = will never buy

**4. Most/Least Questions**
Show 6 features from your list of 10. Ask:
- "Which is MOST important? (Must have, will pay)"
- "Which is LEAST important? (Don't need, won't pay)"

Rotate feature sets. This reveals the 20% driving 80% of willingness to pay.

**5. Trade-off Exercises (Advanced)**
Show realistic packaging/pricing options and ask which they'd choose. Based on choices, reveal mental models and elasticity.

#### The 50% Rule
Half your follow-up questions should be "Why?" The reasoning behind answers is where insights live.

### The Value Metric

**How you charge is more important than how much you charge.**

The value metric (also called pricing metric) is the unit of measurement for your price: per seat, per user, per API call, per resolution, per mile.

**Why it matters so much:**
1. **Acquisition:** Different-sized customers pay different amounts automatically
2. **Retention:** 20-25% lower churn — customers downgrade instead of canceling
3. **Expansion:** 2x higher expansion revenue — growth is implicit, not a resell

**Choosing your value metric:**

| Consider This | Choose Based On |
|---------------|-----------------|
| What customers perceive as value | Not what's easy to meter |
| What scales with their success | Not what's convenient for you |
| What they can track and understand | Not internal technical concepts |

**Example:** Segment switched from "per API" (technical, confusing) to "monthly tracked users" (clear, scales with customer value).

### Pricing Models

There are only three fundamental pricing strategies:

| Strategy | Description | Example | Use When |
|----------|-------------|---------|----------|
| **Skimming** | Launch high, lower over time | Apple iPhone | Premium positioning, quality signals value |
| **Penetration** | Launch low, capture volume | Amazon | Unit economics support it, network effects |
| **Maximization** | Optimize price-volume tradeoff | Microsoft | Neither extreme, balance growth and margin |

**Subscription vs. Usage-Based:**

| Choose Subscription When | Choose Usage When |
|-------------------------|-------------------|
| Customers want predictable bills | Customers want low commitment |
| Usage is consistent month-over-month | Usage varies significantly |
| Value is ongoing, usage is intermittent | Value delivered with usage |
| You want to simplify the conversation | You can track a clear metric |

**AI/Agentic Products:** The new frontier is outcome-based pricing. Charge for results delivered, not access or usage.

```
PRICING POWER QUADRANT

                    HIGH ATTRIBUTION
                          │
     Usage-Based          │      Outcome-Based
     (AWS, backend)       │      (Intercom Fin: $0.99/resolution)
                          │
LOW AUTONOMY ─────────────┼───────────── HIGH AUTONOMY
                          │
     Seat-Based           │      Hybrid
     (Slack, traditional) │      (Cursor: seats + AI credits)
                          │
                    LOW ATTRIBUTION
```

Move toward the upper-right quadrant for maximum pricing power.

### Segmentation

**The three most important words: "You act differently."**

Segmentation is NOT about demographics or personas. It's about identifying groups with:
- Different **needs**
- Different **willingness to pay**
- That you can **productize to** differently

**The test:** If you can't build different products or packages for different segments, you don't have actionable segmentation.

**Example:** Water
- Fountain: Free (price-conscious, convenient)
- Bottle: $2 (portable)
- Sparkling: $2.50 (taste preference)
- Mini-bar: $5 (convenience-maximizer)
- Liquid Death: $8 (identity/brand)

Same underlying product. Different needs. Different willingness to pay. Different packaging.

### Packaging: Leaders, Fillers, and Killers

When building packages (good/better/best), categorize features:

| Type | Definition | What to Do |
|------|------------|------------|
| **Leaders** | Must have, will pay for (50%+ want) | Core of your packages |
| **Fillers** | Nice to have, might pay | Bundle with leaders for value perception |
| **Killers** | Only 10-20% want badly | Sell as add-ons — kills bundle if included |

**Example:** Happy Meal
- Leader: Big Mac (why people come)
- Fillers: Fries, Coke (wouldn't buy alone, but bundle feels valuable)
- Killer: Coffee (only some want it — sell separately)

### Behavioral Pricing

People are irrational. Use it ethically:

**1. Compromise Effect (Good/Better/Best)**
Most people avoid extremes. Design your middle tier to be where you want customers to land. If everyone's buying the low tier, you've given away too much.

**2. Decoy Effect**
Add an option that makes your target option look attractive:
- $49, $99, $199 (most buy $49)
- Add $299 decoy → most buy $99

**3. Pennies-a-Day**
$30/month vs. $1/day — same price, different perception.

**4. Anchoring**
Show the annual price as monthly: "$29.99/month (billed annually)" not "$360/year"

**5. Panini Effect**
Show progress toward "completing" a set of products/features. People are compelled to finish puzzles.

### Negotiation Tactics (B2B)

**Gives and Gets:**
Never give a discount without getting something back:
- Longer contract term
- Case study / reference rights
- Value audit commitment (they track ROI — helps future renewals)
- Reduced payment terms

**Value Selling:**
1. **Create needs** — don't just discover them ("What if this took 3 seconds instead of 3 weeks?")
2. **Create affirmation loops** — pause and ask "How does this play out for you?"
3. **Co-create the ROI model** — agree on inputs during POC so they can't argue outputs

**Show Up with Options:**
Never present one price. Present 3 options:
- If they push back on $500K, offer: "$100K + 10% of value delivered" OR "$500K fixed"
- Now you're discussing value, not just price

**Taper Concessions:**
First discount: 15%. Next: 5%. Next: 2%. Signal that the negotiation is ending.

## Application Checklists

### For Validating a New Product Idea
- [ ] Can you articulate the problem you're solving in customer language?
- [ ] Have you had 10+ willingness to pay conversations?
- [ ] Do you know which 20% of features drive 80% of WTP?
- [ ] Have you identified psychological price thresholds?
- [ ] Can you describe who will pay and why (not just who might use it)?

### For Choosing Your Pricing Model
- [ ] What value metric aligns with how customers perceive value?
- [ ] Is customer usage predictable or highly variable?
- [ ] Do customers want commitment or flexibility?
- [ ] Can you track and attribute the metric reliably?
- [ ] For AI: What's your autonomy and attribution level?

### For Designing Packages
- [ ] Have you identified leaders, fillers, and killers?
- [ ] Does each tier have a clear "reason to upgrade"?
- [ ] Are you leaving room to expand after the initial land?
- [ ] Is your middle tier designed to be the compromise choice?
- [ ] Have you tested for psychological price thresholds between tiers?

### For Pricing Conversations
- [ ] Are you pitching benefits, not features?
- [ ] Do you have 3+ options to present (not just one price)?
- [ ] Do you know your non-negotiables and your gives/gets?
- [ ] Have you prepared a co-created ROI model?
- [ ] Can you contextualize price based on value delivered?

### For Price Increases
- [ ] Do you have data showing the value you've delivered?
- [ ] Have you planned the communication (not just the number)?
- [ ] Are you grandfathering existing customers appropriately?
- [ ] Do you have a lesser-featured downgrade option ready?
- [ ] Can you articulate what's changed to justify the increase?

## Common Mistakes

1. **Pricing after building** — The conversation happens too late to change direction
2. **Asking what to charge directly** — People can't answer; use indirect methods
3. **Confusing features with benefits** — Talk about what customers get, not what you built
4. **One-size-fits-all pricing** — Different customers have different needs and WTP
5. **Giving the farm away in the entry tier** — Nothing left to expand to
6. **Discounting without getting** — Discounts without trade-offs become new baseline
7. **Rushing to usage-based** — It's trendy but not always right for your business
8. **Ignoring psychological thresholds** — $99 vs. $101 can be a cliff
9. **Static segmentation** — Customers change contexts and needs
10. **POCs as feature tests** — POCs should build business cases

## Quick Reference

**Core thesis:** Price before product. Validate willingness to pay BEFORE you build.

**The 20/80 rule:** 20% of features drive 80% of willingness to pay. Find that 20%.

**Value metric > price point:** How you charge matters more than how much.

**Segmentation test:** If you can't act differently, it's not a real segment.

**Packaging framework:** Leaders (must have), Fillers (nice to have), Killers (add-ons).

**Negotiation rule:** Never give without getting. Always show up with options.

**AI pricing direction:** Move toward high autonomy + high attribution = outcome-based pricing.

---

