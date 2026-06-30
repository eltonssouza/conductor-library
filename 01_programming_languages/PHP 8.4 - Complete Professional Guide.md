---
software_dev: stack
stack: php
version: 8
---

# PHP 8.4 - Complete Professional Guide

> **Category:** 01_programming_languages · **Language:** English

---

### Types, OOP, Enums, Attributes, Fibers, Property Hooks, Composer, PSR
**Edition for PHP 8.4**

> **Reference book (English).** Based on the official PHP documentation (php.net), the PHP RFC archive (wiki.php.net), and the PHP-FIG standards (php-fig.org). A professional, in-depth guide for developers, architects, and teams writing modern, typed, production-grade PHP.
>
> **Scope notice:** this book targets **PHP 8.4** and the idioms of *modern* PHP — strict types, value objects, enums, attributes, fibers, and the 8.4 additions (property hooks, asymmetric visibility, `new` without parentheses, the `#[\Deprecated]` attribute). It assumes you can already run a PHP script and read basic code; from there it builds toward enterprise practice. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).

---

## How to read this book

Progressive depth across five maturity levels:

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to typed/modern PHP | Part I |
| 2 — Intermediate | Functions, arrays, OOP basics | Parts II–III |
| 3 — Advanced | Modern features, errors, namespaces | Parts IV–V |
| 4 — Specialist | Stdlib, dates, database, HTTP | Part VI |
| 5 — Enterprise | Testing, performance, security, deployment | Parts VII–VIII |

**Target audience:** backend developers, full-stack engineers, software architects, tech leads, and CTOs building or modernizing PHP systems on 8.4.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete code · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · Official references.

**Example format:** Scenario · Problem · Solution · Implementation · Result · Future improvements.

> **Note on prerequisites.** All code in this book uses `declare(strict_types=1);` and full type declarations. Where an 8.4 feature replaces an older pattern (e.g., property hooks vs. hand-written getters/setters), we show both so you can recognize and migrate legacy code.

---

## Table of Contents

**Part I – Language Foundations & Types**
1. Syntax, values, and the scalar type system
2. Type declarations: nullable, union, and intersection types
3. `strict_types`, coercion, and `mixed`/`never`/`void`

**Part II – Functions & Arrays**
4. Functions, parameters, named arguments, variadics
5. Arrays, the array functions, and the spread operator
6. Closures, arrow functions, and first-class callable syntax

**Part III – Object-Oriented PHP**
7. Classes, properties, constructor promotion, `readonly`
8. Interfaces, abstract classes, and traits
9. Enums (pure and backed) and first-class callables on methods

**Part IV – Modern Language Features**
10. Attributes and reflection
11. `match`, named args, and `new` in initializers
12. Fibers and cooperative concurrency
13. Property hooks and asymmetric visibility (8.4)

**Part V – Errors, Namespaces & Autoloading**
14. Errors vs. exceptions, the Throwable hierarchy
15. Namespaces, Composer, and PSR-4 autoloading
16. Deprecations with `#[\Deprecated]`

**Part VI – Standard Library, Dates, Database & HTTP**
17. Strings, `mb_*`, and the standard library
18. Dates and `DateTimeImmutable`
19. Databases with PDO
20. HTTP and PSR-7/PSR-15

**Part VII – Testing & Performance**
21. Testing with PHPUnit
22. Performance: OPcache and the JIT

**Part VIII – Security & Deployment**
23. Security: input, output, secrets, and crypto
24. Deployment: configuration, processes, and observability

> **Status of this edition:** phased delivery (each part keeps the same depth standard). **Ready:** Parts I–III (Ch. 1–9). **In progress:** Parts IV–VIII.

---

## Part I – Language Foundations & Types

Part I establishes the bedrock: how PHP represents values, how the type system constrains them, and how `strict_types` changes the rules. Modern PHP is a *typed* language in practice — the engine still runs untyped code, but professional codebases declare types everywhere and let the runtime enforce contracts. The three chapters here give you the vocabulary (scalars, compound types, special types) and the discipline (strict mode) that every later chapter assumes.

---

## Chapter 1 — Syntax, values, and the scalar type system

### 1.1 Introduction

PHP is a dynamically typed, interpreted language whose engine (the Zend Engine) compiles source to opcodes and executes them, optionally caching the opcodes (OPcache) and JIT-compiling hot paths. A *value* in PHP has one of a small set of primitive types: `bool`, `int`, `float`, `string`, plus the compound `array` and `object`, and the special `null`, `callable`, `iterable`, and `resource`. This chapter focuses on the **scalars** — `bool`, `int`, `float`, `string` — because they are the atoms from which every richer abstraction is built, and because misunderstanding their conversion rules is the single most common source of subtle bugs.

PHP 8.4 inherits the scalar model unchanged in shape but continues to tighten its edges: implicit, lossy conversions emit deprecation notices, and `strict_types=1` (covered in Chapter 3) lets you opt out of coercion entirely.

### 1.2 Business context

Scalars look trivial, yet they carry real money risk. A `float` used for currency loses cents to binary rounding; a numeric string from a form silently coerced to `int` can drop a leading zero in a postal code; a "truthy" string can flip a feature flag the wrong way. Teams that standardize early on *which scalar represents which concept* — integers in minor units for money, `DateTimeImmutable` for time, validated strings for identifiers — prevent entire classes of production incidents. The business case for understanding scalars is simply correctness at the boundary where untrusted input becomes typed program state.

### 1.3 Theoretical concepts

A scalar is a single, indivisible value. PHP's four scalar types have well-defined literals, ranges, and conversion rules:

- **`bool`** — `true` / `false`. Many values are *falsy*: `false`, `0`, `0.0`, `""`, `"0"`, `[]`, and `null`. Everything else is truthy (notably `"false"` and `"0.0"` are truthy).
- **`int`** — platform-width signed integer (64-bit on modern systems). Literals support `_` separators, hex `0x`, octal `0o`/`0`, and binary `0b`.
- **`float`** — IEEE-754 double. Never use for money. Compare with a tolerance, never with `===`.
- **`string`** — a byte sequence (not inherently Unicode); use `mb_*` functions for multibyte text.

```mermaid
flowchart TD
    V[Raw value] --> Q{Type?}
    Q -->|bool| B[true / false]
    Q -->|int| I[64-bit signed]
    Q -->|float| F[IEEE-754 double]
    Q -->|string| S[byte sequence]
    B --> C[Compound: array, object]
    I --> C
    F --> C
    S --> C
    C --> N[Special: null, callable, iterable]
```

### 1.4 Architecture

Where do scalars sit in the runtime? Every PHP value is stored in a `zval` container that tracks both the value and its type tag. Coercion happens when an operation expects a type different from the tag; the engine either converts (non-strict) or throws a `TypeError` (strict, for typed boundaries).

```mermaid
flowchart LR
    SRC[Source code] --> LEX[Lexer + Parser]
    LEX --> OPC[Opcodes]
    OPC --> OPC2[OPcache]
    OPC2 --> EXE[Zend VM executes]
    EXE --> ZVAL[zval: value + type tag]
    ZVAL --> COE{Operation type matches?}
    COE -->|yes| OK[Use value]
    COE -->|no, non-strict| CONV[Coerce]
    COE -->|no, strict| ERR[TypeError]
```

### 1.5 Real example

**Scenario.** A checkout service receives a price and a quantity from an HTTP form and must compute a line total.

**Problem.** Storing money as `float` produces rounding errors (`0.1 + 0.2 !== 0.3`), and the raw POST values arrive as strings.

**Solution.** Represent money as integer **cents**, validate the inputs explicitly, and never let a `float` touch the total.

**Implementation.**

```php
<?php

declare(strict_types=1);

/**
 * Parse a money string like "19.99" into integer cents (1999).
 */
function parseCents(string $amount): int
{
    if (!preg_match('/^\d+(?:\.\d{1,2})?$/', $amount)) {
        throw new InvalidArgumentException("Invalid money: {$amount}");
    }

    [$whole, $frac] = array_pad(explode('.', $amount), 2, '0');
    $frac = str_pad($frac, 2, '0');           // "9" -> "90"

    return (int) $whole * 100 + (int) $frac;
}

function lineTotalCents(string $unitPrice, string $qty): int
{
    $quantity = filter_var($qty, FILTER_VALIDATE_INT);
    if ($quantity === false || $quantity < 1) {
        throw new InvalidArgumentException("Invalid quantity: {$qty}");
    }

    return parseCents($unitPrice) * $quantity;
}

function formatCents(int $cents): string
{
    return number_format($cents / 100, 2, '.', ',');
}

$total = lineTotalCents('19.99', '3');
echo formatCents($total) . PHP_EOL;   // 59.97
```

**Result.** The total is exact, the inputs are validated, and `float` appears only at the final formatting step where rounding is harmless.

**Future improvements.** Promote money to a dedicated `readonly` value object (Chapter 7) with `Currency`, and use an enum for currency codes (Chapter 9), so the type system enforces that you never add USD to EUR.

### 1.6 Exercises

1. Write a function `isTruthy(mixed $v): bool` and predict the result for `"0"`, `"0.0"`, `"false"`, `[]`, and `0.0`.
2. Print the largest `int` (`PHP_INT_MAX`), then add 1 and observe the conversion to `float`.
3. Parse `"007"` with `(int)` and with `FILTER_VALIDATE_INT`; explain the difference for identifiers like a US zip code.
4. Demonstrate why `0.1 + 0.2 === 0.3` is `false` and write a tolerance-based comparison helper.

### 1.7 Challenges

1. Implement a `Money` parser that supports thousands separators (`"1,234.50"`) and rejects more than two decimal places, with full strict typing.
2. Build a tiny CSV cleaner that reads numeric columns as `int` cents and reports every row that fails validation, without throwing on the first error.

### 1.8 Checklist

- [ ] I know which values are falsy in PHP.
- [ ] I never store money as `float`.
- [ ] I compare floats with a tolerance, never `===`.
- [ ] I validate string-to-int conversions with `filter_var`/`FILTER_VALIDATE_INT`.
- [ ] I use `mb_*` functions for user-facing text.
- [ ] I understand that a PHP `string` is bytes, not Unicode code points.

### 1.9 Best practices

- Treat the HTTP/CLI boundary as untrusted: validate and convert once, then work with typed values internally.
- Prefer integer minor units for money and `DateTimeImmutable` for time.
- Use numeric separators (`1_000_000`) for readability in large literals.
- Reach for `filter_var` over bare casts when input correctness matters.

### 1.10 Anti-patterns

- Casting user input directly with `(int)`/`(float)` and trusting the result.
- Using `==` (loose equality) for security or business decisions — prefer `===`.
- Comparing floats for exact equality.
- Concatenating untrusted strings into SQL or HTML (covered in Chapters 19 and 23).

### 1.11 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `0.1 + 0.2 !== 0.3` | IEEE-754 float rounding | Use integer cents or `bcmath`/tolerance |
| `"007"` becomes `7` | Lossy `(int)` cast | Keep IDs as validated strings |
| Deprecation on implicit conversion | Lossy float→int or null→string | Add explicit casts / enable strict mode |
| `"0"` treated as false in `if` | `"0"` is falsy | Test explicitly (`$s !== ''`) |
| `==` matches unexpected values | Loose type juggling | Use `===` |

### 1.12 Official references

- Types overview: https://www.php.net/manual/en/language.types.php
- Booleans: https://www.php.net/manual/en/language.types.boolean.php
- Integers: https://www.php.net/manual/en/language.types.integer.php
- Floats: https://www.php.net/manual/en/language.types.float.php
- Strings: https://www.php.net/manual/en/language.types.string.php
- Type juggling: https://www.php.net/manual/en/language.types.type-juggling.php

---

## Chapter 2 — Type declarations: nullable, union, and intersection types

### 2.1 Introduction

PHP lets you declare types on parameters, return values, properties, and class constants. Beyond the single scalar types of Chapter 1, the language supports **nullable** types (`?T`), **union** types (`A|B`), **intersection** types (`A&B`), and combinations of these. These declarations are not mere documentation: the engine enforces them at runtime and a static analyzer (PHPStan, Psalm) enforces them at build time. This chapter shows how to express precise contracts so that invalid states become unrepresentable.

### 2.2 Business context

Every untyped boundary is a place where a wrong value can slip through to production. Type declarations move whole categories of bugs from runtime (a 3 a.m. page) to either the developer's editor or the CI pipeline. For a business, that is cheaper defects, faster onboarding (signatures document intent), and safer refactors (the type checker finds every call site that breaks). Intersection types in particular let you say "this argument must satisfy two capabilities at once" — a powerful way to model rich domain contracts without fragile inheritance.

### 2.3 Theoretical concepts

- **Nullable `?T`** — equivalent to `T|null`; the value is either a `T` or `null`.
- **Union `A|B|C`** — the value is exactly one of the listed types. Useful for `int|string` identifiers or `Result|null`.
- **Intersection `A&B`** — the value must be an instance of *all* listed types (interfaces/classes only). Useful for "is both `Countable` and `Traversable`".
- **Special types** — `mixed` (any), `void` (returns nothing), `never` (never returns), `iterable` (`array|Traversable`), `self`/`static`/`parent`.

```mermaid
classDiagram
    class TypeSystem
    class Scalar { bool int float string }
    class Nullable { ?T = T or null }
    class Union { A | B | C }
    class Intersection { A & B }
    class Special { mixed void never iterable }
    TypeSystem --> Scalar
    TypeSystem --> Nullable
    TypeSystem --> Union
    TypeSystem --> Intersection
    TypeSystem --> Special
```

### 2.4 Architecture

Type declarations are checked at two layers that reinforce each other: the static analyzer at build time and the Zend Engine at runtime. A value that violates a declaration raises a `TypeError`. The architecture below shows the flow from a typed signature to enforcement.

```mermaid
flowchart TD
    SIG[Typed signature] --> SA[Static analyzer<br/>PHPStan / Psalm]
    SIG --> RT[Zend Engine runtime check]
    SA -->|build time| PASS1{Valid?}
    RT -->|call time| PASS2{Valid?}
    PASS1 -->|no| CIFAIL[CI fails]
    PASS2 -->|no| TE[TypeError thrown]
    PASS1 -->|yes| OK[Compile]
    PASS2 -->|yes| RUN[Execute]
```

### 2.5 Real example

**Scenario.** A notification service can deliver via email or SMS. A "channel" must be able to both *render* a message and *report* a delivery cost.

**Problem.** Modeling "supports two capabilities" via a deep inheritance tree is rigid; a single interface that bundles unrelated concerns is a leak.

**Solution.** Define two small interfaces and require their **intersection** at the boundary. Use a **union** return for the lookup that may yield a channel or `null`.

**Implementation.**

```php
<?php

declare(strict_types=1);

interface Renderable
{
    public function render(string $message): string;
}

interface Priced
{
    public function costCents(string $message): int;
}

final class EmailChannel implements Renderable, Priced
{
    public function render(string $message): string
    {
        return "Subject: Notification\n\n{$message}";
    }

    public function costCents(string $message): int
    {
        return 0; // email is free in this model
    }
}

final class SmsChannel implements Renderable, Priced
{
    public function render(string $message): string
    {
        return mb_substr($message, 0, 160);
    }

    public function costCents(string $message): int
    {
        return (int) ceil(mb_strlen($message) / 160) * 5;
    }
}

/** Requires BOTH capabilities via an intersection type. */
function dispatch(Renderable&Priced $channel, string $message): int
{
    echo $channel->render($message) . PHP_EOL;
    return $channel->costCents($message);
}

/** Union return: a channel or null when the name is unknown. */
function channelByName(string $name): (Renderable&Priced)|null
{
    return match ($name) {
        'email' => new EmailChannel(),
        'sms'   => new SmsChannel(),
        default => null,
    };
}

$channel = channelByName('sms') ?? throw new RuntimeException('Unknown channel');
$cost = dispatch($channel, 'Your order has shipped.');
echo "Cost: {$cost} cents" . PHP_EOL;
```

**Result.** The compiler and runtime both guarantee that anything passed to `dispatch` can render *and* price a message, with no shared base class.

**Future improvements.** Replace the string channel name with a backed enum (Chapter 9) so `channelByName` cannot be called with an invalid name, and add a `Channel` aggregate interface if the pair of capabilities is always required together.

### 2.6 Exercises

1. Write a function that accepts `int|string` as an identifier and normalizes it to a string.
2. Add a third channel (`PushChannel`) and confirm `dispatch` accepts it with no signature change.
3. Declare a property `private ?DateTimeImmutable $deletedAt` and explain when `null` is meaningful.
4. Change a return type to `never` for a function that always throws; show the analyzer benefits.

### 2.7 Challenges

1. Model a `PaymentMethod` that must be both `Tokenizable` and `Refundable`, then write a processor that only accepts the intersection.
2. Introduce a deliberate type violation and capture the exact `TypeError` message; then fix it and verify PHPStan at level 9 reports nothing.

### 2.8 Checklist

- [ ] Every public function declares parameter and return types.
- [ ] I use `?T` instead of relying on documentation for nullability.
- [ ] I model "all of these capabilities" with intersection types, not god-interfaces.
- [ ] I run a static analyzer at a high level in CI.
- [ ] I prefer `never` for functions that always throw.

### 2.9 Best practices

- Keep interfaces small (interface segregation) so intersections stay expressive.
- Prefer the narrowest type that still compiles; avoid `mixed` unless truly needed.
- Use union types sparingly — many unions hint at a missing abstraction.
- Let the type checker, not comments, document contracts.

### 2.10 Anti-patterns

- Declaring `mixed` everywhere to silence the analyzer.
- Using `@param`/`@return` PHPDoc as the *only* type source when native types exist.
- Wide unions (`int|string|array|object`) that defeat type safety.
- Nullable returns where an exception or a Null Object would be clearer.

### 2.11 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `TypeError` at call site | Argument type mismatch | Fix the caller or widen the parameter |
| Intersection rejected | A type is a scalar/class, not interface-compatible | Use interfaces for intersections |
| Analyzer flags possible `null` | Nullable not handled | Add a guard or `??`/`?->` |
| `void` function "returns null" | Misuse of return value | Don't consume the result of a `void` function |
| `never` function flagged unreachable code | Code after it is dead | Remove the unreachable code |

### 2.12 Official references

- Type declarations: https://www.php.net/manual/en/language.types.declarations.php
- Union types: https://www.php.net/manual/en/language.types.type-system.php
- Intersection types: https://www.php.net/manual/en/language.types.declarations.php#language.types.declarations.composite.intersection
- `null` type: https://www.php.net/manual/en/language.types.null.php
- `never` return type: https://www.php.net/manual/en/migration81.new-features.php

---

## Chapter 3 — `strict_types`, coercion, and `mixed`/`never`/`void`

### 3.1 Introduction

By default PHP runs in *coercive* typing mode: when a typed parameter receives a value of a compatible-but-different scalar type, the engine quietly converts it (`"42"` to `int 42`). The `declare(strict_types=1);` directive flips that file into *strict* mode, where only exact scalar types are accepted (with the single exception of `int` widening to `float`). This chapter explains the two modes, where they apply, and how the special types `mixed`, `void`, and `never` interact with them. Choosing strict mode is the defining decision that separates casual scripts from disciplined applications.

### 3.2 Business context

Coercion is convenient until it hides a bug: a string `"0"` becomes `int 0`, a price `"abc"` becomes `0`, and the error surfaces three layers away as a wrong charge. Strict mode turns these into immediate, localized `TypeError`s at the boundary — failures that are cheap to diagnose. For organizations, mandating `strict_types=1` repository-wide is a low-cost policy with an outsized reduction in "works on my machine" defects, and it makes static analysis dramatically more accurate.

### 3.3 Theoretical concepts

- **Coercive mode (default).** Scalar arguments are converted to the declared type when safe; lossy conversions (e.g., `"1.5"` to `int`) trigger deprecation notices in modern PHP.
- **Strict mode (`declare(strict_types=1);`).** Must be the very first statement in a file. It governs the *calling* file's function calls, not the called function's definitions. Only `int`→`float` widening is allowed.
- **`mixed`** accepts any value; it is the top type and effectively disables checking for that slot.
- **`void`** declares that a function returns no value (you cannot `return $x;`).
- **`never`** declares that a function always throws or exits — control never returns to the caller.

```mermaid
flowchart TD
    CALL[Function call] --> MODE{strict_types in CALLER file?}
    MODE -->|1 strict| EXACT{Exact scalar type?}
    MODE -->|0 coercive| CONV[Coerce if safe]
    EXACT -->|yes, or int to float| RUN[Run]
    EXACT -->|no| TE[TypeError]
    CONV --> LOSSY{Lossy?}
    LOSSY -->|yes| DEP[Deprecation notice]
    LOSSY -->|no| RUN
```

### 3.4 Architecture

The key architectural subtlety: strictness is a property of the **caller's** file. A library can be written without `strict_types`, yet behave strictly when called from a strict file. The diagram shows how the directive at the top of the caller controls the conversion decision in the Zend Engine.

```mermaid
flowchart LR
    A[Caller file<br/>declare strict_types=1] -->|calls| B[Library function<br/>typed params]
    A2[Caller file<br/>coercive] -->|calls| B
    B --> ENGINE[Zend Engine arg check]
    ENGINE --> D{Caller strict?}
    D -->|yes| EXACT[Require exact type]
    D -->|no| COERCE[Coerce if safe]
```

### 3.5 Real example

**Scenario.** A pricing endpoint multiplies a quantity by a unit price in cents and is shared by an HTTP controller and a CLI importer.

**Problem.** In coercive mode, a stray `"3 "` (trailing space) or `"three"` becomes `0`, silently producing a free order line.

**Solution.** Enable `strict_types=1` so the boundary rejects non-`int` quantities, and validate at the edge before calling the strict core.

**Implementation.**

```php
<?php

declare(strict_types=1);

/** Strict core: only true ints are accepted. */
function lineTotalCents(int $quantity, int $unitPriceCents): int
{
    if ($quantity < 1) {
        throw new InvalidArgumentException('Quantity must be >= 1');
    }
    return $quantity * $unitPriceCents;
}

/** Boundary adapter: validates untrusted input, then calls the strict core. */
function lineTotalFromRequest(string $qty, string $price): int
{
    $quantity = filter_var($qty, FILTER_VALIDATE_INT);
    if ($quantity === false) {
        throw new InvalidArgumentException("Bad quantity: {$qty}");
    }

    $cents = filter_var($price, FILTER_VALIDATE_INT);
    if ($cents === false) {
        throw new InvalidArgumentException("Bad price: {$price}");
    }

    return lineTotalCents($quantity, $cents);   // exact ints — passes strict check
}

/** never: this function always terminates the request. */
function abort(string $reason): never
{
    http_response_code(400);
    throw new RuntimeException($reason);
}

try {
    echo lineTotalFromRequest('3', '1999') . PHP_EOL;   // 5997
    echo lineTotalFromRequest('three', '1999');         // throws before reaching core
} catch (InvalidArgumentException $e) {
    abort($e->getMessage());
}
```

**Result.** In strict mode the typed core cannot be fed a coerced zero; bad input fails loudly at the validated boundary, and `never` documents that `abort` does not return.

**Future improvements.** Add a PHP-CS-Fixer rule that requires `declare(strict_types=1);` in every file, and a CI gate that fails the build if it is missing.

### 3.6 Exercises

1. Call `lineTotalCents("3", 1999)` from a strict file and from a coercive file; compare the outcomes.
2. Write a `void` function and confirm the engine rejects `return $value;`.
3. Implement a `redirect(string $url): never` and explain how the analyzer treats code after the call.
4. Trigger a lossy-conversion deprecation in coercive mode and then eliminate it.

### 3.7 Challenges

1. Take a small coercive script and convert it to strict mode, fixing every resulting `TypeError` by adding boundary validation rather than casts.
2. Write a static-analysis configuration that fails when a file is missing `strict_types`, and document the team policy around it.

### 3.8 Checklist

- [ ] Every file begins with `declare(strict_types=1);`.
- [ ] Untrusted input is validated *before* it reaches strict, typed cores.
- [ ] I use `void` for side-effecting functions and `never` for always-throwing ones.
- [ ] I avoid `mixed` unless I truly accept any value.
- [ ] CI enforces strict mode across the repository.

### 3.9 Best practices

- Put `declare(strict_types=1);` as the first line of every PHP file, no exceptions.
- Keep a thin "boundary" layer that validates and converts; keep the core strict and typed.
- Prefer explicit validation (`filter_var`) over relying on coercion to "fix" input.
- Use `never` to give both readers and the analyzer precise control-flow information.

### 3.10 Anti-patterns

- Mixing strict and coercive files and being surprised by inconsistent behavior.
- Sprinkling `(int)`/`(string)` casts to silence `TypeError`s instead of validating.
- Using `mixed` to avoid thinking about the real contract.
- Returning a value from a `void` function (or ignoring a `never` function's intent).

### 3.11 Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Same call works in one file, fails in another | Caller's `strict_types` differs | Standardize strict mode everywhere |
| `"3"` accepted as `int` | File is coercive | Add `declare(strict_types=1);` |
| Deprecation: implicit float→int | Lossy coercion | Validate/cast intentionally |
| `Cannot use return value in void` | Returning from `void` | Change the return type or remove the value |
| Analyzer warns of unreachable code | Code after a `never` call | Delete the dead code |

### 3.12 Official references

- `strict_types` / type juggling: https://www.php.net/manual/en/language.types.declarations.php#language.types.declarations.strict
- `declare`: https://www.php.net/manual/en/control-structures.declare.php
- `mixed` type: https://www.php.net/manual/en/language.types.mixed.php
- `void` return: https://www.php.net/manual/en/language.types.void.php
- `never` return: https://www.php.net/manual/en/language.types.never.php

---

> **End of Part I.** You now have the type vocabulary and the strict-mode discipline that every later chapter assumes: scalars and their conversion traps, the full declaration system (nullable, union, intersection), and the rules of coercive vs. strict typing. Part II builds on this foundation with functions, arrays, and closures — including named arguments, the spread operator, and the first-class callable syntax — before Part III takes the leap into modern object-oriented PHP, where the 8.4 additions (property hooks, asymmetric visibility) finally come into play.

---

## Part II – Functions & Arrays

Part I covered values and PHP's type system. Part II builds the two workhorses of everyday PHP: **functions** (with named arguments and variadics) and **arrays** (PHP's universal ordered map, with its large standard function set), plus **closures** and **arrow functions** for first-class behavior.

---

## Chapter 4 — Functions, parameters, named arguments, variadics

### 4.1 Introduction

A PHP **function** declares typed parameters and a return type (Part I). Modern PHP makes calls clearer and more flexible: **named arguments** (`fee(amount: 100, rate: 0.1)`) let callers pass arguments by parameter name in any order and skip optional ones; **default values** make parameters optional; and **variadics** (`...$items`) accept a variable number of arguments as an array. The **spread** operator (`...$array`) does the reverse, unpacking an array into arguments. Together they make function calls self-documenting and adaptable.

### 4.2 Business context

Functions are the unit of reuse, and their call sites are where bugs and confusion concentrate. A call like `createUser(true, false, true)` is unreadable; **named arguments** (`createUser(active: true, admin: false, verified: true)`) make intent obvious and resist mistakes when parameters are reordered or added. Optional parameters with defaults avoid a combinatorial explosion of overloads (which PHP doesn't have). Variadics let one function handle "one or many" cleanly. These reduce review friction and the misuse that causes defects.

### 4.3 Theoretical concepts

```mermaid
flowchart TB
    call["fee(amount: 100, rate: 0.1)"] --> named["named args: by name, any order, skip optionals"]
    decl["function fee(int amount, float rate = 0.1)"] --> default["default -> optional parameter"]
    var["function sum(int ...nums)"] --> variadic["variadic: collects args into an array"]
    spread["sum(...[1,2,3])"] --> unpack["spread: unpacks an array into args"]
```

Parameters are typed and may have defaults (making them optional). **Named arguments** bind by parameter name, so callers can pass only what they need and in any order — especially valuable for functions with many optional parameters. **Variadics** (`...$nums`) gather trailing arguments into an array; the **spread** (`...$array`) unpacks an array (or Traversable) into positional arguments. PHP has no method overloading, so defaults + named args + variadics are how you express flexible signatures.

### 4.4 Architecture: clear, flexible call sites

```mermaid
flowchart LR
    api["function with typed params + defaults"] --> caller["caller uses named args for clarity"]
    note["Self-documenting calls; optionals skipped by name"]
```

A well-designed signature plus named arguments makes the call site read like documentation, which is most of a function's usability.

### 4.5 Real example

**Scenario.** A function creates a report with several optional settings.

**Problem.** Positional booleans/flags (`makeReport($data, true, false, true)`) are unreadable and error-prone.

**Solution.** Typed parameters with defaults, called with **named arguments**; a variadic for an open-ended list.

**Implementation.**

```php
function makeReport(
    array $data,
    string $format = 'csv',
    bool $includeHeader = true,
    bool $compress = false,
): string {
    // ...
}

// named arguments: clear, reorderable, skip the ones you don't change
$r = makeReport($rows, format: 'json', compress: true);

// variadic + spread
function total(int ...$amounts): int { return array_sum($amounts); }
$sum = total(...[10, 20, 30]);   // spread an array into the variadic
```

**Result.** The call `makeReport($rows, format: 'json', compress: true)` is self-explanatory and leaves `includeHeader` at its default — no positional guessing, no boolean soup. The variadic `total` accepts any number of amounts, and the spread feeds it an existing array. Signatures stay flexible without overloads.

**Future improvements.** Group many related parameters into a typed object (DTO/record-like class) when the list grows; use enums (Ch. 9) for `format` instead of a string.

### 4.6 Exercises

1. What do named arguments let a caller do that positional arguments don't?
2. What is the difference between a variadic parameter and the spread operator?
3. Why does PHP rely on defaults/named args instead of method overloading?

### 4.7 Challenges

- **Challenge.** Write a `formatMoney(int $cents, string $currency = 'BRL', bool $symbol = true)` and call it three ways using named arguments to vary only one option each time.

### 4.8 Checklist

- [ ] I use named arguments to clarify calls with multiple/optional parameters.
- [ ] Optional parameters have sensible defaults.
- [ ] I use variadics for "one or many" and spread to unpack arrays.
- [ ] I group large parameter lists into objects when they grow.

### 4.9 Best practices

- Prefer named arguments for readability at call sites.
- Order parameters required-first; give optionals defaults.
- Use variadics/spread instead of accepting a raw array when arity varies.

### 4.10 Anti-patterns

- Long positional boolean/flag argument lists.
- Huge parameter lists that should be a value object.
- Relying on argument position where names would prevent mistakes.

### 4.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Wrong values passed to params | Positional confusion | Use named arguments |
| Can't skip a middle optional | Positional call | Pass by name and skip the rest |
| Too many parameters | Missing abstraction | Group into a typed object |

### 4.12 References

- PHP Manual, "Function arguments" (named arguments, variadics): https://www.php.net/manual/en/functions.arguments.php.
- J. Lockhart, *Modern PHP* (O'Reilly, 2015) — ISBN 978-1491905012.

---

## Chapter 5 — Arrays, the array functions, and the spread operator

### 5.1 Introduction

The PHP **array** is a single, versatile type: an **ordered map** that serves as list, dictionary, stack, and queue. Keys are integers or strings; values are anything. PHP ships a **large standard library of array functions** — `array_map`, `array_filter`, `array_reduce`, `array_column`, `usort`, `in_array`, `array_keys`, and many more — that cover most data manipulation without manual loops. The **spread operator** (`[...$a, ...$b]`) merges arrays, and destructuring (`[$x, $y] = $pair`) pulls values out.

### 5.2 Business context

Arrays are where most PHP data lives — request input, database rows, config. Reaching for the right built-in array function instead of a hand-written loop makes code shorter, clearer, and less buggy (the function is tested and named for intent). Knowing the difference between, say, `in_array` (O(n)) and an `isset($map[$key])` lookup (O(1)) is a real performance lever on large datasets. Fluency with the array toolkit is one of the highest-leverage PHP skills for everyday productivity.

### 5.3 Theoretical concepts

```mermaid
flowchart TB
    arr["array: ordered map (int/string keys)"] --> list["list usage [0,1,2,...]"]
    arr --> map["dictionary usage ['k' => v]"]
    fns["array_map / array_filter / array_reduce / usort / array_column"] --> transform["declarative transforms"]
    spread["[...a, ...b]"] --> merge["merge / clone"]
```

Use an array as a **list** (sequential int keys) or a **map** (string keys). The functional trio — **`array_map`** (transform), **`array_filter`** (select), **`array_reduce`** (aggregate) — replaces most loops; **`usort`** sorts with a comparator; **`array_column`** extracts a field from rows. For membership, a key lookup (`isset($map[$k])`) is O(1) versus `in_array` O(n). The **spread** merges arrays (string keys are overwritten, int keys renumbered), and list **destructuring** binds elements to variables.

### 5.4 Architecture: declarative data transforms

```mermaid
flowchart LR
    rows["array of rows"] --> filter["array_filter"] --> map["array_map / array_column"] --> reduce["array_reduce -> result"]
    note["Pipeline of array functions instead of manual loops"]
```

Composing array functions expresses a data transformation as a readable pipeline, mirroring the LINQ idea in PHP's idiom.

### 5.5 Real example

**Scenario.** From an array of order rows, total the revenue of completed orders.

**Problem.** A manual loop with running totals and conditionals is verbose and easy to get wrong.

**Solution.** Compose **`array_filter`**, **`array_column`**, and **`array_sum`**.

**Implementation.**

```php
$orders = [
    ['id' => 1, 'status' => 'done', 'total' => 100],
    ['id' => 2, 'status' => 'open', 'total' => 50],
    ['id' => 3, 'status' => 'done', 'total' => 30],
];

$revenue = array_sum(
    array_column(
        array_filter($orders, fn($o) => $o['status'] === 'done'),  // select completed
        'total'                                                      // pull the total column
    )
);   // => 130

$merged = [...$orders, ['id' => 4, 'status' => 'done', 'total' => 20]]; // spread to append
```

**Result.** Three composed built-ins express "completed orders' totals, summed" without a loop or a running accumulator — shorter and harder to get wrong. The spread appends a row immutably. Each function is named for its intent, so the pipeline reads as the business question.

**Future improvements.** For very large datasets, prefer a key-indexed lookup over repeated `in_array`; consider generators (lazy iteration) to avoid building intermediate arrays.

### 5.6 Exercises

1. In what sense is a PHP array both a list and a dictionary?
2. Which functions implement transform, select, and aggregate over arrays?
3. Why can `isset($map[$key])` outperform `in_array($value, $list)`?

### 5.7 Challenges

- **Challenge.** Given rows with `category` and `amount`, use array functions to produce an associative array of total amount per category (hint: `array_reduce`).

### 5.8 Checklist

- [ ] I use `array_map`/`array_filter`/`array_reduce` instead of manual loops.
- [ ] I use key lookups (O(1)) over `in_array` (O(n)) on large data.
- [ ] I use the spread to merge/clone arrays and destructuring to unpack.
- [ ] I pick list vs. map usage deliberately.

### 5.9 Best practices

- Prefer named array functions for clarity and correctness.
- Index by key when you do repeated lookups.
- Use spread/destructuring for concise array assembly and unpacking.

### 5.10 Anti-patterns

- Hand-written loops where a single array function fits.
- `in_array` in a loop over large data (O(n²)).
- Mutating arrays in place where a spread-built copy is clearer.

### 5.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Slow membership checks | `in_array` on large lists | Index by key; use `isset` |
| Verbose loop logic | Manual iteration | Compose `array_map/filter/reduce` |
| Lost/renumbered keys after merge | `+` vs spread/`array_merge` semantics | Choose the merge that preserves the keys you need |

### 5.12 References

- PHP Manual, "Arrays" & "Array functions": https://www.php.net/manual/en/book.array.php.
- J. Lockhart, *Modern PHP* (O'Reilly, 2015) — ISBN 978-1491905012.

---

## Chapter 6 — Closures, arrow functions, and first-class callable syntax

### 6.1 Introduction

PHP treats functions as **values**. A **closure** (`function () use ($x) { ... }`) is an anonymous function that can capture variables from its scope via `use`. An **arrow function** (`fn($x) => $x * 2`) is a concise closure that **automatically** captures variables by value — ideal for the short callbacks array functions consume. The **first-class callable syntax** (`strlen(...)`, `$obj->method(...)`) turns any function or method into a closure value you can pass around. These make PHP's functional style (Ch. 5) ergonomic.

### 6.2 Business context

First-class functions are what let you pass behavior — a comparator to `usort`, a predicate to `array_filter`, a callback to an event system — instead of hard-coding it. Arrow functions remove the `use` boilerplate for the common case, keeping callbacks readable inline. The callable syntax lets existing functions/methods be reused as values without wrapping them. The result is decoupled, composable code: the same array pipeline or pipeline-of-handlers works with any behavior you supply.

### 6.3 Theoretical concepts

```mermaid
flowchart TB
    closure["function () use (x) { ... }"] --> capture["captures x explicitly (by value or &reference)"]
    arrow["fn(x) => expr"] --> auto["captures enclosing vars automatically (by value)"]
    fcc["strlen(...) / obj->m(...)"] --> value["any callable becomes a closure value"]
```

A **closure** captures variables listed in `use` — by value by default, or by reference with `&`. An **arrow function** is a single-expression closure that auto-captures used variables **by value** (no `use` needed), which is why it's perfect for `array_map`/`array_filter` callbacks. The **first-class callable syntax** `f(...)` produces a `Closure` from a named function or method, so you can store and pass it like any value.

### 6.4 Architecture: behavior passed as a value

```mermaid
flowchart LR
    consumer["array_filter / usort / event bus"] --> cb["receives a closure / arrow fn / callable"]
    note["Inject behavior; the consumer stays generic"]
```

Passing closures lets generic consumers (array functions, pipelines, event dispatchers) be specialized with the exact behavior a call site needs.

### 6.5 Real example

**Scenario.** Sort products by a runtime-selected key and filter by a threshold.

**Problem.** Hard-coding the sort key and threshold makes the logic rigid and duplicated.

**Solution.** Pass an **arrow function** comparator and predicate; reuse a method as a callable.

**Implementation.**

```php
$threshold = 50;
$expensive = array_filter($products, fn($p) => $p['price'] > $threshold);  // arrow fn auto-captures $threshold

usort($expensive, fn($a, $b) => $a['price'] <=> $b['price']);              // comparator as a value

// first-class callable: reuse an existing function/method as a Closure
$names = array_map(strtoupper(...), array_column($expensive, 'name'));
```

**Result.** The filter captures `$threshold` automatically (no `use`), the sort takes an inline comparator, and `strtoupper(...)` is reused directly as a mapping function. Behavior is supplied at the call site, so the same array functions handle any key, threshold, or transform — composable and concise.

**Future improvements.** Extract frequently-used predicates/comparators into named functions and pass them via `name(...)`; capture by reference (`use (&$x)`) only when you must mutate the outer variable.

### 6.6 Exercises

1. How does an arrow function's variable capture differ from a closure's `use`?
2. What does the first-class callable syntax `f(...)` produce?
3. When would you capture by reference (`use (&$x)`)?

### 6.7 Challenges

- **Challenge.** Build a small pipeline: filter an array of numbers above a captured threshold with an arrow function, then `array_map` them through an existing function passed via first-class callable syntax.

### 6.8 Checklist

- [ ] I use arrow functions for short callbacks (auto-capture by value).
- [ ] I use `use` (and `&` only when needed) for multi-statement closures.
- [ ] I pass existing functions/methods as values with `f(...)`.
- [ ] I inject behavior into generic consumers instead of hard-coding it.

### 6.9 Best practices

- Prefer arrow functions for array-function callbacks.
- Capture by value by default; use `&` references sparingly.
- Reuse named functions/methods via first-class callable syntax.

### 6.10 Anti-patterns

- Verbose `function() use (...)` where an arrow function suffices.
- Capturing by reference unintentionally, causing surprising mutations.
- Wrapping a function in a closure when `f(...)` would do.

### 6.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Callback doesn't see an outer variable | Closure missing `use` | Add `use ($var)` or use an arrow function |
| Outer variable changed unexpectedly | Captured by reference (`&`) | Capture by value instead |
| Verbose one-line callbacks | Full closure syntax | Use an arrow function `fn() => ...` |

### 6.12 References

- PHP Manual, "Anonymous functions", "Arrow functions", "First-class callable syntax": https://www.php.net/manual/en/functions.anonymous.php.
- J. Lockhart, *Modern PHP* (O'Reilly, 2015) — ISBN 978-1491905012.

---

> **End of Part II.** PHP's everyday workhorses: **functions** with named arguments, defaults, and variadics for clear, flexible calls; the **array** as a universal ordered map manipulated by a rich set of built-in functions; and **closures**, **arrow functions**, and **first-class callables** that pass behavior as a value. Part III covers **object-oriented PHP** — classes with constructor promotion and `readonly`, interfaces/abstracts/traits, and enums.

---

## Part III – Object-Oriented PHP

Part III covers PHP's object model, which modern versions have made concise and safe: **classes** with constructor property promotion and `readonly`, the three abstraction tools **interfaces**, **abstract classes**, and **traits**, and **enums** for fixed sets of values.

---

## Chapter 7 — Classes, properties, constructor promotion, `readonly`

### 7.1 Introduction

A PHP **class** bundles typed **properties** with **methods**, with visibility (`public`/`protected`/`private`). PHP 8 cut the boilerplate: **constructor property promotion** declares and assigns properties directly in the constructor signature (`public function __construct(private string $name) {}`), and **`readonly`** properties can be set once (in the constructor) and never again, giving immutability per property. PHP 8.4 adds **property hooks** and **asymmetric visibility** (Part IV). The result is concise, intention-revealing classes that protect their invariants.

### 7.2 Business context

Encapsulation lets a class enforce that its data is always valid and change its internals without breaking callers. Before promotion, every property meant three lines (declare, parameter, assign) — pure ceremony that obscured intent; promotion removes it. `readonly` makes immutability a guarantee the engine enforces, eliminating "who mutated this?" bugs for value objects and DTOs. Concise, safe classes lower the cost of modeling a domain accurately, which is where correctness in a business application starts.

### 7.3 Theoretical concepts

```mermaid
flowchart TB
    ctor["__construct(private readonly string name)"] --> promote["promotion: declare + assign in one place"]
    promote --> ro["readonly: assigned once, immutable after"]
    vis["visibility: public / protected / private"] --> encap["encapsulate state"]
```

**Constructor promotion** turns a constructor parameter prefixed with a visibility modifier into a class property, declared and assigned automatically. **`readonly`** properties may be initialized once (typically in the constructor) and then are immutable — attempting to write again is a fatal error. Combine them (`private readonly`) for concise immutable value objects. Visibility controls access; prefer the narrowest that works.

### 7.4 Architecture: concise, immutable-by-default state

```mermaid
flowchart LR
    caller["caller"] -->|"constructs once"| obj["object with readonly properties"]
    obj --> safe["state can't change after construction"]
    note["Promotion + readonly = small, safe value types"]
```

Promotion plus `readonly` makes the common case — a small type whose data is set at construction and never mutated — both terse to write and safe by construction.

### 7.5 Real example

**Scenario.** Model an immutable `Money` value object.

**Problem.** Hand-declaring properties and guarding against mutation is verbose and easy to get wrong.

**Solution.** **Promote** the properties and mark them **`readonly`**.

**Implementation.**

```php
final class Money
{
    public function __construct(
        public readonly int $cents,        // promoted + immutable
        public readonly string $currency,
    ) {}

    public function add(Money $other): self
    {
        if ($this->currency !== $other->currency) {
            throw new InvalidArgumentException('currency mismatch');
        }
        return new self($this->cents + $other->cents, $this->currency); // new value, no mutation
    }
}

$price = new Money(1990, 'BRL');
// $price->cents = 0;   // Error: cannot modify readonly property
$total = $price->add(new Money(500, 'BRL'));  // => Money(2490, 'BRL')
```

**Result.** `Money` is declared in a few lines (no separate property declarations or assignments), and its fields are immutable — any mutation is a fatal error, so the value can be shared safely. "Changes" produce new instances via `add`. Promotion + `readonly` made a correct value object cheap to write.

**Future improvements.** Add validation in the constructor (reject negative cents, empty currency); use PHP 8.4 property hooks (Part IV) for computed/validated properties.

### 7.6 Exercises

1. What does constructor property promotion replace?
2. What guarantee does `readonly` provide, and when can the property be set?
3. Why model `Money` as immutable?

### 7.7 Challenges

- **Challenge.** Build an immutable `Point` with promoted `readonly` `x`/`y` and a `translate(int $dx, int $dy): self` that returns a new `Point`.

### 7.8 Checklist

- [ ] I use constructor promotion to declare/assign properties concisely.
- [ ] Value objects use `readonly` for immutability.
- [ ] Properties have the narrowest visibility that works.
- [ ] Invariants are validated in the constructor.

### 7.9 Best practices

- Promote constructor parameters into properties to cut boilerplate.
- Make value objects immutable with `readonly`.
- Keep properties private/protected unless they must be public.

### 7.10 Anti-patterns

- Public mutable properties exposing internal state.
- Hand-written declare/assign triples instead of promotion.
- Mutating a value object instead of producing a new one.

### 7.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| "Cannot modify readonly property" | Writing a `readonly` after construction | Produce a new instance instead |
| Verbose class with repeated assignments | No promotion | Promote parameters in the constructor |
| Object reached an invalid state | No constructor validation | Validate invariants in `__construct` |

### 7.12 References

- PHP Manual, "Constructor Promotion" & "readonly properties": https://www.php.net/manual/en/language.oop5.properties.php.
- J. Lockhart, *Modern PHP* (O'Reilly, 2015) — ISBN 978-1491905012.

---

## Chapter 8 — Interfaces, abstract classes, and traits

### 8.1 Introduction

PHP has three tools for abstraction and reuse. An **interface** is a pure contract — method signatures (and constants) a class promises to implement; a class can implement **many**. An **abstract class** is a partial implementation: it can mix abstract methods (must be implemented) with concrete ones (shared), and cannot be instantiated. A **trait** is a unit of reusable methods (and properties) **composed** into a class with `use` — PHP's answer to horizontal code reuse without multiple inheritance. Choosing among them is a core PHP design skill.

### 8.2 Business context

These tools decide how flexible and DRY a codebase is. Interfaces enable substitution and testing (depend on `LoggerInterface`, inject a fake) and underpin the PSR standards that let PHP packages interoperate. Abstract classes share scaffolding across a family of types. Traits avoid copy-pasting the same helper methods into unrelated classes (e.g., a `TimestampableTrait`). Used correctly they reduce duplication and coupling; overused (especially traits) they obscure where behavior comes from. Knowing which to reach for keeps a large PHP codebase maintainable.

### 8.3 Theoretical concepts

```mermaid
flowchart TB
    i["interface: contract only (implement many)"] --> impl["classes implement it"]
    a["abstract class: contract + shared code (extend one)"] --> sub["subclasses fill abstract methods"]
    t["trait: reusable methods (use in many)"] --> compose["composed into a class"]
```

An **interface** declares *what*, never *how*; a class lists the interfaces it `implements` and the compiler checks coverage. An **abstract class** provides shared implementation plus `abstract` methods subclasses must define; single inheritance applies. A **trait** is `use`d to copy its methods into a class at compile time, enabling reuse across unrelated classes — but conflicts must be resolved explicitly and overuse hides behavior. Rule of thumb: **interface** for a contract, **abstract class** for a shared base of one family, **trait** for cross-cutting helper methods.

### 8.4 Architecture: contracts, shared bases, composed helpers

```mermaid
flowchart LR
    contract["interface (substitutability)"] --> consumer["consumer depends on it"]
    base["abstract base (shared scaffolding)"] --> family["a family of subtypes"]
    helper["trait (cross-cutting methods)"] --> many["unrelated classes"]
```

Each tool fits a different reuse shape; mixing them (an abstract class implementing an interface and using a trait) is common and idiomatic.

### 8.5 Real example

**Scenario.** Multiple exporters share timestamp logic but must be interchangeable.

**Problem.** Copying timestamp code into each exporter duplicates it; a single base class can't be shared with unrelated classes that also need timestamps.

**Solution.** An **interface** for substitutability, an **abstract class** for shared export scaffolding, and a **trait** for the cross-cutting timestamp.

**Implementation.**

```php
interface Exporter { public function export(array $data): string; }   // contract

trait Timestampable {                                                  // cross-cutting reuse
    public function stamp(): string { return (new DateTimeImmutable())->format('c'); }
}

abstract class BaseExporter implements Exporter {                      // shared base
    use Timestampable;
    public function export(array $data): string {
        return $this->stamp() . "\n" . $this->body($data);            // template + hook
    }
    abstract protected function body(array $data): string;            // subtypes implement
}

final class CsvExporter extends BaseExporter {
    protected function body(array $data): string { return implode(',', $data); }
}
```

**Result.** Consumers depend on `Exporter` and can swap any implementation (or a fake in tests). `BaseExporter` shares the export skeleton; `CsvExporter` fills only the body. The `Timestampable` trait provides `stamp()` and could be reused by any unrelated class that needs timestamps — three reuse mechanisms each doing what it's best at.

**Future improvements.** Keep traits small and focused; if two traits both define a method, resolve the conflict with `insteadof`/`as`; prefer composition (holding an object) when a trait starts carrying state.

### 8.6 Exercises

1. When do you choose an interface vs an abstract class vs a trait?
2. Why can a class implement many interfaces but extend only one class?
3. What problem do traits solve, and what risk do they introduce?

### 8.7 Challenges

- **Challenge.** Define a `Comparable` interface, an abstract base implementing a `max()` helper in terms of an abstract `compareTo()`, and a trait that adds a `describe()` method; combine them in one concrete class.

### 8.8 Checklist

- [ ] I use interfaces for contracts and substitutability.
- [ ] I use abstract classes for a shared base of one type family.
- [ ] I use traits for cross-cutting helper methods, kept small.
- [ ] I resolve trait conflicts explicitly.

### 8.9 Best practices

- Depend on interfaces; inject implementations.
- Reserve abstract classes for genuine shared scaffolding.
- Keep traits focused; avoid trait-heavy designs that hide behavior.

### 8.10 Anti-patterns

- "God" traits mixing unrelated responsibilities into many classes.
- Abstract classes used where a simple interface would do.
- Deep inheritance for code reuse (prefer traits/composition).

### 8.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Can't tell where a method comes from | Too many traits | Reduce/rename; prefer explicit composition |
| Trait method name conflict | Two traits define the same method | Resolve with `insteadof`/`as` |
| Rigid hierarchy | Abstract class used for cross-cutting reuse | Extract a trait or compose |

### 8.12 References

- PHP Manual, "Interfaces", "Abstract classes", "Traits": https://www.php.net/manual/en/language.oop5.php.
- PHP-FIG, PSR standards (interfaces for interoperability): https://www.php-fig.org/psr/.

---

## Chapter 9 — Enums (pure and backed) and first-class callables on methods

### 9.1 Introduction

A PHP **enum** (since 8.1) is a type with a fixed set of named cases — `enum Status { case Active; case Closed; }`. A **pure** enum's cases have only a name; a **backed** enum assigns each case a scalar value (`enum Status: string { case Active = 'active'; }`) for storage/serialization. Enums are objects: they can implement interfaces and have **methods**. Combined with the **first-class callable syntax** on methods (`$this->method(...)`, Ch. 6), enums make fixed domains type-safe and expressive, replacing loose string/int constants.

### 9.2 Business context

Domains are full of small fixed sets — order status, user role, currency. Modeling them as raw strings or class constants invites typos and invalid values that surface as runtime bugs and bad data. An **enum** makes the set a **type**: only the defined cases exist, the compiler/IDE checks usage, and `switch`/`match` over it is exhaustive-friendly. Backed enums map cleanly to database columns and JSON. Methods on enums put related behavior (a label, a color, a transition rule) where it belongs. This eliminates a whole class of "invalid status" defects.

### 9.3 Theoretical concepts

```mermaid
flowchart TB
    pure["enum Status { case Active; case Closed; }"] --> cases["a fixed set of singleton cases"]
    backed["enum Status: string { case Active = 'active'; }"] --> scalar["each case has a scalar value (from/tryFrom)"]
    methods["enums can implement interfaces + have methods"] --> behavior["behavior lives with the case"]
```

A **pure** enum case is a singleton object (`Status::Active`). A **backed** enum exposes `from($value)` (throws if invalid) and `tryFrom($value)` (returns null) to convert from the scalar, and `->value` to get it — ideal for persistence and APIs. Enums can declare **methods** and implement **interfaces**, so a `Status` can have a `label()` or `canTransitionTo()` method. Pass an enum method as a value with the first-class callable syntax when a callback is needed.

### 9.4 Architecture: fixed sets as types

```mermaid
flowchart LR
    raw["raw string/int constant"] -->|"replace with"| enum["enum type (only valid cases)"]
    enum --> match["match(status) -> exhaustive handling"]
    note["Invalid values become impossible, not just discouraged"]
```

Turning a fixed set into an enum moves "is this a valid value?" from runtime checks to the type system.

### 9.5 Real example

**Scenario.** An order status drives behavior and is stored in the database.

**Problem.** Using `'active'`/`'closed'` strings allows typos and invalid values, and the label logic is scattered.

**Solution.** A **backed enum** with a method, converting via `tryFrom` at the boundary.

**Implementation.**

```php
enum OrderStatus: string
{
    case Pending = 'pending';
    case Paid    = 'paid';
    case Shipped = 'shipped';

    public function label(): string         // behavior with the case
    {
        return match ($this) {
            self::Pending => 'Awaiting payment',
            self::Paid    => 'Paid',
            self::Shipped => 'On its way',
        };
    }
}

$status = OrderStatus::tryFrom($row['status']) ?? OrderStatus::Pending;  // safe from DB string
echo $status->label();                                                   // 'Paid'
echo $status->value;                                                     // 'paid' (to store)
```

**Result.** Only the three valid statuses exist; a bad database value is handled by `tryFrom` (no invalid enum), and `match` over the enum is checked. The label lives on the type, not in scattered conditionals, and `->value` serializes cleanly back to storage. "Invalid status" bugs are designed out.

**Future improvements.** Add a `canTransitionTo(OrderStatus $next): bool` method to encode the state machine; have the enum implement an interface so consumers depend on the contract.

### 9.6 Exercises

1. What is the difference between a pure and a backed enum?
2. What do `from()` and `tryFrom()` do, and when do you use each?
3. Why put a `label()` method on the enum rather than in a separate function?

### 9.7 Challenges

- **Challenge.** Model a `Role` backed enum with `admin`/`editor`/`viewer`, add a `canEdit(): bool` method, and convert a request string to a `Role` safely with `tryFrom`.

### 9.8 Checklist

- [ ] Fixed sets are modeled as enums, not raw strings/constants.
- [ ] I use backed enums for stored/serialized values.
- [ ] I convert external values with `tryFrom` (or `from` when invalid is exceptional).
- [ ] Case-related behavior lives in enum methods.

### 9.9 Best practices

- Replace string/int constants for fixed sets with enums.
- Use backed enums at persistence/API boundaries.
- Put behavior (labels, rules) on the enum via methods.

### 9.10 Anti-patterns

- Raw string statuses/roles scattered through the code.
- `from()` on untrusted input (use `tryFrom` to avoid exceptions).
- Duplicated `switch` on a constant where an enum method would centralize it.

### 9.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Invalid status values in data | Raw strings, no type | Model as a backed enum |
| Uncaught `ValueError` converting input | `from()` on invalid input | Use `tryFrom()` and handle null |
| Status logic duplicated | Behavior outside the enum | Move it into an enum method |

### 9.12 References

- PHP Manual, "Enumerations": https://www.php.net/manual/en/language.enumerations.php.
- B. D. Wiese et al., PHP RFC "Enumerations" (8.1).

---

> **End of Part III.** Modern PHP's object model is concise and safe: **classes** with constructor promotion and **`readonly`**; **interfaces**, **abstract classes**, and **traits** for contracts, shared bases, and cross-cutting reuse; and **enums** that turn fixed sets into checked types with behavior. Part IV covers PHP 8's **modern language features** — attributes, `match`, fibers, and 8.4's property hooks and asymmetric visibility.

<!--APPEND-PART-IV-->
