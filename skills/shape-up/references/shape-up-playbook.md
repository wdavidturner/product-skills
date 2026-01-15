# Shape Up Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Core Framework

### The Three Phases

```
SHAPING              BETTING              BUILDING
(before cycle)       (cycle start)        (during cycle)
─────────────────────────────────────────────────────────────────

Problem   →   Shaped   →   Bet   →   Kickoff   →   Build   →   Ship
Framing       Pitch        Made      Scopes        Work        Done
```

### Phase 1: Shaping

Shaping is collaborative problem-solving before the build starts. It's NOT:
- Writing a PRD
- Creating Figma mockups
- Making user stories
- Writing tickets

It IS:
- Getting product, design, AND engineering in a room together
- Drawing rough concepts (breadboards, fat marker sketches)
- Finding the holes and rabbit holes before committing time
- Arriving at an idea everyone can hold in their head

**The output test:** Can you describe the solution in 10 or fewer moving pieces? If yes, it's shaped. If not, keep working.

**Example (from the book):**
> Problem: Users can't see empty calendar spaces in the agenda view.
>
> Shaped solution: A two-month dot grid (like airline booking) that shows which days have events. Tapping a day slides an agenda view underneath. A "new" button creates events. Navigation arrows for months.
>
> That's 5-6 moving pieces. An engineer can say "I know what to build."

### Phase 2: Betting

Betting replaces the backlog. Instead of an ever-growing list of tickets, you have a betting table where leadership decides what gets time.

**Key principles:**
- Shaped pitches compete for limited slots
- If a pitch isn't bet on, it goes away (no backlog)
- Betting is a real commitment of resources
- Pitches must include appetite (time budget)

**What gets bet:**
- Important enough to commit 2-6 weeks
- Shaped well enough that the team can see the end from the beginning
- Timely — there's a reason to do it now

### Phase 3: Building

Building happens in fixed time boxes (typically 6 weeks max). The team owns the work and creates their own tasks.

**Key differences from Scrum:**
- No daily standups required
- No sprint planning with prescribed tickets
- Team discovers tasks as they build
- Progress tracked on hill charts, not burndown

**The kickoff exercise:**
Draw a 3x3 grid (9 boxes). Ask the build team to identify 9 major implementation scopes. With 30 business days in 6 weeks, that's ~4 days per scope. If they can't fit it in 9 boxes, there's too much scope.

## Appetite: The Core Concept

Appetite is how much time you're *willing* to spend, not how long something will *take*.

```
TRADITIONAL                          SHAPE UP
───────────────────────────────────────────────────────────────

"What's the estimate     →           "What's our appetite?"
 for this feature?"

"Engineering says        →           "We're willing to spend
 3 months"                            6 weeks max"

"Okay, let's see if      →           "Now shape a version
 we can hit it"                       that fits"
```

**Why this works:**

1. **It forces trade-offs upfront** — Like buying a car with a budget, you make hard choices before committing
2. **It aligns with business value** — The business decides what something is worth
3. **It prevents scope creep** — The constraint is fixed, scope is variable
4. **It enables real commitment** — You can actually promise to finish

**Appetite sizes:**
- **Small Batch:** 1-2 weeks (growth experiments, quick fixes)
- **Big Batch:** 6 weeks max (substantial features)

If something seems to need more than 6 weeks, break it into sequential bets.

## The Shaping Session

### Who's in the Room

- **Product person** — Understands the business context, customer need, and why this matters
- **Senior engineer** — Knows where the bodies are buried, what's truly hard vs. easy
- **Designer** (optional but helpful) — Can sketch interaction ideas quickly

The engineer must be someone who can look at the actual code and say "this is harder than it looks" or "actually, we could do that easily."

### How It Works

1. **Start with a narrowed problem** (from framing work)
   - Not "calendar" but "users can't see empty spaces"

2. **Generate multiple solution approaches**
   - "What if we did a dot grid?"
   - "What if we just showed gaps in the agenda?"
   - Try to break each approach

3. **Find the holes**
   - "What about multi-day events?"
   - "What happens on mobile?"
   - Engineer opens code to check assumptions

4. **Converge on 10 or fewer pieces**
   - If you can't get it under 10 pieces, the scope is too big
   - The pieces must be concrete, not abstract

### Time Required

- **3-hour session** can be very productive
- **Multiple sessions** if needed (with spikes between)
- If the problem is clear and tech is known, 2-3 sessions usually enough

### The Output: A Pitch

The pitch is a document that captures:
1. **Problem** — What we're solving and why it matters
2. **Appetite** — How much time we're betting
3. **Solution** — The shaped idea with breadboards/fat marker sketches
4. **Rabbit holes** — Known risks we've addressed
5. **No-gos** — What we're explicitly NOT doing

## Hill Charts: Tracking Real Progress

Hill charts replace status updates with honest progress visualization.

```
                    ╱╲
                   ╱  ╲
        FIGURING ╱    ╲ MAKING
        IT OUT  ╱      ╲ IT HAPPEN
               ╱        ╲
              ╱          ╲
─────────────●────────────●─────────────
           START        DONE
```

**Left side (uphill):** Unknowns, figuring out the approach, hitting obstacles
**Right side (downhill):** Execution, known work, just building it out

**Why it works:**
- Forces honesty about "stuck" vs. "making progress"
- A scope that won't climb the hill reveals shaping problems
- No fake "50% done" based on tickets completed

**How to use:**
- Each scope (from the 9-box kickoff) gets a dot on the hill
- Team moves dots as work progresses
- If a dot is stuck on the left side, it's a warning sign

## Common Failure Modes

### 1. Adopting Time Boxes Without Shaping

> "We're doing Shape Up now! Teams get 6 weeks. Figure it out."

This is cruel. Without proper shaping, you're just setting arbitrary deadlines.

### 2. PRDs and Figma Files as "Shaping"

> "Here's the PRD. Here's the designs. You have 6 weeks."

This isn't shaping — it's waterfall with a time limit. The engineer wasn't in the room when decisions were made.

### 3. No Engineering in Shaping

> "Product and design will shape it, then hand it to engineering."

The Figma file will explode on contact with engineering reality. You'll discover rabbit holes in week 4 instead of in shaping.

### 4. Endless Shaping

> "We've been shaping this for 3 months..."

Shaping should be fast and intense. If the team will be free next week, you have one week to shape. Real deadlines force real decisions.

### 5. Scope Cutting at the End

> "We ran out of time, so we cut half the features."

This demoralizes everyone. Cut scope BEFORE you start, not when you're out of time. Shaping is where scope gets negotiated.

## Applying Shape Up: Checklists

### Before Starting a Project

- [ ] Is the problem narrowed down? (Not "calendar" but "empty spaces")
- [ ] Do we have an appetite? (Not "as long as it takes")
- [ ] Did we shape with an engineer in the room?
- [ ] Can we describe the solution in 10 or fewer pieces?
- [ ] Have we identified rabbit holes?
- [ ] Is there a pitch document?

### At Kickoff

- [ ] Does the build team understand the shaped solution?
- [ ] Can they map it to 9 or fewer implementation scopes?
- [ ] Do the scopes fit in the time box (30 days / 9 = ~4 days each)?
- [ ] Does anyone see problems with the shape?

### During the Build

- [ ] Is the team making their own tasks? (Not following a ticket list)
- [ ] Are scopes climbing the hill? (If stuck, investigate)
- [ ] Are we resisting scope creep?
- [ ] Are we cutting nice-to-haves, not core functionality?

### At the End

- [ ] Did we ship something meaningful?
- [ ] Was it close to what we shaped?
- [ ] If it went over, why? (Shaping problem? Scope problem?)
- [ ] What would we do differently?

### For Leadership

- [ ] Are we protecting build time from interruptions?
- [ ] Are we betting deliberately, not shuffling a backlog?
- [ ] Are we willing to cancel poorly-shaped projects?
- [ ] Are we doing cool-down between cycles?

## The Role of the PM in Shape Up

In traditional teams, PMs often become project managers — chasing status, running standups, keeping tickets moving.

In Shape Up, the PM moves **upstream**:

| Traditional PM | Shape Up PM |
|----------------|-------------|
| Writes tickets | Narrows problems |
| Runs standups | Runs shaping sessions |
| Tracks progress | Understands business context |
| Manages scope creep | Negotiates appetite upfront |
| Shepherds process | Writes compelling pitches |

The PM's job is to make sure the right problems are shaped well enough that teams can run independently during the build.

## Quick Reference

**Core idea:** Fix the time, vary the scope. Shape solutions collaboratively before committing resources.

**Appetite:** How much time you're willing to spend (not an estimate of how long it will take).

**Shaping:** Collaborative sessions with product, design, AND engineering to arrive at a buildable solution in 10 or fewer pieces.

**Betting:** Leadership chooses which shaped pitches get time. No backlog — unused pitches go away.

**Building:** Teams own the build. They make their own tasks. Track on hill charts.

**Time boxes:** 6 weeks max for big bets. 1-2 weeks for small batches.

**Circuit breaker:** If a project isn't on track, stop and re-shape rather than keep throwing time at it.

---

