---
software_dev: core
---

# Database Transactions and Concurrency - Complete Professional Guide

> **Category:** 05_databases · **Language:** English

---

### ACID, isolation levels, and concurrency control
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches transactions and concurrency from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** transactions let many users hit a database at once without corrupting data or seeing inconsistent state. This guide covers ACID, isolation levels and the anomalies they prevent, and how engines enforce them (locking, MVCC) — current to 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to transactions | Part I |
| 2 — Intermediate | Choosing isolation | Part II |

**Target audience:** application developers who write transactional code against relational databases.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes SQL and the data-intensive-systems guide.

---

## Table of Contents

**Part I – Transactions**
1. ACID: what a transaction guarantees
2. Isolation levels and concurrency anomalies

**Part II – Mechanisms**
3. How engines enforce isolation (locking and MVCC)

> **Status of this guide:** complete. **Ready:** Part I (Ch. 1–2), Part II (Ch. 3).

---

## Part I – Transactions

A **transaction** groups operations so they succeed or fail as a unit and don't corrupt each other when running concurrently. Without transactions, concurrent users produce lost updates, half-applied changes, and inconsistent reads. ACID names the guarantees; isolation levels let you trade strictness for performance.

---

## Chapter 1 — ACID

### 1.1 Introduction

**ACID** is four guarantees a transaction provides. **Atomicity**: all-or-nothing — either every operation applies or none does. **Consistency**: a transaction moves the database from one valid state to another (constraints hold). **Isolation**: concurrent transactions don't see each other's partial work. **Durability**: once committed, changes survive crashes (the WAL, from the internals guide).

### 1.2 Business context

ACID is what lets a business trust its data under concurrency: money isn't lost or double-spent, an order isn't half-created, a report doesn't read mid-update garbage. Many failures that look like application bugs are really missing transactional boundaries. Knowing ACID lets developers draw the right transaction boundaries so correctness holds even when thousands of users act at once.

### 1.3 Theoretical concepts: the four guarantees

```mermaid
mindmap
  root((ACID))
    Atomicity
      all-or-nothing
    Consistency
      invariants preserved
    Isolation
      concurrent txns don't interfere
    Durability
      committed survives crashes
```

The two that most shape application code are **atomicity** (wrap related changes in one transaction so a failure rolls everything back) and **isolation** (Chapter 2, the configurable one). Consistency is partly the database's job (constraints) and partly yours (correct logic). Durability is handled by the engine's WAL.

### 1.4 Architecture: a transaction boundary

```mermaid
flowchart LR
    begin["BEGIN"] --> ops["Operation 1..N"]
    ops --> ok{"All succeed?"}
    ok -- "yes" --> commit["COMMIT (durable)"]
    ok -- "no" --> rollback["ROLLBACK (as if nothing happened)"]
```

Everything between BEGIN and COMMIT is atomic: a failure anywhere triggers ROLLBACK, leaving the database as if the transaction never ran.

### 1.5 Real example

**Scenario.** Transfer money between two accounts.

**Problem.** Two separate statements (debit, credit) without a transaction can leave money debited but not credited if the second fails.

**Solution.** Wrap both in one transaction — atomicity guarantees both or neither.

**Implementation.**

```sql
BEGIN;
  UPDATE accounts SET balance = balance - 100 WHERE id = :from AND balance >= 100;
  -- if the row wasn't updated (insufficient funds), the app aborts:
  UPDATE accounts SET balance = balance + 100 WHERE id = :to;
COMMIT;   -- both applied, durably; any failure -> ROLLBACK, neither applied
```

**Result.** Money can never be debited without being credited; a crash or error rolls back both halves. The invariant "total money conserved" holds.

**Future improvements.** Add a CHECK constraint (balance >= 0) so consistency is enforced by the database too.

### 1.6 Exercises

1. Name the four ACID guarantees in one phrase each.
2. Which two most directly shape application code?
3. Why must a money transfer be one transaction?

### 1.7 Challenges

- **Challenge.** Find two related writes in your code not wrapped in a transaction. What inconsistent state is possible if the second fails? Wrap them.

### 1.8 Checklist

- [ ] I group related writes into one transaction (atomicity).
- [ ] I rely on the DB to enforce constraints (consistency).
- [ ] I understand isolation is configurable (Ch. 2).
- [ ] I trust durability comes from the WAL.

### 1.9 Best practices

- Draw transaction boundaries around invariants.
- Keep transactions short to reduce contention.
- Let database constraints enforce consistency.

### 1.10 Anti-patterns

- Related writes outside a transaction (partial updates).
- Long-running transactions holding locks/contention.
- Relying only on app logic for invariants the DB could enforce.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Half-applied multi-step changes | Missing transaction | Wrap related writes in BEGIN/COMMIT |
| Constraint violations slip through | Logic-only checks | Add DB constraints |
| High contention | Long transactions | Shorten transaction scope |

### 1.12 References

- A. Silberschatz, H. Korth, S. Sudarshan, *Database System Concepts*, 7th ed. (McGraw-Hill, 2019), Chapter 17 "Transactions" — §17.1 Transaction Concept, §17.4 Transaction Atomicity and Durability — ISBN 978-0078022159.
- J. Gray, A. Reuter, *Transaction Processing* (Morgan Kaufmann, 1992) — ISBN 978-1558601901.

---

## Chapter 2 — Isolation levels and anomalies

### 2.1 Introduction

Full isolation (transactions behaving as if run one at a time) is expensive, so databases offer **isolation levels** that trade strictness for concurrency. Each level permits or prevents certain **anomalies** — dirty reads, non-repeatable reads, phantoms. Choosing a level is choosing which concurrency bugs you can tolerate for which performance.

### 2.2 Business context

The default isolation level (often Read Committed) allows anomalies many developers don't expect, causing subtle concurrency bugs — a balance check that's stale by the time you act on it, a count that changes mid-transaction. Understanding the levels lets teams pick the right one per operation: strong isolation where correctness is critical (money), weaker where throughput matters and anomalies are harmless. Getting this wrong produces rare, hard-to-reproduce data bugs.

### 2.3 Theoretical concepts: levels vs anomalies

```mermaid
flowchart TB
    rc["Read Committed: no dirty reads<br/>(allows non-repeatable, phantoms)"]
    rr["Repeatable Read: + no non-repeatable reads"]
    ser["Serializable: no anomalies<br/>(as if one-at-a-time)"]
    rc --> rr --> ser
```

- **Dirty read**: seeing another transaction's uncommitted changes (prevented at Read Committed and above).
- **Non-repeatable read**: re-reading a row and getting a different value (prevented at Repeatable Read).
- **Phantom**: a re-run query returns new rows that appeared (prevented at Serializable).

Higher levels prevent more anomalies at higher cost (more locking/aborts).

### 2.4 Architecture: pick per operation

```mermaid
flowchart LR
    op["An operation"] --> risk{"Anomaly tolerable?"}
    risk -- "yes (throughput matters)" --> weak["Read Committed"]
    risk -- "no (correctness critical)" --> strong["Serializable"]
```

Isolation isn't one global setting you forget — match it to each operation's correctness needs. A reporting read can tolerate weak isolation; a balance-checking transfer may need Serializable.

### 2.5 Real example

**Scenario.** Enforce "an account may have at most 5 active sessions" under concurrent logins.

**Problem.** At Read Committed, two simultaneous logins both count 4 existing sessions and both insert — ending at 6 (a phantom/write-skew anomaly).

**Solution.** Use Serializable (or an explicit lock) so the count-then-insert is safe.

**Implementation.**

```sql
-- Serializable prevents the write-skew: one transaction will be aborted and retried
BEGIN ISOLATION LEVEL SERIALIZABLE;
  SELECT count(*) FROM sessions WHERE user_id = :u AND active;   -- sees a consistent count
  -- if < 5:
  INSERT INTO sessions(user_id, active) VALUES (:u, true);
COMMIT;   -- concurrent conflicting txn gets a serialization error -> retry
```

**Result.** Concurrent logins can't both slip past the limit; the engine serializes the conflicting pair (one retries), upholding the rule.

**Future improvements.** Handle the serialization-failure error with a retry loop (expected under Serializable).

### 2.6 Exercises

1. Name three anomalies and the level that first prevents each.
2. Why isn't everyone on Serializable by default?
3. What is write skew and which level prevents it?

### 2.7 Challenges

- **Challenge.** Find an invariant enforced by count-then-write in your code. Under the default isolation, can two concurrent transactions both pass? Fix with Serializable or a lock.

### 2.8 Checklist

- [ ] I know what anomalies my default level allows.
- [ ] I raise isolation where correctness demands it.
- [ ] I handle serialization failures with retries.
- [ ] I use the weakest level that's still correct per operation.

### 2.9 Best practices

- Match isolation level to each operation's correctness needs.
- Expect and retry serialization failures under Serializable.
- Don't assume the default prevents all anomalies.

### 2.10 Anti-patterns

- Assuming the default level is fully isolated.
- Count-then-insert invariants under weak isolation.
- Using Serializable everywhere, ignoring its abort/retry cost.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Rare invariant violations under load | Weak isolation / write skew | Raise to Serializable or lock |
| Stale value used in a decision | Non-repeatable read | Use Repeatable Read or re-check |
| Serialization errors appearing | Serializable conflicts (expected) | Add a retry loop |

### 2.12 References

- A. Silberschatz, H. Korth, S. Sudarshan, *Database System Concepts*, 7th ed. (McGraw-Hill, 2019), Chapter 17 "Transactions" — §17.5 Transaction Isolation, §17.8 Transaction Isolation Levels — ISBN 978-0078022159.
- PostgreSQL docs, "Transaction Isolation": https://www.postgresql.org/docs/current/transaction-iso.html.

---

> **End of Part I.** You can now reason about transactions: the ACID guarantees (especially atomicity for boundaries and isolation as the tunable one), and the isolation levels that trade strictness for concurrency by permitting or preventing dirty reads, non-repeatable reads, and phantoms — choosing the weakest level that's still correct per operation. **Part II — Mechanisms** (Chapter 3) covers how engines actually enforce isolation: pessimistic locking versus multi-version concurrency control (MVCC), the model behind PostgreSQL and most modern databases.

---

## Part II – Mechanisms

Part I described *what* each isolation level promises. Part II explains *how* an engine delivers it. Two mechanisms do almost all the work, and the one your database uses explains its behavior under contention: whether readers block writers, why a "lost" row is actually an old version, and where deadlocks come from.

---

## Chapter 3 — How engines enforce isolation (locking and MVCC)

### 3.1 Introduction

An isolation level is a promise; **concurrency control** is the machinery that keeps it. Two families dominate. **Pessimistic** control (two-phase locking, 2PL) assumes conflicts will happen and prevents them with **locks** — a transaction must hold a lock before it reads or writes, so conflicting transactions wait. **Optimistic / multi-version** control (MVCC) assumes conflicts are rare and lets transactions proceed on their own **snapshot** of the data, checking for conflicts only at commit. PostgreSQL, Oracle, MySQL/InnoDB, and SQL Server (in its snapshot modes) are all MVCC. Knowing which mechanism runs underneath turns "the database is slow under load" into a specific, diagnosable cause.

### 3.2 Business context

Under load, the *mechanism* — not the SQL — decides whether requests queue, abort, or sail through. A team that does not know its engine is MVCC will misread bloated tables and long-running-transaction warnings; a team that does not know it uses locking will be baffled by deadlocks and lock-wait timeouts. The mechanism also dictates the cheapest correct fix: add a lock, shorten a transaction, or retry an aborted one. Getting this wrong wastes incident time and ships fragile workarounds.

### 3.3 Theoretical concepts: locks vs versions

```mermaid
flowchart TB
    twopl["2PL (pessimistic): acquire locks, hold to commit, then release<br/>conflicting txns WAIT — readers can block writers"]
    mvcc["MVCC (multi-version): each txn reads a consistent SNAPSHOT<br/>writes create new versions — readers never block writers"]
```

- **Two-phase locking (2PL).** A transaction acquires locks in a **growing** phase and releases them only in a **shrinking** phase (in practice, at commit). This serializes conflicting access but means a write can block a read and vice versa, and two transactions waiting on each other's locks **deadlock** — the engine detects the cycle and aborts a victim.
- **MVCC.** Every write creates a **new version** of a row tagged with the transaction that made it; it does not overwrite the old one. A reading transaction sees the snapshot consistent with its start, so **readers never block writers and writers never block readers**. The old versions are cleaned up later (PostgreSQL's `VACUUM`).

**Snapshot isolation** is MVCC's headline level: every statement (or transaction) reads a frozen, consistent snapshot — eliminating dirty and non-repeatable reads without a single read lock.

### 3.4 Architecture: write conflicts and the cost of each model

```mermaid
flowchart LR
    w1["Txn A updates row R"] --> ver["MVCC: new version of R, old kept"]
    w2["Txn B updates same row R"] --> wait["B waits for A, then re-checks"]
    wait --> outcome["A commits -> B sees conflict -> abort/retry (or proceed if no overlap)"]
```

MVCC makes reads cheap but does not make *write* conflicts disappear: two transactions updating the **same row** still serialize, and under snapshot isolation a **write skew** anomaly can slip through (two transactions each read a shared invariant, then write — both pass their own snapshot, together they break it). The fixes are *Serializable Snapshot Isolation* (PostgreSQL's `SERIALIZABLE`, which tracks read/write dependencies and aborts a transaction that would violate serializability) or an explicit lock (`SELECT … FOR UPDATE`). The costs differ: 2PL pays in **blocking and deadlocks**; MVCC pays in **version bloat and aborts** that the application must retry.

### 3.5 Real example

**Scenario.** A PostgreSQL app reports occasional `could not serialize access` errors and, separately, tables that keep growing even though row counts are flat.

**Problem.** The team treats both as bugs. They are both MVCC behaving as designed: the serialization errors are `SERIALIZABLE` aborting a conflicting transaction; the growth is **dead tuples** (old row versions) awaiting `VACUUM`.

**Solution.** Wrap the serializable transaction in a **retry loop** (the abort is expected, not a failure), and ensure autovacuum keeps up with the dead-version churn. For a specific invariant that snapshot isolation alone can't hold, take an explicit row lock.

**Implementation (the two fixes).**

```sql
-- 1. Lock the rows whose invariant you are about to depend on (prevents write skew)
BEGIN;
SELECT balance FROM accounts WHERE id = 42 FOR UPDATE;   -- pessimistic lock under MVCC
UPDATE accounts SET balance = balance - 100 WHERE id = 42;
COMMIT;

-- 2. Under SERIALIZABLE, treat a serialization failure as "retry", not "error"
--    (application pseudocode)
--    retry up to N times on SQLSTATE 40001 before surfacing the error
```

**Result.** The serialization aborts are retried transparently; the invariant is held by the explicit lock; autovacuum reclaims the old versions so tables stop bloating. Each symptom now maps to a deliberate MVCC mechanism, not a mystery.

**Future improvements.** Monitor long-running transactions — under MVCC they pin old versions and block vacuum, the root cause of most "unexplained bloat." Alert on transaction age.

### 3.6 Exercises

1. Under 2PL, why can a read block a write? Under MVCC, why can't it?
2. What does a write to a row physically do under MVCC, and what must clean it up afterward?
3. Snapshot isolation prevents dirty and non-repeatable reads but allows **write skew** — why, and what are two ways to prevent it?

### 3.7 Challenges

- **Challenge.** On your database, run two concurrent transactions that update the same row and observe the wait. Then run two that update *different* rows under `SERIALIZABLE` with a shared read invariant and trigger a serialization failure. Explain each outcome in terms of locks vs versions.

### 3.8 Checklist

- [ ] I know whether my engine uses 2PL, MVCC, or both.
- [ ] I understand readers don't block writers under MVCC — and what that costs (version bloat, vacuum).
- [ ] I treat serialization failures as retryable, not as bugs.
- [ ] I use `SELECT … FOR UPDATE` to hold an invariant snapshot isolation can't.
- [ ] I watch long-running transactions because they pin old versions.

### 3.9 Best practices

- Keep transactions short — under MVCC, long ones block vacuum; under 2PL, they hold locks longer.
- Wrap `SERIALIZABLE` transactions in a bounded retry loop.
- Reach for an explicit row lock only for the specific invariant that needs it.
- Keep autovacuum (or the equivalent) healthy so old versions are reclaimed.

### 3.10 Anti-patterns

- Treating expected serialization aborts as application errors instead of retrying.
- Long-lived transactions that pin old row versions and starve vacuum.
- Locking everything `FOR UPDATE` "to be safe," reintroducing the blocking MVCC avoids.
- Assuming snapshot isolation is fully serializable (ignoring write skew).

### 3.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| `could not serialize access` errors | `SERIALIZABLE` aborting a real conflict (by design) | Retry the transaction on SQLSTATE 40001 |
| Deadlock detected / victim aborted | Cyclic lock waits under 2PL / `FOR UPDATE` | Order locks consistently; shorten transactions; retry |
| Tables grow while row counts are flat | MVCC dead tuples not reclaimed | Ensure autovacuum keeps up; find blocking long transactions |
| Rare invariant violation under load | Write skew under snapshot isolation | Use `SERIALIZABLE` or lock the read rows `FOR UPDATE` |

### 3.12 References

- A. Silberschatz, H. Korth, S. Sudarshan, *Database System Concepts*, 7th ed. (McGraw-Hill, 2019), Chapter 18 "Concurrency Control" — §18.1 Two-Phase Locking, §18.7 Multiversion Schemes, §18.8 Snapshot Isolation — ISBN 978-0078022159.
- PostgreSQL docs, "Concurrency Control" (MVCC, snapshot & serializable): https://www.postgresql.org/docs/current/mvcc.html.

---

> **End of guide.** You can now reason about transactions and concurrency end to end: the **ACID** guarantees and the **isolation levels** that trade strictness for concurrency (Part I), and the **mechanisms** that enforce them (Part II) — **pessimistic 2PL**, where conflicting transactions wait and can deadlock, versus **MVCC**, where every write is a new version and readers never block writers, at the cost of version bloat and retryable aborts. The through-line: pick the weakest isolation that stays correct, know which mechanism your engine uses, and let that knowledge name the cheapest correct fix for contention.
