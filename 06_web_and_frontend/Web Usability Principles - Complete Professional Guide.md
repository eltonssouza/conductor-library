---
software_dev: core
---

# Web Usability Principles - Complete Professional Guide

> **Category:** 06_web_and_frontend · **Language:** English

---

### Don't make users think: clarity, conventions, and self-evident design
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches web usability from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** usability is about reducing the effort a person spends figuring out an interface. This guide covers the core principle (don't make users think), conventions, and clear visual hierarchy — current to 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to usability | Part I |
| 2 — Intermediate | Improving interfaces | Part II |

**Target audience:** frontend developers, designers, and product people building interfaces people must use without training.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** None beyond having used websites and apps.

---

## Table of Contents

**Part I – The core principle**
1. Don't make me think: self-evident design
2. Conventions and visual hierarchy

**Part II – Validating**
3. Cheap usability testing

> **Status of this guide:** complete. **Ready:** Part I (Ch. 1–2) and Part II (Ch. 3).

---

## Part I – The core principle

The guiding rule of usability: a page should be **self-evident**. Users shouldn't have to puzzle out what things are or how to use them — every moment of confusion is friction that costs attention and goodwill. Most usability work is removing small questions ("Is this clickable?" "Where am I?") before they're asked.

---

## Chapter 1 — Don't make me think

### 1.1 Introduction

The central usability principle: **don't make users think** about how to use your interface. Every element should be obvious — what it is, whether it's clickable, what will happen. People don't read pages carefully; they scan, satisfice (pick the first reasonable option), and muddle through. Design for that reality and the interface feels effortless.

### 1.2 Business context

Confusion is abandonment: each "huh?" moment increases the chance a user gives up, and on the web a competitor is one click away. Self-evident design directly improves conversion, task completion, and satisfaction — and reduces support load. It's cheaper to remove confusion in design than to recover users lost to it. Clarity is a revenue lever, not a nicety.

### 1.3 Theoretical concepts: how people actually use sites

```mermaid
mindmap
  root((Real user behavior))
    Scan, don't read
      grab first reasonable option
    Satisfice
      "good enough" beats optimal
    Muddle through
      use without understanding
```

Design accordingly: make important things **obvious and prominent**, label things in plain words, and make clickable things look clickable. Reduce the **questions** the interface raises — "What is this?", "Can I click it?", "Did that work?" — because each unanswered one is friction.

### 1.4 Architecture: minimize questions per screen

```mermaid
flowchart LR
    screen["A screen"] --> q{"What questions does it raise?"}
    q --> remove["Remove or answer each one"]
    remove --> obvious["Self-evident screen"]
```

### 1.5 Real example

**Scenario.** A signup page where users hesitate at a styled-but-ambiguous "Continue" element.

**Problem.** It's a `div` styled like text; users aren't sure it's a button, so they pause or miss it.

**Solution.** Make it unmistakably a button — obvious affordance, clear label of the outcome.

**Implementation.**

```html
<!-- AMBIGUOUS: looks like text, unclear if clickable -->
<div class="cta">Continue</div>

<!-- SELF-EVIDENT: obviously a button, says what happens -->
<button class="btn btn--primary">Create my account</button>
```

**Result.** No hesitation: it clearly looks clickable and the label states the outcome ("Create my account" beats vague "Continue"). One less question, smoother conversion.

**Future improvements.** Add a visible focus state and loading feedback so the click's result is obvious too.

### 1.6 Exercises

1. State the core usability principle in five words.
2. Name three things real users do instead of reading carefully.
3. Why is each "question" an interface raises a cost?

### 1.7 Challenges

- **Challenge.** Open a screen you built. List every question a first-time user might ask ("Is this clickable?"). Remove or answer the top three.

### 1.8 Checklist

- [ ] Important elements are obvious and prominent.
- [ ] Clickable things look clickable.
- [ ] Labels are plain and outcome-focused.
- [ ] The screen raises few questions.

### 1.9 Best practices

- Make affordances obvious; don't disguise buttons.
- Use plain, specific labels over clever or vague ones.
- Remove ambiguity before adding features.

### 1.10 Anti-patterns

- Mystery-meat navigation (unclear what's clickable).
- Clever labels that prioritize style over clarity.
- Dense screens where the primary action isn't obvious.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Users miss the primary action | Not prominent/obvious | Make it visually dominant and clearly clickable |
| Hesitation on controls | Weak affordances | Style clickable things as clickable |
| Vague label confusion | Clever/abstract wording | Use plain, outcome-based labels |

### 1.12 References

- S. Krug, *Don't Make Me Think, Revisited*, 3rd ed. (New Riders, 2014) — ISBN 978-0321965516.
- J. Nielsen, "Usability Heuristics," https://www.nngroup.com/articles/ten-usability-heuristics/.

---

## Chapter 2 — Conventions and visual hierarchy

### 2.1 Introduction

Two tools make pages self-evident: **conventions** (established patterns users already know — logo top-left links home, a magnifier means search) and **visual hierarchy** (size, weight, color, and grouping that show what's important and how things relate). Following conventions and expressing hierarchy lets users understand a page at a glance, without learning it.

### 2.2 Business context

Reinventing conventions ("innovating" navigation) forces users to relearn basics, raising friction and abandonment for no benefit. Conventions are free comprehension — users transfer knowledge from every other site. Clear visual hierarchy guides the eye to what matters, speeding tasks and reducing errors. Together they cut the cognitive cost of every visit, which compounds across millions of sessions into real business impact.

### 2.3 Theoretical concepts: known patterns + clear emphasis

```mermaid
flowchart TB
    conv["Conventions: reuse known patterns"] --> fast["Instant understanding"]
    hier["Hierarchy: size/weight/color/grouping"] --> guide["Eye guided to importance"]
    fast --> usable["Self-evident page"]
    guide --> usable
```

Use conventions unless you have a strong, tested reason not to. Express hierarchy so that **more important = more visually prominent**, and **related things look related** (proximity, alignment, consistent styling). The visual structure should mirror the logical structure.

### 2.4 Architecture: hierarchy mirrors meaning

```mermaid
flowchart LR
    primary["Primary action: largest, highest contrast"]
    secondary["Secondary: less prominent"]
    related["Related items grouped/aligned"]
```

### 2.5 Real example

**Scenario.** A dashboard where everything is the same size and weight.

**Problem.** No hierarchy — users can't tell the key metric from minor details, and the primary action competes with everything else.

**Solution.** Establish hierarchy: emphasize the key number and primary action; de-emphasize the rest; group related items.

**Implementation (hierarchy via emphasis, conceptual).**

```text
Before: all text 14px, same weight/color  -> flat, no focus
After:  key metric  -> 32px bold, high contrast
        primary CTA -> prominent button color
        secondary   -> muted, smaller
        related KPIs grouped in one card, aligned
```

**Result.** The eye lands on what matters first; the primary action stands out; related data reads as a group. Users grasp the screen instantly.

**Future improvements.** Apply consistent spacing and a type scale (see the visual-design guide) to make hierarchy systematic.

### 2.6 Exercises

1. Why follow UI conventions instead of inventing new ones?
2. Name three tools for creating visual hierarchy.
3. What does "related things look related" mean concretely?

### 2.7 Challenges

- **Challenge.** Take a flat screen. Establish hierarchy: make the single most important thing clearly dominant and group related items. Does comprehension improve?

### 2.8 Checklist

- [ ] I reuse established conventions.
- [ ] Visual prominence matches importance.
- [ ] Related items are visually grouped.
- [ ] The visual structure mirrors the logical one.

### 2.9 Best practices

- Follow conventions unless testing justifies breaking them.
- Make the most important element the most prominent.
- Group and align related content.

### 2.10 Anti-patterns

- Reinventing standard navigation/icons.
- Flat designs with no emphasis.
- Important and trivial elements given equal weight.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Users confused by navigation | Broke conventions | Return to familiar patterns |
| Key info overlooked | No hierarchy | Emphasize what matters most |
| Page feels cluttered | No grouping | Group and align related items |

### 2.12 References

- S. Krug, *Don't Make Me Think, Revisited*, 3rd ed. (New Riders, 2014) — ISBN 978-0321965516.
- J. Tidwell, *Designing Interfaces*, 3rd ed. (O'Reilly, 2020) — ISBN 978-1492051961.

---

> **End of Part I.** You can now apply the core usability principle — make interfaces self-evident so users don't have to think — by designing for how people actually behave (scan, satisfice, muddle through), reusing conventions, and expressing visual hierarchy so prominence matches importance. **Part II — Validating** (Chapter 3) covers cheap, frequent usability testing — watching a few real users attempt tasks — as the reliable way to find the confusion you can't see yourself.

---

## Part II – Validating

You cannot tell whether your interface is self-evident, because you already know how it works — you're too close to it to see what confuses a first-time user. Design debates ("I think users will…", "no, users prefer…") are usually unresolvable opinions about an *average* user who doesn't exist. The only reliable way out is to **watch real people use it**. Part II makes that practical: not an expensive lab study, but a cheap, repeatable habit any team can sustain — a morning a month, a few users, fixes shipped before the next round.

---

## Chapter 3 — Cheap usability testing

### 3.1 Introduction

Usability testing is **watching one person at a time try to do typical tasks** with your interface while they think out loud, so you can see where they hesitate, misread, or get stuck. Krug's central, liberating claim is that it does **not** need to be expensive or formal: testing **three users** in a **morning, once a month**, then debriefing over lunch and fixing the worst problems before the next round, finds the vast majority of serious issues for almost no cost. The goal is **actionable insight, not statistical proof**. This chapter covers why a few users suffice, how to run a session, and how to turn what you see into fixes.

### 3.2 Business context

Disagreements about design are expensive when settled by seniority or loudest voice — they ship the wrong thing and you discover it after launch, in support tickets and lost conversions. Testing replaces opinion with observation: it ends "religious debates" cheaply and early, when changes still cost little. Because the method is so light (a morning a month), it fits inside real schedules instead of being the study that's always deferred until "after the deadline." And because it surfaces the confusion that costs real users — the unclear label, the invisible button, the form that traps them — it pays back directly in completion rates and reduced support load. The trap it avoids is testing too late and too rarely; small and frequent beats big and occasional.

### 3.3 Theoretical concepts: a few users, often

```mermaid
flowchart TB
    three["Test ~3 users"] --> most["They hit most of the serious problems"]
    most --> fix["Fix the worst few"]
    fix --> again["Test 3 more next month"]
    again --> more["Catch what the fixes revealed -- iterate"]
```

You don't need many participants because the **most serious problems are the most common** — three users will stumble on them. Testing a huge sample to find *every* problem is wasted effort: "you can find more problems in half a day than you can fix in a month," so finding more isn't the bottleneck — fixing is. The leverage is **iteration**: test a few, fix the worst, and test again next month, because each fix exposes the next layer of problems. Frequent small rounds beat one large study because they keep validating as the design changes. The output is qualitative — *where* people struggle and *why* — not a metric.

### 3.4 Architecture: the morning-a-month session

```mermaid
flowchart LR
    recruit["Recruit ~3 roughly-representative users"] --> tasks["Give real tasks, ask them to think aloud"]
    tasks --> observe["Facilitator stays neutral; team observes"]
    observe --> debrief["Debrief over lunch: pick the few worst problems"]
    debrief --> next["Fix before next month's round"]
```

The mechanics are deliberately simple. **Recruit** loosely — "recruit users who are roughly representative," because most serious problems aren't specific to your exact audience. Give **real tasks** ("buy a ticket to…") and ask the user to **think aloud**. The **facilitator** stays neutral: no leading, no rescuing, no explaining — let the interface speak. The **team watches** (a screen share is enough), because seeing a real user struggle is far more persuasive than a report. Then **debrief immediately** over lunch and agree on the **handful of most serious problems** to fix before next month — resisting the urge to log everything.

### 3.5 Real example

**Scenario.** A team argues for weeks about whether their checkout's "Continue" button is clear or whether users want a visible cart summary first. No one can prove it.

**Problem.** The debate is about an imaginary average user; opinions don't converge, and shipping either version is a guess.

**Solution.** A morning-a-month test: three roughly-representative users, one real task, the team watching.

**Implementation.**

> **Task given:** "You want to buy two tickets to Saturday's show — go ahead and do that, and say what you're thinking as you go."
>
> **What the team observes (3 users):**
> - User 1 clicks "Continue," then backtracks: "Wait — did it add both? I can't tell."
> - User 2 hunts for a cart total: "I'd want to see the price before I commit."
> - User 3 reads "Continue" as "continue shopping," not "go to payment."
>
> **Debrief over lunch — the few worst problems:**
> 1. "Continue" label is ambiguous → rename to "Go to payment."
> 2. No order summary before payment → add a cart total on the page.
>
> (Smaller nits are noted but not fixed this round.)

**Result.** The weeks-long debate is settled in one morning by observation, not opinion. Two concrete, high-value fixes are agreed and shipped before the next round — which will reveal the *next* layer of confusion.

**Future improvements.** Make it a standing date (e.g. the third Thursday); rotate which team members facilitate and observe; keep a running list of the worst problems so fixes are prioritized by severity, not by who shouted loudest.

### 3.6 Exercises

1. Why do three users find most of the *serious* problems?
2. What is the facilitator's main job during a session — and what must they avoid?
3. Why is "a morning a month" better than one big study before launch?

### 3.7 Challenges

- **Challenge.** Run a 60-minute test with three people who haven't seen your product. Give one realistic task, ask them to think aloud, stay neutral, and have the team watch. Debrief afterward and commit to fixing only the three most serious problems before testing again.

### 3.8 Checklist

- [ ] I test a few users (≈3) frequently rather than many users rarely.
- [ ] I use real tasks and ask participants to think aloud.
- [ ] The facilitator stays neutral — no leading or rescuing.
- [ ] The team observes the sessions directly.
- [ ] We debrief immediately and fix the few most serious problems before the next round.

### 3.9 Best practices

- Schedule a recurring testing day so it survives busy weeks.
- Recruit loosely; most serious problems aren't audience-specific.
- Focus on the worst problems first — you'll always find more than you can fix.
- Treat results as actionable insight, not proof; iterate.

### 3.10 Anti-patterns

- Settling design debates by opinion or seniority instead of observation.
- Deferring testing until "after launch" (or until a big formal study is affordable).
- Leading or rescuing the participant, so the interface is never really tested.
- Logging every minor issue and fixing none of the big ones.

### 3.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Endless design debates | Opinions, no observation | Watch three users do the task |
| "We never have time to test" | Test tied to milestones | Fix a recurring morning-a-month date |
| Sessions feel inconclusive | Facilitator leads/explains | Stay neutral; give tasks, then watch |
| Nothing improves between rounds | Fixing too many small things | Fix only the few most serious problems |

### 3.12 References

- S. Krug, *Don't Make Me Think, Revisited*, 3rd ed. (New Riders, 2014) — Ch. 9 (Usability testing on 10 cents a day), Ch. 8 (resolving design debates by testing). ISBN 978-0321965516.
- S. Krug, *Rocket Surgery Made Easy* (New Riders, 2010) — do-it-yourself usability testing.
- Nielsen Norman Group, "Why You Only Need to Test with 5 Users": https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/.

---

> **End of guide.** You can now make web interfaces usable end to end: design them to be self-evident for how people actually behave, using conventions and clear visual hierarchy (Part I), then validate that they are — cheaply and continuously — by watching a few real users attempt real tasks and fixing the worst problems first (Part II).
