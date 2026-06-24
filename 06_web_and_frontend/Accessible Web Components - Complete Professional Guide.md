---
software_dev: core
---

# Accessible Web Components - Complete Professional Guide

> **Category:** 06_web_and_frontend · **Language:** English

---

### Semantic HTML, ARIA, and keyboard support for everyone
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches accessible component building from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** accessibility (a11y) means people with disabilities can use your interface — via keyboard, screen reader, or other assistive tech. This guide covers semantic HTML, when (and when not) to use ARIA, and keyboard support, current to 2026 (WCAG 2.2).

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to a11y | Part I |
| 2 — Intermediate | Building components | Part II |

**Target audience:** frontend developers building interactive components that everyone can use.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes HTML/CSS/JS and the CSS-layout guide.

---

## Table of Contents

**Part I – Foundations**
1. Semantic HTML first
2. ARIA: the rules and when to use it

**Part II – Interaction**
3. Keyboard support and focus management

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – Foundations

The biggest accessibility wins come not from special tools but from using the **right HTML elements**. A real `<button>`, `<a>`, `<label>`, and `<nav>` come with keyboard support, screen-reader semantics, and focus behavior for free. Most a11y failures are caused by reinventing these with `<div>`s. Build on semantics first; reach for ARIA only to fill gaps.

---

## Chapter 1 — Semantic HTML first

### 1.1 Introduction

**Semantic HTML** means using elements for their meaning: `<button>` for actions, `<a>` for navigation, `<h1>`–`<h6>` for structure, `<label>` for form fields, `<nav>`/`<main>`/`<header>` for landmarks. These elements carry built-in **roles**, keyboard behavior, and focusability that assistive technology understands. Using them correctly is 80% of accessibility, for free.

### 1.2 Business context

Accessibility is both an ethical and legal requirement (WCAG/ADA/EN 301 549) and a market reach issue — a significant share of users rely on assistive tech, and accessible sites also rank and convert better. Most accessibility lawsuits and failures stem from non-semantic markup (clickable `<div>`s, missing labels). Using semantic HTML prevents the bulk of these problems at no extra cost, while custom `<div>` widgets create expensive, ongoing remediation.

### 1.3 Theoretical concepts: elements carry semantics

```mermaid
flowchart LR
    div["div/span: no semantics, not focusable, no keyboard"]
    sem["button/a/label/nav: role + keyboard + focus, free"]
    div --> work["must rebuild everything (and usually fail)"]
    sem --> ok["works with assistive tech out of the box"]
```

A native `<button>` is focusable, activates on Enter/Space, and announces as "button" to a screen reader — automatically. A `<div onclick>` has none of that. The rule: **use the element that means what you intend**; only style it, don't replace it.

### 1.4 Architecture: semantics → accessibility tree

```mermaid
flowchart TB
    html["Semantic HTML"] --> tree["Accessibility tree (roles, names, states)"]
    tree --> at["Assistive tech (screen readers, etc.)"]
```

The browser builds an **accessibility tree** from your HTML; assistive tech reads it. Semantic elements populate it correctly; generic `<div>`s leave it empty of meaning.

### 1.5 Real example

**Scenario.** A custom "button" built as a styled `<div>`.

**Problem.** It's not focusable, doesn't respond to keyboard, and a screen reader doesn't announce it as a button — unusable for many.

**Solution.** Use a real `<button>` and style it.

**Implementation.**

```html
<!-- INACCESSIBLE: no focus, no keyboard, no role -->
<div class="btn" onclick="submit()">Submit</div>

<!-- ACCESSIBLE: focusable, Enter/Space work, announced as a button -->
<button type="button" class="btn" onclick="submit()">Submit</button>
```

**Result.** The native button is keyboard-operable, focusable, and announced correctly — accessible by default, with the same styling. A whole class of users regains access.

**Future improvements.** Audit the app for other `<div onclick>` controls and replace them with semantic elements.

### 1.6 Exercises

1. Name four semantic elements and the behavior each provides for free.
2. What does a screen reader read — the HTML or the accessibility tree?
3. Why is a `<div onclick>` button inaccessible?

### 1.7 Challenges

- **Challenge.** Find a `<div>`/`<span>` acting as a control in your app. Replace it with the correct semantic element and test with keyboard only.

### 1.8 Checklist

- [ ] I use elements for their meaning.
- [ ] Actions are `<button>`, navigation is `<a>`.
- [ ] Form fields have associated `<label>`s.
- [ ] Landmarks (`nav`/`main`/`header`) structure the page.

### 1.9 Best practices

- Default to semantic HTML; style it rather than rebuild it.
- Associate every input with a label.
- Use headings and landmarks for structure.

### 1.10 Anti-patterns

- Clickable `<div>`/`<span>` controls.
- Skipping or visually-hiding labels with no accessible name.
- Using headings for size instead of structure.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Control unreachable by keyboard | Non-semantic element | Use `<button>`/`<a>` |
| Screen reader says nothing useful | Empty accessibility tree | Use semantic HTML/labels |
| Form fields unlabeled | Missing `<label>` association | Associate labels with inputs |

### 1.12 References

- H. Pickering, *Inclusive Components* (2018) — https://inclusive-components.design.
- W3C, "WCAG 2.2": https://www.w3.org/TR/WCAG22/; MDN ARIA: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA.

---

## Chapter 2 — ARIA: rules and when to use it

### 2.1 Introduction

**WAI-ARIA** adds roles, states, and properties to HTML to describe custom widgets to assistive tech (e.g. `role="tablist"`, `aria-expanded`, `aria-label`). It's powerful but easy to misuse. The most important guidance is the **first rule of ARIA**: *don't use ARIA if a native HTML element already does the job*. ARIA fills gaps; it doesn't replace semantics.

### 2.2 Business context

Misused ARIA actively breaks accessibility — incorrect roles or unmanaged states confuse assistive tech worse than no ARIA at all ("bad ARIA is worse than no ARIA"). Knowing the rules lets teams build the custom widgets they genuinely need (complex menus, tabs, comboboxes) correctly, while not sprinkling ARIA on things HTML already handles. This avoids both inaccessible widgets and self-inflicted regressions.

### 2.3 Theoretical concepts: the rules of ARIA

```mermaid
flowchart TB
    r1["1. Use native HTML if it does the job (prefer it)"]
    r2["2. Don't change native semantics needlessly"]
    r3["3. Custom interactive widgets must be keyboard-operable"]
    r4["4. Don't hide focusable elements with aria-hidden"]
    r5["5. Interactive elements need an accessible name"]
    r1 --> r2 --> r3 --> r4 --> r5
```

ARIA provides three things: **roles** (what it is), **states/properties** (`aria-expanded`, `aria-checked`, `aria-label`), and a way to relate elements (`aria-describedby`). You must keep states **in sync** with reality via JS — a `role="checkbox"` whose `aria-checked` never updates is broken.

### 2.4 Architecture: ARIA describes, JS keeps it true

```mermaid
flowchart LR
    widget["Custom widget (role + states)"] --> js["JS updates aria-* on interaction"]
    js --> at["Assistive tech reflects current state"]
```

### 2.5 Real example

**Scenario.** A custom collapsible section (accordion) built with divs.

**Problem.** Screen-reader users can't tell it's expandable or whether it's open.

**Solution.** Use a real `<button>` for the trigger and `aria-expanded` reflecting state — minimal, correct ARIA on a semantic base.

**Implementation.**

```html
<h3>
  <button aria-expanded="false" aria-controls="sect1" id="acc1">Shipping details</button>
</h3>
<div id="sect1" role="region" aria-labelledby="acc1" hidden>...</div>
```

```js
// keep aria-expanded in sync with reality
btn.addEventListener('click', () => {
  const open = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', String(!open));
  panel.hidden = open;
});
```

**Result.** The trigger is a real button (keyboard + focus free); `aria-expanded` tells screen-reader users whether it's open and updates on toggle. Minimal ARIA, correct behavior.

**Future improvements.** Follow the established ARIA Authoring Practices pattern for the full widget (e.g. disclosure/accordion).

### 2.6 Exercises

1. State the first rule of ARIA.
2. Why is bad ARIA worse than none?
3. What must you keep in sync for `aria-*` states?

### 2.7 Challenges

- **Challenge.** Find a custom widget using ARIA. Check each rule: native element preferred? keyboard-operable? states synced? accessible name present? Fix one gap.

### 2.8 Checklist

- [ ] I prefer native HTML over ARIA.
- [ ] Custom widgets are keyboard-operable.
- [ ] `aria-*` states stay in sync via JS.
- [ ] Interactive elements have accessible names.

### 2.9 Best practices

- Use ARIA only to fill genuine gaps.
- Follow the ARIA Authoring Practices patterns for complex widgets.
- Keep states accurate at all times.

### 2.10 Anti-patterns

- ARIA on elements HTML already covers.
- Roles without the required keyboard behavior/states.
- `aria-hidden` over focusable content.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Widget confuses screen readers | Bad/incomplete ARIA | Follow the authoring pattern; sync states |
| State not announced | aria-* not updated | Update `aria-*` on every change |
| Redundant role warnings | ARIA duplicating native semantics | Remove; use native element |

### 2.12 References

- W3C, "ARIA Authoring Practices Guide": https://www.w3.org/WAI/ARIA/apg/.
- H. Pickering, *Inclusive Components* (2018) — https://inclusive-components.design.

---

> **End of Part I.** You can now build accessible components by starting from semantic HTML (which gives roles, keyboard support, and focus for free) and adding ARIA only to fill genuine gaps — following its rules, keeping states in sync, and always providing accessible names. **Part II — Interaction** (Chapter 3) covers keyboard support and focus management for custom widgets: tab order, focus trapping in dialogs, and visible focus indicators.

<!--APPEND-PART-II-->
