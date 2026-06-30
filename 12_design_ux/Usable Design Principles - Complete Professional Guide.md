---
software_dev: supporting
---

# Usable Design Principles - Complete Professional Guide

> **Category:** 12_design_ux · **Language:** English

---

### Affordances, signifiers, feedback, and mental models
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches usable design from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** good design makes things understandable and usable by making how they work visible. This guide covers the foundational concepts — affordances, signifiers, feedback, mapping, and mental models — that apply to any interface, current to 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to design thinking | Part I |
| 2 — Intermediate | Designing interactions | Part II |

**Target audience:** designers, developers, and product people building anything people interact with.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** None.

---

## Table of Contents

**Part I – Making things understandable**
1. Affordances and signifiers
2. Feedback and mapping

**Part II – The user's mind**
3. Mental models and conceptual models

**Part III – How people act**
4. The seven stages of action and the two gulfs

**Part IV – Knowledge and constraints**
5. Knowledge in the head and in the world
6. Constraints, forcing functions, and discoverability

**Part V – Designing for error**
7. Human error: slips, mistakes, and error-tolerant design

> **Status of this guide:** phased delivery. **Ready:** Parts I–V (Ch. 1–7). **In progress:** Part VI (the design process).

---

## Part I – Making things understandable

When something is hard to use, it's usually the **design's fault, not the user's**. Good design communicates how a thing works through its form — you can tell what to do just by looking. The core concepts (affordances, signifiers, feedback, mapping) are the vocabulary for designing that self-evidence, whether for a door, an app, or an API.

---

## Chapter 1 — Affordances and signifiers

### 1.1 Introduction

An **affordance** is a relationship between an object and a user — what actions are *possible* (a chair affords sitting; a button affords pushing). A **signifier** is a *signal* that communicates where and how to act (the visual cue that a button is pressable). Affordances make action possible; signifiers make it **discoverable**. Confusing the two leads to interfaces where the right action exists but no one can find it.

### 1.2 Business context

Users who can't discover how to use a product abandon it — and on the web, a competitor is a click away. Clear signifiers reduce confusion, support calls, and abandonment, directly improving conversion and satisfaction. Designing affordances and signifiers well is cheaper than the support and lost-user costs of an "intuitive to us, baffling to them" interface. Discoverability is a measurable business lever.

### 1.3 Theoretical concepts: possible vs perceivable

```mermaid
flowchart LR
    affordance["Affordance: action is POSSIBLE"] --> sig["Signifier: action is PERCEIVABLE"]
    sig --> discover["User discovers what to do"]
```

A control can afford an action (it works) but lack a signifier (no one knows it's there) — e.g. a swipe gesture with no visual hint. Good design provides **perceivable signifiers** for every important action: buttons that look pressable, links that look clickable, hints for gestures. Don't rely on hidden affordances users must guess.

### 1.4 Architecture: signal every action

```mermaid
flowchart TB
    action["An available action"] --> q{"Is there a perceivable signifier?"}
    q -- "no" --> hidden["Undiscoverable -> users miss it"]
    q -- "yes" --> found["Discoverable -> users act confidently"]
```

### 1.5 Real example

**Scenario.** An app supports a useful swipe-to-archive gesture on list items.

**Problem.** The gesture (affordance) exists but has no signifier — users never discover it.

**Solution.** Add a perceivable signifier (a visible hint/icon, or a partially revealed action) so the gesture is discoverable.

**Implementation (add the signifier).**

```text
Before: swipe-to-archive works, but nothing on screen suggests it -> unused
After:  show a faint trailing "Archive" affordance on the row / a one-time hint
        -> users see the action is possible and how to trigger it
```

**Result.** The capability is now discoverable and used, instead of being a hidden feature only power users find by accident. The action existed; the signifier unlocked it.

**Future improvements.** Provide a visible alternative (a menu action) so the feature isn't gesture-only — affordances shouldn't be hidden behind one undiscoverable interaction.

### 1.6 Exercises

1. Distinguish an affordance from a signifier.
2. Why can an action exist but be undiscoverable?
3. Give an example of a hidden affordance and how you'd signify it.

### 1.7 Challenges

- **Challenge.** Find a feature in your product users miss. Is its affordance signified? Add a perceivable signifier and see if discovery improves.

### 1.8 Checklist

- [ ] Every important action has a perceivable signifier.
- [ ] I don't rely on hidden gestures/affordances alone.
- [ ] Clickable/actionable things look that way.
- [ ] Discoverability is designed, not assumed.

### 1.9 Best practices

- Signify every important action visibly.
- Provide discoverable alternatives to gestures.
- Make controls look like what they do.

### 1.10 Anti-patterns

- Hidden gestures with no hint (mystery-meat interaction).
- Controls that don't look interactive.
- Relying on users to "just know."

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Feature unused | Affordance not signified | Add a perceivable signifier |
| Users don't click a control | Weak signifier | Make it look actionable |
| Gesture-only feature missed | No alternative/hint | Provide a visible alternative |

### 1.12 References

- D. Norman, *The Design of Everyday Things*, revised ed. (Basic Books, 2013) — ISBN 978-0465050659.
- NN/g, "Affordances and Signifiers": https://www.nngroup.com/articles/.

---

## Chapter 2 — Feedback and mapping

### 2.1 Introduction

**Feedback** is communicating the result of an action — telling the user something happened and what. **Mapping** is the relationship between controls and their effects; **good mapping** makes the relationship obvious (a control laid out like the thing it controls). Together they close the loop: the user acts (signifier), the system responds (feedback), and the controls make sense (mapping).

### 2.2 Business context

Without feedback, users don't know if their action worked — they click again (double-submits), give up, or distrust the system. Without good mapping, they trigger the wrong thing. Both cause errors, frustration, and support load. Immediate, clear feedback and intuitive mapping make interfaces feel responsive and trustworthy, reducing mistakes and increasing confidence — which shows up as fewer errors, fewer support tickets, and higher satisfaction.

### 2.3 Theoretical concepts: close the loop, match controls to effects

```mermaid
flowchart LR
    act["User acts"] --> feedback["Immediate, clear feedback (it worked / failed / in progress)"]
    controls["Controls"] --> mapping["Good mapping: layout mirrors the effect"]
```

Feedback must be **immediate** and **informative** (not just "something happened" but what — success, error, progress). Mapping is strongest when **spatial/natural**: controls arranged like what they affect (stove knobs matching burner positions; volume up = up). Poor mapping forces users to memorize arbitrary relationships.

### 2.4 Architecture: action → feedback; control → effect

```mermaid
flowchart TB
    click["Click 'Save'"] --> state["Show progress -> success/error feedback"]
    layout["Control layout"] --> effect["Mirrors the effect it controls"]
```

### 2.5 Real example

**Scenario.** A form's Save button does its work but gives no feedback.

**Problem.** Users can't tell if it saved — they click repeatedly (causing duplicates) or assume failure.

**Solution.** Immediate feedback: disable the button + show a spinner during save, then a clear success/error message.

**Implementation (close the loop).**

```text
On Save click:
  - immediately: disable button, show "Saving..." spinner (feedback: in progress)
  - on success:  "Saved" confirmation (feedback: done)
  - on error:    clear message + how to fix (feedback: failed, actionable)
-> no uncertainty, no double-submits
```

**Result.** Users always know the state of their action; duplicate submits and confusion disappear. The loop is closed with immediate, informative feedback.

**Future improvements.** Ensure control layout maps naturally to effects elsewhere in the UI (good mapping) to reduce wrong-action errors too.

### 2.6 Exercises

1. Why must feedback be immediate and informative?
2. What is "good mapping"? Give an example.
3. What goes wrong with no feedback on an action?

### 2.7 Challenges

- **Challenge.** Find an action in your app with weak feedback. Add immediate, informative feedback (progress + result). Did confusion/double-submits drop?

### 2.8 Checklist

- [ ] Every action gives immediate, clear feedback.
- [ ] Feedback says what happened (success/error/progress).
- [ ] Controls map naturally to their effects.
- [ ] Users are never left uncertain.

### 2.9 Best practices

- Give immediate, informative feedback for every action.
- Use natural/spatial mapping for controls.
- Prevent double-submits with in-progress feedback.

### 2.10 Anti-patterns

- Silent actions (no feedback).
- Arbitrary control-to-effect mappings.
- Generic "something happened" messages.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Double-submits / repeated clicks | No in-progress feedback | Disable + show progress on action |
| Users trigger wrong control | Poor mapping | Lay controls out to mirror effects |
| Confusion after acting | No/unclear feedback | Add immediate, specific feedback |

### 2.12 References

- D. Norman, *The Design of Everyday Things*, revised ed. (Basic Books, 2013) — ISBN 978-0465050659.
- J. Nielsen, "Visibility of System Status" (heuristic): https://www.nngroup.com/articles/ten-usability-heuristics/.

---

> **End of Part I.** You can now design for understandability: provide perceivable **signifiers** for the actions your interface **affords** so they're discoverable, give immediate, informative **feedback** that closes the action loop, and use natural **mapping** so controls relate obviously to their effects. **Part II — The user's mind** (Chapter 3) covers the **mental and conceptual models** people build of a system — and how the design either matches them or fights them. (Error-tolerant design — preventing errors and making them recoverable, blaming the design rather than the user — gets its own treatment later, in **Part V**.)

---

## Part II – The user's mind

People don't operate the system you built; they operate the system they *think* you built. Every user constructs a **mental model** — a private story of how the thing works — and acts on that story. When the story is right, the interface feels obvious; when it's wrong, even a "powerful" product feels broken. The designer's leverage is indirect: you can't install a model in someone's head, but you can shape the **system image** — everything the product shows and says — so the model people infer is the one that lets them succeed.

---

## Chapter 3 — Mental models and conceptual models

### 3.1 Introduction

A **conceptual model** is a simplified explanation of how something works — enough to predict what it will do, not a complete or technically accurate account. Three models matter and must be distinguished. The **design model** is the conceptual model held by the designer — how the system *actually* works. The **user's model** (the mental model) is the conceptual model the user builds from experience. Crucially, the designer and the user never talk directly: the only thing that connects them is the **system image** — the visible structure, controls, labels, behavior, documentation, everything the product presents. If the system image doesn't clearly communicate the design model, the user builds a *wrong* model — and a wrong model produces confident mistakes. Good design is, in large part, building a system image that hands the user the right model for free.

### 3.2 Business context

A correct mental model is the difference between a product people master and one they abandon. When the system image teaches the right model, users predict behavior, recover from surprises, and need little support; when it teaches a wrong (or no) model, they hesitate, distrust the system, fabricate superstitions ("always do X twice or it won't save"), and flood support with "why did it do that?" tickets. Mental-model failures are expensive precisely because they're invisible in a feature list — the feature works, yet adoption stalls because no one can form a story that makes it usable. Investing in a coherent, communicated model is cheaper than the churn and support cost of a product that is powerful but unexplainable.

### 3.3 Theoretical concepts: three models, one channel

```mermaid
flowchart LR
    design["Design model<br/>(how it really works)"] --> image["System image<br/>(what the product shows)"]
    image --> user["User's model<br/>(what the user infers)"]
    user --> predict["User predicts &amp; acts"]
```

The designer's model reaches the user *only* through the system image — never directly. So the design question is not "do I understand my system?" but "does what I show let the user reconstruct a model that works?" Models are allowed to be **incomplete and even technically wrong** as long as they're *predictive*: a thermostat user who believes "higher setting = heats faster" holds a false model that still mostly works for setting a temperature — until it causes the error of cranking it to maximum. The fix is a system image that suggests the correct model (the room heats at a fixed rate toward the target), not a physics lecture.

### 3.4 Architecture: does the image teach the model?

```mermaid
flowchart TB
    img["What the interface shows"] --> q{"Does it suggest how the system works?"}
    q -- "no" --> wrong["User invents a model -> confident, wrong predictions -> errors"]
    q -- "yes" --> right["User infers the design model -> correct predictions -> mastery"]
```

### 3.5 Real example

**Scenario.** A note-taking app syncs to the cloud in the background. There is no visible model of *when* a note is safe.

**Problem.** Users build the wrong mental model — "it saved when I closed it" — or no model at all, so they distrust sync, manually copy notes elsewhere, and lose edits made offline because they assumed an immediate save.

**Solution.** Make the model visible through the system image: show sync state explicitly ("Saving… / Saved / Offline — will sync when connected") so the user's model matches reality.

**Implementation (communicate the model).**

```text
Before: silent background sync -> user guesses the rules -> wrong model, lost trust
After:  per-note status: "Saved 2s ago", "Offline — changes kept locally, will sync",
        a one-line explainer on first use ("Notes save locally instantly, then sync")
        -> user infers the real model: local-first, sync-when-online
```

**Result.** Users stop inventing superstitions and manual backups; they correctly predict that offline edits are safe and will sync later. The behavior didn't change — the *communicated model* did.

**Future improvements.** Surface conflict resolution in the same model ("edited on two devices — keep both?") so the user's model extends gracefully to the hard cases instead of breaking on them.

### 3.6 Exercises

1. Distinguish the design model, the user's model, and the system image.
2. Why can a *technically wrong* mental model still be useful — and when does it bite?
3. The designer "talks" to the user through only one channel. Which one, and what follows from that?

### 3.7 Challenges

- **Challenge.** Pick a feature users misunderstand. Write the model they *currently* infer and the model you *want* them to have. Change the system image (labels, states, defaults, a one-line explainer) to close the gap — then check whether the misunderstanding drops.

### 3.8 Checklist

- [ ] The system image clearly suggests how the system works.
- [ ] The model I want users to hold is written down — and visible in the UI, not just in my head.
- [ ] Hidden state that affects predictions (sync, modes, background work) is made visible.
- [ ] I've checked the *wrong* models users might infer and designed against them.

### 3.9 Best practices

- Decide the conceptual model you want users to hold, then engineer the system image to teach it.
- Make invisible state visible — users can only model what they can perceive.
- Prefer a simple, predictive model over a complete, accurate one.

### 3.10 Anti-patterns

- Hidden behavior that forces users to guess the rules (and guess wrong).
- Assuming "obvious to me" equals "communicated" — the design model never reaches users directly.
- Inconsistent behavior that makes a coherent model impossible to form.

### 3.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Users invent superstitions/workarounds | No communicated model — they guessed | Make the model visible in the system image |
| "Why did it do that?" surprises | User's model diverges from the design model | Align the image (states, labels) to the real behavior |
| Same input, unpredictable result to users | Inconsistent behavior blocks model-building | Make behavior consistent, then signal it |

### 3.12 References

- D. Norman, *The Design of Everyday Things*, revised ed. (Basic Books, 2013) — ISBN 978-0465050659. See Chapter 1 ("The Psychopathology of Everyday Things"), the section on conceptual models, the design model / user's model / system image, and the *Gulfs* introduced there.
- NN/g, "Mental Models": https://www.nngroup.com/articles/mental-models/.

---

## Part III – How people act

A mental model explains what users *believe*; this part explains what they *do*. Every interaction, from flipping a switch to filing taxes, runs through the same loop: form a goal, figure out how to act, act, then check whether it worked. Norman names the seven steps of that loop and the two places designs most often fail it — the gap between intention and action, and the gap between result and understanding. Naming these gaps turns "the user is confused" into a diagnosis you can fix.

---

## Chapter 4 — The seven stages of action and the two gulfs

### 4.1 Introduction

Norman breaks any action into **seven stages**: one for the **goal**, three on the *doing* (execution) side, and three on the *checking* (evaluation) side. Execution: form an **intention/plan**, **specify** the action sequence, **perform** it. Evaluation: **perceive** the state of the world, **interpret** it, **compare** it against the goal. Two gaps decide whether the loop succeeds. The **Gulf of Execution** is the gap between the user's intention and the actions the system actually allows — *"I know what I want; how do I do it here?"* The **Gulf of Evaluation** is the gap between the system's state and the user's ability to perceive and understand it — *"Something happened; did it do what I wanted?"* The designer's whole job, in this frame, is to **bridge both gulfs**.

### 4.2 Business context

Most "the user couldn't figure it out" failures are really an unbridged gulf, and each gulf has a distinct cost. A wide Gulf of Execution shows up as drop-off and "I couldn't find how to…" — users abandon a task because the system offers no obvious action that matches their intention. A wide Gulf of Evaluation shows up as repeated actions, mistrust, and "did that work?" support tickets — users can't read the result, so they retry, give up, or call. Diagnosing which gulf is wide tells you *where* to spend: make actions discoverable (execution) versus make state perceivable (evaluation). It turns a vague usability complaint into a targeted, measurable fix.

### 4.3 Theoretical concepts: the action loop and where it breaks

```mermaid
flowchart LR
    goal["Goal"] --> plan["Plan / intention"]
    plan --> specify["Specify actions"]
    specify --> perform["Perform"]
    perform --> world["The world changes"]
    world --> perceive["Perceive"]
    perceive --> interpret["Interpret"]
    interpret --> compare["Compare with goal"]
    compare --> goal
```

The seven stages are an **approximate model, not a literal sequence** — people skip stages, run them out of order, and loop tightly. Its value is diagnostic: when an interaction fails, you can ask *which stage broke*. Couldn't the user find a control matching their intention? That's a **specify/execution** failure. Did they act but couldn't tell if it worked? That's a **perceive/interpret/evaluation** failure. The two gulfs are simply the execution side and the evaluation side viewed as gaps to be bridged.

### 4.4 Architecture: bridge both gulfs

```mermaid
flowchart TB
    intention["User intention"] --> ge{"Gulf of Execution:<br/>is there an obvious action?"}
    ge -- "no" --> stuck["User can't act -> abandons"]
    ge -- "yes" --> acted["User acts"]
    acted --> gv{"Gulf of Evaluation:<br/>is the result perceivable?"}
    gv -- "no" --> unsure["User can't tell -> retries / distrusts"]
    gv -- "yes" --> done["User confirms success"]
```

### 4.5 Real example

**Scenario.** A user wants to export a report as PDF from a dashboard.

**Problem.** *Execution gulf:* export is buried behind a non-obvious icon, so the user's intention ("get a PDF") has no visible matching action. *Evaluation gulf:* when they finally trigger it, the file generates in the background with no indication — they can't tell it worked, so they click again and get duplicate exports.

**Solution.** Bridge both: surface an explicit **"Export ▸ PDF"** action where the intention arises (execution), and show **progress then a clear result** ("Preparing PDF… / Downloaded report.pdf") (evaluation).

**Implementation (bridge execution, then evaluation).**

```text
Execution gulf -> add a labelled "Export" control next to the report,
                  with "PDF" as a visible option (intention maps to an action)
Evaluation gulf -> on click: "Preparing PDF…" -> "Downloaded report.pdf"
                  (and disable re-click while running) -> result is perceivable
```

**Result.** Users complete the export on the first try and know it succeeded — drop-off and duplicate-export tickets both fall. The fix targeted the two specific gulfs instead of redesigning blindly.

**Future improvements.** Instrument the loop: measure where users stall (no action taken = execution gulf; repeated triggers = evaluation gulf) so the next fix is aimed by data, not guesswork.

### 4.6 Exercises

1. List the seven stages of action and group them into the execution side and the evaluation side.
2. Define the Gulf of Execution and the Gulf of Evaluation in one sentence each.
3. A user clicks a button repeatedly because "nothing happened." Which gulf is wide, and which stage broke?

### 4.7 Challenges

- **Challenge.** Take one task in your product. Walk it through all seven stages and mark where a user could get stuck. Classify each stuck point as an execution-gulf or evaluation-gulf problem, then fix the widest one.

### 4.8 Checklist

- [ ] For each user goal, there is an obvious action that matches the intention (execution bridged).
- [ ] After every action, the resulting state is perceivable and interpretable (evaluation bridged).
- [ ] I can name which stage breaks when a task fails.
- [ ] Progress and outcome are shown, so users never have to guess whether an action worked.

### 4.9 Best practices

- Design from the user's goal backward through the seven stages, not from the feature forward.
- Bridge the Gulf of Execution: make the right action visible and matched to the intention.
- Bridge the Gulf of Evaluation: make state and outcomes perceivable and easy to interpret.

### 4.10 Anti-patterns

- Hiding the action that fulfills a common intention (wide execution gulf).
- Acting silently, leaving users to infer the result (wide evaluation gulf).
- "Powerful but unusable": every feature present, none of them reachable through a user's actual goal.

### 4.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Users abandon a task early | Wide Gulf of Execution — no obvious matching action | Surface a labelled action mapped to the intention |
| Repeated clicks / duplicate results | Wide Gulf of Evaluation — result not perceivable | Show progress + a clear outcome; block re-trigger |
| "I didn't know it could do that" | Capability not reachable from the user's goal | Place the action where the goal arises |

### 4.12 References

- D. Norman, *The Design of Everyday Things*, revised ed. (Basic Books, 2013) — ISBN 978-0465050659. See Chapter 2 ("The Psychology of Everyday Actions"): the seven stages of action and the Gulf of Execution / Gulf of Evaluation.
- NN/g, "The Gulf of Evaluation and the Gulf of Execution": https://www.nngroup.com/articles/two-ux-gulfs/.

---

## Part IV – Knowledge and constraints

Why can people operate a hundred-control device they barely studied, yet fumble a five-button one? Because behavior doesn't run on memory alone — it runs on the **combination of what's in your head and what's in the world**. The environment carries much of the information, and **constraints** quietly rule out the wrong actions so the right one stands out. This part covers the trade-off between internal and external knowledge, and the four kinds of constraint (plus forcing functions) you can design into a product so the correct action is the easy, discoverable one.

---

## Chapter 5 — Knowledge in the head and in the world

### 5.1 Introduction

Norman distinguishes **knowledge in the world** from **knowledge in the head**. Knowledge in the world is information sitting in the environment — labels, visible options, the shape of a control, the constraints of a situation — available to be *read* rather than remembered. Knowledge in the head is internal memory — fast and usable without looking anything up, but it must be learned, can be forgotten, and is error-prone. The striking observation is that people achieve **precise behavior from imprecise knowledge**: nobody remembers exactly what a coin looks like, yet everyone uses coins, because the world supplies the missing detail and constraints handle the rest. Good design exploits this: **put knowledge in the world** (or make it cheap to retrieve) instead of forcing users to carry it in their heads.

### 5.2 Business context

Every bit of knowledge you force into the user's head is a tax — on learning time, on error rate, on support. Interfaces that demand memorized codes, hidden steps, or "you just have to know" sequences raise the cost of every session and exclude anyone who uses the product occasionally. Moving that knowledge into the world — visible labels, options shown instead of recalled, sensible defaults, on-screen state — lowers training cost, cuts errors, and makes a product usable by newcomers and infrequent users, who are often the majority. The trade-off is deliberate: knowledge in the head is faster for experts, so the best designs offer both (visible guidance *and* shortcuts), rather than betting everything on memory.

### 5.3 Theoretical concepts: the trade-off

```mermaid
flowchart LR
    world["Knowledge in the world<br/>visible, read not recalled"] --> easy["Easy to use, low learning<br/>but needs the info present"]
    head["Knowledge in the head<br/>memorized, internal"] --> fast["Fast, works anywhere<br/>but must be learned, forgettable"]
```

Knowledge in the world is **its own reminder** — it requires no learning and little memory, but it only works when the information is actually present and perceivable, and reading it is slower than recall. Knowledge in the head is efficient and portable but expensive to acquire and easy to lose. Neither wins outright; the design move is to **shift the burden toward the world** for anything users shouldn't have to memorize (so the interface is self-explaining), while still allowing learned shortcuts for speed. Recognition (seeing the choices) beats recall (remembering them) for most users most of the time.

### 5.4 Architecture: where does the knowledge live?

```mermaid
flowchart TB
    task["A step the user must take"] --> q{"Must they recall it from memory?"}
    q -- "yes" --> head["In the head -> learning cost, errors, exclusion"]
    q -- "no, it's shown" --> world["In the world -> self-explaining, low error"]
```

### 5.5 Real example

**Scenario.** A CLI-style admin tool requires users to type exact command names and flags from memory.

**Problem.** All the operating knowledge lives *in the head* — users memorize commands, mistype flags, and infrequent users are locked out, generating errors and support load.

**Solution.** Move knowledge into the world: show available commands and options (menus, autocomplete, inline help, visible current state) so users **recognize** instead of **recall** — while keeping typed shortcuts for experts.

**Implementation (shift knowledge to the world).**

```text
Before: user must remember `deploy --env=prod --strategy=canary` exactly
After:  show the commands as a discoverable list; autocomplete flags with
        descriptions; display current env/state on screen
        -> recognition replaces recall; experts still type the shortcut
```

**Result.** New and occasional users succeed without memorizing anything; mistyped-flag errors drop; experts keep their speed. The knowledge required to operate the tool now lives in the world, with the head as an optional fast path.

**Future improvements.** Add sensible defaults and constraints (Chapter 6) so even the visible options can't be combined into an invalid command — pushing more of the burden off the user entirely.

### 5.6 Exercises

1. Define knowledge in the world and knowledge in the head, with one example each.
2. Why does "recognition over recall" follow from this distinction?
3. Give a feature in a tool you use that forces knowledge into the head, and describe how to move it into the world.

### 5.7 Challenges

- **Challenge.** Audit one workflow for every piece of knowledge the user must supply from memory (codes, steps, exact names). Move as many as you can into the world (show them), and measure whether error rate or task time for infrequent users improves.

### 5.8 Checklist

- [ ] Users recognize choices on screen rather than recalling them from memory.
- [ ] Critical state is visible, not something the user must remember.
- [ ] Defaults and labels carry knowledge so users don't have to.
- [ ] Experts still have fast paths (knowledge in the head is offered, not required).

### 5.9 Best practices

- Put knowledge in the world: show options, state, and labels instead of demanding recall.
- Favor recognition over recall for anything users shouldn't have to memorize.
- Offer both modes — visible guidance for everyone, shortcuts for experts.

### 5.10 Anti-patterns

- "You just have to know" — operating knowledge locked in the user's head.
- Hidden state the user must track mentally across steps.
- Memorized codes or sequences with no on-screen support.

### 5.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Frequent mistyped/forgotten inputs | Knowledge forced into the head | Show options/state; use recognition over recall |
| Infrequent users can't operate it | No knowledge in the world to lean on | Add visible labels, menus, inline help |
| Long learning curve | Everything must be memorized first | Move guidance into the interface; keep shortcuts optional |

### 5.12 References

- D. Norman, *The Design of Everyday Things*, revised ed. (Basic Books, 2013) — ISBN 978-0465050659. See Chapter 3 ("Knowledge in the Head and in the World"): the trade-off, precise behavior from imprecise knowledge, and memory.
- NN/g, "Recognition vs. Recall in User Interfaces": https://www.nngroup.com/articles/recognition-and-recall/.

---

## Chapter 6 — Constraints, forcing functions, and discoverability

### 6.1 Introduction

**Constraints** are limitations the design builds in so that the *wrong* actions are difficult or impossible and the right one stands out. Norman names four kinds. **Physical** constraints limit possible actions by the shape of things (a plug that only fits one way). **Cultural** constraints are learned conventions (red means stop; an X closes a window). **Semantic** constraints come from the meaning of the situation (a motorcycle rider faces forward, so the windshield goes in front). **Logical** constraints use reasoning and natural mapping (the only remaining screw goes in the only empty hole; the leftmost switch controls the leftmost light). A **forcing function** is a strong physical constraint that *stops* the user from proceeding until a required step is done — its three classic forms are **interlocks**, **lock-ins**, and **lock-outs**. Together, constraints plus signifiers plus feedback produce **discoverability**: the user can figure out what to do and confirm it worked.

### 6.2 Business context

Constraints are the cheapest error-prevention you can buy, because a mistake that's impossible costs nothing to handle. Every invalid state a design *allows* becomes validation code, error messaging, support tickets, and sometimes real damage (an accidental "delete everything," a payment in the wrong currency). Designing the wrong action out — disabling impossible options, ordering steps with an interlock, guarding destructive actions with a lock-in confirmation — prevents whole classes of error before they happen, which is far cheaper than detecting and recovering from them. Constraints also speed users up: fewer choices to reason about means faster, more confident action and lower abandonment.

### 6.3 Theoretical concepts: four constraints, then forcing functions

```mermaid
flowchart TB
    c["Constraints reduce the possible actions"] --> phys["Physical: shape limits what fits"]
    c --> cult["Cultural: learned conventions"]
    c --> sem["Semantic: meaning of the situation"]
    c --> logic["Logical: natural mapping &amp; reasoning"]
```

Constraints work by **shrinking the space of possible actions** until the right one is nearly forced — that's why people assemble unfamiliar objects correctly: physical and semantic constraints rule out the wrong orderings. **Forcing functions** are the strongest version, used where an error would be costly: an **interlock** forces operations into the correct sequence (a microwave won't run with the door open); a **lock-in** keeps an operation going to prevent stopping prematurely ("Save changes before closing?"); a **lock-out** prevents entering a dangerous area (stairs blocked past the ground floor so people don't flee into the basement). Use forcing functions sparingly — they also block legitimate exceptions — but use them where the cost of the error is high.

### 6.4 Architecture: constrain, then confirm

```mermaid
flowchart TB
    action["A possible action"] --> q{"Is it valid / safe here?"}
    q -- "no" --> block["Constrain it out: disable, reorder, or guard (forcing function)"]
    q -- "yes" --> allow["Allow it -> give feedback it worked"]
```

### 6.5 Real example

**Scenario.** A deployment console lets anyone trigger "Delete production database" with a single click, in any order, anytime.

**Problem.** Nothing constrains the dangerous action — it can be hit accidentally or out of sequence, with catastrophic, irreversible cost.

**Solution.** Apply constraints and a forcing function: disable the action unless a backup exists (**logical/physical** constraint), require steps in order (**interlock**), and guard the trigger with a typed-confirmation **lock-in** ("type the database name to proceed").

**Implementation (constrain the dangerous path).**

```text
Disable "Delete" unless a recent backup is present      (constraint)
Require: select target -> confirm scope -> then enable   (interlock: correct order)
Guard the final click: type the exact DB name to proceed (lock-in confirmation)
-> the accidental / out-of-order destructive action becomes impossible
```

**Result.** The catastrophic mistake can no longer happen by accident or in the wrong order; the valid path is still available to someone who genuinely intends it. Error prevention moved upstream, into the design, instead of relying on the user's care.

**Future improvements.** Pair the constraints with clear feedback and an undo/recovery window where possible (Chapter 7) — prevent what you can, and make the rest recoverable.

### 6.6 Exercises

1. Name the four kinds of constraint and give an interface example of each.
2. Define interlock, lock-in, and lock-out, with one example apiece.
3. Why should forcing functions be used sparingly?

### 6.7 Challenges

- **Challenge.** Find a destructive or order-sensitive action in your product. Add the lightest constraint that prevents the bad case (disable, reorder via interlock, or guard via lock-in) without blocking legitimate use. Verify the error class is now impossible, not merely discouraged.

### 6.8 Checklist

- [ ] Invalid options are disabled or impossible, not just discouraged by a warning.
- [ ] Order-sensitive steps are enforced with an interlock where it matters.
- [ ] Destructive/irreversible actions are guarded by a forcing function (lock-in).
- [ ] Constraints follow conventions (cultural/semantic) so they feel natural, not arbitrary.

### 6.9 Best practices

- Prevent errors by design: constrain the wrong action out instead of validating after the fact.
- Use the four constraints (physical, cultural, semantic, logical) to make the right action obvious.
- Reserve forcing functions for high-cost errors; don't block routine actions with friction.

### 6.10 Anti-patterns

- Leaving dangerous actions one careless click away.
- Relying on warning text where a constraint would prevent the error outright.
- Over-constraining: forcing functions on routine tasks that frustrate legitimate use.

### 6.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Users perform an invalid action then see an error | No constraint — the wrong action was allowed | Disable/impossible-ify it; constrain by design |
| Steps done out of order cause failures | Missing interlock | Enforce the required sequence |
| Accidental destructive actions | No forcing function on a high-cost path | Guard with a lock-in (typed confirmation) |

### 6.12 References

- D. Norman, *The Design of Everyday Things*, revised ed. (Basic Books, 2013) — ISBN 978-0465050659. See Chapter 4 ("Knowing What to Do: Constraints, Discoverability, and Feedback"): physical / cultural / semantic / logical constraints and forcing functions (interlocks, lock-ins, lock-outs).
- NN/g, "Preventing User Errors: Avoiding Conscious Mistakes": https://www.nngroup.com/articles/slips/.

---

## Part V – Designing for error

People will make errors. Not because they're careless, but because that's how human cognition works — attention wanders, automatic actions misfire, and reasonable assumptions turn out wrong. The unproductive response is to blame the user; the design response is to **assume error and design for it**. This part separates the two fundamentally different kinds of error, then turns each into a design strategy: prevent what you can with constraints, and make the rest cheap to notice and undo.

---

## Chapter 7 — Human error: slips, mistakes, and error-tolerant design

### 7.1 Introduction

Norman splits human error into **slips** and **mistakes**, and the distinction is not pedantic — it changes the fix. A **slip** happens when you have the *right* goal but the *wrong* action slips out: you meant to click Save and clicked Close; the intention was correct, the execution failed. Slips come from **automatic, subconscious behavior** and include familiar types — **capture errors** (a more frequent action hijacks a similar one), **description errors** (the right action on the wrong object — flipping the switch next to the one you meant), **mode errors** (a correct action that means something different in the current mode), and **data-driven errors** (an external stimulus triggers the wrong action). A **mistake** is deeper: the goal or plan itself was wrong, usually because the user's **conceptual model** was wrong. Slips are errors of *action*; mistakes are errors of *intention*. The design takeaway: **assume people will err, and design so errors are prevented, visible, and recoverable** — blame the design, not the user.

### 7.2 Business context

Treating error as user failure is a business mistake. A product that punishes slips — losing work, committing destructive actions, offering no undo — generates churn, data loss, support escalations, and in safety-critical contexts real harm. A product that *expects* error — confirms the costly stuff, makes the common path the safe path, and makes almost everything reversible — feels trustworthy and forgiving, which raises retention and lowers support cost. The framing matters internally too: a **blame culture** hides the design flaws that caused the error, so they recur; treating "human error" as a **design signal** (the Swiss-cheese view — incidents happen when several latent design holes line up) turns each incident into a fix instead of a scapegoat.

### 7.3 Theoretical concepts: two kinds of error, two strategies

```mermaid
flowchart TB
    err["A user error"] --> q{"Was the goal/plan right?"}
    q -- "yes, action misfired" --> slip["Slip (action error)<br/>capture / description / mode / data-driven"]
    q -- "no, plan was wrong" --> mistake["Mistake (intention error)<br/>wrong conceptual model"]
    slip --> fix1["Fix: constraints, confirmations, undo, clear modes"]
    mistake --> fix2["Fix: better system image &amp; feedback so the right plan forms"]
```

Because slips come from correct intentions, you fight them with **constraints, mode visibility, sensible defaults, and undo** — make the wrong action hard and the right one easy, and make any slip cheap to reverse. Because mistakes come from a wrong model, you fight them upstream with a **clear system image and good feedback** (Chapters 3–4) so the user forms the right plan in the first place, plus **confirmation and reversibility** for high-stakes decisions. A single design often needs both: prevent the slip *and* help the user not form the mistake.

### 7.4 Architecture: prevent, reveal, recover

```mermaid
flowchart LR
    design["Error-tolerant design"] --> prevent["Prevent: constraints &amp; forcing functions"]
    design --> reveal["Reveal: make errors visible immediately"]
    design --> recover["Recover: undo &amp; non-destructive defaults"]
```

### 7.5 Real example

**Scenario.** An email client sends immediately on "Send," and a bulk-action screen deletes selected items with no recovery.

**Problem.** *Slips* are unforgiving: a mis-aimed click (description error) or a wrong-mode action sends an unfinished email or deletes the wrong records, with no way back — a small action error becomes a large, irreversible loss.

**Solution.** Design for error: add a short **undo window** on Send ("Undo" for a few seconds), make deletes **reversible** (soft-delete + restore), show the **current mode/selection** clearly, and confirm only the genuinely irreversible cases.

**Implementation (prevent, reveal, recover).**

```text
Send:   queue for a few seconds with a visible "Undo" -> a slip is recoverable
Delete: soft-delete to a recoverable area, not immediate destruction
Mode:   show the active mode/selection so a mode/description error is visible
Confirm: reserve hard confirmation for the truly irreversible (Chapter 6)
```

**Result.** Slips stop turning into disasters — users recover from the mis-click instead of losing work, and trust rises. The errors didn't vanish (they never will); the design absorbed them.

**Future improvements.** Log where slips cluster (which control, which mode) and treat each cluster as a Swiss-cheese hole to close — feeding real incidents back into prevention rather than blaming users.

### 7.6 Exercises

1. Distinguish a slip from a mistake, and give the design implication of each.
2. Identify the slip type: a user flips the wrong one of two identical switches. Now: a user does the right thing but the app was in a different mode.
3. Why is "human error" often better read as a design signal than a user failure?

### 7.7 Challenges

- **Challenge.** Pick a destructive or error-prone flow. Classify the likely errors as slips or mistakes, then apply the matching strategy (constraints/undo for slips; clearer model/feedback for mistakes). Make at least one previously irreversible action recoverable.

### 7.8 Checklist

- [ ] Costly actions are reversible (undo / soft-delete) wherever possible.
- [ ] The active mode and current selection are always visible (mode/description errors prevented).
- [ ] Confirmation is reserved for the genuinely irreversible — not used as a catch-all.
- [ ] Errors are treated as design signals and fed back into prevention, not blamed on users.

### 7.9 Best practices

- Assume people will err; design so errors are prevented, visible, and recoverable.
- Match the fix to the error: constraints/undo for slips, clearer model/feedback for mistakes.
- Make the safe path the easy path; reserve friction for the truly dangerous.

### 7.10 Anti-patterns

- Irreversible actions with no undo and no recovery.
- Blaming the user ("operator error") instead of fixing the design hole that allowed it.
- Confirmation dialogs on everything — users learn to click through them, so they stop protecting.

### 7.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Users lose work from a mis-click | Unforgiving slip handling | Add undo / make the action reversible |
| Right action, wrong result | Mode or description error | Show the active mode/selection clearly |
| Same incident keeps recurring | Blame culture hides the design cause | Treat error as a design signal; close the hole |
| Confirmations ignored | Over-confirmation trained users to click through | Reserve confirmation for the irreversible; prevent the rest by design |

### 7.12 References

- D. Norman, *The Design of Everyday Things*, revised ed. (Basic Books, 2013) — ISBN 978-0465050659. See Chapter 5 ("Human Error? No, Bad Design"): slips vs mistakes, the categories of slip (capture, description, mode, data-driven), designing for error, and the Swiss-cheese model. (In the original 1988 edition this material is Chapter 5, "To Err Is Human.")
- NN/g, "Slips vs. Mistakes" / error-prevention guidelines: https://www.nngroup.com/articles/slips/.

<!--APPEND-PART-II-->
