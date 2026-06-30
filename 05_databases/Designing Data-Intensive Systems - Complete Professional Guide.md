---
software_dev: core
---

# Designing Data-Intensive Systems - Complete Professional Guide

> **Category:** 05_databases · **Language:** English

---

### Reliability, scalability, and maintainability for modern data systems
**Original guide written from primary sources, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches the topic from first principles and primary sources (database documentation, distributed-systems papers, and protocol specifications). Where a canonical book covers the same ground, it is listed under **References** as a pointer only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** this guide covers how to reason about systems whose primary challenge is **data** — its volume, velocity, complexity, and the guarantees applications need from it. It is technology-agnostic but grounded in how real engines (PostgreSQL, Cassandra, Kafka, object stores, modern lakehouse/streaming platforms) behave in 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to data systems | Part I |
| 2 — Intermediate | App developers choosing a store | Parts II–III |
| 3 — Advanced | Designing for scale & failure | Parts IV–V |
| 4 — Specialist | Consistency & coordination | Part VI |
| 5 — Architect | Streaming & system integration | Part VII |

**Target audience:** backend and data engineers, architects, platform/SRE teams, and tech leads who must choose, combine, and operate databases, queues, caches, and stream processors.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes basic SQL, HTTP, and familiarity with at least one programming language. No prior distributed-systems background is required; the concepts are built up from first principles.

---

## Table of Contents

**Part I – Foundations**
1. The three pillars: reliability, scalability, maintainability
2. Thinking in data models (relational, document, graph)

**Part II – Storage & Retrieval**
3. How storage engines actually work (B-trees vs LSM-trees)
4. Encoding, schema evolution, and compatibility

**Part III – Distributing Data**
5. Replication (leader-based, multi-leader, leaderless)
6. Partitioning (sharding) and rebalancing

**Part IV – Consistency & Correctness**
7. Transactions and isolation levels
8. The trouble with distributed systems (clocks, failures, quorums)

**Part V – Consensus & Coordination**
9. Consistency models and consensus

**Part VI – Derived & Streaming Data**
10. Batch and stream processing
11. Designing systems of integration (the "unbundled database")

> **Status of this guide:** phased delivery. **Ready:** Parts I–II (Ch. 1–4). **In progress:** Parts III–VII.

---

## Part I – Foundations

A "data-intensive" system is one where the **hard part is the data** — not raw CPU. The bottlenecks are data volume, the rate it changes, and the complexity of the guarantees applications place on it. Almost every such system is assembled from a handful of building blocks — databases, caches, search indexes, message queues, and stream processors — wired together. The skill is knowing what each block guarantees, where it breaks, and how the seams between them behave.

---

## Chapter 1 — The three pillars: reliability, scalability, maintainability

### 1.1 Introduction

Before choosing any technology, name the **non-functional goals** the system must meet. Three recur in every data system: it should keep working correctly when things go wrong (**reliability**), keep performing as load grows (**scalability**), and stay workable for the humans who operate and change it (**maintainability**). These are not vague ideals — each can be made measurable and turned into design pressure.

### 1.2 Business context

These pillars are where engineering meets money. An hour of downtime has a euro figure; so does a checkout page that takes three seconds under Black-Friday load, or an on-call engineer burning out on a system nobody understands. Stating the targets explicitly — "99.9% of writes acknowledged under 50 ms at 10× today's traffic" — turns architecture from taste into a decision you can defend and verify.

### 1.3 Theoretical concepts: defining each pillar

```mermaid
mindmap
  root((Data system goals))
    Reliability
      Tolerate hardware faults
      Tolerate software bugs
      Tolerate human error
    Scalability
      Describe load (parameters)
      Describe performance (percentiles)
      Cope as load grows
    Maintainability
      Operability
      Simplicity
      Evolvability
```

- **Reliability** = continuing to work *correctly* even when faults occur. A *fault* is one component deviating from spec; a *failure* is the system as a whole stopping. The goal is to prevent faults from becoming failures. You raise reliability by **tolerating** faults, not by hoping they never happen — and the only way to trust fault tolerance is to deliberately trigger faults (fault injection, chaos testing).
- **Scalability** = the system's ability to cope with **increased load**. It is meaningless until you (a) describe load with concrete **parameters** (requests/sec, read/write ratio, fan-out, concurrent users) and (b) describe performance with **percentiles**, not averages. Tail latency (p95/p99) is what users actually feel and what amplifies under fan-out.
- **Maintainability** = the cost of *living with* the system over years: **operability** (easy for ops to keep it healthy), **simplicity** (easy for new engineers to understand — fight accidental complexity), and **evolvability** (easy to change as requirements move).

### 1.4 Architecture: where the goals bite

```mermaid
flowchart LR
    load["Load parameters<br/>(rps, read/write mix, fan-out)"] --> design["Design choices"]
    design --> rel["Reliability<br/>(replication, retries, isolation)"]
    design --> scal["Scalability<br/>(partitioning, caching, async)"]
    design --> maint["Maintainability<br/>(clear seams, observability)"]
    rel --> slo["SLOs / error budget"]
    scal --> slo
    maint --> slo
```

Every later decision in this guide — replication, partitioning, isolation level, batch vs stream — is a trade between these three. There is no "best database," only the best fit for a stated load and a stated guarantee.

### 1.5 Real example

**Scenario.** A social feed must show each user a timeline of posts from people they follow.

**Problem.** A celebrity with 30M followers makes naive "fan-out on read" (query all followees at read time) too slow at the tail, while naive "fan-out on write" (push each post into every follower's timeline) explodes for that same celebrity.

**Solution.** Make load a parameter: most users are cheap to fan out **on write**; a small set of high-follower accounts are handled **on read** and merged in. The split point is chosen from the actual follower-count distribution.

**Implementation (sketch).**

```text
on new post by U:
    if followers(U) <= THRESHOLD:        # ordinary user
        for f in followers(U):           # fan-out on write
            append post_id to timeline_cache[f]
    else:                                # celebrity: skip the fan-out
        mark U as "pull at read time"

on read timeline for V:
    base   = timeline_cache[V]                    # precomputed
    celebs = [u for u in follows(V) if is_pull(u)]
    extra  = recent_posts(celebs)                 # fan-out on read, few accounts
    return merge_by_time(base, extra)
```

**Result.** The expensive operation (touching 30M timelines) never happens; the tail is bounded because the read-time merge touches only a handful of accounts.

**Future improvements.** Measure the threshold from the live follower histogram; cache the celebrity merge for a few seconds; track p99 timeline-build latency as the SLI.

### 1.6 Exercises

1. Give two load parameters for a payment API and two for a chat app — why do they differ?
2. Why is p99 latency a better target than mean latency for a user-facing read?
3. Define *fault* vs *failure* and give one example of turning a fault into a non-failure.

### 1.7 Challenges

- **Challenge.** Take any service you know. Write its load in 3 parameters and its performance goal as a percentile. Then name the single design choice most likely to break first as load grows 10×.

### 1.8 Checklist

- [ ] I can state load as concrete parameters, not "a lot of traffic."
- [ ] I describe latency with percentiles, not averages.
- [ ] I distinguish reliability (tolerating faults) from "no faults."
- [ ] I treat operability, simplicity, and evolvability as design targets.

### 1.9 Best practices

- Write the SLO **before** the architecture; let it drive the trade-offs.
- Test fault tolerance by injecting faults — untested failover is not failover.
- Track tail latency (p95/p99) per endpoint, not just the average.

### 1.10 Anti-patterns

- "Scalable" as a marketing adjective with no load parameter behind it.
- Averaging latency, hiding the tail users actually experience.
- Adding components for resilience without ever exercising the failure path.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| p99 spikes under load, mean looks fine | Tail amplified by fan-out / queueing | Measure per-stage percentiles; bound fan-out |
| Failover never triggers in an outage | Untested fault-tolerance path | Add fault injection to CI/staging |
| "It got slow" with no baseline | No load/perf targets defined | Define load parameters + percentile SLOs |

### 1.12 References

These are pointers for further study; this guide does not reproduce their text.

- M. Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017) — ISBN 978-1449373320.
- Official docs: PostgreSQL (https://www.postgresql.org/docs/), Apache Cassandra (https://cassandra.apache.org/doc/), Apache Kafka (https://kafka.apache.org/documentation/).

---

## Chapter 2 — Thinking in data models

### 2.1 Introduction

A **data model** shapes not just how you store information but how you are able to *think* about the problem. Picking relational, document, or graph is less about "which is newer" and more about **where the relationships live** and **who needs to traverse them**. This chapter frames the choice and the modern (2026) reality that most systems use more than one.

### 2.2 Business context

The data model is the contract between the product's concepts and the storage that outlives any single feature. Get it wrong and every future query fights the schema; get it right and new features fall out naturally. Because migrations are expensive and risky at scale, this is one of the highest-leverage early decisions.

### 2.3 Theoretical concepts: three families

- **Relational** — data as **tables of rows**; relationships expressed by **joins** at read time. Strong fit when the data is highly interconnected and you need flexible, ad-hoc queries with strong integrity (foreign keys, constraints). The dominant default for transactional systems.
- **Document** — data as **self-contained documents** (typically JSON). Strong fit for tree-shaped, one-to-many data read as a unit (an order with its line items). Locality is the win; relationships *across* documents are the weakness — you re-implement joins in the application.
- **Graph** — data as **vertices and edges**, relationships are first-class. Strong fit when the *connections* are the point and traversals are many-hop (social graphs, fraud rings, recommendations, knowledge graphs).

```mermaid
flowchart TB
    q{"Where is the complexity?"}
    q -- "many-to-many, ad-hoc queries" --> rel["Relational"]
    q -- "tree read as a unit, locality" --> doc["Document"]
    q -- "the connections themselves" --> graph["Graph"]
```

The "right" answer is usually **polyglot persistence**: a relational system of record, a document store or cache for read-optimized views, a search index for text, and a graph store where traversal dominates — kept consistent through the integration patterns in Part VII.

### 2.4 Architecture: impedance and locality

```mermaid
flowchart LR
    app["Application objects"] -->|map| store["Storage model"]
    store -->|relational| join["Joins at read time"]
    store -->|document| local["Locality: read whole tree"]
    store -->|graph| trav["Cheap multi-hop traversal"]
```

The friction between in-memory objects and the stored shape is the classic **impedance mismatch**. Document models reduce it for tree-shaped aggregates; relational models reduce it for many-to-many; graph models reduce it for deep traversal. Modern relational engines blur the lines by storing and indexing JSON natively, so "relational vs document" is now often a spectrum within one engine.

### 2.5 Real example

**Scenario.** A marketplace needs orders (with line items), product search, and "customers who bought X also bought Y."

**Problem.** No single model serves all three well: orders are tree-shaped, search is text, recommendations are graph traversal.

**Solution.** System of record in a relational store (orders, payments, integrity). A document/JSON projection for fast order reads. A search index for the catalog. A graph projection for co-purchase traversal. One source of truth; the rest are **derived views** kept current by a change stream (Part VII).

**Implementation (relational core, JSON locality where it helps).**

```sql
-- Orders: relational integrity for money, JSON for the flexible line-item shape.
CREATE TABLE orders (
    id           BIGINT PRIMARY KEY,
    customer_id  BIGINT NOT NULL REFERENCES customers(id),
    status       TEXT   NOT NULL,
    total_cents  BIGINT NOT NULL CHECK (total_cents >= 0),
    items        JSONB  NOT NULL,          -- read the order as one unit
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Index inside the JSON for a common filter (e.g. orders containing a SKU).
CREATE INDEX idx_orders_items_sku ON orders USING gin ((items -> 'skus'));
```

**Result.** Money and relationships get relational guarantees; the order document is read in one shot; search and recommendations live in stores built for them.

**Future improvements.** Drive the derived views from the order table's change stream so they cannot silently drift; add a contract test asserting projection ↔ source-of-truth consistency.

### 2.6 Exercises

1. Give one dataset that is painful in a document store and explain why.
2. When does a graph database beat recursive SQL for a many-hop query?
3. What is the impedance mismatch, and how does a document model reduce it?

### 2.7 Challenges

- **Challenge.** Model a "team → projects → tasks → assignees" domain three ways (relational, document, graph). For each, write the query "all tasks assigned to people on team T" and compare effort.

### 2.8 Checklist

- [ ] I choose a model from where the relationships and queries live, not by fashion.
- [ ] I know when locality (document) helps and when it hurts.
- [ ] I treat non-source-of-truth stores as derived views.
- [ ] I consider native JSON in a relational engine before adding a second database.

### 2.9 Best practices

- Keep **one** system of record; make every other store a derived, rebuildable view.
- Use the relational engine's JSON support before introducing a separate document store.
- Let query patterns — not table count — drive the model.

### 2.10 Anti-patterns

- Scattering the source of truth across several stores with no clear owner.
- Forcing deep graph traversals through many self-joins in SQL.
- Choosing a database for its category buzz rather than the access pattern.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| App is full of hand-written "joins" | Document model used for many-to-many data | Move relationships to a relational core |
| Recommendation queries time out | Multi-hop traversal on a relational schema | Add a graph projection for traversal |
| Derived view disagrees with source | Drift in the projection pipeline | Drive views from a change stream; add contract tests |

### 2.12 References

- E. F. Codd, "A Relational Model of Data for Large Shared Data Banks," *CACM* (1970).
- Official docs: PostgreSQL JSON types (https://www.postgresql.org/docs/current/datatype-json.html), Neo4j Cypher (https://neo4j.com/docs/).
- M. Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017) — ISBN 978-1449373320, for the broader treatment.

---

> **End of Part I.** You can now (1) state a data system's goals as measurable reliability, scalability, and maintainability targets, and (2) choose a data model from where the relationships and queries actually live, defaulting to a single source of truth with derived views. **Part II — Storage & Retrieval** (Chapters 3–4) goes one level down: how B-tree and LSM-tree engines store and find data, and how to evolve schemas without breaking readers or writers.

---

## Part II – Storage & Retrieval

A database does two fundamental things: store data you give it, and give it back when you ask. *How* it does that — the on-disk structure and the wire/format encoding — sets its whole performance and evolution profile. Part II covers the storage engine underneath every query and the encoding that lets a system change shape over time without breaking the programs reading it.

---

## Chapter 3 — How storage engines actually work (B-trees vs LSM-trees)

### 3.1 Introduction

Every database write eventually becomes bytes laid out by a **storage engine**, and two families dominate. **B-tree** engines (PostgreSQL, InnoDB) keep data in sorted, fixed-size pages updated **in place** — excellent reads, random-ish writes. **LSM-tree** engines (Cassandra, RocksDB, ScyllaDB) **append** writes to an in-memory buffer, flush sorted immutable files, and **compact** them in the background — excellent write throughput, with read cost managed by bloom filters and compaction. Knowing which family a database belongs to explains its behavior under load before you ever benchmark it.

### 3.2 Business context

The storage engine is the hardest thing to change after launch — it is baked into the database choice. A write-heavy ingestion product on a B-tree engine fights page contention; a low-latency read product on an untuned LSM setup suffers read amplification. Matching the engine family to whether the workload is read- or write-dominant is a structural decision that avoids an expensive re-platforming later, and it lets an on-call engineer reason about why a system slows the way it does.

### 3.3 Theoretical concepts: in-place vs append-and-merge

```mermaid
flowchart TB
    btree["B-tree: sorted pages updated IN PLACE<br/>read-optimized; writes do random I/O + page splits"]
    lsm["LSM-tree: APPEND to memtable -> flush SSTables -> compact<br/>write-optimized; reads check several files (bloom filters help)"]
```

- **B-tree** keeps a balanced tree of sorted pages; a lookup is a few page reads, a range scan walks leaves in order. Writes update the page in place (and may split it), causing random I/O — but the write-ahead log (a sequential append) makes those writes crash-safe.
- **LSM-tree** buffers writes in a sorted in-memory **memtable**, flushes it as an immutable sorted file (**SSTable**), and merges SSTables via **compaction**. Writes are sequential (fast); a read may consult the memtable plus several SSTables, so **bloom filters** short-circuit "key definitely not here" and compaction keeps the file count bounded.

The trade is **read amplification vs write amplification**: B-trees write each page possibly several times (page + WAL), LSM-trees rewrite data during compaction but turn writes sequential.

### 3.4 Architecture: the read and write paths

```mermaid
flowchart LR
    w["Write"] --> mem["LSM: memtable"] --> flush["SSTable (immutable)"] --> comp["compaction merges"]
    r["Read"] --> mem
    r --> bloom["bloom filter -> skip SSTables"] --> sst["SSTable"]
```

A storage engine's secondary indexes layer on the same machinery: a **clustered** index stores the row in the index leaf (InnoDB primary key), a **non-clustered** index stores a pointer. Either way, every index is extra write work — the price of a faster read. The engineering judgment is the same in both families: add an index for a real read pattern, not speculatively, because each one taxes every write.

### 3.5 Real example

**Scenario.** A telemetry platform ingests millions of events per second; reads are mostly recent ranges and a few key lookups.

**Problem.** A B-tree engine cannot sustain the write rate (random page updates, contention, WAL pressure).

**Solution.** An LSM-based engine: sequential appends absorb the write rate; bloom filters and tiered compaction keep recent-range reads fast.

**Implementation (engine-fit reasoning).**

```text
Workload: write-heavy ingestion, range reads of recent data, sparse point lookups
  B-tree:  random writes + page splits -> write bottleneck at this rate
  LSM:     sequential appends -> sustains the write rate
           compaction tuned for read latency on recent SSTables
Decision: LSM store; size memtables for the write rate; monitor compaction backlog.
```

**Result.** The ingestion rate is met structurally; reads stay fast with appropriate compaction — fitting the engine to the workload instead of fighting it.

**Future improvements.** Watch compaction backlog (the key LSM health metric); for the point-lookup path, confirm bloom-filter false-positive rate is low enough.

### 3.6 Exercises

1. Why does an LSM-tree sustain higher write throughput than a B-tree?
2. What is read amplification, and which two mechanisms mitigate it in LSM engines?
3. Why is every secondary index a tax on writes regardless of engine family?

### 3.7 Challenges

- **Challenge.** Identify the storage engine behind a database you operate. Classify your workload as read- or write-dominant and argue whether the engine family fits — and what metric you'd watch to confirm.

### 3.8 Checklist

- [ ] I know B-tree updates in place and LSM appends-and-compacts.
- [ ] I match engine family to read- vs write-heavy workloads.
- [ ] I understand compaction's role and cost in LSM.
- [ ] I add indexes for real read patterns, knowing each taxes writes.

### 3.9 Best practices

- Choose the engine family to fit the dominant access pattern.
- For LSM, monitor and tune compaction; for B-tree, watch write contention and bloat.
- Justify every secondary index with a concrete query.

### 3.10 Anti-patterns

- Write-heavy ingestion on a read-optimized B-tree without tuning.
- Ignoring LSM compaction until reads degrade.
- Index-shotgunning — adding indexes "to be safe," slowing every write.

### 3.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Write throughput hits a wall | Random-write engine for a write-heavy load | Consider an LSM engine; tune WAL/checkpoint |
| Read latency rising over time | LSM compaction falling behind | Tune/scale compaction |
| Writes slow, table bloated | B-tree page splits/fragmentation | Maintenance (vacuum/rebuild); review index count |

### 3.12 References

- M. Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017), Chapter 3 "Storage and Retrieval" — ISBN 978-1449373320.
- See also the sibling guide *How Databases Work Internally* (Part I) for storage-engine and WAL internals.

---

## Chapter 4 — Encoding, schema evolution, and compatibility

### 4.1 Introduction

Data outlives the code that wrote it, and in a running system old and new code coexist. **Encoding** (serialization) is how in-memory structures become bytes for storage or the network; **schema evolution** is changing that shape over time without breaking the programs on either side. The goal is two-way compatibility: **backward** (new code reads old data) and **forward** (old code reads new data). Get encoding wrong and a deploy becomes an outage when a new field meets old readers.

### 4.2 Business context

In any system bigger than one process, you cannot upgrade every component at once — rolling deploys, multiple services, and stored data from last year all coexist. Schema evolution is what makes that survivable: it lets teams ship changes independently instead of coordinating a risky big-bang upgrade. A format chosen for compatibility (and a discipline of compatible changes) is the difference between "add a field, deploy gradually" and "freeze everything for a synchronized release."

### 4.3 Theoretical concepts: compatibility directions

```mermaid
flowchart LR
    new["New code"] -->|backward compat| old_data["reads OLD data"]
    old["Old code"] -->|forward compat| new_data["reads NEW data (ignores unknown fields)"]
```

- **Backward compatibility** — newer code can read what older code wrote. Usually easy (you know the old format).
- **Forward compatibility** — older code can read what newer code writes. Harder: old code must *ignore* fields it doesn't understand rather than choke.

Schema-based binary formats (**Protocol Buffers**, **Avro**, **Thrift**) give both cheaply: fields carry tags/IDs, so adding an **optional** field with a new tag is backward- and forward-compatible; removing a required field or reusing a tag breaks compatibility. Textual JSON is forward/backward tolerant by convention (ignore unknown keys) but lacks enforced schemas and is larger on the wire.

### 4.4 Architecture: where encoding lives

```mermaid
flowchart TB
    disk["On disk (rows, log segments)"]
    wire["Over the network (RPC, events)"]
    rules["Compatible-change rules:<br/>add optional fields, never reuse tags, never make a field required late"]
    disk --> rules
    wire --> rules
```

Encoding shows up in three places, each needing evolution discipline: **databases** (a column added today, rows from last year), **service calls** (RPC between independently deployed services), and **message/event streams** (an event written now, consumed months later after replay). The same rule set governs all three: additive, optional changes are safe; destructive or type-changing edits are not. A **schema registry** (common with Avro on Kafka) enforces this automatically by rejecting incompatible schema updates.

### 4.5 Real example

**Scenario.** A payments service and a ledger service exchange `Payment` events on Kafka, deployed independently. A new `currency` field is needed.

**Problem.** If `currency` is added as **required**, old consumers (not yet redeployed) fail to decode new events — a forward-compatibility break that halts the ledger.

**Solution.** Add `currency` as an **optional** field with a new tag and a sensible default; deploy producers and consumers in any order; enforce the rule with a schema registry.

**Implementation (compatible Protobuf change).**

```protobuf
message Payment {
  int64  id          = 1;
  int64  amount_cents = 2;
  string status      = 3;
  string currency    = 4;   // NEW: new tag, optional; old readers ignore it,
                            //      new readers default it when absent. Compatible both ways.
}
// Forbidden: reusing tag 4 later, or deleting a still-read field, or making 4 required.
```

**Result.** Producers and consumers roll out independently with zero coordination; old and new events interoperate. The registry blocks any future incompatible edit before it ships.

**Future improvements.** Add compatibility checks to CI (schema-diff gate); document the field-evolution rules where the schemas live.

### 4.6 Exercises

1. Define backward vs forward compatibility and say which is usually harder, and why.
2. Why does adding an optional, new-tag field keep a binary format compatible both ways?
3. What does a schema registry enforce, and at what point in the lifecycle?

### 4.7 Challenges

- **Challenge.** Take an event or API payload you own. Plan adding one field and removing one field as a sequence of *compatible* steps that never break a rolling deploy. Identify which step must wait for all readers to upgrade.

### 4.8 Checklist

- [ ] I know backward vs forward compatibility and design for both.
- [ ] I make additive changes optional with new field tags/IDs.
- [ ] I never reuse a field tag or make a field required after the fact.
- [ ] I use a schema registry (or equivalent gate) for shared event/RPC formats.

### 4.9 Best practices

- Prefer schema-based binary formats (Avro/Protobuf) for high-volume or long-lived data.
- Evolve schemas additively; sequence destructive changes behind reader upgrades.
- Enforce compatibility automatically in CI / a registry, not by review alone.

### 4.10 Anti-patterns

- Making a new field required, breaking not-yet-upgraded readers.
- Reusing or renumbering field tags, silently corrupting old data.
- Coordinating big-bang upgrades because the format can't evolve.

### 4.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Consumers fail decoding after a producer deploy | New required field / incompatible change | Make the field optional; add a registry gate |
| Old rows/events misread after a schema edit | Field tag reused or type changed | Restore tags; treat changes as additive |
| Teams blocked on synchronized releases | Format lacks evolution support | Adopt a schema-based format + compatibility rules |

### 4.12 References

- M. Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017), Chapter 4 "Encoding and Evolution" — ISBN 978-1449373320.
- Apache Avro spec (https://avro.apache.org/docs/) and Protocol Buffers (https://protobuf.dev/).

---

> **End of Part II.** You can now reason one level below the data model: how **B-tree** and **LSM-tree** storage engines trade reads against writes, and how **schema-compatible encoding** (additive, optional fields in formats like Avro/Protobuf) lets a system evolve while old and new code coexist. **Part III — Distributing Data** (Chapters 5–6) takes the next step: copying data across nodes (replication) and splitting it across nodes (partitioning), the two moves that turn a single database into a distributed one.

<!--APPEND-PART-III-->
