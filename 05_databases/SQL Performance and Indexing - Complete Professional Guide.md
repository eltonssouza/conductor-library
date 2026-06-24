---
software_dev: core
---

# SQL Performance and Indexing - Complete Professional Guide

> **Category:** 05_databases · **Language:** English

---

### How indexes work and how to read what the database is doing
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches SQL performance from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** most SQL performance problems are **indexing** problems, and most are diagnosed by reading the **execution plan**. This guide explains how B-tree indexes work, the rules for designing them (including composite-column order), and how to read a plan — current to 2026 engines (PostgreSQL/MySQL).

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to indexing | Part I |
| 2 — Intermediate | Designing indexes | Part II |

**Target audience:** application developers who write queries and need them to be fast.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes basic SQL and WHERE/ORDER BY.

---

## Table of Contents

**Part I – Indexes**
1. How a B-tree index works
2. Composite indexes and column order

**Part II – Diagnosis**
3. Reading the execution plan

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – Indexes

An index is a separate, sorted data structure that lets the database find rows without scanning the whole table — like a book's index versus reading every page. Understanding how indexes work, and designing them for your real queries, is the single highest-leverage database performance skill.

---

## Chapter 1 — How a B-tree index works

### 1.1 Introduction

The default index type is the **B-tree** (balanced tree): a sorted, multi-level structure that lets the database locate a value in logarithmic time. Because it keeps entries **sorted**, a B-tree accelerates equality lookups (`= x`), range scans (`BETWEEN`, `<`, `>`), and ordered reads (`ORDER BY`) on the indexed column(s).

### 1.2 Business context

A missing or wrong index is the most common cause of a query that's fast on test data and unusably slow in production — performance that silently degrades as the table grows. Understanding indexes lets developers prevent these problems at design time rather than firefighting them after an outage. Indexes are also a trade-off (they speed reads but slow writes and use space), so knowing how they work is needed to choose well.

### 1.3 Theoretical concepts: sorted lookup

```mermaid
flowchart TB
    root["B-tree root"] --> b1["branch"]
    root --> b2["branch"]
    b1 --> leaf1["leaf: sorted keys -> row pointers"]
    b2 --> leaf2["leaf: sorted keys -> row pointers"]
```

The B-tree's branches narrow the search at each level; leaves hold the sorted keys pointing to rows. Logarithmic depth means even a billion-row table is a handful of steps deep. Because keys are sorted, the index serves three things: **point lookups**, **range scans**, and **sorted order** — the basis of every indexing decision.

### 1.4 Architecture: index vs table scan

```mermaid
flowchart LR
    q["WHERE email = 'a@b.com'"] --> idx{"Index on email?"}
    idx -- "yes" --> seek["Index seek: O(log n) -> few rows"]
    idx -- "no" --> scan["Full table scan: O(n) -> read everything"]
```

With an index the engine seeks straight to matching rows; without one it scans the whole table. On large tables that's the difference between milliseconds and seconds.

### 1.5 Real example

**Scenario.** Users are looked up by email at login.

**Problem.** No index on `email`; every login scans the whole `users` table — fine at 1k rows, terrible at 10M.

**Solution.** Add a B-tree index (and a uniqueness constraint, which creates one).

**Implementation.**

```sql
-- creates a B-tree index AND enforces uniqueness
ALTER TABLE users ADD CONSTRAINT users_email_unique UNIQUE (email);

-- now this is an index seek, not a full scan
SELECT id, password_hash FROM users WHERE email = :email;
```

**Result.** Login lookups go from O(n) scans to O(log n) seeks; latency stays flat as the table grows.

**Future improvements.** Verify with the execution plan (Chapter 3) that the index is actually used.

### 1.6 Exercises

1. Why does a sorted B-tree help equality, range, and ORDER BY?
2. What's the cost trade-off of adding an index?
3. What's the difference between an index seek and a table scan?

### 1.7 Challenges

- **Challenge.** Find a frequent `WHERE col = ?` query with no index on `col`. Add one and compare the execution plan and timing before/after on realistic data.

### 1.8 Checklist

- [ ] I understand B-trees serve equality, ranges, and order.
- [ ] I index columns used in frequent WHERE/JOIN/ORDER BY.
- [ ] I weigh read speed against write/space cost.
- [ ] Uniqueness constraints give me an index too.

### 1.9 Best practices

- Index the columns your hot queries filter, join, and sort on.
- Use unique constraints for natural keys (they index too).
- Don't over-index — each index taxes writes and storage.

### 1.10 Anti-patterns

- No index on frequently filtered columns.
- Indexing everything, slowing writes needlessly.
- Assuming small-data speed will hold at scale.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Query fast in dev, slow in prod | Missing index, full scan at scale | Add an index on the filter column |
| Writes slowing down | Too many indexes | Remove unused ones |
| Lookup still slow with an index | Index not used (see Ch. 3) | Check the execution plan |

### 1.12 References

- M. Winand, *SQL Performance Explained* (2012) — ISBN 978-3950307825; also https://use-the-index-luke.com.
- PostgreSQL docs, "Indexes": https://www.postgresql.org/docs/current/indexes.html.

---

## Chapter 2 — Composite indexes and column order

### 2.1 Introduction

A **composite index** covers multiple columns, and the **order of those columns matters enormously**. A composite index on `(a, b)` works like a phone book sorted by last name then first name: great for "find by last name" or "last + first," useless for "find by first name alone." This leftmost-prefix rule governs composite index design.

### 2.2 Business context

Getting composite-index column order wrong is a subtle, common cause of "I added an index but it's still slow." Understanding the leftmost-prefix rule lets developers design one well-ordered index that serves several queries, instead of piling on redundant single-column indexes (which bloat writes and storage). It's the difference between a lean, effective index strategy and an expensive, ineffective one.

### 2.3 Theoretical concepts: leftmost prefix

```mermaid
flowchart LR
    idx["INDEX (a, b, c)"] --> uses["serves: a · a,b · a,b,c · a + range on b"]
    idx --> nope["does NOT serve: b alone · c alone · b,c"]
```

A composite index can be used for queries that filter on a **leftmost prefix** of its columns: `(a)`, `(a, b)`, `(a, b, c)`. It cannot efficiently serve a query filtering only on `b` or `c`. Put the most **selective**, most-often-equality-filtered columns first; a column used only for ranges typically goes last.

### 2.4 Architecture: one index, many queries

```mermaid
flowchart TB
    q1["WHERE tenant_id = ?"] --> idx["INDEX (tenant_id, created_at)"]
    q2["WHERE tenant_id = ? ORDER BY created_at"] --> idx
    q3["WHERE tenant_id = ? AND created_at > ?"] --> idx
```

A well-ordered composite index serves equality on the first column plus range/sort on the next — covering several common query shapes with one structure.

### 2.5 Real example

**Scenario.** A multi-tenant app lists a tenant's recent orders: `WHERE tenant_id = ? ORDER BY created_at DESC`.

**Problem.** Separate indexes on `tenant_id` and `created_at` don't serve the combined filter-then-sort well.

**Solution.** One composite index `(tenant_id, created_at)` — equality on tenant, ordered by date.

**Implementation.**

```sql
CREATE INDEX idx_orders_tenant_created ON orders (tenant_id, created_at DESC);

-- served efficiently: seek to tenant, read already-sorted by created_at
SELECT * FROM orders
WHERE tenant_id = :tenant
ORDER BY created_at DESC
LIMIT 20;
```

**Result.** The engine seeks to the tenant's rows already sorted by date — no separate sort step, no scan. One index serves the filter and the order.

**Future improvements.** If queries also filter by status, consider `(tenant_id, status, created_at)` — order by selectivity and usage.

### 2.6 Exercises

1. State the leftmost-prefix rule.
2. Why does `INDEX (a, b)` not help a query filtering only on `b`?
3. Where should a range-filtered column go in a composite index?

### 2.7 Challenges

- **Challenge.** Take a query with an equality filter plus an ORDER BY. Design a single composite index that serves both and verify the plan drops the sort step.

### 2.8 Checklist

- [ ] I order composite columns by selectivity and query usage.
- [ ] Equality columns come before range columns.
- [ ] I rely on the leftmost-prefix rule, not redundant indexes.
- [ ] One composite index serves multiple query shapes where possible.

### 2.9 Best practices

- Put the most selective equality columns first.
- Place a single range/sort column last.
- Prefer one well-ordered composite over many single-column indexes.

### 2.10 Anti-patterns

- Composite column order that ignores the query's filters.
- Many overlapping single-column indexes "just in case."
- A range column early, blocking use of later columns.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Index added but unused | Wrong column order / not a prefix | Reorder to match the query's filters |
| Extra sort step in the plan | Order-by column not in index order | Add it after the equality column |
| Too many indexes, slow writes | Redundant single-column indexes | Consolidate into composites |

### 2.12 References

- M. Winand, *SQL Performance Explained* (2012) — ISBN 978-3950307825; also https://use-the-index-luke.com.
- MySQL docs, "Multiple-Column Indexes": https://dev.mysql.com/doc/refman/en/multiple-column-indexes.html.

---

> **End of Part I.** You can now reason about indexing: how a B-tree serves equality, range, and ordered reads, and how composite-index column order (the leftmost-prefix rule) lets one well-designed index serve several query shapes. **Part II — Diagnosis** (Chapter 3) teaches reading the execution plan (EXPLAIN) so you can see whether your indexes are actually used, spot full scans and missing-index sorts, and verify a fix.

<!--APPEND-PART-II-->
