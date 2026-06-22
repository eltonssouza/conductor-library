# Spec-Driven Development - The Complete Book

> **Category:** 04_engineering_and_practices · **Language:** English

---

# Spec-Driven Development (SDD)

### The Complete Book: Specification-Guided Software Development in the Age of Artificial Intelligence

---

> *"The next generation of programmers won't write code. They'll write the specifications that teach machines to write code — and discover, along the way, that writing a good specification was always the hard part."*

---

## Table of Contents

**Part I — Foundations**
1. What Spec-Driven Development Is
2. Why SDD Emerged Now
3. The Mindset Shift: From "How" to "What"
4. SDD Versus Other Methodologies

**Part II — Anatomy of a Specification**
5. What Makes a Good Specification
6. The Components of a Spec
7. Levels of Specification
8. The Language of Specification

**Part III — The Workflow**
9. The SDD Lifecycle
10. From Intent to Specification
11. From Specification to Plan
12. From Plan to Code
13. Validation and the Feedback Loop

**Part IV — Practice**
14. Writing Your First Spec
15. Patterns and Anti-Patterns
16. Specifying for Existing Systems (Brownfield)
17. Tools and Ecosystem

**Part V — Maturity and Scale**
18. SDD in Teams
19. Governance, Traceability, and ADRs
20. Quality, Testing, and the Quality Gate
21. The Future of SDD

**Appendices**
- A. Ready-to-Use Templates
- B. Glossary
- C. Checklists
- D. Further Reading and References

---

---

# PART I — FOUNDATIONS

---

## Chapter 1 — What Spec-Driven Development Is

### 1.1 Definition

**Spec-Driven Development (SDD)** is a software development methodology in which the central artifact of the process is no longer the code, but the **specification**: a clear, structured, versioned document describing *what* the software must do, *why* it must do it, and *under what conditions* it will be considered correct — **before** a single line of implementation is written.

In the context of generative Artificial Intelligence, SDD takes on a sharper, more operational definition:

> SDD is the practice of **creating clear, structured specifications before asking the AI to write the code**, so that the AI has enough context, constraints, and acceptance criteria to generate a correct, predictable, and verifiable implementation.

The specification becomes the **source of truth**. Code becomes a **derived output** of the specification — something that can be regenerated, refined, or replaced, as long as the spec remains correct.

### 1.2 The Fundamental Inversion

For decades, software development worked like this:

```
Vague idea → Code → (maybe) Documentation afterward
```

Documentation, when it existed at all, was written *after* the code, went stale, and rarely reflected reality. Code was king. The specification was a bureaucratic detail.

SDD inverts that order:

```
Intent → Clear specification → Code generated from it → Validation against the spec
```

The specification comes **first**. The code comes **after**, derived from it. And validation closes the loop, comparing what was generated against what was specified.

### 1.3 The Sentence That Sums It All Up

> **In SDD, you don't program the computer. You program the specification, and the specification programs the computer.**

This changes the developer's job. The most valuable skill stops being "knowing the syntax of language X" and becomes **"being able to describe a problem with enough precision that it can be solved correctly by another intelligence"** — whether that intelligence is an AI or a human colleague.

### 1.4 An Analogy: The Architect and the Builder

Think of a civil construction project:

- The **architect** creates the blueprint: dimensions, materials, structural constraints, client requirements, legal codes.
- The **builder** executes the blueprint, turning it into a physical structure.

Nobody builds a skyscraper by stacking bricks and "seeing how it goes." The blueprint comes first. It's validated, reviewed, approved — and only then does construction begin.

In SDD:

- **You are the architect.** You write the blueprint (the specification).
- **The AI is the builder.** It turns the blueprint into code.

And just as a bad blueprint produces a flawed building, a bad specification produces bad code — no matter how capable the builder is.

---

## Chapter 2 — Why SDD Emerged Now

### 2.1 The Bottleneck Moved

Throughout the history of programming, the bottleneck of software production was **writing code**. It was slow, required years of training, and every line cost expensive human time.

With language models capable of generating code (LLMs), writing code stopped being the bottleneck. An AI can produce hundreds of lines in seconds. The new bottleneck became:

> **Telling the AI, precisely, what you actually want.**

When generating code is cheap and fast, the cost shifts to **clarity of intent**. That is exactly the problem SDD attacks.

### 2.2 The "Vibe Coding" Problem

The first wave of AI-assisted programming was what became popularly known as *vibe coding*: the developer describes something vaguely ("make a nice to-do app"), the AI generates something, they look at it, ask for tweaks, the AI redoes it, and so on — steering by "vibe," by feel.

This works surprisingly well for prototypes and demos. But it collapses on real software, because:

- **There's no source of truth.** What the system "should" do exists only in the developer's head and in a chat history — which gets lost.
- **It's not reproducible.** Asking for the same thing twice yields different results.
- **It doesn't scale.** With 50 features and 5 people, nobody knows the original intent of any part anymore.
- **It accumulates invisible debt.** Important decisions are made implicitly by the AI, with no record.
- **It's not verifiable.** Without acceptance criteria, "is it done?" becomes a matter of opinion.

SDD is the mature answer to vibe coding. It keeps the speed of AI generation but adds **rigor, traceability, and verifiability**.

### 2.3 The Evolution Table

| Era | Central artifact | Bottleneck | Main risk |
|-----|------------------|------------|-----------|
| Traditional programming | Source code | Writing code | Slowness, human cost |
| Vibe coding (early AI) | Chat conversation | Communicating intent | Chaos, irreproducibility |
| **Spec-Driven Development** | **Specification** | **Specifying precisely** | **Badly written specs** |

### 2.4 Why This Is Not Just "Documentation Back in Fashion"

A common objection: "This is just documenting before coding, and we know nobody does that."

The crucial difference is **the incentive**. In traditional programming, writing the spec was *extra* work that produced nothing executable — so it got skipped. In SDD, the spec is **the direct input** that generates the code. It's not optional; it's the raw material. Writing the spec *is* programming. The incentive has flipped: now skipping the spec is what costs more, because it means steering the AI blind.

---

## Chapter 3 — The Mindset Shift: From "How" to "What"

### 3.1 Imperative vs. Declarative Thinking

Traditional development is mostly **imperative**: you tell the machine *how* to do something, step by step.

```python
total = 0
for item in cart:
    total += item.price * item.quantity
if total > 100:
    total = total * 0.9
```

SDD pushes the developer toward **declarative** thinking: you describe *what* must happen and *which* properties the result must have, leaving the *how* to the AI.

```
RULE: The cart total is the sum of (price × quantity) for each item.
RULE: Orders above $100.00 receive a 10% discount on the total.
CRITERION: Given a cart with items totaling $150.00,
           when the total is calculated,
           then the final value must be $135.00.
```

Note that the SDD version doesn't say *how* to iterate, *how* to apply the discount, or in what language. It says **what is true about the system**. The implementation is the builder's responsibility.

### 3.2 The Discipline of Not Saying Too Much

A common mistake from people coming out of the imperative world is "leaking" implementation decisions into the spec:

❌ **Leaking the how:**
> "Create a `for` loop that iterates over the item list and uses an accumulator variable..."

✅ **Keeping the what:**
> "The total is the sum of each item's subtotal. Subtotal = price × quantity."

The first version ties the AI to a specific implementation and loses the benefits of SDD. The second lets the AI choose the best form, and stays valid even if the language or data structure changes.

> **Golden rule:** Specify constraints and outcomes, not algorithms. Say *what must be true*, not *which instructions to execute* — unless the "how" is itself a requirement (for example, "must use algorithm X for compliance reasons").

### 3.3 What the Developer Gains and Loses

**Gains:**
- Focus on the business problem, not the syntax.
- The ability to operate across multiple languages/stacks without deeply mastering each.
- Durable artifacts (specs) that survive refactors and technology swaps.
- Real speed without losing control.

**Loses (or must relearn):**
- The illusion of line-by-line control. In SDD, you control through **constraints and verification**, not through typing.
- The habit of "just coding and seeing what happens."

This transition is uncomfortable at first. It's like a manual-transmission driver learning to trust an automatic gearbox: the urge to step on the nonexistent clutch lingers for a while.

---

## Chapter 4 — SDD Versus Other Methodologies

SDD wasn't born in a vacuum. It inherits and recombines ideas from established practices. Understanding these relationships helps position it correctly.

### 4.1 SDD vs. TDD (Test-Driven Development)

**TDD** says: write the test first, then the code that makes it pass. The test is a form of **executable** specification.

SDD is, in a sense, **TDD raised to a higher level**:
- In TDD, the "spec" is a test written in code, by someone who already thinks in code.
- In SDD, the spec is a document in structured language (and often *generates* the tests automatically).

They are **complementary**, not competing. A mature SDD flow usually produces, from the spec, both the code and the tests — and uses the tests to validate that the code truly fulfills the spec.

| Aspect | TDD | SDD |
|--------|-----|-----|
| Primary artifact | Test in code | Structured specification |
| Who writes it | Developer | Developer / PO / any technical stakeholder |
| Level of abstraction | Code unit | Behavior and business rules |
| Generates code? | Not directly | Yes, via AI |
| Relationship | Complementary: the spec can generate the TDD tests |

### 4.2 SDD vs. BDD (Behavior-Driven Development)

**BDD** already came very close to SDD with its **Given/When/Then** syntax:

```gherkin
Given the cart has items totaling $150.00
When the customer checks out
Then a 10% discount must be applied
And the total must be $135.00
```

SDD often **adopts the BDD format** for the acceptance-criteria part. The difference is that BDD focuses on describing behavior to align business and tech, while SDD uses those descriptions as a **direct input for code generation by the AI**. BDD is one of the tools inside SDD.

### 4.3 SDD vs. DDD (Domain-Driven Design)

**DDD** is about modeling the problem domain with a *ubiquitous language* shared between business and development. SDD benefits enormously from DDD: a good spec uses the domain's ubiquitous language, and describes entities, aggregates, and business rules with the right terms.

DDD answers *"how to model the domain."* SDD answers *"how to turn that model into software with AI help."* They go hand in hand.

### 4.4 SDD vs. Waterfall

At first glance, "specify everything before coding" sounds like the old **Waterfall** — and that's a frequent criticism. But there are decisive differences:

| Waterfall | SDD |
|-----------|-----|
| Huge spec, done once, frozen | Small, iterative, living specs |
| Feedback cycle of months | Feedback cycle of minutes/hours |
| Spec and code diverge over time | Spec is the source; code derives from it |
| Change is expensive and bureaucratic | Change = edit the spec and regenerate |

SDD is **iterative and agile**. You specify a small slice, generate, validate, learn, and refine the spec. It's not "specify the whole universe and never change it." It's the opposite: the spec is so cheap to change that changing it is the normal flow of work.

### 4.5 Where SDD Fits

```
        DDD ──────► provides the language and model of the domain
         │
         ▼
   SPECIFICATION (SDD) ──► source of truth
         │
    ┌────┴─────┐
    ▼          ▼
   CODE      TESTS (TDD/BDD derived from the spec)
    │          │
    └────┬─────┘
         ▼
    VALIDATION ──► does the code fulfill the spec?
         │
         ▼
    (feedback refines the spec)
```

---

---

# PART II — ANATOMY OF A SPECIFICATION

---

## Chapter 5 — What Makes a Good Specification

### 5.1 The Five Properties of an Excellent Spec

A quality specification in SDD has five properties, forming the acronym **CIVET**:

1. **Clear** — no ambiguity. Each sentence has a single possible interpretation.
2. **Inambiguous / Complete** — covers the normal cases, the edge cases, and the error cases. Leaves no gaps the AI has to "guess."
3. **Verifiable** — each requirement can be tested objectively. "The system must be fast" is not verifiable; "the response must arrive within 200ms at the 95th percentile" is.
4. **structurEd** — organized into predictable sections, with identifiers, easy to navigate by both humans and AI.
5. **Traceable** — each requirement has an ID; each decision has a record; it's possible to link code → spec → original intent.

### 5.2 The Stranger Test

A good mental test for your spec:

> **If I handed this spec to a competent person who knows nothing about the project and has never spoken to me, could they build the right thing without asking me questions?**

The AI is exactly that "competent stranger." It doesn't have the context that lives in your head. Everything not written down, it will infer — and inference is where the risk lives.

### 5.3 Ambiguity: Enemy Number One

Consider the requirement:

> "The user can reset their password."

It seems clear. But a real spec needs to eliminate all of these questions:

- Through which channel? (email, SMS, security questions?)
- Does the reset link expire? After how long?
- Can it be used more than once?
- What's the strength policy for the new password?
- Can the old password be reused?
- What happens to active sessions after the change?
- What if the email doesn't exist in the system — does it reveal that or not (a security concern)?
- Is there an attempt limit (rate limiting)?

Each unanswered question is a decision the AI will make on its own — probably differently from what you wanted. **Specifying is, in large part, the act of anticipating and answering those questions before they become bugs.**

### 5.4 Specific, Measurable, and the "etc." Trap

Avoid the word **"etc."** and its cousins ("and so on," "among others," "things like that"). They are black holes of ambiguity. If there's a list, **list everything**. If the list is open-ended, **state the rule** that defines the list, not examples followed by "etc."

❌ "Validate the required fields: name, email, etc."
✅ "Validate the required fields: name (1–100 characters), email (RFC 5322 format), tax ID (11 digits, check-digit validation)."

---

## Chapter 6 — The Components of a Spec

A complete SDD-style specification usually contains the sections below. Not every spec needs all of them — small slices use a subset — but this is the full menu.

### 6.1 Header / Metadata

```markdown
---
title: Password Reset
id: SPEC-AUTH-014
status: approved
author: Elton
date: 2026-06-08
version: 1.2
---
```

Metadata gives traceability. The `id` lets you reference the spec in commits, tests, and code.

### 6.2 Overview

Two or three paragraphs answering: *What is this? For whom? What problem does it solve? Why now?* It gives the **why** — the context that prevents the AI (and humans) from optimizing for the wrong thing.

### 6.3 Goals & Non-Goals

- **Goals:** what this feature aims to achieve.
- **Non-goals (Out of scope):** what it explicitly *does not* do.

The **non-goals section is one of the most important and most neglected.** It prevents *scope creep* and stops the AI from "helping too much" by implementing things you didn't ask for. Saying "this feature does NOT handle two-factor authentication" is as valuable as saying what it does.

### 6.4 Functional Requirements (FR)

The heart of the spec. *What* the system does. Each requirement gets an ID and is written in a testable way.

```markdown
- **FR-01:** The system must allow the user to request a password reset
  by providing their registered email.
- **FR-02:** Upon receiving the request, the system must send an email containing
  a unique reset link valid for 30 minutes.
- **FR-03:** The reset link must be single-use; after the first successful use,
  it must be invalidated.
- **FR-04:** For security reasons, the system must display the same confirmation
  message ("If the email exists, we'll send instructions") regardless of whether
  the email exists in the database.
```

### 6.5 Non-Functional Requirements (NFR)

The system's **qualities**: performance, security, accessibility, scalability, availability, legal compliance.

```markdown
- **NFR-01 (Performance):** The request endpoint must respond within 300ms (p95).
- **NFR-02 (Security):** Maximum of 5 requests per email per hour (rate limiting).
- **NFR-03 (Security):** The reset token must have at least 256 bits of entropy.
- **NFR-04 (Compliance):** Logs must not record the token or the new password (GDPR/LGPD).
```

NFRs are often forgotten and are where real systems fail. The AI won't guess your SLA or your data-protection requirement — you have to say it.

### 6.6 Business Rules (BR)

Domain logic that governs behavior, independent of screen or technology.

```markdown
- **BR-01:** The new password cannot be the same as any of the last 5 passwords used.
- **BR-02:** The new password must have at least 12 characters, with at least one
  uppercase letter, one lowercase letter, one number, and one symbol.
```

### 6.7 User Stories

Narrative format connecting the requirement to human value:

```markdown
**As** a user who forgot their password,
**I want** to reset it from my email,
**so that** I can recover access to my account without contacting support.
```

### 6.8 Acceptance Criteria

The most important part for verification. Written in **Given/When/Then**. They are, in practice, the specification of the tests.

```gherkin
Scenario: Request with a valid email
  Given a registered user with the email "ana@example.com"
  When she requests a password reset for that email
  Then an email with a reset link must be sent
  And the link must expire in 30 minutes

Scenario: Expired link
  Given a reset link generated more than 30 minutes ago
  When the user tries to access it
  Then the system must refuse the reset
  And display the message "Link expired. Request a new one."

Scenario: Link reuse
  Given a reset link already used successfully
  When the user tries to use it again
  Then the system must refuse with the message "Invalid link."
```

### 6.9 Data Model / Entities

When relevant, describe the entities, their fields, types, and relations.

```markdown
**Entity: ResetToken**
- id: UUID
- userId: UUID (FK → User)
- tokenHash: string (hash of the token, never the token in plaintext)
- createdAt: timestamp
- expiresAt: timestamp
- usedAt: timestamp | null
```

### 6.10 API Contracts / Interfaces

Endpoints, parameters, responses, status codes.

```markdown
**POST /auth/password-reset/request**
Request: { "email": "string" }
Response 202: { "message": "If the email exists, we'll send instructions." }
Response 429: { "error": "Too many attempts. Try again later." }
```

### 6.11 Edge Cases and Errors

The section that separates amateur specs from professional ones. *What happens when something goes wrong?*

```markdown
- Malformed email → 400 with a validation message.
- Email service unavailable → queue for retry; don't fail the user's request.
- User requests 10 resets in a row → block after 5 (NFR-02).
- Tampered/invalid token → treat as an invalid link, leaking no information.
```

### 6.12 Dependencies and Constraints

External systems, mandatory libraries, stack constraints, decisions already made.

### 6.13 Risks and Open Decisions

Points that still need a human decision, with options and a recommendation. Honesty about what isn't resolved yet keeps the AI from "inventing" an answer.

---

## Chapter 7 — Levels of Specification

Not every spec is the same size. SDD operates at different levels of granularity, forming a hierarchy.

### 7.1 The Spec Pyramid

```
        ┌─────────────────┐
        │     VISION       │  Why the product exists (1 doc, rarely changes)
        ├─────────────────┤
        │   PRD / EPIC     │  A large set of features
        ├─────────────────┤
        │  FEATURE SPEC    │  A cohesive feature (the most common level)
        ├─────────────────┤
        │   TASK SPEC      │  A slice implementable in one session
        └─────────────────┘
```

- **Vision / Product Charter:** rarely changes. Defines the north star.
- **PRD (Product Requirements Document):** describes an epic or an entire product at a high level.
- **Feature Spec:** the most common level of work. A complete feature, with FR, NFR, acceptance criteria.
- **Task Spec:** a small slice, sized for a single work session with the AI. This is what effectively becomes a generation *prompt*.

### 7.2 Decomposition: Top-Down

The natural flow is to decompose from the general to the specific:

```
VISION
  └─► PRD: "Complete authentication system"
        ├─► FEATURE: "Login with email and password"
        ├─► FEATURE: "Password reset"   ◄── our example spec
        │     ├─► TASK: "Reset-request endpoint"
        │     ├─► TASK: "Email sending with token"
        │     └─► TASK: "New-password confirmation endpoint"
        └─► FEATURE: "Two-factor authentication"
```

Each lower level inherits the context of the one above. The task spec doesn't need to repeat the product vision — it references it (`see PRD-AUTH`, `see SPEC-AUTH-014`).

### 7.3 The Ideal Slice Size

A good heuristic: **a task spec should be small enough for the AI to implement and for you to validate in a single work session**, and large enough to deliver something coherent and testable.

Good slices have:
- A single, clear goal.
- Verifiable acceptance criteria.
- Few dependencies on things not yet built.
- A "Definition of Done" (DoD) that is machine-checkable wherever possible.

---

## Chapter 8 — The Language of Specification

### 8.1 Structured Natural Language

SDD doesn't use a formal programming language for specs. It uses **structured natural language**: clear English (or any language), organized into sections, with lists, IDs, and predictable formats like Given/When/Then.

The choice is deliberate: natural language is accessible to all stakeholders (business, design, QA, legal), and LLMs were trained precisely to understand it. Trying to invent an overly formal "spec language" loses both benefits.

### 8.2 Words With Weight: The RFC 2119 Vocabulary

A valuable convention, borrowed from the internet RFCs, is to use keywords with precise meaning:

- **MUST / REQUIRED:** an absolute requirement.
- **MUST NOT:** an absolute prohibition.
- **SHOULD / RECOMMENDED:** a strong recommendation, but justifiable exceptions exist.
- **MAY / OPTIONAL:** truly optional.

Using "must" for everything dilutes the signal. Reserving "MUST" for what's truly non-negotiable and "MAY" for what's flexible gives the AI (and humans) a clear hierarchy of priorities.

### 8.3 Active Voice, Explicit Subject

❌ "The password will be validated." (By whom? When?)
✅ "The server MUST validate the password against policy BR-02 before persisting."

Passive voice hides the actor and the timing. In a spec, both matter.

### 8.4 Examples Are Worth More Than Prose

Whenever a rule is subtle, **include a concrete example**:

> **BR:** The progressive discount is 5% above $100, 10% above $500, 15% above $1000.
>
> **Examples:**
> - $80 → no discount → $80.00
> - $100 → no discount (the rule is *above*) → $100.00
> - $100.01 → 5% → $95.01
> - $600 → 10% → $540.00

The boundary example (`$100` vs. `$100.01`) eliminates the classic ambiguity of "above" meaning `>` or `>=`. A single example settles what paragraphs of prose would leave open.

### 8.5 Tables for Combinatorial Rules

When behavior depends on combinations of conditions, use a **decision table**:

| Logged in? | In stock? | Result |
|------------|-----------|--------|
| No | — | Redirect to login |
| Yes | Yes | Add to cart |
| Yes | No | Show "Notify me when available" |

Tables make it impossible to forget a combination — and a missing row becomes an obvious question.

---

---

# PART III — THE WORKFLOW

---

## Chapter 9 — The SDD Lifecycle

### 9.1 The Five Phases

SDD, in practice, unfolds in five phases that form a cycle:

```
   ┌──────────────────────────────────────────────┐
   │                                               │
   ▼                                               │
1. DISCOVERY  →  2. SPECIFICATION  →  3. PLAN  →  4. GENERATION  →  5. VALIDATION
  (understand)     (write the spec)   (decompose)  (AI codes)        (verify)
                                                                        │
                          feedback refines the spec ◄───────────────────┘
```

1. **Discovery:** understand the problem, gather requirements, eliminate ambiguity.
2. **Specification:** turn the understanding into a structured spec.
3. **Plan:** decompose the spec into ordered, implementable tasks.
4. **Generation:** the AI produces the code (and tests) from the specs/tasks.
5. **Validation:** verify that the generated code fulfills the spec; whatever fails comes back as feedback.

### 9.2 It's a Loop, Not a Line

Despite the diagram, this is **not waterfall**. Each small slice runs through the whole cycle quickly. You don't write the entire product spec before generating anything. You:

1. Specify a feature.
2. Generate and validate.
3. Learn something.
4. Go back and adjust the spec (or move on to the next feature).

The feedback loop is short — often measured in hours, not months.

### 9.3 Who Does What

| Phase | Human role | AI role |
|-------|------------|---------|
| Discovery | Leads, decides | Interviews, suggests, surfaces gaps |
| Specification | Approves, refines | Drafts, structures |
| Plan | Approves priorities | Decomposes, orders, estimates |
| Generation | Supervises | **Does the bulk of the work** |
| Validation | Judges what matters | Runs tests, generates reports |

The human climbs the value chain: from code typist to **director of intent and judge of quality**.

---

## Chapter 10 — From Intent to Specification (Discovery)

### 10.1 Raw Intent

It all starts with a vague intent in someone's head:

> "I need users to be able to recover their password."

This sentence is the starting point — and it's full of holes. The discovery phase is the process of **turning vague intent into complete understanding**.

### 10.2 The Interview Technique (Grilling)

A powerful SDD technique is to let the AI **interview you** before it writes the spec. Instead of you trying to guess everything, the AI asks targeted questions, one decision at a time, often already suggesting a recommended answer for you to simply confirm.

Example discovery dialogue:

> **AI:** Through which channel does the user receive the reset? I recommend email (most common, cheaper than SMS). Confirm?
> **You:** Yes, email.
> **AI:** Should the link expire? I recommend 30 minutes (balance of security and convenience). Confirm?
> **You:** Make it 1 hour.
> **AI:** When an email doesn't exist, should we reveal that it doesn't? I recommend NOT revealing it (prevents account enumeration — a security best practice). Confirm?
> **You:** Confirmed.

Each question closes a gap that would have become a bug. By the end, there's **shared understanding** — and the spec practically writes itself.

### 10.3 The Question Categories That Can't Be Missing

A complete discovery covers, at minimum:

- **Actors:** who uses it? Which profiles/permissions?
- **Happy path:** what's the main route when everything goes right?
- **Alternative flows:** what variations exist?
- **Error cases:** what can go wrong and what to do in each case?
- **Business rules:** what domain logic governs this?
- **Data:** what's stored, for how long, with what sensitivity?
- **Non-functional:** performance, security, scale, compliance.
- **Boundaries:** what's explicitly out of scope?
- **Integrations:** what depends on external systems?

### 10.4 When to Explore Instead of Asking

In existing systems, many questions have answers in the code itself. SDD best practice: **if a question can be answered by looking at the code, look at the code** instead of asking the human. Reserve questions for what only the person knows — business decisions, priorities, intent.

---

## Chapter 11 — From Specification to Plan

### 11.1 Why Separate Spec From Plan

The **spec** says *what* must exist. The **plan** says *in what order* to build and *how* to divide the work. Mixing them overloads both. Separating them lets the spec stay stable while the plan adapts to the reality of execution.

### 11.2 Decomposition Into Tasks

From the feature spec, the plan breaks the work into implementable tasks. For "Password Reset":

```markdown
## Sprint 1 — Password Reset

- [ ] T-01: Model and migration for the ResetToken entity  (DoD: table created, migration tests pass)
- [ ] T-02: POST /request endpoint  (DoD: FR-01, FR-04 covered by tests; rate limit NFR-02 tested)
- [ ] T-03: Email sending service with token  (DoD: token hashed, 30-min expiry, queue test)
- [ ] T-04: POST /confirm endpoint  (DoD: FR-03 single-use, BR-01 and BR-02 validated)
- [ ] T-05: Invalidate active sessions after change  (DoD: "old sessions" acceptance criterion passes)
```

### 11.3 Ordering by Dependency

Tasks are ordered so that each depends only on things already built. You can't test the confirmation endpoint (T-04) without first having the model (T-01) and token generation (T-03). The plan respects that dependency graph.

### 11.4 The Machine-Checkable Definition of Done (DoD)

Each task carries a **Definition of Done** — and the best DoD is **machine-checkable**:

❌ Bad DoD: "Endpoint working well."
✅ Good DoD: "Endpoint returns 202 for a valid email, 429 after 5 attempts/hour; coverage ≥ 85%; acceptance scenario tests C-01 and C-04 pass."

A machine-checkable DoD lets validation be automated — and removes the subjectivity of "is it done?"

---

## Chapter 12 — From Plan to Code (Generation)

### 12.1 The Prompt Is the Spec

In the generation phase, the specification (or the task spec) **is the prompt**. You don't improvise a vague request in chat. You hand the AI the structured context:

```
Context: [reference to feature spec SPEC-AUTH-014 and PRD-AUTH]
Stack: [language, framework, versions, project patterns]
Task: T-02 — POST /request endpoint
Requirements: FR-01, FR-04, NFR-01, NFR-02
Acceptance criteria: [relevant Given/When/Then scenarios]
Definition of Done: [the checkable DoD]
Constraints: [don't log the token; follow the project's error pattern]
```

The richer the spec, the better the code. The effort invested in the specification **pays back with interest** in generation quality.

### 12.2 Generating Tests From Acceptance Criteria

One of SDD's greatest powers: the Given/When/Then acceptance criteria **map almost 1:1 to automated tests**. The AI can generate the tests first (from the criteria) and then the code that satisfies them — automated TDD, derived from the spec.

```
Acceptance criterion C-02 (Expired link)
        │  generates
        ▼
Automated test: test_expired_link_refuses_reset()
        │  drives
        ▼
Code that makes the test pass
```

### 12.3 Stack and Patterns: The Context the AI Needs

The AI generates better code when it knows the project's conventions: the language, the framework and version, the architectural patterns, the preferred libraries, the error-handling style. In mature SDD, this stack context is **injected automatically** into every generation, so the new code is indistinguishable from the existing code — same aesthetics, same idioms, same patterns.

### 12.4 Multiple Attempts and the Judge Panel

For critical tasks, an advanced technique is to generate **several independent solutions** (from different angles) and use a panel of "judges" (other AI instances, or automated criteria) to pick the best, synthesizing the good ideas from each. This trades compute cost for confidence in the result — appropriate when an error is expensive.

---

## Chapter 13 — Validation and the Feedback Loop

### 13.1 To Validate Is to Compare Against the Spec

Validation in SDD has one central, objective question:

> **Does the generated code fulfill the specification?**

Because the spec contains verifiable acceptance criteria and a checkable DoD, that question has an objective answer — it's not an opinion. This is radically different from the "looks good to me" of vibe coding.

### 13.2 The Layers of Validation

Complete validation operates in layers:

1. **Automated tests:** the acceptance criteria became tests; do they pass?
2. **Coverage and mutation:** how much of the code is exercised by the tests? Do the tests detect behavior changes (mutation score)?
3. **Static analysis:** linters, bug detectors, security scanners.
4. **Security and compliance:** OWASP, dependency vulnerabilities, GDPR/LGPD.
5. **Design review:** is the structure cohesive? Is coupling acceptable? (human + AI judgment)
6. **Functional / integration validation:** do front and back talk to each other? Does the real flow work end to end?

### 13.3 The Quality Gate

Many SDD flows institute a **quality gate**: a set of mandatory checks that must pass before a task is considered complete. Example gate criteria:

- Test suite 100% green.
- Coverage ≥ a threshold (e.g., 85%).
- Mutation score ≥ a threshold (e.g., 70%).
- Zero critical/high vulnerabilities.
- Zero critical static-analysis violations.

An important governance principle: **whoever wrote the code is not the only one who approves it.** Independent vetoes (design, verification, security) prevent errors from slipping through on the author's overconfidence.

### 13.4 Closing the Loop

When validation fails, the result is not frustration — it's **information**. The failure points to:

- A bug in the implementation → regenerate/fix the code.
- **Or a gap in the spec** → the code did exactly what the spec said, but the spec was wrong or incomplete.

The second case is the most valuable. Every validation failure that reveals a spec gap **makes the spec better**. Over time, the spec converges toward a complete and correct description of the system. **The system improves because its source of truth improves.**

```
Validation fails
   │
   ├─► Is it a code bug?  → fix the code, keep the spec
   │
   └─► Is it a spec gap?  → fix the SPEC, then regenerate the code
                            (the source of truth got stronger)
```

---

---

# PART IV — PRACTICE

---

## Chapter 14 — Writing Your First Spec

### 14.1 A Complete Example, From Scratch

Let's build an entire spec for a simple feature: **"URL Shortener."** Follow the evolution from raw intent to a finished spec.

**Step 0 — Raw intent:**
> "I want a URL shortener."

**Step 1 — Discovery (questions and answers):**
- Do shortened URLs expire? → Yes, optionally; default no expiration.
- Is the code random or customizable? → Random by default; optional custom alias.
- Is login required to shorten? → No to shorten; yes to view stats.
- Does it count clicks? → Yes, total clicks per link.
- Code length? → 7 alphanumeric characters.
- What about an invalid URL? → Reject with 400.
- What if the custom alias already exists? → Reject with 409.

**Step 2 — The resulting spec:**

```markdown
---
title: URL Shortener
id: SPEC-URL-001
status: draft
version: 1.0
---

## Overview
A service that turns long URLs into shareable short codes, redirects
visitors to the original URL, and counts accesses.
Audience: general users (shortening) and link owners (stats).

## Goals
- Shorten a long URL into a 7-character code.
- Redirect the short code to the original URL.
- Count the total accesses per link.

## Non-Goals (Out of Scope)
- Does NOT offer advanced analytics (geolocation, device).
- Does NOT offer QR codes (planned for v2).
- Does NOT offer custom domains.

## Functional Requirements
- FR-01: The system MUST generate a unique 7-character alphanumeric code
  [a-zA-Z0-9] for each shortened URL.
- FR-02: The system MUST validate that the input URL is a well-formed
  HTTP/HTTPS URL; otherwise, reject with HTTP 400.
- FR-03: The system MAY accept a custom alias; if it already exists,
  reject with HTTP 409.
- FR-04: When /{code} is accessed, the system MUST redirect (HTTP 301)
  to the original URL and increment the access counter.
- FR-05: Access to a nonexistent code MUST return HTTP 404.

## Non-Functional Requirements
- NFR-01 (Performance): Redirection MUST respond within 50ms (p95).
- NFR-02 (Security): Input URLs MUST be checked against a list of known
  malicious domains before being accepted.
- NFR-03 (Scale): The system MUST support 1000 redirects/second.

## Business Rules
- BR-01: Codes are case-sensitive ("abc" ≠ "Abc").
- BR-02: The same long URL shortened twice produces two different codes
  (no deduplication).

## Acceptance Criteria
Scenario: Shorten a valid URL
  Given a URL "https://example.com/a-very-long-page"
  When the user shortens it
  Then they receive a code of exactly 7 alphanumeric characters

Scenario: Invalid URL
  Given an input "this is not a url"
  When the user tries to shorten it
  Then the system responds HTTP 400 with a validation message

Scenario: Redirect and count
  Given a code "aB3xY9z" pointing to "https://example.com"
  When someone accesses "/aB3xY9z"
  Then they are redirected (301) to "https://example.com"
  And that link's access counter increases by 1

Scenario: Alias already exists
  Given the alias "promo" is already in use
  When a user tries to create the alias "promo" again
  Then the system responds HTTP 409

## Data Model
Entity: Link
- code: string(7), PK
- originalUrl: string, required
- createdAt: timestamp
- accesses: integer, default 0
- alias: boolean (whether it was customized)

## Edge Cases
- URL longer than 2048 characters → reject 400.
- Random code collision → regenerate until a unique code is obtained.
- Concurrent access to the counter → atomic increment.
```

Note how each discovery decision became a numbered, testable requirement. This spec can be handed to an AI (or a human developer) and produce a correct implementation.

### 14.2 The Beginner's Mistakes

When writing your first spec, avoid:

1. **Specifying the implementation** ("use a HashMap") instead of the behavior.
2. **Forgetting the error cases** (describing only the happy path).
3. **Vague acceptance criteria** ("must work well").
4. **Omitting the non-functionals** (security, performance).
5. **Not defining the negative scope** (what it does NOT do).
6. **Using "etc."** and open-ended lists.
7. **Boundary ambiguity** ("above" without saying whether the limit is included).

---

## Chapter 15 — Patterns and Anti-Patterns

### 15.1 Patterns That Work

**Pattern: Small, iterative spec.** Specify a slice, generate, validate, learn, repeat. Don't try to specify the universe at once.

**Pattern: Boundary example.** For every rule with a numeric limit or condition, give the exact boundary example.

**Pattern: Explicit negative scope.** Always list what's out. Stops the AI from "helping too much."

**Pattern: IDs on everything.** FR-01, NFR-02, C-03. Enables traceability across spec, code, tests, and commits.

**Pattern: Acceptance criterion = test.** Write the criteria already thinking they'll become automated tests.

**Pattern: The spec is alive.** When reality changes, update the spec first, then the code. The spec can never lag behind the code.

**Pattern: Recorded decisions (ADR).** Important architectural decisions get their own record (see Ch. 19).

### 15.2 Anti-Patterns to Avoid

**Anti-pattern: The monster spec.** An 80-page document trying to foresee everything, frozen, that nobody reads. It's Waterfall in disguise. Prefer small, living specs.

**Anti-pattern: The retroactive spec.** Writing the spec *after* the code, just to "have documentation." Loses all the value — becomes dead documentation again.

**Anti-pattern: The spec that leaks implementation.** Filling the spec with code details ties the AI down and ages fast.

**Anti-pattern: Non-verifiable criteria.** "Must be intuitive," "must be fast," "must be secure" with no numbers and no scenarios.

**Anti-pattern: Blindly trusting generation.** Skipping validation because "the AI is good." The quality gate exists precisely because the AI errs in plausible, hard-to-notice ways.

**Anti-pattern: Spec and code diverge silently.** Someone fixes the code directly, without updating the spec. The source of truth rots. Discipline: change starts in the spec.

### 15.3 The Summary Table

| Do | Don't |
|----|-------|
| Small, living, iterative specs | Frozen monster spec |
| Describe behavior (the what) | Describe implementation (the how) |
| Verifiable criteria with numbers | "Must be good/fast/intuitive" |
| Explicit negative scope | Leave boundaries implicit |
| Update the spec before the code | Fix only the code and forget the spec |
| Validate against the spec | Blindly trust generation |
| IDs and traceability | "etc." and open-ended lists |

---

## Chapter 16 — Specifying for Existing Systems (Brownfield)

### 16.1 The Brownfield Challenge

Everything up to here assumed a *greenfield* scenario (new project). But most software is *brownfield*: systems that already exist, with legacy code, no specs, with business rules hidden in the code itself.

Applying SDD to brownfield requires a different strategy: **specification by archaeology**.

### 16.2 Reverse-Engineering Specs

Instead of writing the spec before the code, you:

1. **Read the existing code** (or ask the AI to read it) to extract the current behavior.
2. **Document the observed behavior** as a descriptive spec ("the system *today* does X").
3. **Identify the desired behavior** ("the system *should* do Y").
4. **The gap between the two becomes the work** to be done.

The AI is especially useful here: it can sweep thousands of lines and produce a summary of what the code does, which you then validate and turn into a spec.

### 16.3 Specs as a Safety Net for Changes

Before changing a legacy system, writing the spec of its *current* behavior — and generating tests from it — creates a **safety net**. You capture the existing behavior in tests (characterization), and can then refactor or change with confidence, knowing any unintended break will be detected.

```
Legacy code with no tests
   │  1. AI reads and describes the current behavior
   ▼
Descriptive spec ("how it is today")
   │  2. generates characterization tests
   ▼
Safety net (tests that lock in the current behavior)
   │  3. now it's safe to change
   ▼
Prescriptive spec ("how it should be")  →  regenerate/change with confidence
```

### 16.4 Incremental Strategy

Don't try to specify the entire legacy system at once. Specify **the slice you're about to change**. Over time, the system's most active areas gain specs, while the stable, untouched parts can wait. Spec coverage grows organically, following the real work.

---

## Chapter 17 — Tools and Ecosystem

### 17.1 What an SDD Tool Does

SDD can be practiced with nothing more than Markdown files and an AI assistant. But dedicated tools amplify the power, offering:

- **Standardized spec templates.**
- **Formalized phases** (discovery → spec → plan → generation → validation).
- **Automatic context injection** (stack, project patterns).
- **Test generation** from acceptance criteria.
- **Automated quality gates.**
- **Traceability** across spec, code, and commits.
- **Orchestration of multiple specialized agents** (one for backend, one for tests, one for security, etc.).

### 17.2 The Ecosystem in 2026

The field has matured rapidly. Approaches and tools have emerged that formalize the SDD flow — from open frameworks that structure the "specify → plan → implement" cycle, to internal productivity kits that chain specialized agents under a plan generated from the spec. IDE-integrated code assistants have incorporated planning modes that explicitly separate the specification/plan phase from the execution phase.

The common denominator of all these tools is the central principle of this book: **the spec comes first, the code derives from it, and validation closes the loop.**

### 17.3 Markdown: The Honest Format

The overwhelming majority of specs in SDD live in **Markdown**. The reasons:

- Readable by humans and machines.
- Versions well in Git (clean diffs).
- Requires no proprietary tool.
- LLMs understand it natively.
- Supports structure (headers, lists, tables, code blocks) without ceremony.

A Markdown spec, versioned alongside the code in the same repository, is the state of the art of simplicity — and it works.

### 17.4 Versioning: The Spec Lives in the Repository

Principle: **the spec lives in the same repository as the code it describes.** This ensures that:
- Spec and code evolve together, in the same commit/PR.
- The Git history records the evolution of intent, not just of code.
- Whoever clones the project gets the source of truth too.

---

---

# PART V — MATURITY AND SCALE

---

## Chapter 18 — SDD in Teams

### 18.1 The Spec as a Common Language

In a team, the spec becomes the **interface between roles**. Product Owner, designer, developer, QA, and even legal can read and contribute to the same spec, because it's in structured natural language — not in code that only devs understand.

This solves an old problem: the "telephone game" between what the business wants, what the PO writes in the ticket, what the dev understands, and what ends up being built. With the spec as a single source, everyone looks at the same artifact.

### 18.2 Spec Review

Just as *code review* exists, in mature SDD there's **spec review**. Reviewing the spec *before* generation is far cheaper than reviewing the code *after*:

- An error caught in the spec costs minutes to fix.
- The same error caught after the code is generated costs the regeneration plus another review.
- The same error caught in production costs an incident.

> **Shifting defect detection to the left** (to the spec phase) is the central economic gain of SDD in a team.

### 18.3 Roles in an SDD Team

SDD doesn't eliminate roles — it reallocates them to higher levels of abstraction:

- **Product Owner / Business Analyst:** owner of the *what* and the *why*; writes and prioritizes feature specs.
- **Architect / Tech Lead:** owner of structural decisions; reviews specs through the lens of design and feasibility.
- **Developer:** owner of generation and validation; turns specs into verified code, supervises the AI, fixes what fails.
- **QA / Test Engineer:** owner of verification; ensures the acceptance criteria are sufficient and the tests prove something.
- **Security:** owner of the security requirements and the veto over vulnerabilities.

### 18.4 Parallelism: Many Slices, Many Agents

Because each task spec is self-contained (it carries its own context and criteria), several can be generated **in parallel** — whether by several people or by several orchestrated AI agents. A well-decomposed spec is the key that unlocks parallelism without chaos: each slice has clear boundaries and doesn't step on the others.

---

## Chapter 19 — Governance, Traceability, and ADRs

### 19.1 Why Governance Matters

When the AI generates a large share of the code, the risk isn't speed — it's **losing the record of the why**. Why was this decision made? Who approved it? Under what context? Without governance, the system becomes a black box nobody understands six months later.

### 19.2 ADR — Architecture Decision Record

An **ADR (Architecture Decision Record)** is a short document capturing an important decision. Typical structure:

```markdown
# ADR-007: Use hashed tokens for password reset

## Status
Accepted — 2026-06-08

## Context
We need to store reset tokens. Storing them in plaintext would expose
all tokens in case of a database leak.

## Decision
Store only the HASH of the token (SHA-256). The plaintext token exists
only in the sent email and is never persisted.

## Consequences
- (+) A database leak does not compromise active tokens.
- (+) Compliance with security best practices / data-protection law.
- (-) Impossible to "resend the same token"; a new one is always generated.

## Alternatives considered
- Plaintext token with short expiry — rejected (leak risk).
- Reversible encryption — rejected (a hash is sufficient and simpler).
```

ADRs answer the future's golden question: *"why on earth was this done this way?"*

### 19.3 End-to-End Traceability

SDD governance aims for a traceable chain:

```
Business intent
   │
   ▼
PRD (PRD-AUTH)
   │
   ▼
Feature spec (SPEC-AUTH-014, requirement FR-03)
   │
   ▼
Recorded decision (ADR-007)
   │
   ▼
Plan task (T-04)
   │
   ▼
Commit / code (references SPEC-AUTH-014 FR-03)
   │
   ▼
Test (covers acceptance criterion C-03)
```

With IDs on each link, you can navigate from the code back to the original intent — and from intent to where it was implemented and tested. This is gold for auditing, maintenance, and onboarding.

### 19.4 The Project's "Brain"

An advanced practice is to keep a **living historical record** of the project: a journal of decisions, delivered features, fixed bugs, accepted technical debt. This project "brain" — often a set of interlinked notes — preserves the context normally lost when people leave the team or as time passes. In SDD, where the AI takes part in generation, having this context recorded and retrievable is what keeps the system comprehensible.

---

## Chapter 20 — Quality, Testing, and the Quality Gate

### 20.1 Quality Is Not Negotiable

A legitimate fear about AI programming: "it'll generate a lot of bad code, fast." SDD's answer is to make **quality a mandatory gate**, not an aspiration. Nothing advances without proof.

### 20.2 The Test Pyramid in SDD

SDD doesn't abandon the classic test pyramid — it *feeds* it:

```
        /\
       /E2E\        Few: complete end-to-end flows
      /------\
     / Integ. \     Some: modules talking (front↔back, DB)
    /----------\
   /    Unit    \   Many: business rules in isolation
  /--------------\
```

Because the acceptance criteria already describe behaviors at multiple levels, the AI can generate tests at every layer — and the gate verifies the pyramid has the right shape (many unit, some integration, few E2E).

### 20.3 Metrics the Gate Verifies

A rigorous quality gate checks, among others:

- **Test coverage** — what % of the code is exercised (e.g., ≥ 85%).
- **Mutation score** — do the tests really detect behavior changes, or do they just "pass for the sake of passing"? (e.g., ≥ 70%). This metric is crucial: high coverage with weak tests is a false sense of security; mutation exposes that.
- **Static analysis** — likely bugs, *code smells*, complexity.
- **Security** — OWASP Top 10, vulnerable dependencies, leaked secrets.
- **Accessibility** — for front-ends (e.g., WCAG 2.2 AA).
- **Performance** — latency/load budgets when there's an SLA.

### 20.4 Independent Vetoes

A governance principle already mentioned, worth reinforcing: **whoever writes is not who approves alone.** In mature SDD flows, there are independent vetoes:

- **Design veto:** is the structure sound?
- **Verification veto:** do the tests really prove something?
- **Security veto:** is there a critical vulnerability?

Any veto blocks the delivery and sends it back. This prevents enthusiasm (or overconfidence in the AI) from letting through problems that "seemed okay."

### 20.5 Adversarial Verification

An advanced validation technique: instead of asking the AI "is this correct?", ask "**try to prove this is wrong**." Multiple verifiers, each trying to refute a claim from a different angle (correctness, security, reproducibility), catch errors that naive verification would let through. Diversity of perspective catches failures that redundancy doesn't.

---

## Chapter 21 — The Future of SDD

### 21.1 The Spec as the New Source Code

The trajectory points toward a world where the **specification is the artifact that matters**, and the code is a compilation detail — generatable, disposable, regeneratable. Just as almost nobody writes assembly by hand today (we let the compiler translate a high-level language), tomorrow perhaps few will write application code by hand: we'll write specs, and the AI will "compile" specs into code.

In this vision, **the spec is the new high-level code, and today's programming language is the new assembly.**

### 21.2 What Doesn't Change

Despite the revolution in tooling, the core remains the same age-old problem: **understanding the problem clearly enough to solve it.** SDD doesn't eliminate the hard part of software engineering — it *isolates it and makes it central*. The hard part was always thinking precisely; typing the code was the easy part. SDD finally acknowledges this and organizes the work around the part that matters.

### 21.3 The Skills That Gain Value

In the SDD world, value accrues to:

- **Structured thinking and problem decomposition.**
- **Precise communication** (writing without ambiguity is a superpower).
- **Domain modeling** (deeply understanding the business).
- **Critical thinking and skepticism** (judging what the AI produced).
- **Systems thinking** (understanding how the pieces fit together).

And relative value is lost by syntax memorization, manual *boilerplate*, and the mechanical typing of repetitive patterns.

### 21.4 The Risk to Watch

SDD's biggest risk isn't technical — it's **spec atrophy**. The temptation to slide back into vibe coding ("it's just a quick thing") is constant. Every time the spec is skipped "just this once," invisible debt accumulates. The discipline of specifying first is exactly that: a discipline. Like all discipline, it only works when practiced even (especially) when it seems unnecessary.

### 21.5 Final Word

Spec-Driven Development is neither a tool nor a fad. It's a **repositioning of the intellectual work of software engineering**: from the *how* to the *what*, from code to intent, from typing to thinking, from opinion to verification.

AI made cheap the part that was expensive (writing code) and, in doing so, made expensive the part that was always hard but that we managed to hide (thinking clearly). SDD is the methodology that faces this new reality head-on and turns it into an advantage.

> **Write the spec. Let the machine write the code. Verify relentlessly. Refine the source of truth. Repeat.**
>
> That's the cycle. That's the craft. That's Spec-Driven Development.

---

---

# APPENDICES

---

## Appendix A — Ready-to-Use Templates

### A.1 Feature Spec Template

```markdown
---
title: <Feature Name>
id: SPEC-<AREA>-<NNN>
status: draft | in-review | approved
author: <name>
date: <YYYY-MM-DD>
version: 1.0
---

## Overview
<2-3 paragraphs: what, for whom, what problem, why>

## Goals
- <goal 1>
- <goal 2>

## Non-Goals (Out of Scope)
- Does NOT <explicitly excluded thing>

## Functional Requirements
- FR-01: The system MUST <testable behavior>.
- FR-02: ...

## Non-Functional Requirements
- NFR-01 (Performance): ...
- NFR-02 (Security): ...

## Business Rules
- BR-01: ...

## User Stories
As <actor>, I want <action>, so that <value>.

## Acceptance Criteria
Scenario: <name>
  Given <context>
  When <action>
  Then <expected result>

## Data Model
Entity: <Name>
- <field>: <type>, <constraints>

## API Contracts
<METHOD> <route>
Request: { ... }
Response <code>: { ... }

## Edge Cases and Errors
- <condition> → <behavior>

## Dependencies and Constraints
- <dependency>

## Risks and Open Decisions
- <unanswered question + options + recommendation>
```

### A.2 Acceptance Criterion Template (Given/When/Then)

```gherkin
Scenario: <short scenario description>
  Given <the initial state/context>
  And <additional context, if any>
  When <the action that triggers the behavior>
  Then <the expected observable result>
  And <additional result, if any>
```

### A.3 ADR Template

```markdown
# ADR-<NNN>: <Decision title>

## Status
<Proposed | Accepted | Superseded by ADR-XXX> — <date>

## Context
<What is the situation forcing a decision?>

## Decision
<What was decided, in active voice: "We will use X">

## Consequences
- (+) <positive consequence>
- (-) <negative consequence / trade-off>

## Alternatives considered
- <alternative> — <why it was rejected>
```

### A.4 Task Template With DoD

```markdown
- [ ] T-<NN>: <task description>
      Requirements: <FR-xx, NFR-xx>
      Acceptance criteria: <C-xx>
      DoD (checkable): <objective, measurable "done" conditions>
      Depends on: <T-xx>
```

---

## Appendix B — Glossary

- **SDD (Spec-Driven Development):** specification-guided development; the spec is the source of truth and the code derives from it.
- **Spec (Specification):** a structured document describing what the software must do, why, and under what correctness criteria.
- **Vibe coding:** AI programming guided by feel/conversation, with no spec; fast for prototypes, fragile for real software.
- **PRD (Product Requirements Document):** a high-level product requirements document.
- **FR / NFR / BR:** Functional Requirement / Non-Functional Requirement / Business Rule.
- **Acceptance Criterion:** a verifiable condition defining when a requirement is fulfilled; often in Given/When/Then.
- **Given/When/Then:** a BDD format for describing behavior in a testable way.
- **DoD (Definition of Done):** the set of objective conditions for considering a task complete.
- **ADR (Architecture Decision Record):** a short record of an architectural decision, with context, decision, and consequences.
- **Quality gate:** a gate of mandatory checks that blocks delivery if anything fails.
- **Test coverage:** the percentage of code exercised by the tests.
- **Mutation score:** measures whether the tests actually detect behavior changes (test quality, not just quantity).
- **Greenfield / Brownfield:** a brand-new project / an existing legacy system.
- **Ubiquitous language:** the shared vocabulary between business and tech (from DDD).
- **Shift-left:** moving defect detection to the early phases (e.g., reviewing the spec instead of the code).
- **Source of truth:** the authoritative artifact; in SDD, it's the spec.
- **Traceability:** the ability to link code → test → spec → decision → intent.
- **Adversarial verification:** validating by trying to refute the claim, from multiple angles.

---

## Appendix C — Checklists

### C.1 Spec Checklist (before generating code)

- [ ] The overview explains the *why*, not just the *what*.
- [ ] The goals are clear and there's a **non-goals** section.
- [ ] Every functional requirement has an ID and is testable.
- [ ] The non-functional requirements (performance, security, compliance) are present and have numbers.
- [ ] The business rules have boundary examples.
- [ ] There are Given/When/Then acceptance criteria for the main scenarios.
- [ ] The error and edge cases are covered (not just the happy path).
- [ ] There's no "etc." or open-ended list without a rule.
- [ ] There's no leakage of implementation details.
- [ ] The MUST/SHOULD/MAY words are used with intent.
- [ ] A competent stranger could build the right thing without asking.

### C.2 Plan Checklist

- [ ] The feature was decomposed into small, coherent tasks.
- [ ] The tasks are ordered by dependency.
- [ ] Each task has a machine-checkable DoD.
- [ ] Each task references the requirements/criteria it covers.

### C.3 Validation Checklist (quality gate)

- [ ] All acceptance criteria became tests and are green.
- [ ] Coverage ≥ the defined threshold.
- [ ] Mutation score ≥ the defined threshold.
- [ ] Zero critical/high vulnerabilities.
- [ ] Zero critical static-analysis violations.
- [ ] (Front) accessibility verified.
- [ ] Design review done by someone who didn't write the code.
- [ ] Failures that revealed gaps became spec updates.

---

## Appendix D — Further Reading and Conceptual References

SDD draws on several well-established traditions of software engineering. To deepen the foundations it rests on:

- **Test-Driven Development** — the idea that the executable specification (the test) comes before the code.
- **Behavior-Driven Development** — the Given/When/Then syntax and the business↔tech alignment.
- **Domain-Driven Design** — domain modeling and ubiquitous language, which give vocabulary to specs.
- **Architecture Decision Records** — the practice of recording decisions and their context.
- **The principles of RFCs (MUST/SHOULD/MAY keywords)** — the vocabulary of obligation.
- **"Shift-left" and quality practices** — moving defects to the left; coverage and mutation.
- **The emerging literature on prompt engineering and agentic flows** — how to structure context so LLMs generate reliable code.

> **How to continue:** the best way to learn SDD isn't to read more — it's to write a spec today, generate from it, validate, and feel firsthand where your spec was ambiguous. The first spec always has holes. By the tenth, it's instinct.

---

*End of book.*

**Spec-Driven Development — The Complete Book**
*Write the spec. Let the machine write the code. Verify relentlessly.*
