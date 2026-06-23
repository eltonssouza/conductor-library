# Using this library with Conductor

This repository is the **reference-book corpus** behind [Conductor](https://github.com/eltonssouza/conductor-main) — the long-term **Library (RAG)** memory that grounds Conductor's answers in "what good engineering practice says" instead of model memory.

You do **not** install this repo by hand. Conductor fetches and indexes it for you during its own installation. This document explains how that works and how to point Conductor at a fork/branch.

---

## How Conductor consumes the library

```
cdt up
  │
  ├─ fetch  ──►  github.com/<CONDUCTOR_LIBRARY_REPO>@<CONDUCTOR_LIBRARY_REF>   (this repo)
  │             keep only the SELECTED books (tier + stack)
  ├─ pull   ──►  bge-m3 embedding model (Ollama, GPU if available)
  └─ ingest ──►  selected .md → chunked → embedded → upserted into ChromaDB
```

- **Fetch.** `cdt up` downloads this repo (default `eltonssouza/conductor-library@main`) and writes to disk **only the books matching your selection** (see *Choosing what to ingest*). Nothing is downloaded by hand.
- **Category.** Each chunk's `category` metadata is the **top-level folder name** (`00_academic_curriculum`, `03_design_and_architecture`, …). That is the unit `cdt library --category` filters on.
- **Ingest is incremental.** Each chunk stores a content hash, so re-running only re-embeds new or changed files.

See the Conductor README's *Installation* and *The Docker backends → RAG stack (`cdt up`)* sections for the full install flow.

---

## Install / wire-up (from the Conductor side)

```bash
# 1. Install Conductor (once) — see the Conductor README for the one-liner
#    (curl … | sh  /  irm … | iex). It installs from the git repo, not PyPI.

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
| `CONDUCTOR_LIBRARY_TIERS` | `core` | comma list of `software_dev` tiers to ingest (`core,supporting,foundational,optional`) |
| `CONDUCTOR_LIBRARY_STACKS` | _(none)_ | comma list of languages/frameworks to add (e.g. `python,angular`), or `all` |

---

## Choosing what to ingest

The repo is downloaded once, but **only the selected books are written to disk —
and thus chunked and embedded** into ChromaDB. So a Java + Angular dev never even
extracts the Ruby/Go/React books, and the index stays small and on-topic.

**Auto-selection (default).** Run `cdt up` from a project and Conductor detects
its stack and ingests the matching books automatically — `cdt detect` shows what
it would pick. The library is one global index, so the choice **accumulates**:
work on an Angular app today and a Go service tomorrow, and the index grows to
cover both. Override or pin it explicitly with the two dials below, read at
`cdt up`:

- **Tiers** (`CONDUCTOR_LIBRARY_TIERS`, default `core`) — language-agnostic
  `software_dev` tiers. The default is `core` only: the engineering craft that
  doesn't depend on a language. Widen with
  `CONDUCTOR_LIBRARY_TIERS=core,supporting` (DevOps, security, product, UX).
- **Stacks** (`CONDUCTOR_LIBRARY_STACKS`, default none) — `software_dev: stack`
  books carry a `stack: <id>` field and are **opt-in**: add the ones you use.
  `CONDUCTOR_LIBRARY_STACKS=python,angular` adds those; `all` adds every stack.
- **Edition (`stack@major`)** — pin a version with `stack@major`
  (`java@25,spring@4,angular@21`). It resolves to the **nearest** `version` book
  (ties prefer the higher), so an Angular 21 project still grounds in the Angular
  22 book. A bare `stack` takes every edition.

```bash
cdt up                                                  # default: core, language-agnostic
CONDUCTOR_LIBRARY_STACKS=python,angular cdt up          # + those stacks
CONDUCTOR_LIBRARY_STACKS=java@25,spring@4,angular@21 cdt up   # pin editions (nearest match)
CONDUCTOR_LIBRARY_TIERS=core,supporting CONDUCTOR_LIBRARY_STACKS=all cdt up   # broad
```

Ingest is incremental, so changing the selection and re-running `cdt up` only
adds what's newly included. Available `stack` ids: `java`, `javascript`, `node`,
`python`, `go`, `ruby`, `rails`, `angular`, `react-native`, `graphql`, `n8n`,
`hermes`, `php`, `rust`, `dotnet`, `react`, `vue`, `svelte`, `nextjs`,
`spring`, `nestjs`, `express`, `fastify`, `django`, `fastapi`, `flask`,
`flutter`, `swift`.

---

## Corpus contract (what Conductor relies on)

Conductor's ingest assumes the standard defined in [`FILE_CONVENTIONS.md`](FILE_CONVENTIONS.md):

1. **English only, no images** — clean text, no binary/figure noise in the index.
2. **Top-level folder = category** — `NN_topic`; the folder name is the RAG `category` filter.
3. **Standard header per file** — title + author/edition/category metadata for traceable citations.
4. **`software_dev` frontmatter tier** — every content file is tagged `core | stack | supporting | foundational | optional` (see `FILE_CONVENTIONS.md` §4). Use it to filter the corpus to software-development-relevant material:
   - `core` → language-agnostic craft of building software (always relevant),
   - `stack` → a specific language/framework — **the project chooses these** per its detected tech stack (Java, Go, Angular, React Native, …); don't ground in stacks the project doesn't use,
   - `+ supporting` → adjacent delivery disciplines (DevOps, security, product, UX),
   - `+ foundational` → the CS base (algorithms, OS, networks, compilers),
   - `optional` → pure math/theory/hardware, usually excluded from dev grounding.

   This pairs with Conductor's stack detection: select `core` always, then add the `stack` books matching the project's languages/frameworks, and `supporting` by the active roles.

When adding books, keep these invariants so Conductor keeps fetching, chunking, and citing the corpus cleanly.

---

## Related documents

- [`README.md`](README.md) — navigable index of the whole corpus.
- [`FILE_CONVENTIONS.md`](FILE_CONVENTIONS.md) — the universal file standard (naming, format, frontmatter).
- [`ROLES_AND_ACRONYMS.md`](ROLES_AND_ACRONYMS.md) — tech roles glossary (matches Conductor's role agents).
- [`AGENTS_AND_SKILLS_BY_ROLE.md`](AGENTS_AND_SKILLS_BY_ROLE.md) — Agent prompt + Skill per role; mirrors the agents Conductor scaffolds into `.claude/`.
