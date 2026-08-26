# Audit

An audit of this pack against the goals it was built for: distil three
books into agent-usable skills, keep them language-agnostic, make them
work in both Claude Code and Codex, and pass `markdownlint` under default
rules with no configuration.

## What was built

| Item (skills and evals)     | Count  |
| --------------------------- | ------ |
| Skills                      | 39     |
| Core, language-agnostic     | 33     |
| Language packs              | 6      |
| Markdown files under skills | 124    |
| Reference files             | 85     |
| Worked examples             | 5      |
| Routing eval cases          | 74     |
| Agent scenarios             | 29     |
| Lines of markdown           | 17,439 |
| Words                       | 95,460 |

## Verification

All six checks in `scripts/verify.sh` pass.

| Check               | Result                                         |
| ------------------- | ---------------------------------------------- |
| markdownlint        | Clean, default rules, no config, no directives |
| Frontmatter         | 39 of 39 have exactly `name` + `description`   |
| Name matches folder | 39 of 39, all kebab-case                       |
| Description length  | Longest is 158 characters, cap is 160          |
| Description opening | 39 of 39 begin with "Use when"                 |
| Codex list budget   | 6,725 characters against a limit of 8,000      |
| Relative links      | 0 broken across 124 files                      |
| Routing coverage    | 74 of 74 cases in the top 3; 58 first          |
| Index coverage      | Every skill reachable from `functional-design` |
| Orphans             | None; every skill has an incoming link         |

The linter is `markdownlint-cli` at its defaults. Notable defaults this
pack had to satisfy: `MD013` at 80 columns applied to code blocks and
tables, `MD060` requiring aligned table pipes, `MD024` forbidding
duplicate headings anywhere in a file, `MD033` forbidding inline HTML,
`MD010` forbidding hard tabs even inside code blocks, and `MD040`
requiring a language on every fence.

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

## Gaps found in the first audit, and closed

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

A second review, of whether complete extraction was the same as being
useful, produced the work recorded under Increment 2 below.

## Beyond the three books

Two skills are not derived from the books, and say so in their own
overviews instead of citing a chapter. They are here because a functional
design that stops at the process boundary leaves real problems
unanswered.

| Skill                       | What it covers                      |
| --------------------------- | ----------------------------------- |
| `making-effects-reliable`   | Idempotency, delivery, compensation |
| `designing-what-to-observe` | What to log, trace and measure      |

Both build on book-derived skills — the pure core and shell split, the
consistency boundary, deciding what matters — and neither claims chapter
provenance. `functional-design/references/book-map.md` records the same
distinction where a reader will meet it.

Three smaller extensions carry no chapter citation either: the
calibration guidance in the index, the boundary schema library
comparison in `functional-typescript`, and the evals.

## Increment 2

Added after the first delivery, in response to the question of whether
complete extraction was the same as being useful.

| Added                        | Where                                      |
| ---------------------------- | ------------------------------------------ |
| Calibration of design effort | Index skill, plus a reference              |
| Routing evals, 74 cases      | `evals/`, gated in `verify.sh`             |
| Three more worked examples   | Refactor, read model, long-running process |
| Reliability skill            | `making-effects-reliable`                  |
| Observability skill          | `designing-what-to-observe`                |
| Schema library comparison    | `functional-typescript`                    |

### Description defects the routing check found

Writing the cases and running the scorer surfaced fifteen skills whose
descriptions lacked the words people use for the problem they solve.
All were rewritten; the worst were:

| Skill                          | Missing word           |
| ------------------------------ | ---------------------- |
| `handling-errors-with-results` | "throws"               |
| `translating-gof-patterns`     | "factory", "strategy"  |
| `using-recursion-and-laziness` | "memory"               |
| `making-effects-reliable`      | "timeout", "twice"     |
| `programming-strategically`    | "shortcut", "deadline" |
| `managing-state-immutably`     | "lost update"          |

The scorer also caught a collision it had itself created: adding "what to
call something" to `choosing-precise-names` made it outrank
`separating-layers` on a symptom about callers. Both were reworded.

Score after the rewrites: 74 of 74 cases place the expected skill in the
top three on description text alone, and 58 of 74 place it first. The
top-one figure is the number to improve; it is recorded as a baseline,
not as a target that was met.

### Scenario run against agents

The scenarios in `evals/scenarios.md` were run against fresh agents.
Each saw only the discovery list — name and description for all 39
skills — plus the scenario text. None was told which skill was expected,
or that it was being evaluated. Each chose what to open from the
descriptions alone, read it, and answered.

The first round of fifteen was written from problems that came to mind.
Counting afterwards showed it had exercised only 25 of the 39 skills,
including none of the six language packs, so a second round of fourteen
was written by working from the list of skills no scenario had reached.

| Measure                     | Round 1  | Round 2  |
| --------------------------- | -------- | -------- |
| Scenarios                   | 15       | 14       |
| Expected skill opened       | 14 of 15 | 14 of 14 |
| Expected skill opened first | 12 of 15 | 12 of 14 |
| Required substance present  | 15 of 15 | 14 of 14 |

Across both rounds, 62 skill openings covered **39 of 39 skills**, an
average of 2.1 per scenario.

Answers used vocabulary that exists only inside the pack — "conjoined
functions", "change amplification", "dependency rejection",
"at-least-once", "characterisation tests" — which is evidence the files
were read rather than the names guessed. Several added correct material
the grading list had not asked for.

**The one miss was the most important scenario.** Asked how to structure
a throwaway script, the agent did not open `functional-design`, where
the calibration table lives. It reached the right answer anyway, from a
line in `programming-strategically` that happens to exclude spikes — so
the guard against over-applying the pack was working by luck.

The cause was plain once looked for: the index description contained
none of the words that question uses. No "how much", no "warrants", no
"throwaway", no "script". It was rewritten to name that trigger, a
routing case was added for the symptom, and the scenario was re-run with
a fresh agent. It then opened `functional-design` alone and answered from
the calibration guidance, including the rule that sizes only ratchet
upward.

This is the defect the keyword lint could not have caught by itself: the
words were missing from the description _and_ from the case list,
because neither had that symptom in it. Only a real scenario surfaced
it.

### The second round, and what writing it exposed

The gap was in the eval, not the pack: fourteen skills had keyword cases
but had never been opened by an agent, among them
`reviewing-functional-design`, which the README snippet tells every
project to run before finishing a change. Writing scenarios from a list
of problems produces whatever problems come to mind; writing them from
the list of untouched skills produces coverage.

The second round routed 14 of 14 correctly. Two answers went beyond what
the grading list asked for in ways worth recording: the concurrency
scenario spotted a second race the question had not mentioned, in a
stored total sitting beside the collection it was derived from; and the
export-format scenario noted that two of the three formats are pure
while the third needs I/O, and should be split on that line.

### What the scenario run does not establish

Grading was done by the same author who wrote both the skills and the
"must contain" lists, which is the weakest part of the method. Each
scenario ran once, against one model, on one day. Full coverage means
every skill was reached at least once, not that every skill is well
tested — most were reached by a single question.

Treat the run as a spot check that the pack works end to end, not as a
score to defend or a regression test.

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
- **Design effort is calibrated.** Met. The index carries a table
  keyed to observable facts about the task, plus
  `functional-design/references/calibration.md` for the failure modes
  in both directions.
- **Routing is checked, not assumed.** Met. 74 keyword cases run in
  `verify.sh`, and 29 agent scenarios were run once, reaching every
  skill at least once; see below.

## Known limitations

**Codex list budget.** The 39 descriptions total 6,725 characters against
a limit of about 8,000. A project that installs all 39 plus a dozen of
its own skills can exceed it, and Codex will truncate the list. Copy only
the language packs the project uses.

**The routing check is a keyword lint, not an oracle.** It scores word
overlap and has no idea what any word means. A green run means every
description contains the vocabulary people use for that problem; it does
not mean an agent routes correctly. The scenario run below covers that
question, but only as a single sample.

**Effect API drift.** `functional-typescript-effect` targets Effect 3,
and `schema-libraries.md` describes Zod, Valibot, ArkType and TypeBox as
of writing. Both say so and tell the reader to check the installed
version. Anything version-specific here will age.

**Neutral notation is not executable.** Core examples use the notation in
`functional-design/references/notation.md`. That keeps them honest about
being language-independent, and means they cannot be compiled or run.
The language packs carry runnable syntax.

**One domain across the worked examples.** Four of the five use a clinic
or an order domain. A reader unfamiliar with either has to translate.

## Attribution

Every rule here is a restatement or synthesis, credited at chapter level
inside each skill. No book text is reproduced. The books remain worth
reading in full; this pack is a checklist derived from them.
