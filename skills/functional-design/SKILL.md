---
name: functional-design
description: Use when starting design, review, or refactoring in a functional codebase, or when unsure which functional-design skill fits a symptom.
---

# Functional Design

## Overview

This pack turns three books into executable design rules for functional
codebases: **A Philosophy of Software Design** (Ousterhout) on complexity
and modules, **Domain Modeling Made Functional** (Wlaschin) on types and
workflows, and **Functional Design** (Martin) on immutability, SOLID, and
patterns.

One method connects them: make the domain explicit in types, express
behaviour as composed total functions, push effects to the edges, and hide
everything else behind deep interfaces.

## When to use

- Starting a new module, workflow, endpoint, or bounded context
- A small change forces edits in many places, or nobody can predict what
  a change will break
- Reviewing a design or a diff and needing a concrete checklist
- Unsure which skill in this pack applies to the problem in front of you

Not for: language syntax lookups, or build and tooling problems.

## The design loop

Run in order. Skip a step only when the previous one proved it irrelevant.

1. Say what the software must do in the domain's own words, as commands
   and events. See
   [capturing-the-domain](../capturing-the-domain/SKILL.md).
2. Model the data so impossible states cannot be built. See
   [modeling-with-algebraic-types](../modeling-with-algebraic-types/SKILL.md)
   and
   [making-illegal-states-unrepresentable](../making-illegal-states-unrepresentable/SKILL.md).
3. Write the workflow as a pipeline of total functions, typed end to end.
   See
   [designing-workflow-pipelines](../designing-workflow-pipelines/SKILL.md).
4. Decide where effects live: pure core, effectful shell. See
   [separating-pure-core-from-shell](../separating-pure-core-from-shell/SKILL.md).
5. Shape the modules so each hides more than it reveals. See
   [designing-deep-modules](../designing-deep-modules/SKILL.md) and
   [hiding-information](../hiding-information/SKILL.md).
6. Name things precisely and comment only what code cannot say. See
   [choosing-precise-names](../choosing-precise-names/SKILL.md).
7. Audit the result against the red-flag catalogue. See
   [reviewing-functional-design](../reviewing-functional-design/SKILL.md).

## Symptom to skill

- Small change touches many files -> [diagnosing-complexity](../diagnosing-complexity/SKILL.md)
- Shipping fast now, paying later -> [programming-strategically](../programming-strategically/SKILL.md)
- Reader cannot tell what matters -> [deciding-what-matters](../deciding-what-matters/SKILL.md)
- Interface as large as the code behind it -> [designing-deep-modules](../designing-deep-modules/SKILL.md)
- Callers know internal details -> [hiding-information](../hiding-information/SKILL.md)
- Layers repeat the same abstraction -> [separating-layers](../separating-layers/SKILL.md)
- Unsure whether to split a function -> [splitting-and-joining-code](../splitting-and-joining-code/SKILL.md)
- Dependency direction feels wrong -> [applying-solid-functionally](../applying-solid-functionally/SKILL.md)
- Code and business speak different words -> [capturing-the-domain](../capturing-the-domain/SKILL.md)
- Types are records of primitives -> [modeling-with-algebraic-types](../modeling-with-algebraic-types/SKILL.md)
- Booleans and nullable fields encode state -> [making-illegal-states-unrepresentable](../making-illegal-states-unrepresentable/SKILL.md)
- Strings and numbers used raw -> [constraining-primitive-values](../constraining-primitive-values/SKILL.md)
- Status fields and if-ladders -> [modeling-state-machines](../modeling-state-machines/SKILL.md)
- Unclear what one transaction covers -> [enforcing-consistency-boundaries](../enforcing-consistency-boundaries/SKILL.md)
- Use case spread across services -> [designing-workflow-pipelines](../designing-workflow-pipelines/SKILL.md)
- Functions do not fit together -> [composing-functions](../composing-functions/SKILL.md)
- Database calls deep inside logic -> [parameterizing-dependencies](../parameterizing-dependencies/SKILL.md)
- Errors thrown and caught everywhere -> [handling-errors-with-results](../handling-errors-with-results/SKILL.md)
- Error handling dwarfs the happy path -> [defining-errors-out-of-existence](../defining-errors-out-of-existence/SKILL.md)
- Logic cannot be tested without I/O -> [separating-pure-core-from-shell](../separating-pure-core-from-shell/SKILL.md)
- Shared mutable state or race conditions -> [managing-state-immutably](../managing-state-immutably/SKILL.md)
- Wire and storage shapes leak inward -> [crossing-io-boundaries](../crossing-io-boundaries/SKILL.md)
- Reaching for a class-based pattern -> [translating-gof-patterns](../translating-gof-patterns/SKILL.md)
- Loops accumulating into variables -> [folding-over-data](../folding-over-data/SKILL.md)
- Deep recursion or expensive repeats -> [using-recursion-and-laziness](../using-recursion-and-laziness/SKILL.md)
- Names are vague or hard to choose -> [choosing-precise-names](../choosing-precise-names/SKILL.md)
- Comments restate the code -> [writing-useful-comments](../writing-useful-comments/SKILL.md)
- Tests need heavy mocking -> [testing-functional-code](../testing-functional-code/SKILL.md)
- Need to judge a design or a diff -> [reviewing-functional-design](../reviewing-functional-design/SKILL.md)
- Imperative code to be moved forward -> [refactoring-toward-functional-design](../refactoring-toward-functional-design/SKILL.md)

## Language packs

Core skills use a neutral notation. For real syntax, load the pack that
matches the project and use it alongside the core skill.

- [functional-javascript](../functional-javascript/SKILL.md)
- [functional-typescript](../functional-typescript/SKILL.md)
- [functional-typescript-effect](../functional-typescript-effect/SKILL.md)
- [functional-typescript-ts-pattern](../functional-typescript-ts-pattern/SKILL.md)
- [functional-react-nextjs](../functional-react-nextjs/SKILL.md)
- [functional-elixir-phoenix](../functional-elixir-phoenix/SKILL.md)

## Quick reference

| Question                     | Answer                             |
| ---------------------------- | ---------------------------------- |
| Where does validation go?    | At the boundary, into domain types |
| Where does I/O go?           | Edges only; core stays pure        |
| How are errors returned?     | Result values, not exceptions      |
| How are dependencies passed? | As function parameters             |
| What makes an interface good | It hides far more than it reveals  |
| When is a design done?       | When the red-flag audit finds none |

## Red flags

- A design decision was made before anyone named the domain concept
- A type can represent a state the business forbids
- A function's signature does not say what it can fail with
- A module's interface is as complicated as its implementation
- Only one design was considered

## Further reading

- [notation.md](references/notation.md) is the neutral notation used by
  every core skill in this pack.
- [design-loop.md](references/design-loop.md) is a worked pass through
  the seven steps on one small feature.
- [book-map.md](references/book-map.md) maps each book to the skills that
  carry its material.
- [principles.md](references/principles.md) is every rule in the pack
  compressed onto one page, for when there is no time to read a skill.
