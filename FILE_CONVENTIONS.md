# File & Folder Conventions

> This document defines the **universal standard** every file in this library follows: folder layout, file **naming**, and the **internal format** of each `.md` book and reading-list file. Use it as the single source of truth when adding or editing files.
>
> Three rules are absolute and apply to **every** file:
>
> 1. **English only.** No Portuguese (or any other language). Titles, metadata, descriptions, and body text are in English.
> 2. **No images.** No book covers, figures, or embedded image references. (Literal `<img>` text that appears *inside* a book's prose or code examples — e.g. an HTML/JavaScript book teaching the `<img>` tag — is content, not an image, and is kept.)
> 3. **Standard header.** Every file opens with the standard metadata header (section 4), then `---`, then content.

---

## 1. Folder structure

The library is a single corpus, split into topic folders. Each folder name is prefixed with a two-digit number that fixes its display order.

```
.
├── 00_academic_curriculum/         ← academic reading lists (one file per discipline)
├── 01_programming_languages/       ┐  ← languages only (software_dev: stack)
├── 02_algorithms_and_data_structures/ │
├── 03_design_and_architecture/     │
├── 04_engineering_and_practices/   │
├── 05_databases/                   │
├── 06_web_and_frontend/            │  professional books
├── 07_devops_sre_operations/       │  (one full book per file)
├── 08_distributed_systems/         │
├── 09_security_and_privacy/        │
├── 10_ai_and_llm/                  │
├── 11_management_product_process/  │
├── 12_design_ux/                   │
├── 13_automation_and_integration/  │
├── 14_frameworks/                  ┘  ← frameworks/runtimes (software_dev: stack)
├── README.md                       ← navigable index of the whole corpus
├── FILE_CONVENTIONS.md             ← this file (the standard)
├── ROLES_AND_ACRONYMS.md           ← tech roles glossary
└── AGENTS_AND_SKILLS_BY_ROLE.md    ← Agent prompt + Skill per role
```

**Folder-name rule:** `NN_words_separated_by_underscore` — lowercase, English, no spaces, no accents. The number defines ordering (roughly a Computer Engineering track: languages → algorithms → design → engineering → data → web → operations → security → AI → management → design → automation → frameworks). Language and framework books are split into `01_programming_languages/` and `14_frameworks/` so a project can opt into only the stacks it uses.

There are two kinds of content file, and both obey the three absolute rules above.

---

## 2. Academic reading lists — `00_academic_curriculum/`

Each file is the reading list for one discipline. **One language: English.** (These files were previously bilingual; the Portuguese sections have been removed.)

### Naming

```
NN_slug_in_english.md
```

- `NN` = the discipline number from the source curriculum (gaps are expected, e.g. 01, 02, 03, 05, … 34).
- `slug_in_english` = short English identifier, lowercase, underscores (e.g. `digital_circuits`, `theory_of_computation`).

Examples: `01_digital_circuits.md`, `18_database.md`, `31_theory_of_computation.md`.

### File structure

```markdown
# NN — Discipline Title

> Reading list for this discipline.

---

## <Book Title>

| Field | Value |
|-------|-------|
| Authors | … |
| Publication Year | … |
| Edition | … |
| ISBN | … |

### Description

<one descriptive paragraph about the book>

---

## <Next Book Title>
…
```

Rules for each book entry:

1. **`## <Title>`** — the book title as an `H2`. (No cover image precedes it — covers are removed.)
2. **Metadata table** — a markdown table with exactly these fields: `Authors`, `Publication Year`, `Edition`, `ISBN`. Omit a row only if the value is genuinely unknown.
3. **`### Description`** — followed by a single English paragraph.
4. Entries are separated by `---`.

---

## 3. Professional books — `01_*` to `13_*`

Each file is the full text of one book, extracted from EPUB/PDF and converted to `.md`, grouped by topic.

### Naming

```
Title (Edition) - Author(s).md
```

Human-readable "Title - Author", normal capitalization and spaces. Rules:

- Clean, recognizable title — strip download noise (ISBNs, `z-lib`, `_compress`, publisher codes).
- Edition in parentheses when relevant: `(2nd Ed)`, `(3rd Ed)`, `(7th Ed)`.
- Author(s) by surname after ` - `; multiple authors separated by commas.

Examples:

- `Clean Architecture - Martin.md`
- `Designing Data-Intensive Applications - Kleppmann.md`
- `CSS in Depth (2nd Ed) - Grant.md`
- `REST in Practice - Webber, Parastatidis, Robinson.md`

### Internal format

The **body** of a professional book is the **full extracted text**, kept close to the source — it is *not* re-typeset into a rigid template. Expect natural book structure (front matter, chapters, sections), minimal/irregular markdown, and occasional extraction artifacts (stray characters, odd spacing, inherited line breaks). That is acceptable and is **not** "fixed" by hand without reason — the extracted text is the RAG source.

What the standard **does** enforce on every professional file:

- The file **opens with the standard header** (section 4), then `---`, then the extracted body.
- **No image references** anywhere — cover blocks (`<p align="center"><img …></p>`) and figure embeds (`![](…)`) are removed. (Again: `<img>` written as part of prose or a code example is content and stays.)
- **English only.** Portuguese translations are **not** kept (the previous "sibling `(PT-BR)` file" model is retired).

---

## 4. YAML frontmatter — software-development relevance

Every content file **opens with a YAML frontmatter block** that tags how relevant the material is to building software. This lets the corpus be filtered (e.g. a RAG query can prefer `core`/`supporting` and skip pure theory).

```yaml
---
software_dev: core
---
```

`software_dev` is one of five tiers:

| Tier | Meaning | Examples |
|------|---------|----------|
| `core` | **Language-agnostic** craft of building software — writing, designing, testing | *Clean Code*, *Domain-Driven Design*, *Designing Data-Intensive Applications*, architecture/web/engineering books |
| `stack` | A specific **programming language or framework** — the project (user) chooses these per its tech stack, not universal | Core Java, Eloquent JavaScript, The Go Programming Language, Angular, React Native, GraphQL |
| `supporting` | Adjacent discipline that supports delivery | DevOps/SRE, security & privacy, management/product/process, design/UX |
| `foundational` | Computer-science / math base underneath software | algorithms, operating systems, networks, compilers, automata, AI fundamentals |
| `optional` | Pure math, theory, or hardware not strictly needed to build software | calculus, linear algebra, statistics, digital circuits, quantum computing |

`core` is deliberately **language- and framework-neutral**: it is the craft every project needs regardless of stack. Anything tied to one language or framework is `stack`, so the user can opt into only the technologies they actually use.

### `stack:` — which language/framework

Every `software_dev: stack` file also carries a **`stack:` id** so the user can pick *which* technologies to ingest (not all-or-nothing):

```yaml
---
software_dev: stack
stack: angular
version: 22
---
```

- `stack` is a single lowercase id: a language or framework (`java`, `javascript`, `node`, `python`, `go`, `ruby`, `rails`, `angular`, `react-native`, `graphql`, …). Add new ids as books arrive.
- `version` (optional) is the **single major** the book targets (e.g. `22` for the Angular 22 guide, `4` for Spring Boot 4, `25` for Core Java 25). Omit it for an edition-agnostic book.
- Conductor ingests a `stack` book only when its id is in `CONDUCTOR_LIBRARY_STACKS` (or that is `all`). When the request pins an edition (`stack@major`, e.g. `angular@21`), it resolves to the **nearest** `version` available (ties prefer the higher) — so an Angular 21 project still gets the Angular 22 book. `core` and the other tiers never use `stack:`/`version:`.

Assignment rule: professional books inherit the tier of their topic folder — **except** language/framework titles, which are `stack` and live in `01_programming_languages/` (languages) or `14_frameworks/` (frameworks/runtimes: Angular, React Native, Rails, Node, GraphQL). Each `stack` file also carries a `stack: <id>` field (see `CONDUCTOR.md`). Academic reading lists are tiered per discipline. When unsure between two tiers, prefer the **more** dev-relevant one only if the book is routinely used while building software.

## 5. The standard header (every file)

Directly below the frontmatter, every content file has this header, derived from the filename and folder:

```markdown
# <Title>

> **Author(s):** <names> · **Edition:** <edition> · **Year:** <year> · **ISBN:** <isbn>
> **Category:** <NN_folder_name> · **Language:** English

---
```

- Drop any field whose value is unknown (e.g. omit `Year`/`ISBN` for raw extractions that do not state them).
- For academic reading-list files the `# <Title>` is `NN — Discipline Title` and the per-book metadata lives in each entry's table (section 2) rather than the header.

---

## 6. Root support files

Documents that describe or index the corpus. Named `UPPERCASE_WITH_UNDERSCORE.md` (except `README.md`), all in English:

- `README.md` — navigable index of every folder and file.
- `CONDUCTOR.md` — how the Conductor app fetches, ingests, and filters this library (install integration).
- `FILE_CONVENTIONS.md` — this standard.
- `ROLES_AND_ACRONYMS.md` — tech roles glossary (acronym + name).
- `AGENTS_AND_SKILLS_BY_ROLE.md` — Agent prompt + Skill per role.

---

## 7. Quick reference

| Item | Standard |
|------|----------|
| Language | **English only**, every file |
| Images | **None** — covers and figure embeds removed (literal `<img>` in prose/code is kept) |
| Frontmatter | `software_dev: core \| stack \| supporting \| foundational \| optional` at the very top of every file |
| Folder | `NN_lowercase_words` (English, no accents/spaces) |
| Academic file | `NN_slug.md`, English, one entry per book (table + description, no cover) |
| Professional book | `Title (Edition) - Author.md`, English, raw body + standard header |
| Header | frontmatter, then standard metadata block (section 5) at the top of every file |
| Support docs (root) | `UPPERCASE_WITH_UNDERSCORE.md` |
| Ordering | by the numeric `NN_` prefix |
