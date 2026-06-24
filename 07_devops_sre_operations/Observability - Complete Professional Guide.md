---
software_dev: supporting
---

# Observability - Complete Professional Guide

> **Category:** 07_devops_sre_operations · **Language:** English

---

### Understanding systems from the outside: metrics, logs, and traces
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches observability from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** observability is the ability to understand a system's internal state from its external outputs — crucial for debugging modern distributed systems. This guide covers the telemetry types, high-cardinality structured events, and how observability differs from monitoring, current to 2026 (OpenTelemetry).

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to observability | Part I |
| 2 — Intermediate | Instrumenting systems | Part II |

**Target audience:** developers and SREs who operate and debug production systems.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes the SRE and DevOps-principles guides.

---

## Table of Contents

**Part I – Foundations**
1. Observability vs monitoring
2. Metrics, logs, and traces

**Part II – Modern observability**
3. High-cardinality structured events

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – Foundations

You can't fix what you can't see. As systems became distributed and dynamic, the old model (predefined dashboards for known failure modes) stopped being enough — you face failures you never anticipated. **Observability** is about being able to ask **new questions** of your system without shipping new code, so you can debug the unknown-unknowns.

---

## Chapter 1 — Observability vs monitoring

### 1.1 Introduction

**Monitoring** watches for **known** problems via predefined metrics and alerts ("is CPU > 90%?"). **Observability** is the property that lets you investigate **unknown** problems — ask arbitrary new questions about what your system is doing, after the fact, from rich telemetry. Monitoring tells you *that* something is wrong; observability helps you find out *why*, even for a failure you never predicted.

### 1.2 Business context

In complex distributed systems, most serious incidents are novel — combinations no one dashboarded for. Pure monitoring leaves teams blind when a new failure mode hits, extending outages. Observability shortens time-to-diagnosis by letting engineers slice and explore live data to find the actual cause, directly reducing downtime and its cost. As systems grow more dynamic (microservices, serverless), observability shifts from nice-to-have to essential.

### 1.3 Theoretical concepts: known vs unknown

```mermaid
flowchart LR
    mon["Monitoring: known failure modes, predefined dashboards/alerts"]
    obs["Observability: ask new questions of rich data, debug unknowns"]
    mon --> known["'Is X broken?' (yes/no)"]
    obs --> why["'Why is this specific request slow?' (explore)"]
```

Observability requires telemetry rich and granular enough to answer questions you didn't anticipate — which means **context-rich, high-cardinality** data (Chapter 3), not just pre-aggregated counters. Monitoring is a subset: useful for known conditions, insufficient for novel debugging.

### 1.4 Architecture: instrument for exploration

```mermaid
flowchart TB
    app["Instrumented app"] --> telemetry["Rich telemetry (metrics/logs/traces)"]
    telemetry --> store["Queryable store"]
    store --> explore["Engineers ask ad-hoc questions"]
```

### 1.5 Real example

**Scenario.** A small subset of users see slow checkouts, but all dashboards are green.

**Problem.** Monitoring covers aggregate metrics (overall latency is fine), so the targeted slowness is invisible.

**Solution.** Observability: query the data by user/region/version to isolate the affected slice.

**Implementation (asking a new question).**

```text
With rich, high-cardinality telemetry you can query:
  p99 latency WHERE region = 'sa-east' AND app_version = '1.4.2' AND payment = 'pix'
  -> reveals one provider+region+version combo is slow
No code change needed; the question is answered from existing telemetry.
```

**Result.** The affected slice (a specific provider/region/version) is isolated by exploring data, despite green aggregate dashboards. Diagnosis goes from days of guessing to minutes of querying.

**Future improvements.** Add the dimensions that mattered (provider, region, version) as standard fields so such questions are always answerable.

### 1.6 Exercises

1. Distinguish monitoring from observability.
2. Why is monitoring insufficient for distributed systems?
3. What kind of data does observability require?

### 1.7 Challenges

- **Challenge.** Recall an incident where dashboards were green but users hurt. What dimension would you have needed to slice by? Add it to your telemetry.

### 1.8 Checklist

- [ ] I distinguish known-problem monitoring from observability.
- [ ] My telemetry is rich enough to ask new questions.
- [ ] I can slice data by meaningful dimensions.
- [ ] I don't rely only on pre-aggregated dashboards.

### 1.9 Best practices

- Instrument for exploration, not just known alerts.
- Capture context-rich, queryable telemetry.
- Keep both: monitoring for knowns, observability for unknowns.

### 1.10 Anti-patterns

- Only predefined dashboards; blind to novel failures.
- Pre-aggregating away the detail needed to debug.
- Treating observability as just "more dashboards."

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Green dashboards, hurting users | Aggregate-only monitoring | Add high-cardinality, queryable data |
| Long diagnosis for novel issues | No observability | Instrument for ad-hoc questions |
| Can't isolate affected slice | Missing dimensions | Add relevant fields to telemetry |

### 1.12 References

- C. Majors, L. Fong-Jones, G. Miranda, *Observability Engineering* (O'Reilly, 2022) — ISBN 978-1492076445.
- OpenTelemetry docs: https://opentelemetry.io/docs/.

---

## Chapter 2 — Metrics, logs, and traces

### 2.1 Introduction

Observability is commonly built on three telemetry types (the "three pillars"): **metrics** (numeric measurements over time), **logs** (discrete event records), and **traces** (the path of one request across services). Each answers different questions; together — and especially when correlated — they let you go from "something's wrong" to "here's exactly where and why."

### 2.2 Business context

Using only one telemetry type leaves blind spots: metrics show *that* latency rose but not *which* request or *why*; logs are detailed but hard to aggregate; traces show cross-service flow but not system-wide trends. Combining them — and being able to jump between them (a spiking metric → the slow traces → their logs) — is what makes diagnosis fast. The business payoff is shorter outages and less engineer time lost to guesswork.

### 2.3 Theoretical concepts: three views

```mermaid
flowchart TB
    metrics["Metrics: aggregate trends (rates, latencies, counts)"]
    logs["Logs: detailed discrete events"]
    traces["Traces: one request across services (spans)"]
```

- **Metrics** — cheap, aggregate, great for trends and alerting ("is error rate up?").
- **Logs** — rich detail per event; best **structured** (JSON) so they're queryable.
- **Traces** — a request's journey through services as **spans**, revealing where time goes in a distributed call.

The power is **correlation**: a request/trace id links a metric spike to the exact traces and their logs.

### 2.4 Architecture: correlate across the three

```mermaid
flowchart LR
    spike["Metric spike (latency up)"] --> trace["Drill into slow traces"]
    trace --> span["Find the slow span/service"]
    span --> log["Read that span's logs for the cause"]
```

### 2.5 Real example

**Scenario.** Checkout latency rises; you must find the cause across five services.

**Problem.** A metric shows the rise but not where; logs alone can't show the cross-service path.

**Solution.** Use a trace to follow one slow request through the services and see which span is slow, then its logs.

**Implementation (correlated debugging).**

```text
1. Metric: checkout p99 latency up at 14:00
2. Trace: open a slow checkout trace -> spans:
     gateway 5ms -> orders 8ms -> payment 1200ms (!) -> ...
3. Logs of the payment span: "upstream provider timeout, retrying"
-> root cause: payment provider slow; retries inflating latency
```

**Result.** Three correlated views pinpoint the slow service (payment) and the reason (provider timeout/retries) in minutes — impossible with any one pillar alone.

**Future improvements.** Propagate trace context everywhere (OpenTelemetry); ensure logs include the trace id for instant correlation.

### 2.6 Exercises

1. What question does each of metrics, logs, and traces best answer?
2. Why should logs be structured?
3. What makes correlation across the three powerful?

### 2.7 Challenges

- **Challenge.** For a recent latency issue, trace one slow request end-to-end. Identify the slow span and confirm the cause from its logs.

### 2.8 Checklist

- [ ] I use metrics for trends/alerting.
- [ ] Logs are structured and queryable.
- [ ] Traces propagate across services.
- [ ] Telemetry is correlated by trace/request id.

### 2.9 Best practices

- Emit structured logs with a trace id.
- Instrument distributed tracing (OpenTelemetry).
- Design so you can jump metric → trace → log.

### 2.10 Anti-patterns

- Unstructured logs that resist querying.
- Metrics with no way to drill into specifics.
- Traces that break at service boundaries (no context propagation).

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Know latency rose, not where | Metrics only | Add tracing to locate the slow span |
| Logs hard to search | Unstructured | Emit structured (JSON) logs |
| Traces stop mid-flow | No context propagation | Propagate trace context end-to-end |

### 2.12 References

- C. Majors, L. Fong-Jones, G. Miranda, *Observability Engineering* (O'Reilly, 2022) — ISBN 978-1492076445.
- OpenTelemetry, "Signals": https://opentelemetry.io/docs/concepts/signals/.

---

> **End of Part I.** You can now distinguish observability (asking new questions of rich data to debug unknown failures) from monitoring (alerting on known conditions), and use the three telemetry types — metrics for trends, structured logs for detail, traces for cross-service flow — correlated by trace id to diagnose distributed problems fast. **Part II — Modern observability** (Chapter 3) covers high-cardinality, context-rich structured events as the foundation that makes truly arbitrary querying — and debugging the unknown-unknowns — possible.

<!--APPEND-PART-II-->
