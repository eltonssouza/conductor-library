---
software_dev: core
---

# SQL Database Antipatterns - Complete Professional Guide

> **Category:** 05_databases · **Language:** English

---

### Common schema and query mistakes, and how to fix them
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches SQL antipatterns from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** the same database mistakes recur across projects — storing lists in a comma-separated column, naive tree storage, relying on implicit behavior. This guide names the most common SQL antipatterns and gives the relational fix for each, current to 2026 engines.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to schema design | Part I |
| 2 — Intermediate | Fixing existing schemas | Part II |

**Target audience:** application developers who design and query relational schemas.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes basic SQL (SELECT/JOIN, primary/foreign keys).

---

## Table of Contents

**Part I – Schema antipatterns**
1. Storing multiple values in one column
2. Naive trees: storing hierarchies with parent_id only

**Part II – Query & integrity antipatterns**
3. Relying on implicit columns and missing constraints

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – Schema antipatterns

Most database pain comes from a handful of schema mistakes that feel convenient at first and become expensive later. Recognizing them by name — and knowing the relational fix — saves projects from data integrity problems and slow, awkward queries down the line.

---

## Chapter 1 — Storing multiple values in one column

### 1.1 Introduction

A frequent antipattern: storing a list of values in a single column as a delimited string (e.g. `tags = "java,sql,web"`). It looks simple but breaks the relational model — you can't index individual values, enforce referential integrity, or query them cleanly. The fix is an **intersection (junction) table**.

### 1.2 Business context

The comma-separated shortcut saves minutes when first writing the schema and costs days later: searching for one tag requires fragile string matching, you can't guarantee a tag exists, and updates are error-prone. Modeling it relationally costs a little more up front but makes the data queryable, indexable, and trustworthy — the difference between a feature that scales and one that's quietly broken.

### 1.3 Theoretical concepts: one value per cell

```mermaid
flowchart LR
    bad["post.tags = 'java,sql,web'<br/>(many values, one cell)"] --> problems["can't index/join/validate per tag"]
    good["post --< post_tag >-- tag<br/>(junction table)"] --> wins["indexable, FK-enforced, queryable"]
```

The relational rule (first normal form) is **one value per cell**. A many-to-many relationship (a post has many tags; a tag belongs to many posts) is modeled with a **junction table** holding one row per (post, tag) pair, with foreign keys to both.

### 1.4 Architecture: the junction table

```mermaid
flowchart TB
    post["posts (id, title)"] --> pt["post_tags (post_id, tag_id)"]
    tag["tags (id, name)"] --> pt
```

`post_tags` has a foreign key to each side; a composite primary key (post_id, tag_id) prevents duplicates. Now every tag is a real, referenceable entity.

### 1.5 Real example

**Scenario.** Posts need tags, and users must be able to find all posts with a given tag.

**Problem.** `posts.tags = "java,sql"` makes "find posts tagged sql" a `LIKE '%sql%'` that also matches "mysql", can't use an index, and lets typos in.

**Solution.** A junction table with foreign keys.

**Implementation.**

```sql
CREATE TABLE tags (
    id   BIGINT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);
CREATE TABLE post_tags (
    post_id BIGINT NOT NULL REFERENCES posts(id),
    tag_id  BIGINT NOT NULL REFERENCES tags(id),
    PRIMARY KEY (post_id, tag_id)
);

-- find posts tagged 'sql' (indexed, exact, integrity-checked)
SELECT p.* FROM posts p
JOIN post_tags pt ON pt.post_id = p.id
JOIN tags t       ON t.id = pt.tag_id
WHERE t.name = 'sql';
```

**Result.** Tag queries are exact and indexed; a tag can't be misspelled into existence; counts and joins are trivial.

**Future improvements.** Add an index on `post_tags(tag_id)` for "posts by tag" lookups.

### 1.6 Exercises

1. Why does a comma-separated value column break the relational model?
2. What is a junction table and when do you need one?
3. Why is `LIKE '%x%'` a poor substitute for a real relationship?

### 1.7 Challenges

- **Challenge.** Find a delimited-list column in a schema you know. Model it as a junction table and rewrite a query against it. Compare correctness and indexability.

### 1.8 Checklist

- [ ] Each cell holds a single value (1NF).
- [ ] Many-to-many uses a junction table.
- [ ] Related values are foreign-keyed.
- [ ] I don't store lists as delimited strings.

### 1.9 Best practices

- Model multi-valued attributes as their own rows.
- Use junction tables with foreign keys for many-to-many.
- Let the database enforce existence and uniqueness.

### 1.10 Anti-patterns

- Comma-separated value columns ("jaywalking").
- Querying lists with `LIKE` substring matches.
- No foreign key, so invalid values creep in.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Tag/category search slow or wrong | Delimited-list column | Move to a junction table |
| Invalid values in a list field | No referential integrity | Foreign-key the values |
| Can't count/join by value | Values not first-class rows | Normalize to rows |

### 1.12 References

- B. Karwin, *SQL Antipatterns* (Pragmatic Bookshelf, 2010) — ISBN 978-1934356555.
- C. Date, *SQL and Relational Theory*, 3rd ed. (O'Reilly, 2015) — ISBN 978-1491941171.

---

## Chapter 2 — Naive trees

### 2.1 Introduction

Hierarchies (categories, comments, org charts) are commonly stored with a single `parent_id` column (the **adjacency list**). That's fine for simple cases, but querying an arbitrary-depth subtree ("all descendants") with plain `parent_id` requires many queries or recursion. Knowing the alternatives — and that modern SQL has **recursive CTEs** — avoids the classic pain.

### 2.2 Business context

Teams often hit a wall when a feature needs "the whole subtree" (all comments under a thread, all sub-categories) and the naive `parent_id` schema forces N+1 queries or application-side recursion that's slow and complex. Choosing the right tree model — or using recursive queries — keeps hierarchy features fast and simple, avoiding a painful schema migration later when the data grows.

### 2.3 Theoretical concepts: tree storage options

```mermaid
flowchart TB
    adj["Adjacency list<br/>(parent_id): simple, hard subtree reads"]
    cte["Adjacency list + recursive CTE<br/>(query whole subtree in one statement)"]
    closure["Closure table<br/>(stores all ancestor-descendant pairs)"]
    path["Materialized path<br/>(stores path string)"]
```

- **Adjacency list** (`parent_id`): trivial inserts; subtree reads are hard without recursion.
- **Recursive CTE**: query an adjacency list's full subtree in **one** statement — the 2026 default for most cases.
- **Closure table**: a separate table of every ancestor→descendant pair; fast subtree/ancestor queries at the cost of more storage and write complexity.
- **Materialized path**: store the path (`/1/4/9/`); easy subtree by prefix, weaker integrity.

### 2.4 Architecture: recursive CTE over an adjacency list

```mermaid
flowchart LR
    node["categories(id, parent_id, name)"] --> cte["WITH RECURSIVE subtree AS (...)"]
    cte --> result["entire subtree, one query"]
```

For most applications, keep the simple `parent_id` schema and use a recursive CTE to read subtrees — no extra tables, supported by all major engines in 2026.

### 2.5 Real example

**Scenario.** Nested categories; you need every descendant of a category.

**Problem.** With only `parent_id`, fetching all descendants meant looping queries in the app.

**Solution.** A recursive CTE returns the whole subtree in one query.

**Implementation.**

```sql
-- categories(id, parent_id, name)
WITH RECURSIVE subtree AS (
    SELECT id, parent_id, name FROM categories WHERE id = :root
    UNION ALL
    SELECT c.id, c.parent_id, c.name
    FROM categories c
    JOIN subtree s ON c.parent_id = s.id
)
SELECT * FROM subtree;
```

**Result.** The full descendant set comes back in a single, index-friendly query — no application recursion, no N+1.

**Future improvements.** If subtree reads dominate and trees are huge, consider a closure table; otherwise the CTE is enough.

### 2.6 Exercises

1. Why is a plain `parent_id` schema awkward for subtree reads?
2. What does a recursive CTE let you do over an adjacency list?
3. When is a closure table worth its extra complexity?

### 2.7 Challenges

- **Challenge.** Take a `parent_id` hierarchy. Write a recursive CTE to fetch a full subtree and an ancestor chain. Measure vs the app-side loop it replaces.

### 2.8 Checklist

- [ ] I know the tree-storage options and their trade-offs.
- [ ] I use recursive CTEs for subtree queries by default.
- [ ] I reach for closure tables only when reads demand it.
- [ ] I don't loop queries in the app to walk trees.

### 2.9 Best practices

- Default to adjacency list + recursive CTE.
- Add a closure table only when subtree reads are hot and large.
- Index `parent_id` for traversal.

### 2.10 Anti-patterns

- Application-side recursion / N+1 to read subtrees.
- Choosing a complex tree model before it's needed.
- No index on the parent column.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Subtree reads do many queries | Naive parent_id loop | Use a recursive CTE |
| Tree reads slow at scale | Repeated recursion | Consider a closure table |
| Slow parent lookups | No index on parent_id | Add the index |

### 2.12 References

- B. Karwin, *SQL Antipatterns* (Pragmatic Bookshelf, 2010) — ISBN 978-1934356555.
- PostgreSQL docs, "WITH Queries (Recursive)": https://www.postgresql.org/docs/current/queries-with.html.

---

> **End of Part I.** You can now spot and fix two pervasive schema antipatterns: storing multiple values in one column (fix: junction tables with foreign keys) and naive tree storage (fix: adjacency list with recursive CTEs, escalating to a closure table only when reads demand it). **Part II — Query & integrity antipatterns** (Chapter 3) covers relying on implicit columns (`SELECT *`, ambiguous defaults) and the cost of skipping constraints that the database could enforce for you.

<!--APPEND-PART-II-->
