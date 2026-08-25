# Audit

An audit of this pack against the goals it was built for: distil three
books into agent-usable skills, keep them language-agnostic, make them
work in both Claude Code and Codex, and pass `markdownlint` under default
rules with no configuration.

## What was built

| Item                        | Count  |
| --------------------------- | ------ |
| Skills                      | 37     |
| Core, language-agnostic     | 31     |
| Language packs              | 6      |
| Markdown files under skills | 112    |
| Reference files             | 75     |
| Lines of markdown           | 15,194 |
| Words                       | 81,718 |

## Verification

All five checks in `scripts/verify.sh` pass.

| Check               | Result                                                |
| ------------------- | ----------------------------------------------------- |
| markdownlint        | Clean, default rules, no config, no inline directives |
| Frontmatter         | 37 of 37 have exactly `name` + `description`          |
| Name matches folder | 37 of 37, all kebab-case                              |
| Description length  | Longest is 158 characters, cap is 160                 |
| Description opening | 37 of 37 begin with "Use when"                        |
| Codex list budget   | 6,417 characters against a limit of 8,000             |
| Relative links      | 0 broken across 112 files                             |
| Index coverage      | Every skill is reachable from `functional-design`     |
| Orphans             | None; every skill has an incoming link                |

The linter is `markdownlint-cli` at its defaults. Notable defaults this
pack had to satisfy: `MD013` at 80 columns applied to code blocks and
tables, `MD060` requiring aligned table pipes, `MD024` forbidding
duplicate headings anywhere in a file, `MD033` forbidding inline HTML,
and `MD040` requiring a language on every fence.

`PROMPT.md` is excluded from linting. It is the input brief for this
work, written in Thai, not a produced artefact.

## Coverage: A Philosophy of Software Design

| Chapter                      | Carried by                         |
| ---------------------------- | ---------------------------------- |
| 1 Introduction               | `diagnosing-complexity`            |
| 2 Nature of Complexity       | `diagnosing-complexity`            |
| 3 Working Code Isn't Enough  | `programming-strategically`        |
| 4 Modules Should Be Deep     | `designing-deep-modules`           |
| 5 Information Hiding         | `hiding-information`               |
| 6 General-Purpose Modules    | `designing-deep-modules`           |
| 7 Layer and Abstraction      | `separating-layers`                |
| 8 Pull Complexity Downward   | `separating-layers`                |
| 9 Together or Apart          | `splitting-and-joining-code`       |
| 10 Errors Out of Existence   | `defining-errors-out-of-existence` |
| 11 Design It Twice           | `programming-strategically`        |
| 12 Why Write Comments        | `writing-useful-comments`          |
| 13 Non-Obvious Comments      | `writing-useful-comments`          |
| 14 Choosing Names            | `choosing-precise-names`           |
| 15 Comments First            | `writing-useful-comments`          |
| 16 Modifying Existing Code   | `programming-strategically`        |
| 17 Consistency               | `programming-strategically`        |
| 18 Code Should Be Obvious    | `deciding-what-matters`            |
| 19 Software Trends           | Split across four skills, below    |
| 20 Designing for Performance | `programming-strategically`        |
| 21 Decide What Matters       | `deciding-what-matters`            |
| Red flag summary             | `reviewing-functional-design`      |

Chapters 6, 8, 11, 15, 17 and 20 sit in a reference file inside the
skill named, not in its `SKILL.md`.

Chapter 16 is also carried by
`refactoring-toward-functional-design`. Chapter 19 is split: the
incremental-development critique is in `programming-strategically`, the
test-driven-design critique in `testing-functional-code`, the design
patterns caution in `translating-gof-patterns`, and the accessors and
inheritance critique in `applying-solid-functionally`.

## Coverage: Domain Modeling Made Functional

| Chapter                      | Carried by                             |
| ---------------------------- | -------------------------------------- |
| 1 Introducing DDD            | `capturing-the-domain`                 |
| 2 Understanding the Domain   | `capturing-the-domain`, reference      |
| 3 A Functional Architecture  | `separating-pure-core-from-shell`      |
| 4 Understanding Types        | `modeling-with-algebraic-types`        |
| 5 Domain Modeling with Types | Three skills, below                    |
| 6 Integrity and Consistency  | `enforcing-consistency-boundaries`     |
| 7 Workflows as Pipelines     | `designing-workflow-pipelines`         |
| 8 Understanding Functions    | `composing-functions`                  |
| 9 Composing a Pipeline       | `designing-workflow-pipelines`         |
| 10 Working with Errors       | `handling-errors-with-results`         |
| 11 Serialization             | `crossing-io-boundaries`, reference    |
| 12 Persistence               | `crossing-io-boundaries`, reference    |
| 13 Evolving a Design         | `refactoring-toward-functional-design` |

Chapter 5 is split across `modeling-with-algebraic-types`,
`constraining-primitive-values`, and `modeling-state-machines`. Chapter 6
is also carried by `making-illegal-states-unrepresentable`. Chapter 9
additionally carries `parameterizing-dependencies`. Bounded contexts and
context maps from chapters 2 and 3 are in
`capturing-the-domain/references/bounded-contexts.md`.

## Coverage: Functional Design

| Theme                       | Carried by                        |
| --------------------------- | --------------------------------- |
| Immutability and assignment | `managing-state-immutably`        |
| Persistent data structures  | `managing-state-immutably`        |
| Concurrency without locks   | `managing-state-immutably`        |
| Recursion and iteration     | `using-recursion-and-laziness`    |
| Laziness and streams        | `using-recursion-and-laziness`    |
| Statefulness at the edge    | `separating-pure-core-from-shell` |
| Reduce, fold, monoids       | `folding-over-data`               |
| Typing discipline           | `modeling-with-algebraic-types`   |
| SOLID for functions         | `applying-solid-functionally`     |
| Design patterns in FP       | `translating-gof-patterns`        |
| Test-driven development     | `testing-functional-code`         |

Persistent structures, concurrency, and typing discipline sit in
reference files inside those skills.

The book's extended case studies are not reproduced. Their teaching value
is carried by
`designing-workflow-pipelines/references/worked-example.md`, an
end-to-end workflow built with the same method. This is a deliberate
omission: the pack is a working checklist, not a substitute for the
books.

## Gaps found during the audit, and closed

1. **DMMF chapter attributions were wrong in four skills.** Pipelines
   cited 9-10, functions cited 7-8, state machines cited 5 and 9, and
   dependencies cited 10. Corrected to 7 and 9, 8, 5 and 7, and 9.
2. **The four excuses for not writing comments were referred to but not
   stated.** Added as a table with answers in `writing-useful-comments`.
3. **The incremental-development critique from chapter 19 was missing.**
   Added as a section on incrementing on abstractions rather than
   features in `programming-strategically`, with the related caution
   about any practice that focuses on one unit at a time.
4. **No single-page summary existed.** Added
   `functional-design/references/principles.md`, every rule in the pack
   compressed, for use when there is no budget to load a skill.

## Requirements check

- **Works in Claude Code and Codex.** Met. Frontmatter carries only
  `name` and `description`; cross-links are sibling-relative, so they
  resolve under both `.claude/skills/` and `.agents/skills/`; and no
  instruction names a runtime-specific tool.
- **Copied into a target project.** Met. A flat `skills/` directory,
  with the two copy commands documented in the README.
- **Language-agnostic core.** Met. The 31 core skills use a neutral
  notation defined once in `functional-design/references/notation.md`.
- **Extra skills for the named stacks.** Met. JavaScript, TypeScript,
  TypeScript with Effect, TypeScript with ts-pattern, React and Next.js,
  Elixir and Phoenix.
- **Markdown in English only.** Met.
- **Passes markdownlint with no warnings or errors.** Met.
- **Default rules only, no overrides or inline directives.** Met, and
  asserted by `scripts/verify.sh` rather than only claimed.
- **Extracted in depth.** Met. 75 reference files sit behind the 37
  skills, so each skill stays short enough to always read while the
  depth loads only when it is needed.
- **Audited before delivery.** This document.

## Known limitations

**Codex list budget.** The 37 descriptions total 6,417 characters against
a limit of about 8,000. A project that installs all 37 plus a dozen of
its own skills can exceed it, and Codex will truncate the list. Copy only
the language packs the project uses; core plus two packs is roughly 5,700
characters.

**Effect API drift.** `functional-typescript-effect` targets Effect 3.
The library has changed shape across major versions, and the skill says
so at the top. Check the installed version before following its examples.

**No automated skill-behaviour tests.** The pack is verified structurally
by `scripts/verify.sh`, not behaviourally. Whether an agent routes the
right symptom to the right skill was checked by reading the index routing
table, not by running scenarios.

**Neutral notation is not executable.** Core examples are written in a
notation defined in `functional-design/references/notation.md`. That
keeps them honest about being language-independent, and it means they
cannot be compiled or run. The language packs carry runnable syntax.

**One worked example.** There is a single end-to-end example, in
`designing-workflow-pipelines/references/worked-example.md`. A second, in
a different domain, would help readers who find the clinic domain
unfamiliar.

## Attribution

Every rule here is a restatement or synthesis, credited at chapter level
inside each skill. No book text is reproduced. The books remain worth
reading in full; this pack is a checklist derived from them.
