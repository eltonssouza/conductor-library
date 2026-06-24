---
software_dev: supporting
---

# Secure Code Review - Complete Professional Guide

> **Category:** 09_security_and_privacy · **Language:** English

---

### Auditing code for vulnerabilities with taint analysis
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches secure code review from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** secure code review finds vulnerabilities by reading code systematically, especially by tracing how untrusted data flows to dangerous operations. This guide covers the auditing mindset and taint analysis (source → sink), current to 2026 (SAST tooling).

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to code auditing | Part I |
| 2 — Intermediate | Reviewing for security | Part II |

**Target audience:** developers and security engineers reviewing code for vulnerabilities.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes the web-security and threat-modeling guides.

---

## Table of Contents

**Part I – Method**
1. The auditing mindset
2. Taint analysis: tracing source to sink

**Part II – Coverage**
3. Trust boundaries and where bugs cluster

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – Method

Reviewing code for security is different from reviewing for correctness: you read **adversarially**, asking "how could an attacker abuse this?" rather than "does it do what's intended?" The most productive technique is **taint analysis** — following untrusted input from where it enters (a **source**) to where it could cause harm (a **sink**) — because that path is where vulnerabilities live.

---

## Chapter 1 — The auditing mindset

### 1.1 Introduction

Security code review requires an **adversarial mindset**: assume inputs are hostile, look for what the code *fails* to defend against, and focus on the highest-risk areas rather than reading everything uniformly. You're hunting for the assumptions the developer made that an attacker can violate — unchecked input, missing authorization, unsafe operations on untrusted data.

### 1.2 Business context

Vulnerabilities found in review are far cheaper than those found by attackers. But reviewing all code equally is inefficient; a focused, risk-driven audit (input handling, auth, sensitive operations) finds the serious bugs fast. Skilled secure review — and the SAST tools that automate parts of it — is a high-leverage defense, catching whole vulnerability classes before release. The business value is fewer breaches at a fraction of the post-incident cost.

### 1.3 Theoretical concepts: read for what's missing

```mermaid
flowchart LR
    code["Code"] --> ask["Ask: how can this be abused?"]
    ask --> focus["Focus: untrusted input, auth, dangerous sinks"]
    focus --> missing["Look for MISSING checks/encoding/authorization"]
```

Prioritize by risk: input parsing, authentication/authorization, cryptography, file/command/DB operations, and anything crossing a trust boundary. The bug is usually an **absence** — a validation not done, an authorization not checked, encoding not applied. Combine manual review (judgment, business logic) with **SAST** tools (scale, known patterns); each catches what the other misses.

### 1.4 Architecture: risk-driven attention

```mermaid
flowchart TB
    surface["Attack surface: inputs, boundaries, sensitive ops"] --> review["Concentrate review here"]
    review --> tools["SAST automates pattern-finding"]
    review --> human["Humans find logic/auth flaws"]
```

### 1.5 Real example

**Scenario.** Reviewing an endpoint that returns a user's document by id.

**Problem.** A correctness review confirms it returns the right document; a security review asks "can I read *someone else's*?"

**Solution.** Adversarial reading reveals a missing authorization check (an IDOR / broken access control bug).

**Implementation (what the audit finds).**

```java
// Correctness: returns the document for the given id -> "works"
Document get(long id) { return repo.findById(id); }   // BUG: no ownership check!

// Secure review asks: is the caller allowed THIS id?
Document get(long id, User caller) {
    Document d = repo.findById(id);
    if (!d.ownerId().equals(caller.id())) throw new ForbiddenException(); // missing check
    return d;
}
```

**Result.** The audit catches that any user could fetch any document by guessing ids (a classic broken-access-control flaw) — invisible to a correctness review but obvious to an adversarial one. The fix is the missing authorization check.

**Future improvements.** Add an authorization test asserting cross-user access is denied; apply the check pattern across all id-based endpoints.

### 1.6 Exercises

1. How does security review differ from correctness review?
2. Why is a vulnerability usually an "absence"?
3. Where should review attention concentrate?

### 1.7 Challenges

- **Challenge.** Take an endpoint that fetches a resource by id. Review it adversarially: can a user access another's resource? If the ownership check is missing, that's the bug.

### 1.8 Checklist

- [ ] I read adversarially ("how can this be abused?").
- [ ] I focus on input, auth, and sensitive operations.
- [ ] I look for missing checks/encoding/authorization.
- [ ] I combine manual review with SAST.

### 1.9 Best practices

- Prioritize high-risk code (boundaries, auth, dangerous sinks).
- Hunt for absent defenses, not just present bugs.
- Pair human judgment with automated SAST.

### 1.10 Anti-patterns

- Reviewing all code uniformly, missing the risky parts.
- Only checking correctness, never abuse cases.
- Relying solely on tools (miss logic/auth flaws) or solely on humans (miss scale).

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Auth bugs slip through | Correctness-only review | Review adversarially for access control |
| Vulnerabilities missed at scale | No SAST | Add automated scanning |
| Tool noise, real bugs missed | Tools only | Add focused human review |

### 1.12 References

- M. Dowd, J. McDonald, J. Schuh, *The Art of Software Security Assessment* (Addison-Wesley, 2006) — ISBN 978-0321444424.
- OWASP, "Code Review Guide": https://owasp.org/www-project-code-review-guide/.

---

## Chapter 2 — Taint analysis: source to sink

### 2.1 Introduction

**Taint analysis** is the core technique of vulnerability hunting: treat data from untrusted **sources** (user input, network, files) as "tainted," and trace whether it can reach a dangerous **sink** (a SQL query, an HTML page, an OS command, a file path) **without being sanitized**. A tainted source reaching a sink unsanitized *is* a vulnerability. Following these flows finds injection, XSS, path traversal, and more.

### 2.2 Business context

Most high-severity web vulnerabilities are a tainted-data-reaches-sink problem (SQL injection, XSS, command injection, SSRF, path traversal). Taint analysis gives reviewers a systematic, repeatable way to find them instead of hoping to spot them. It's also what modern SAST tools automate. Teams that think in source→sink terms catch these classes consistently, dramatically reducing the vulnerabilities that reach production and get exploited.

### 2.3 Theoretical concepts: source → (sanitizer?) → sink

```mermaid
flowchart LR
    source["SOURCE: untrusted input"] --> flow["data flow through code"]
    flow --> san{"Sanitized/validated?"}
    san -- "no" --> sink["SINK: dangerous operation -> VULNERABILITY"]
    san -- "yes" --> safe["Safe"]
```

To audit, enumerate **sources** (request params, headers, body, files, env), enumerate **sinks** (DB queries, HTML output, `exec`, file paths, redirects, deserialization), and for each source-to-sink path ask: is the data **sanitized appropriately for that sink** in between? A correct sanitizer for one sink (HTML-encoding) may be wrong for another (SQL) — sanitization must match the sink.

### 2.4 Architecture: trace each path

```mermaid
flowchart TB
    src["Sources (inputs)"] --> paths["Trace data flows"]
    paths --> sinks["Sinks (dangerous ops)"]
    paths --> check["Each path: sanitized for THIS sink?"]
```

### 2.5 Real example

**Scenario.** A file-download endpoint takes a filename parameter.

**Problem.** The filename (a tainted source) is used to build a file path (a sink) with no sanitization → **path traversal** (`../../etc/passwd`).

**Solution.** Taint analysis flags the source→sink path; add validation that confines the path to the intended directory.

**Implementation (close the tainted path).**

```java
// VULNERABLE: tainted 'name' flows to a file-path sink unsanitized
File f = new File(baseDir, request.getParameter("name"));  // ../../ -> traversal

// SAFE: validate/canonicalize; confine to baseDir (sanitizer matched to the sink)
Path base = baseDir.toPath().toRealPath();
Path target = base.resolve(name).normalize().toRealPath();
if (!target.startsWith(base)) throw new ForbiddenException();  // reject traversal
```

**Result.** The tainted filename can no longer escape the intended directory; the path-traversal vulnerability on this source→sink path is closed. Systematic taint tracing found it.

**Future improvements.** Map all sources and sinks in the app; let SAST continuously check these flows in CI.

### 2.6 Exercises

1. Define source, sink, and tainted data.
2. Why must a sanitizer match the specific sink?
3. Trace a source→sink path for a vulnerability you know.

### 2.7 Challenges

- **Challenge.** Pick an endpoint. List its sources (inputs) and sinks (dangerous ops). For each source→sink path, check whether the data is sanitized for that sink. Find one gap.

### 2.8 Checklist

- [ ] I enumerate untrusted sources.
- [ ] I enumerate dangerous sinks.
- [ ] I trace each source→sink path for sanitization.
- [ ] Sanitizers match their specific sink.

### 2.9 Best practices

- Think in source→sink flows when auditing.
- Match sanitization to each sink's context.
- Automate taint checks with SAST in CI.

### 2.10 Anti-patterns

- Assuming "we sanitize input" covers all sinks (wrong sanitizer).
- Untracked data flows from input to dangerous operations.
- Relying on one global filter for every sink.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Injection/traversal bugs | Tainted source reaches sink unsanitized | Trace and sanitize per sink |
| Sanitization didn't help | Wrong sanitizer for the sink | Match sanitizer to the sink context |
| Recurring vuln classes | No systematic taint analysis | Adopt source→sink review + SAST |

### 2.12 References

- M. Dowd, J. McDonald, J. Schuh, *The Art of Software Security Assessment* (Addison-Wesley, 2006) — ISBN 978-0321444424.
- OWASP, "Source and Sink" / SAST guidance: https://owasp.org.

---

> **End of Part I.** You can now review code for security: read adversarially (hunting the missing defense, focused on high-risk areas, combining human judgment with SAST), and apply taint analysis — tracing untrusted data from sources to dangerous sinks and verifying it's sanitized appropriately for each sink along the way. **Part II — Coverage** (Chapter 3) covers using trust boundaries to drive review scope and the categories of bug that cluster at each boundary, so audits are systematic rather than ad hoc.

<!--APPEND-PART-II-->
