---
software_dev: supporting
---

# Continuous Delivery and Deployment Pipelines - Complete Professional Guide

> **Category:** 07_devops_sre_operations · **Language:** English

---

### Build once, automate the path to production, deploy safely
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches continuous delivery from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** continuous delivery (CD) is the practice of keeping software **always releasable** by automating the path from commit to production. This guide covers the deployment pipeline, build-once principle, and safe release strategies, current to 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to CD | Part I |
| 2 — Intermediate | Building pipelines | Part II |

**Target audience:** developers and platform engineers automating delivery.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes the DevOps-principles guide and basic CI.

---

## Table of Contents

**Part I – The pipeline**
1. The deployment pipeline and build-once
2. Always releasable: continuous delivery vs deployment

**Part II – Safe release**
3. Progressive delivery (blue-green, canary)

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – The pipeline

Continuous delivery turns "preparing a release" from a manual, risky event into a routine, automated, repeatable process. The core artifact is the **deployment pipeline**: an automated path that takes every change through build, test, and deploy stages, providing fast feedback and a push-button (or fully automatic) release.

---

## Chapter 1 — The deployment pipeline and build-once

### 1.1 Introduction

A **deployment pipeline** is the automated implementation of your path from version control to production: each commit triggers a build, runs progressively broader tests, and can deploy through environments. A central rule is **build once**: produce a single immutable artifact and promote that *same* artifact through every environment — never rebuild per environment.

### 1.2 Business context

Manual, environment-specific builds and deploys are slow and a top source of "works in staging, breaks in prod" failures, because each environment runs subtly different bits. An automated pipeline with one immutable artifact makes releases fast, repeatable, and trustworthy — what ran in test is exactly what runs in production. This reliability is what lets a business release often and confidently instead of fearing every deploy.

### 1.3 Theoretical concepts: stages and immutability

```mermaid
flowchart LR
    commit["Commit"] --> build["Build ONCE -> immutable artifact"]
    build --> unit["Unit tests (fast gate)"]
    unit --> integ["Integration/acceptance tests"]
    integ --> stage["Deploy to staging (same artifact)"]
    stage --> prod["Deploy to production (same artifact)"]
```

Early stages are **fast** (fail quick on cheap checks); later stages are broader and slower. Configuration differs per environment (injected at deploy), but the **artifact** is identical everywhere. This eliminates "it built differently for prod" as a failure class.

### 1.4 Architecture: promote the same artifact

```mermaid
flowchart TB
    artifact["Immutable artifact (built once)"] --> e1["Test env"]
    artifact --> e2["Staging env"]
    artifact --> e3["Production env"]
    config["Env-specific config injected at deploy"] --> e1
    config --> e2
    config --> e3
```

### 1.5 Real example

**Scenario.** A team rebuilds the app separately for staging and production.

**Problem.** A dependency resolves to different versions in the two builds; staging passes, production breaks — a classic environment drift bug.

**Solution.** Build one immutable artifact; promote it unchanged; inject only config per environment.

**Implementation (build-once promotion).**

```text
CI build (once):  produce app:1.4.2 (immutable image/artifact)
deploy test:      run app:1.4.2 + test config
deploy staging:   run app:1.4.2 + staging config   # SAME artifact
deploy prod:      run app:1.4.2 + prod config       # SAME artifact
# config injected via env vars/secrets, not baked per build
```

**Result.** Exactly the same bits run everywhere; "different build for prod" bugs vanish. Releases become predictable promotions of a tested artifact.

**Future improvements.** Sign artifacts and verify provenance; record which artifact version is in each environment.

### 1.6 Exercises

1. What is a deployment pipeline?
2. State the build-once principle and why it matters.
3. What differs per environment if the artifact doesn't?

### 1.7 Challenges

- **Challenge.** Check whether your app is built once and promoted, or rebuilt per environment. If rebuilt, design a single-artifact promotion flow.

### 1.8 Checklist

- [ ] Every change flows through an automated pipeline.
- [ ] One immutable artifact is built and promoted.
- [ ] Config is injected per environment, not baked in.
- [ ] Fast checks run first; broader tests later.

### 1.9 Best practices

- Build once; promote the same artifact everywhere.
- Order pipeline stages fast-to-slow for quick feedback.
- Inject environment config at deploy time.

### 1.10 Anti-patterns

- Rebuilding per environment (drift).
- Manual, snowflake deployments.
- Baking environment config into the artifact.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Works in staging, breaks in prod | Per-environment rebuilds | Build once, promote the artifact |
| Slow feedback on failures | Slow checks run first | Reorder fast checks earlier |
| Config errors across envs | Config baked into builds | Inject config at deploy |

### 1.12 References

- J. Humble, D. Farley, *Continuous Delivery* (Addison-Wesley, 2010) — ISBN 978-0321601919.
- continuousdelivery.com: https://continuousdelivery.com.

---

## Chapter 2 — Always releasable

### 2.1 Introduction

The defining goal of CD is that software is **always in a releasable state** — `main` is never broken, and a release can happen at any time with low risk. **Continuous delivery** means every change is *ready* to deploy (deploy is a business decision, often push-button); **continuous deployment** goes further and deploys every passing change automatically. Both depend on keeping the mainline always green.

### 2.2 Business context

When the mainline is often broken or "not ready," releasing is a stressful, infrequent event, and value is stuck in inventory. Keeping software always releasable decouples *deploy* from *release decision*, so the business can ship whenever it wants — for a fix, an experiment, or a deadline — without a scramble. This agility (release on demand, low risk) is a major competitive advantage.

### 2.3 Theoretical concepts: delivery vs deployment

```mermaid
flowchart LR
    passing["Change passes the pipeline"] --> cd["Continuous Delivery: ready to deploy (manual trigger)"]
    passing --> cdep["Continuous Deployment: auto-deploys to prod"]
```

Both require: a mainline that's always green (trunk-based development, feature flags to hide unfinished work), comprehensive automated tests, and the ability to deploy safely (Chapter 3). The difference is only whether the final production deploy is automatic (deployment) or a human decision (delivery).

### 2.4 Architecture: keep main green with flags

```mermaid
flowchart TB
    dev["Small changes to main"] --> flags["Unfinished work behind feature flags"]
    flags --> green["Main always releasable"]
    green --> release["Release any time"]
```

### 2.5 Real example

**Scenario.** A team wants to merge a half-built feature without breaking releasability.

**Problem.** Merging incomplete work to main would block releases until it's done (or force a long-lived branch).

**Solution.** Merge small increments behind a **feature flag**, off in production, so main stays releasable while the feature is built.

**Implementation (feature flag).**

```text
merge small pieces to main continuously, each behind FEATURE_NEW_CHECKOUT=off
  -> main is always releasable (flag hides unfinished UI/logic)
  -> enable the flag for staff/canary, then everyone, when ready
  -> remove the flag after rollout
```

**Result.** The team integrates continuously without ever blocking releases; the feature ships by flipping a flag when complete. Main is always green and deployable.

**Future improvements.** Track flags and remove stale ones; use the flag to do a gradual rollout (Chapter 3).

### 2.6 Exercises

1. What does "always releasable" mean and why is it the goal?
2. Distinguish continuous delivery from continuous deployment.
3. How do feature flags keep main releasable?

### 2.7 Challenges

- **Challenge.** Find a long-lived branch in your repo. Plan how to land it in small flagged increments to main instead, keeping main releasable.

### 2.8 Checklist

- [ ] Main is always in a releasable state.
- [ ] Unfinished work is hidden behind flags.
- [ ] Comprehensive automated tests gate the mainline.
- [ ] Deploy is decoupled from the release decision.

### 2.9 Best practices

- Practice trunk-based development with small merges.
- Hide incomplete features behind flags.
- Keep the test suite trustworthy so main stays green.

### 2.10 Anti-patterns

- Long-lived feature branches blocking releasability.
- A frequently-broken mainline.
- Coupling deploy to a big manual release ceremony.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Can't release on demand | Main not always green | Trunk-based dev + flags |
| Big merge conflicts/risk | Long-lived branches | Merge small increments behind flags |
| Release is a stressful event | Deploy coupled to readiness | Keep always-releasable; decouple deploy |

### 2.12 References

- J. Humble, D. Farley, *Continuous Delivery* (Addison-Wesley, 2010) — ISBN 978-0321601919.
- P. Hodgson, "Feature Toggles," https://martinfowler.com/articles/feature-toggles.html.

---

> **End of Part I.** You can now build a continuous delivery capability: an automated deployment pipeline that builds one immutable artifact and promotes it through fast-to-slow stages, keeping software always releasable via trunk-based development and feature flags — so deploying becomes a routine, low-risk decision rather than a risky event. **Part II — Safe release** (Chapter 3) covers progressive delivery: blue-green deployments and canary releases that expose new versions to a fraction of traffic first, with automatic rollback on trouble.

<!--APPEND-PART-II-->
