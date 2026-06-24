---
software_dev: core
---

# The Practice of Architecting - Complete Professional Guide

> **Category:** 03_design_and_architecture · **Language:** English

---

### Risk-driven design, decisions, and the architect's day-to-day craft
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches the practice of architecting from first principles. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** architecting is an **activity**, not a title — the ongoing work of making and communicating the decisions that shape a system. This guide covers risk-driven design (do just enough architecture), how to run design as a team, and recording decisions as ADRs. Current to 2026 collaborative practice.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | First architecture role | Part I |
| 2 — Intermediate | Leading design | Part II |

**Target audience:** senior engineers stepping into architecture, tech leads, and anyone responsible for cross-cutting design decisions.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes the quality-attribute and architecture-styles guides.

---

## Table of Contents

**Part I – The activity**
1. Architecting as risk-driven, just-enough design
2. Architecture Decision Records (ADRs)

**Part II – Collaboration**
3. Running design as a team activity

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – The activity

Architecting is not a phase you finish before coding; it is the continuous activity of identifying the decisions that matter, making them with enough (but not too much) analysis, and communicating them. The amount of architecture work should be **proportional to risk** — heavyweight up-front design for a low-risk CRUD app is as wrong as no design for a safety-critical system.

---

## Chapter 1 — Risk-driven, just-enough design

### 1.1 Introduction

**Risk-driven architecture** says: spend design effort where the **risk** is, and stop when the risk is acceptable. You identify what could derail the project (a scaling unknown, a tricky integration, a security exposure), apply design techniques to reduce exactly those risks, then build. This avoids both reckless under-design and wasteful big-up-front-design.

### 1.2 Business context

Design effort is a cost; its only justification is reducing risk that would otherwise cost more. Teams that over-architect burn budget modeling things that were never going to fail; teams that under-architect get blindsided by the one decision that was hard to reverse. Tying architecture effort to risk maximizes return — you invest analysis precisely where being wrong is expensive.

### 1.3 Theoretical concepts: risk as the guide

```mermaid
flowchart TB
    risks["List the risks<br/>(what could derail us?)"] --> prioritize["Prioritize by impact × uncertainty"]
    prioritize --> design["Apply design techniques to top risks"]
    design --> assess{"Risk acceptable?"}
    assess -- "no" --> design
    assess -- "yes" --> build["Stop designing; build"]
```

The loop: enumerate risks, prioritize, attack the worst with the cheapest effective technique (a spike, a prototype, a model, a review), and stop when remaining risk is acceptable. "How much architecture?" has a concrete answer: enough to bring risk below your threshold.

### 1.4 Architecture: technique matched to risk

```mermaid
flowchart LR
    r["A specific risk"] --> t{"Cheapest technique to reduce it?"}
    t --> spike["Spike / prototype"]
    t --> model["Model / diagram"]
    t --> review["Review / ATAM-lite"]
```

Different risks need different techniques: an unknown performance ceiling → a load-test spike; an unclear integration → a thin end-to-end prototype; a contested structure → a quick evaluation workshop. Pick the lightest technique that actually retires the risk.

### 1.5 Real example

**Scenario.** A team fears a new third-party payments integration might not meet latency needs.

**Problem.** They could spend weeks designing around a problem that might not exist — or ignore it and discover it in production.

**Solution.** A two-day spike: call the real API under expected load, measure. The result tells them whether to design for it.

**Implementation (the decision).**

```text
Risk: payments API latency may exceed our 300ms budget at peak.
Technique: timeboxed spike against sandbox under load.
Result: p99 = 180ms within budget -> risk retired; no extra architecture needed.
        (if it had failed: design async confirmation + queue.)
```

**Result.** A small, targeted experiment retired the risk; the team avoided both over-design and a production surprise.

**Future improvements.** Keep the spike as a load test in CI to catch regressions in the provider's latency.

### 1.6 Exercises

1. State the risk-driven rule for how much architecture to do.
2. Give two risks and the cheapest technique to reduce each.
3. When do you stop designing?

### 1.7 Challenges

- **Challenge.** For your current project, list the top three risks. For each, name the lightest technique that would meaningfully reduce it, and timebox one.

### 1.8 Checklist

- [ ] I size architecture effort to project risk.
- [ ] I enumerate and prioritize risks explicitly.
- [ ] I pick the lightest technique that retires a risk.
- [ ] I stop designing when risk is acceptable.

### 1.9 Best practices

- Make risks explicit and revisit them as the project evolves.
- Prefer cheap experiments (spikes/prototypes) over speculative design.
- Timebox design work against a risk, not a calendar.

### 1.10 Anti-patterns

- Big design up front for low-risk systems.
- No design at all for genuinely risky decisions.
- Modeling everything uniformly regardless of where risk concentrates.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Months of design, nothing built | Over-design / no risk focus | Switch to risk-driven, timeboxed work |
| Production surprise on a known-hard area | Risk ignored | Spike the risk before committing |
| Endless design debates | No risk framing | Frame each decision by the risk it reduces |

### 1.12 References

- M. Keeling, *Design It! From Programmer to Software Architect* (Pragmatic Bookshelf, 2017) — ISBN 978-1680502091.
- G. Fairbanks, *Just Enough Software Architecture* (Marshall & Brainerd, 2010) — ISBN 978-0984618101.

---

## Chapter 2 — Architecture Decision Records

### 2.1 Introduction

An **Architecture Decision Record (ADR)** is a short document capturing one significant decision: its **context**, the **decision**, and its **consequences**. ADRs make architecture **legible over time** — six months later, anyone can see *why* a choice was made, what alternatives were weighed, and what trade-offs were accepted. They are the cheapest high-value documentation an architect produces.

### 2.2 Business context

Undocumented decisions are re-litigated endlessly and accidentally reversed by people who didn't know the reasons. ADRs preserve rationale, so the team stops repeating debates, onboards faster, and changes decisions deliberately (with a new ADR superseding the old) rather than by accident. The cost is minutes per decision; the payoff is durable institutional memory.

### 2.3 Theoretical concepts: the minimal record

```mermaid
flowchart LR
    ctx["Context<br/>(forces, constraints)"] --> dec["Decision<br/>(what we chose)"]
    dec --> cons["Consequences<br/>(trade-offs, follow-ups)"]
    cons --> status["Status<br/>(proposed/accepted/superseded)"]
```

A good ADR is short (one page), immutable once accepted (you supersede rather than edit), numbered, and stored **in the repo** next to the code. Capturing the alternatives considered and why they lost is what makes it valuable later.

### 2.4 Architecture: ADRs live with the code

```mermaid
flowchart TB
    repo["repo/docs/adr/"] --> a1["0001-use-postgres.md (accepted)"]
    repo --> a2["0002-event-driven-billing.md (accepted)"]
    repo --> a3["0007-replace-0001-with-distributed-sql.md (supersedes 0001)"]
```

Keeping ADRs in version control ties each decision to the code state when it was made, and the supersede chain shows how thinking evolved.

### 2.5 Real example

**Scenario.** The team chooses PostgreSQL over a document database.

**Problem.** A year later, someone asks "why not Mongo?" and nobody remembers.

**Solution.** A one-page ADR recorded at decision time.

**Implementation (ADR template).**

```markdown
# 0001. Use PostgreSQL for the system of record
Status: Accepted
## Context
Strong relational integrity and ad-hoc queries are required; team knows SQL.
## Decision
Use PostgreSQL as the primary store, with JSONB for flexible sub-documents.
## Consequences
+ Transactions and constraints for free; mature tooling.
- Horizontal scaling needs planning later (revisit if write volume 10x).
Alternatives considered: MongoDB (rejected: weaker multi-document integrity).
```

**Result.** The "why not Mongo?" question is answered in 30 seconds by reading ADR-0001; if the decision changes, ADR-0007 supersedes it with new context.

**Future improvements.** Add an ADR index/README; lint PRs that make a big decision without an ADR.

### 2.6 Exercises

1. What three parts must every ADR have?
2. Why supersede an ADR instead of editing it?
3. Why store ADRs in the code repository?

### 2.7 Challenges

- **Challenge.** Write an ADR for a decision your team already made implicitly. Include the alternatives and why they lost. Share it and see if it settles a recurring debate.

### 2.8 Checklist

- [ ] Significant decisions get a short ADR.
- [ ] Each ADR records context, decision, consequences, status.
- [ ] ADRs are immutable; changes supersede them.
- [ ] ADRs live in version control.

### 2.9 Best practices

- Keep ADRs to one page; capture alternatives and trade-offs.
- Number them and maintain a supersede chain.
- Make "is there an ADR?" part of reviewing big changes.

### 2.10 Anti-patterns

- Decisions living only in chat threads and people's memory.
- Editing accepted ADRs in place, erasing history.
- ADRs so long nobody writes or reads them.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Same decision re-debated repeatedly | No recorded rationale | Write an ADR; point to it |
| A choice was silently reversed | Decision undocumented | Record decisions; supersede deliberately |
| Nobody writes ADRs | Too heavyweight | Use a one-page template |

### 2.12 References

- M. Nygard, "Documenting Architecture Decisions" (2011), https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.
- M. Keeling, *Design It!* (Pragmatic Bookshelf, 2017) — ISBN 978-1680502091.

---

> **End of Part I.** You can now treat architecting as a continuous, risk-driven activity — investing design effort in proportion to risk and stopping when risk is acceptable — and capture significant choices as short, immutable ADRs stored with the code. **Part II — Collaboration** (Chapter 3) covers running architecture as a team activity: shared modeling, decision ownership, and avoiding the ivory-tower architect.

<!--APPEND-PART-II-->
