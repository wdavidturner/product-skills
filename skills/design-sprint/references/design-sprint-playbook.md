# Design Sprint Playbook

Use this reference only when you need deeper guidance beyond the overview and patterns.

## The Five Days

### Monday: Map

**Goal:** Create a shared understanding of the problem and pick a target.

The team starts by agreeing on a long-term goal and listing the questions/risks that could derail success (Sprint Questions). Then you map the problem: a simple diagram showing how customers encounter and move through the challenge.

**Key activities:**
1. **Set the long-term goal** — Where do you want to be in 6 months to 2 years?
2. **List Sprint Questions** — What are the biggest unknowns? What could cause failure?
3. **Make a map** — Simple flow diagram: actors on left, end goal on right, steps in between
4. **Interview experts** — Team members and outside experts share what they know (How Might We notes)
5. **Pick a target** — The Decider chooses one customer and one moment in the map to focus the sprint

```
┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
│          │      │          │      │          │      │          │
│ Customer │─────►│  Step 1  │─────►│  Step 2  │─────►│   Goal   │
│          │      │          │      │          │      │          │
└──────────┘      └──────────┘      └──────────┘      └──────────┘
     ▲
     │
  TARGET
```

### Tuesday: Sketch

**Goal:** Generate solutions through individual work, not group brainstorming.

Instead of shouting out ideas in a room, each team member works alone to develop detailed solutions. The "work alone together" approach produces better ideas because:
- Introverts have equal voice
- Ideas are developed, not just shouted
- No anchoring on the first idea mentioned

**Key activities:**
1. **Lightning Demos** — 15-minute tour of existing solutions for inspiration (competitors, analogous products)
2. **Divide or swarm** — Decide whether everyone focuses on one part or different parts of the problem
3. **Four-Step Sketch:**
   - Notes (20 min): Review and jot down key info
   - Ideas (20 min): Rough ideas, ugly is fine
   - Crazy 8s (8 min): Fold paper in 8, sketch 8 variations in 8 minutes
   - Solution Sketch (30+ min): One detailed, self-explanatory 3-panel storyboard

**Critical rule:** Solution sketches are anonymous and self-explanatory (no verbal pitches).

### Wednesday: Decide

**Goal:** Choose the best solution without endless debate.

Wednesday morning, the team reviews all sketches in a structured process designed to avoid design-by-committee. The Decider makes the final call.

**Key activities:**
1. **Art museum** — Tape all solution sketches on the wall
2. **Heat map** — Everyone walks around silently, putting dot stickers on interesting parts
3. **Speed critique** — 3 minutes per sketch: narrator describes, team calls out standouts, creator explains missed ideas
4. **Straw poll** — Each person gets one "supervote" sticker on their favorite
5. **Decider votes** — The Decider gets 3 special votes. Their choice wins.
6. **Rumble or all-in-one** — If supervotes split, Decider either picks one direction or combines into one prototype
7. **Storyboard** — Map out the prototype scene by scene (15 frames is typical)

**The Decider:** This is usually the CEO, founder, product lead, or whoever will make the real decision after the sprint. Without a Decider present, sprint outcomes get overturned on Monday.

### Thursday: Prototype

**Goal:** Build a realistic facade — just real enough to test, just fake enough to finish in one day.

The prototype is not a real product. It's a facade that lets you test a specific experience with real customers. Think of it as a movie set: looks real from the front, but there's nothing behind it.

**Key activities:**
1. **Pick the right tools** — Keynote/PowerPoint for apps, Squarespace for websites, paper for physical products
2. **Divide and conquer:**
   - Makers (2+): Build the prototype screens/pages
   - Stitcher (1): Combine pieces into seamless flow
   - Writer (1): Write realistic copy (not lorem ipsum)
   - Asset Collector (1): Gather images, icons, sample data
   - Interviewer (1): Write the interview script, confirm Friday customers
3. **Prototype the critical path** — Only build what you'll test. Skip login screens, settings, edge cases.
4. **Trial run** — End of day, do a dry run of the whole flow

**Goldilocks quality:**
- Too high: Takes too long, team gets attached, hard to throw away
- Too low: Customers can't engage, feedback is about quality not concept
- Just right: Customers can forget it's not real, team can throw it away

### Friday: Test

**Goal:** Learn from 5 target customers whether your solution works.

Five customer interviews is the sweet spot: enough to see patterns, few enough to do in one day. You'll often see 85% of usability issues with just 5 tests.

**Key activities:**
1. **Five interviews** — 1 hour each, back to back
2. **Two rooms:**
   - Interview room: Interviewer + customer + prototype
   - Watch room: Rest of team watches live feed, takes notes
3. **Interview structure:**
   - Friendly welcome (5 min): Warm up, explain format
   - Context questions (10 min): Learn about their current situation
   - Prototype introduction (5 min): Hand off the prototype
   - Tasks and reactions (30 min): Watch them use it, ask questions
   - Debrief (5 min): Overall impressions, would they use it?
4. **Capture patterns** — Each team member takes notes. After each interview, quick debrief. After all five, look for patterns across customers.

**What you're looking for:**
- Did they understand it?
- Did they want it?
- Could they use it?
- What confused them?
- What excited them?

## After the Sprint

A sprint isn't just a one-time event — it's a forcing function for decisions.

### Possible Outcomes

1. **Efficient failure** — The idea didn't work, but you found out in 5 days instead of 5 months. Pivot to the next hypothesis.
2. **Flawed success** — The core idea worked, but specific parts failed. Iterate and test again.
3. **Clear success** — Strong positive signal. Move to building with confidence.

### Next Steps by Outcome

| Outcome | What To Do |
|---------|-----------|
| Clear win | Build it. You have confidence and a tested prototype as a spec. |
| Partial win | Run a follow-up sprint focused on the parts that failed. |
| Clear failure | Back to Monday. New target, new approach, new sprint. |
| Mixed signals | Review Friday patterns. Is there a job you missed? A segment that responded differently? |

## Common Mistakes

### 1. Using sprints for the wrong problems
Sprints work for big, risky, important questions. Using them for small optimizations or problems with obvious solutions wastes everyone's time.

### 2. Not having the Decider present
The Decider must be in the room for the full five days. If they're not, their uninformed objections will kill the prototype on Monday.

### 3. Group brainstorming instead of sketching
The instinct is to gather everyone in a room and "brainstorm." This produces shallow ideas dominated by the loudest voices. Individual sketching produces better, more developed solutions.

### 4. Prototyping too much
You're not building a real product. You're building a facade to test a hypothesis. Prototype only the critical path you'll test.

### 5. Testing to validate, not to learn
If you're hoping customers will prove you right, you'll miss the real signal. Stay curious. The unexpected reactions are the valuable ones.

### 6. Not recruiting the right customers
Five interviews with target customers beats 50 with random people. Screen carefully for your target segment.

## Sprint Checklist

### Before the Sprint

- [ ] **Big, important question** — Is this the right challenge for a sprint?
- [ ] **Decider confirmed** — Is the decision-maker committed to all 5 days?
- [ ] **Team assembled** — 4-7 people, cross-functional (design, engineering, product, marketing, domain expert)
- [ ] **Space booked** — Dedicated room for the full week, whiteboards, supplies
- [ ] **Customers recruited** — 5 target customers scheduled for Friday (with backup candidates)
- [ ] **Facilitator assigned** — One person to run the process, not pitch ideas

### Monday

- [ ] Long-term goal set
- [ ] Sprint questions written (biggest risks and unknowns)
- [ ] Map drawn with team input
- [ ] Expert interviews completed (How Might We notes generated)
- [ ] Target selected by Decider (one customer, one moment)

### Tuesday

- [ ] Lightning demos reviewed
- [ ] Four-step sketch completed by all
- [ ] Solution sketches turned in (anonymous, self-explanatory)

### Wednesday

- [ ] Art museum set up
- [ ] Heat map voting done
- [ ] Speed critique completed
- [ ] Decider vote cast
- [ ] Storyboard drawn (15+ frames, concrete scenes)

### Thursday

- [ ] Prototype roles assigned
- [ ] Prototype built and stitched
- [ ] Realistic copy written
- [ ] Trial run completed
- [ ] Friday interview script ready

### Friday

- [ ] 5 customer interviews completed
- [ ] Team watched and took notes
- [ ] Patterns identified across interviews
- [ ] Sprint questions answered
- [ ] Next steps decided

---

