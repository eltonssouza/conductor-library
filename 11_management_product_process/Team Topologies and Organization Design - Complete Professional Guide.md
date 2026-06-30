---
software_dev: supporting
---

# Team Topologies and Organization Design - Complete Professional Guide

> **Category:** 11_management_product_process · **Language:** English

---

### Team types, interaction modes, and Conway's Law
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches organization design from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** how you organize teams shapes the software they build (and vice versa). This guide covers team types, interaction modes, cognitive load, and Conway's Law as levers for fast, sustainable delivery, current to 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to org design | Part I |
| 2 — Intermediate | Structuring teams | Part II |

**Target audience:** engineering leaders, architects, and anyone shaping how teams are organized.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes the DevOps and architecture guides.

---

## Table of Contents

**Part I – Structure shapes software**
1. Conway's Law and cognitive load
2. The four team types

**Part II – Interaction**
3. The three interaction modes

> **Status of this guide:** complete for its declared scope. **Ready:** Parts I–II (Ch. 1–3).

---

## Part I – Structure shapes software

Organizations ship their **org chart**: the way you split teams ends up reflected in the architecture of the software (Conway's Law). So team structure is an architectural decision. The goal is **fast flow** — teams that can deliver value with minimal dependencies and hand-offs — which requires managing each team's cognitive load and choosing the right team shapes.

---

## Chapter 1 — Conway's Law and cognitive load

### 1.1 Introduction

**Conway's Law:** a system's design mirrors the communication structure of the organization that built it. If three teams build a compiler, you get a three-pass compiler. This means you can **design the architecture you want by designing the teams** (the "Inverse Conway Maneuver"). The constraint on team scope is **cognitive load** — a team can only effectively own so much complexity.

### 1.2 Business context

Ignoring Conway's Law produces architectures that fight the org (constant cross-team dependencies, slow delivery). Overloading teams with too much cognitive load causes burnout, errors, and slow delivery. Deliberately aligning team boundaries with desired architecture, and limiting each team's load to what it can handle, is what enables fast, sustainable flow. For a business, this is the difference between teams that ship independently and an org gridlocked by dependencies.

### 1.3 Theoretical concepts: org = architecture; bound the load

```mermaid
flowchart LR
    org["Team/communication structure"] --> arch["System architecture (mirrors it)"]
    arch -.->|design teams to get the architecture you want| org
    load["Cognitive load per team"] --> bound["Must stay within what the team can handle"]
```

To get a modular architecture, create teams with clear, modular ownership. **Cognitive load** (the total mental burden of everything a team must understand — domain, tech, tools) must be bounded: a team owning too many disparate things does all of them poorly. Limit a team's scope to a **single, comprehensible domain**.

### 1.4 Architecture: align boundaries, limit load

```mermaid
flowchart TB
    desired["Desired architecture (modular services)"] --> teams["Teams with matching ownership boundaries"]
    teams --> flow["Independent delivery, low cross-team friction"]
```

### 1.5 Real example

**Scenario.** A company wants independent, modular services but has teams split by technical layer (a frontend team, a backend team, a DBA team).

**Problem.** By Conway's Law, layer-split teams produce a tightly-coupled layered monolith with cross-team dependencies for every feature.

**Solution.** Re-org into cross-functional teams owning whole services/domains (Inverse Conway Maneuver) so the architecture can be modular.

**Implementation (the re-org).**

```text
Before: frontend team | backend team | DBA team   (layer split -> coupled layers)
After:  Orders team   | Payments team | Catalog team (each owns its whole service:
        UI + API + data)  -> independent, modular services that mirror the teams
Cognitive load: each team owns ONE domain, bounded and comprehensible.
```

**Result.** Team boundaries now match the desired modular architecture; teams deliver features independently without cross-layer dependencies, and each owns a bounded domain. Structure produced the architecture.

**Future improvements.** Watch each team's cognitive load as the domain grows; split a team/domain before it overloads.

### 1.6 Exercises

1. State Conway's Law and the Inverse Conway Maneuver.
2. What is cognitive load and why bound it?
3. Why do layer-split teams produce coupled architectures?

### 1.7 Challenges

- **Challenge.** Look at your org's team boundaries. Do they match the architecture you want? Identify one team split that's producing unwanted coupling.

### 1.8 Checklist

- [ ] I treat team structure as an architectural decision.
- [ ] Team boundaries align with desired system boundaries.
- [ ] Each team's cognitive load is bounded.
- [ ] Teams own a single, comprehensible domain.

### 1.9 Best practices

- Design teams to produce the architecture you want.
- Limit each team's cognitive load to one clear domain.
- Prefer cross-functional, domain-owning teams.

### 1.10 Anti-patterns

- Layer-split teams expecting modular services.
- Overloaded teams owning too many disparate things.
- Ignoring the org→architecture mirror.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Constant cross-team dependencies | Boundaries fight architecture | Re-align teams to domains |
| Team burnt out / slow | Cognitive overload | Reduce scope; split domain |
| Coupled architecture | Conway's Law ignored | Apply Inverse Conway Maneuver |

### 1.12 References

- M. Skelton, M. Pais, *Team Topologies* (IT Revolution, 2019) — Ch. 2, "Conway's Law and Why It Matters," and Ch. 3, "Team-First Thinking" (cognitive load). ISBN 978-1942788812.
- M. Conway, "How Do Committees Invent?" (1968), origin of Conway's Law.

---

## Chapter 2 — The four team types

### 2.1 Introduction

Team Topologies proposes just **four fundamental team types**, and says most organizations need only these. A **stream-aligned** team delivers value for a business stream (the default, primary team). Three supporting types help stream-aligned teams go fast: **platform** (provides self-service infrastructure), **enabling** (coaches/upskills), and **complicated-subsystem** (owns a part needing deep specialist expertise).

### 2.2 Business context

Most org-design confusion comes from a sprawl of ad-hoc team types with unclear purposes, creating overhead and hand-offs. Limiting to four well-defined types with clear purposes reduces that confusion and keeps the focus on **stream-aligned teams delivering value**, with the others existing only to reduce those teams' cognitive load. This clarity speeds delivery and makes the org understandable — everyone knows why each team exists.

### 2.3 Theoretical concepts: one primary, three supporting

```mermaid
flowchart TB
    stream["Stream-aligned: delivers value for a stream (PRIMARY, most teams)"]
    platform["Platform: self-service capabilities for stream teams"]
    enabling["Enabling: coaches/upskills stream teams"]
    subsystem["Complicated-subsystem: deep-specialist part"]
    platform --> stream
    enabling --> stream
    subsystem --> stream
```

- **Stream-aligned** — owns a slice of the business end to end; the team type that delivers value. Most teams should be this.
- **Platform** — provides paved-road, self-service capabilities so stream teams don't reinvent infrastructure (reduces their cognitive load).
- **Enabling** — temporarily helps stream teams adopt new skills/practices, then steps back.
- **Complicated-subsystem** — owns a component requiring rare deep expertise (e.g. a video codec, a risk engine), so stream teams don't all need that expertise.

### 2.4 Architecture: supporting teams serve stream teams

```mermaid
flowchart LR
    p["Platform"] -->|self-service| s["Stream-aligned teams (deliver value)"]
    e["Enabling"] -->|coach| s
    c["Complicated-subsystem"] -->|specialist component| s
```

### 2.5 Real example

**Scenario.** Every stream team is building its own CI/CD, monitoring, and infra setup — duplicating effort and carrying high cognitive load.

**Problem.** No platform team; each stream team reinvents undifferentiated infrastructure, slowing feature work.

**Solution.** Create a **platform** team providing self-service CI/CD, observability, and environments as a paved road; stream teams consume it.

**Implementation (introduce a platform team).**

```text
Platform team provides (self-service): CI/CD pipelines, monitoring, environments
Stream teams: consume the paved road -> focus on their domain/features
Result: stream teams' cognitive load drops; less duplication; faster delivery
```

**Result.** Stream teams stop reinventing infrastructure and focus on value; the platform team reduces everyone's cognitive load via self-service. The four-type structure clarifies who does what.

**Future improvements.** Treat the platform as a product with the stream teams as customers (measure adoption/satisfaction).

### 2.6 Exercises

1. Name the four team types and the primary one.
2. What is the purpose of the three supporting types?
3. Why should most teams be stream-aligned?

### 2.7 Challenges

- **Challenge.** Classify your org's teams into the four types. Are there too many non-stream-aligned teams? Is anything missing (e.g. a platform team)?

### 2.8 Checklist

- [ ] Most teams are stream-aligned (deliver value).
- [ ] A platform team provides self-service capabilities.
- [ ] Enabling teams upskill, then step back.
- [ ] Deep-specialist parts are complicated-subsystem teams.

### 2.9 Best practices

- Default teams to stream-aligned; justify other types.
- Run platforms as products that reduce cognitive load.
- Use enabling teams temporarily, not permanently.

### 2.10 Anti-patterns

- A sprawl of ad-hoc team types with unclear purpose.
- Permanent "enabling" teams that become gatekeepers.
- Every stream team rebuilding infrastructure (no platform).

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Duplicated infra effort | No platform team | Create a self-service platform team |
| Confusing team landscape | Too many ad-hoc types | Consolidate to the four types |
| Specialists spread thin | No complicated-subsystem team | Concentrate deep expertise in one team |

### 2.12 References

- M. Skelton, M. Pais, *Team Topologies* (IT Revolution, 2019) — Ch. 5, "The Four Fundamental Team Topologies" (stream-aligned, platform, enabling, complicated-subsystem). ISBN 978-1942788812.
- teamtopologies.com: https://teamtopologies.com.

---

> **End of Part I.** You can now use team structure as a design lever: apply Conway's Law (the org mirrors the architecture, so design teams to get the architecture you want) while bounding each team's cognitive load, and organize around the four team types — stream-aligned teams delivering value, supported by platform, enabling, and complicated-subsystem teams. **Part II — Interaction** (Chapter 3) covers the three interaction modes (collaboration, X-as-a-service, facilitating) that define how teams should work together to minimize friction.

## Part II – Interaction

Four team types tell you *what* teams should exist; they don't tell you *how* teams should work together. Get the interactions wrong and even well-shaped teams grind: everyone collaborates with everyone, boundaries blur, and cognitive load creeps back. Team Topologies reduces all the ways teams can interact to **three well-defined modes** — and the discipline is to choose one *deliberately* per relationship, and to let it change over time.

---

## Chapter 3 — The three interaction modes

### 3.1 Introduction

There are exactly three ways two teams should interact: **collaboration** (working closely together for a defined period on a shared problem), **X-as-a-Service** (one team consumes what another provides through a clear, low-friction interface), and **facilitating** (one team helps another learn or unblock). The point is not to discover these modes after the fact but to **assign one on purpose** to each team-to-team relationship — and to expect the mode to evolve as the boundary between teams becomes better understood.

### 3.2 Business context

When interaction is left implicit, the default is "collaborate with everyone," which scales terribly: high-bandwidth collaboration is expensive, raises every team's cognitive load, and dissolves accountability for the shared work. Naming the mode for each relationship makes the cost explicit and bounds it. The biggest payoff is the **evolution**: two teams collaborate intensely to discover an unclear boundary, then deliberately switch to X-as-a-Service once the interface is stable — collapsing ongoing coordination cost to near zero. Organizations that manage interaction modes consciously spend far less effort on cross-team friction.

### 3.3 Theoretical concepts: three modes, each with a cost

```mermaid
flowchart TB
    collab["Collaboration: two teams, shared goal,<br/>defined period — high bandwidth"]
    service["X-as-a-Service: provider exposes a clear<br/>interface; consumer self-serves — low bandwidth"]
    facil["Facilitating: one team coaches another<br/>to unblock/learn — temporary"]
    collab --> cost1["Best for discovery at an unclear boundary;<br/>expensive, raises cognitive load — use sparingly"]
    service --> cost2["Best once the boundary is well understood;<br/>predictable, scales — needs a good interface"]
    facil --> cost3["Best to remove an obstacle or build capability;<br/>enabling teams' default — then step back"]
```

**Collaboration** is high-bandwidth and creative but costly and blurry on responsibility — keep it time-boxed. **X-as-a-Service** trades discovery for predictability: it only works when the provided thing has a clean, documented interface (a true paved road). **Facilitating** is a coaching relationship, typically how an enabling team works, and is explicitly temporary.

### 3.4 Architecture: match the mode, then let it evolve

```mermaid
flowchart LR
    unclear["Unclear boundary / new capability"] --> collab["Collaboration (discover the interface)"]
    collab --> stable["Interface now stable"]
    stable --> service["X-as-a-Service (consume, self-serve)"]
    gap["Capability gap on a team"] --> facil["Facilitating (enabling team coaches)"]
    facil --> done["Gap closed -> step back"]
```

### 3.5 Real example

**Scenario.** A stream-aligned Orders team needs a new payments capability from a Payments team that is still defining what it offers.

**Problem.** They default to permanent close collaboration: constant meetings, shared tickets, neither team fully owning the result — high cognitive load on both, slow delivery.

**Solution.** Make the mode explicit *and* time-boxed: **collaborate** only while the payments interface is unclear, then deliberately switch to **X-as-a-Service** once Payments can expose a stable API.

**Implementation (mode chosen, then evolved).**

```text
Phase 1 (boundary unclear): Orders <-> Payments = COLLABORATION (time-boxed, 1 quarter)
        goal: discover and harden the payments interface together
Phase 2 (interface stable):  Payments exposes a self-service API (paved road)
        Orders <-> Payments = X-AS-A-SERVICE
        -> Orders self-serves; coordination cost drops to ~zero; each team owns its side
Separately: a Platform-enabling team FACILITATES Orders' adoption of the new API, then steps back
```

**Result.** The expensive collaboration is bounded to the period it adds value (discovering the boundary); once the interface is stable the teams settle into low-friction X-as-a-Service, reclaiming cognitive load and restoring clear ownership. The mode was chosen on purpose and allowed to change.

**Future improvements.** Periodically review each team-to-team relationship: is it still in the right mode, or has a "temporary" collaboration silently become permanent?

### 3.6 Exercises

1. Name the three interaction modes and the situation each fits.
2. Why must collaboration be time-boxed?
3. What must be true before two teams can use X-as-a-Service?

### 3.7 Challenges

- **Challenge.** Pick one cross-team relationship in your org. Which mode is it *actually* in, and which *should* it be in? If it's a stale, permanent collaboration, design the interface that would let it become X-as-a-Service.

### 3.8 Checklist

- [ ] Every important team-to-team relationship has a named mode.
- [ ] Collaboration is time-boxed, not permanent.
- [ ] X-as-a-Service relationships have a clear, documented interface.
- [ ] Facilitating (enabling) relationships are temporary and end when the gap closes.

### 3.9 Best practices

- Choose an interaction mode deliberately for each relationship.
- Use collaboration to discover an unclear boundary, then evolve to X-as-a-Service.
- Treat a stable interface (paved road) as the prerequisite for self-service.

### 3.10 Anti-patterns

- "Everyone collaborates with everyone" as the default.
- Permanent collaboration that should have become a service.
- An enabling team that never steps back (turns into a gatekeeper).

### 3.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Endless cross-team meetings | Permanent collaboration | Define an interface; move to X-as-a-Service |
| Consumer team always blocked on a provider | No real self-service interface | Harden the interface; make it a paved road |
| Enabling team became a bottleneck | Facilitating never ended | Time-box coaching; hand ownership back |

### 3.12 References

- M. Skelton, M. Pais, *Team Topologies* (IT Revolution, 2019) — Ch. 7, "Team Interaction Modes" (collaboration, X-as-a-Service, facilitating). ISBN 978-1942788812.
- M. Skelton, M. Pais, *Team Topologies* (IT Revolution, 2019) — Ch. 6, "Choose Team-First Boundaries," on stable interfaces between teams.

---

> **End of Part II.** You now have the full Team Topologies toolkit: shape teams with **Conway's Law and bounded cognitive load** (Ch. 1), organize around the **four fundamental team types** (Ch. 2), and connect them with the **three interaction modes** — collaboration, X-as-a-Service, and facilitating — chosen deliberately and evolved over time (Ch. 3). Together these let an organization design for fast, sustainable flow rather than inheriting whatever structure history left behind.
