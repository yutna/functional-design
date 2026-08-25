---
name: refactoring-toward-functional-design
description: Use when moving imperative or object-oriented code toward a functional design, or when an existing design must absorb new requirements without decaying.
---

# Refactoring Toward Functional Design

## Overview

Most functional codebases are not new. They are imperative or
object-oriented systems being moved, module by module, while they keep
running. The work is not a rewrite: it is a sequence of small,
behaviour-preserving moves, each of which pays for itself, applied to the
code you are already editing for another reason.

The second half of the job is keeping a design clean once it is right.
Designs decay by absorbing requirements they were not shaped for, one
reasonable-looking patch at a time.

Source: Domain Modeling Made Functional, chapter 13 (Wlaschin), and A
Philosophy of Software Design, chapter 16 (Ousterhout).

## When to use

- Editing imperative or object-oriented code in a project moving to a
  functional style
- A new requirement does not fit the existing model
- A module has accumulated special cases
- Deciding whether to patch or restructure
- Planning an incremental migration

Not for: designing something new, which starts at
[functional-design](../functional-design/SKILL.md).

## Core rules

1. **Refactor where you are already working.** Unrelated cleanup is hard
   to review and hides the real change.
2. **One move at a time, tests green between each.** A move that cannot
   be verified is a rewrite in disguise.
3. **Start at the boundary of the module you are in**, not at the centre
   of the system.
4. **Make each move pay for itself.** If a step leaves the code no
   better, it is not one of the moves below.
5. **Move rules inward, effects outward.** Every step should shrink the
   impure region.
6. **Convert types before functions.** A precise type makes the function
   changes obvious and often mechanical.
7. **Never widen a type to accommodate a new requirement.** Ask first
   whether the requirement is a different concept.

## The ordered moves

Apply in this order. Each one makes the next easier.

| Order | Move                                         |
| ----- | -------------------------------------------- |
| 1     | Wrap primitives in domain types              |
| 2     | Replace status strings with choice types     |
| 3     | Collapse correlated optionals into cases     |
| 4     | Return `Result` instead of throwing          |
| 5     | Pass the clock, random, and identifiers in   |
| 6     | Turn a service parameter into function types |
| 7     | Extract the pure decision from the effects   |
| 8     | Give the workflow stage types                |
| 9     | Add a boundary mapping, split the DTO        |
| 10    | Make the aggregate opaque                    |

Each move, with its mechanics and its verification, is in
[migration-moves.md](references/migration-moves.md).

## Pattern

A typical starting point:

```text
class OrderService {
  save(order) {
    if (!order.customerId) throw new Error("bad order")
    order.status = "placed"
    order.placedAt = new Date()
    this.repo.update(order)
    this.mailer.send(order.email, "placed")
  }
}
```

After moves 1, 2, 4, 5 and 7, in five separate commits:

```text
-- pure
placeOrder :
  Instant -> ValidatedOrder -> Result<PlacedOrder, PlaceOrderError>

-- shell
handlePlaceOrder repo mailer now raw =
  validateOrder raw
    |> bind (placeOrder now)
    |> bind (\o -> save repo o |> map (const o))
    |> bind (\o -> notify mailer o)
```

No step required understanding the whole system, and each was
individually reviewable.

## Deciding: patch or restructure

When a new requirement arrives, ask whether it is an instance of what the
module already claims to do.

| Situation                           | Action                 |
| ----------------------------------- | ---------------------- |
| The new case fits the abstraction   | Add it, in the idiom   |
| It is the same kind of thing, wider | Widen the abstraction  |
| It is a different kind of thing     | Split it out           |
| It fits but needs a flag            | It does not fit        |
| Fixing properly is out of budget    | Patch, record the debt |

The flag row is the one people get wrong. A boolean parameter added to
select behaviour is the standard sign that two things have been merged.
See
[splitting-and-joining-code](../splitting-and-joining-code/SKILL.md).

## Keeping it clean afterwards

- Every change leaves the module at least slightly better.
- When a comment becomes false, fix it in the same edit.
- When a name stops matching, rename it in the same edit.
- When the purpose sentence acquires an "and", split before adding more.
- Record every knowingly deferred improvement in the module, not in a
  ticket. See
  [keeping-design-clean.md](references/keeping-design-clean.md).

## Red flags

- A refactoring branch that has been open for weeks
- A commit that changes behaviour and structure together
- A migration that requires the whole team to stop
- A new adapter layer added before anything is moved through it
- Both the old and the new shape in use with no plan to remove one
- A "temporary" flag distinguishing old and new code paths

## Common mistakes

- **Rewriting instead of moving.** A rewrite reproduces the design unless
  you can say what was wrong with it.
- **Building the target architecture first.** Folders and interfaces
  named after the destination, with the old code still inside.
- **Converting everything to `Result` at once.** Do it module by module,
  converting at each boundary as you reach it.
- **Migrating code nobody edits.** Effort is best spent where the change
  rate is highest.
- **Leaving two idioms in place.** Finish each module; do not leave half.
- **Refactoring without tests.** Add characterisation tests first; they
  need not be pretty, and they can be deleted afterwards.

## Related skills

- [programming-strategically](../programming-strategically/SKILL.md)
- [reviewing-functional-design](../reviewing-functional-design/SKILL.md)
- [diagnosing-complexity](../diagnosing-complexity/SKILL.md)
- [separating-pure-core-from-shell](../separating-pure-core-from-shell/SKILL.md)

## Further reading

- [migration-moves.md](references/migration-moves.md) is each move with
  its mechanics, its verification, and its payoff.
- [keeping-design-clean.md](references/keeping-design-clean.md) covers
  absorbing new requirements without decay.
