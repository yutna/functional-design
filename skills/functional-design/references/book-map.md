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

## Reading orders

- **Cleaning up an existing codebase**: `diagnosing-complexity`,
  `reviewing-functional-design`, then
  `refactoring-toward-functional-design`.
- **Designing a new feature**: `capturing-the-domain`,
  `modeling-with-algebraic-types`, `designing-workflow-pipelines`,
  `separating-pure-core-from-shell`.
- **Fixing error handling**: `handling-errors-with-results`, then
  `defining-errors-out-of-existence`.
