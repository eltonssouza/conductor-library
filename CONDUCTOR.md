# Using this library with Conductor

This repository is the **reference-book corpus** behind [Conductor](https://github.com/eltonssouza/conductor-main) — the long-term **Library (RAG)** memory that grounds Conductor's answers in "what good engineering practice says" instead of model memory.

You do **not** install this repo by hand. Conductor fetches and indexes it for you during its own installation. This document explains how that works and how to point Conductor at a fork/branch.

---

## How Conductor consumes the library

```
cdt up
  │
  ├─ fetch  ──►  github.com/<CONDUCTOR_LIBRARY_REPO>@<CONDUCTOR_LIBRARY_REF>   (this repo)
  ├─ pull   ──►  bge-m3 embedding model (Ollama, GPU if available)
  └─ ingest ──►  every .md → chunked → embedded → upserted into ChromaDB
```

- **Fetch.** `cdt up` clones this repo (default `eltonssouza/conductor-library@main`). Nothing is downloaded by hand.
- **Category.** Each chunk's `category` metadata is the **top-level folder name** (`00_academic_curriculum`, `03_design_and_architecture`, …). That is the unit `cdt library --category` filters on.
- **Ingest is incremental.** Each chunk stores a content hash, so re-running only re-embeds new or changed files.

See the Conductor README's *Installation* and *The Docker backends → RAG stack (`cdt up`)* sections for the full install flow.

---

## Install / wire-up (from the Conductor side)

```bash
# 1. Install Conductor (once)
pipx install conductor

# 2. Start the RAG stack — fetches THIS repo and indexes it
cdt up                    # attached; or `cdt up -d` for detached

# 3. Ground an answer in the books
cdt library "STRIDE threat model"
cdt library --category 09_security_and_privacy "data minimization"
```

To index a fork or branch instead of the default corpus, set the environment variables below **before** `cdt up`.

---

## Environment variables that point at this repo

| Variable | Default | Purpose |
|----------|---------|---------|
| `CONDUCTOR_LIBRARY_REPO` | `eltonssouza/conductor-library` | GitHub repo the corpus is fetched from on `cdt up` |
| `CONDUCTOR_LIBRARY_REF` | `main` | branch/tag of this repo to fetch |
| `CONDUCTOR_LIBRARY_ARCHIVE` | _(unset)_ | optional offline seed: a mounted `.7z` used instead of the repo fetch |
| `CONDUCTOR_LIBRARY` | `~/.conductor/library` (host) · `/data/library` (container) | corpus markdown root |

---

## Corpus contract (what Conductor relies on)

Conductor's ingest assumes the standard defined in [`FILE_CONVENTIONS.md`](FILE_CONVENTIONS.md):

1. **English only, no images** — clean text, no binary/figure noise in the index.
2. **Top-level folder = category** — `NN_topic`; the folder name is the RAG `category` filter.
3. **Standard header per file** — title + author/edition/category metadata for traceable citations.
4. **`software_dev` frontmatter tier** — every content file is tagged `core | supporting | foundational | optional` (see `FILE_CONVENTIONS.md` §4). Use it to filter the corpus to software-development-relevant material:
   - `core` + `supporting` → everything used while building software,
   - `+ foundational` → adds the CS base (algorithms, OS, networks, compilers),
   - `optional` → pure math/theory/hardware, usually excluded from dev grounding.

When adding books, keep these invariants so Conductor keeps fetching, chunking, and citing the corpus cleanly.

---

## Related documents

- [`README.md`](README.md) — navigable index of the whole corpus.
- [`FILE_CONVENTIONS.md`](FILE_CONVENTIONS.md) — the universal file standard (naming, format, frontmatter).
- [`ROLES_AND_ACRONYMS.md`](ROLES_AND_ACRONYMS.md) — tech roles glossary (matches Conductor's role agents).
- [`AGENTS_AND_SKILLS_BY_ROLE.md`](AGENTS_AND_SKILLS_BY_ROLE.md) — Agent prompt + Skill per role; mirrors the agents Conductor scaffolds into `.claude/`.
