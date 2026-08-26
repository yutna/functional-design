# Book Map

Which skills carry which book. Use this to read the pack in an order that
matches a book you already know, or to check coverage.

## A Philosophy of Software Design, John Ousterhout

| Theme                         | Skill                                  |
| ----------------------------- | -------------------------------------- |
| Complexity, its symptoms      | `diagnosing-complexity`                |
| Strategic vs tactical, twice  | `programming-strategically`            |
| What matters, obviousness     | `deciding-what-matters`                |
| Deep modules, general purpose | `designing-deep-modules`               |
| Information hiding and leaks  | `hiding-information`                   |
| Layers, complexity downward   | `separating-layers`                    |
| Together or apart             | `splitting-and-joining-code`           |
| Errors out of existence       | `defining-errors-out-of-existence`     |
| Names                         | `choosing-precise-names`               |
| Comments, comments first      | `writing-useful-comments`              |
| Modifying existing code       | `refactoring-toward-functional-design` |
| Trends, tests, patterns       | `testing-functional-code`              |

## Domain Modeling Made Functional, Scott Wlaschin

| Theme                         | Skill                                   |
| ----------------------------- | --------------------------------------- |
| Shared language, events       | `capturing-the-domain`                  |
| Bounded contexts, context map | `capturing-the-domain`                  |
| Functional architecture       | `separating-pure-core-from-shell`       |
| Algebraic types               | `modeling-with-algebraic-types`         |
| Illegal states                | `making-illegal-states-unrepresentable` |
| Constrained values            | `constraining-primitive-values`         |
| Choice types as lifecycles    | `modeling-state-machines`               |
| Integrity and consistency     | `enforcing-consistency-boundaries`      |
| Workflows as pipelines        | `designing-workflow-pipelines`          |
| Functions, currying, totality | `composing-functions`                   |
| Dependencies                  | `parameterizing-dependencies`           |
| Working with errors           | `handling-errors-with-results`          |
| Serialization and persistence | `crossing-io-boundaries`                |
| Evolving a design             | `refactoring-toward-functional-design`  |

## Functional Design, Robert C. Martin

| Theme                         | Skill                          |
| ----------------------------- | ------------------------------ |
| Immutability, persistent data | `managing-state-immutably`     |
| Concurrency without locks     | `managing-state-immutably`     |
| Recursion, laziness           | `using-recursion-and-laziness` |
| Reduce, fold, monoids         | `folding-over-data`            |
| SOLID for functions           | `applying-solid-functionally`  |
| Design patterns in FP         | `translating-gof-patterns`     |
| Test-driven development       | `testing-functional-code`      |

## Beyond the books

Three skills in this pack are not derived from any of the three books.
They are marked as such in their own overviews, and none claims chapter
provenance.

| Skill                          | Why it is here                         |
| ------------------------------ | -------------------------------------- |
| `making-effects-reliable`      | Effects across a process can duplicate |
| `designing-what-to-observe`    | A running system must explain itself   |
| `choosing-types-or-plain-data` | Not every shape should be modelled     |

## Supporting sources

Three further works fill gaps the brief's three books leave. None gets a
skill of its own; each lands in the skill that already owns its subject,
labelled where it appears.

| Source                              | Contributes                     |
| ----------------------------------- | ------------------------------- |
| Refactoring, 2nd ed. (Fowler)       | Smell catalogue, tactical moves |
| Out of the Tar Pit (Moseley, Marks) | Essential versus accidental     |
| Data-Oriented Programming (Sharvit) | The data-first school           |

Where each one lives:

- **Fowler** —
  [smell-catalogue.md](../../refactoring-toward-functional-design/references/smell-catalogue.md)
  and
  [fowler-moves.md](../../refactoring-toward-functional-design/references/fowler-moves.md).
  Read the catalogue's last two sections first: four of the twenty-four
  smells are not smells in functional code.
- **Out of the Tar Pit** —
  [essential-and-accidental.md](../../diagnosing-complexity/references/essential-and-accidental.md).
  It adds a necessity question in front of Ousterhout's locality
  question: complexity you added should be deleted, not refactored.
- **Sharvit** — the whole of `choosing-types-or-plain-data`, which sets
  data-oriented programming's four principles against this pack's rules
  and marks the two that genuinely conflict. It is a tiebreaker, not a
  fourth authority: type-first stays the default, and the data-first
  route opens only on named observable facts.

Why no fourth authority: two contradictory rules of equal standing are
worse than one rule, because whichever was read last wins. The conflict
is therefore resolved once, in one place, per value.

## Reading orders

- **Cleaning up an existing codebase**: `diagnosing-complexity`,
  `reviewing-functional-design`, then
  `refactoring-toward-functional-design`.
- **Designing a new feature**: `capturing-the-domain`,
  `modeling-with-algebraic-types`, `designing-workflow-pipelines`,
  `separating-pure-core-from-shell`.
- **Fixing error handling**: `handling-errors-with-results`, then
  `defining-errors-out-of-existence`.
