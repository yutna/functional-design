# Two Schools of Functional Design

Where the type-first and data-first schools agree, where they genuinely
conflict, and what each one is actually optimising for.

Source: not from the three books. Data-Oriented Programming (Sharvit),
Out of the Tar Pit (Moseley and Marks), and Rich Hickey's talks.

## The four principles of data-oriented programming

| No. | Principle                                        | This pack |
| --- | ------------------------------------------------ | --------- |
| 1   | Separate code from data                          | agrees    |
| 2   | Represent data with generic structures           | conflicts |
| 3   | Data is immutable                                | agrees    |
| 4   | Separate the data schema from its representation | conflicts |

Two of four agree, and they are not the trivial two. The conflict is
narrower than the two schools' rhetoric suggests, and knowing exactly
where it sits is what lets you decide per value instead of per religion.

## Principle 1 — separate code from data

Data is inert. Behaviour lives in functions that take data and return
data. No methods attached to values, no objects that own their own rules.

**This pack already requires it.** Every signature in the notation takes
data and returns data;
[separating-pure-core-from-shell](../../separating-pure-core-from-shell/SKILL.md)
separates decisions from effects;
[parameterizing-dependencies](../../parameterizing-dependencies/SKILL.md)
passes capabilities in as functions rather than binding them to values.

A single-case wrapper does not violate this. `OrderId of String` attaches
no behaviour; it attaches a name. The constructor is a function like any
other.

## Principle 2 — represent data with generic structures

Use maps, lists, and primitives. Do not introduce a distinct type per
concept, because a distinct type is a wall: generic operations stop at
it, and every new operation needs a new method.

**This is the real conflict.** It is the direct negation of
[constraining-primitive-values](../../constraining-primitive-values/SKILL.md).

The argument for it is not laziness. It is that a codebase full of
distinct types cannot express operations over _any_ value: a generic
audit log, a structural diff, a projection that selects fields by name, a
serialiser that needs no per-type code. Every one of those is trivial
over maps and requires either reflection or per-type boilerplate over
distinct types. That cost is real and this pack does not otherwise name
it.

The argument against it is equally real: nothing stops a caller passing
the customer's map where the order's was expected, and no name in the
codebase tells a reader what a key means.

## Principle 3 — data is immutable

Values never change in place. Updates produce new values, sharing
structure with the old.

**This pack already requires it**, in
[managing-state-immutably](../../managing-state-immutably/SKILL.md).
Data-oriented programming reaches the same concurrency advice
independently: one state reference, updated by comparing and swapping on
a version, with all logic operating on immutable snapshots. That is what
[concurrency.md](../../managing-state-immutably/references/concurrency.md)
already says.

Where a difference remains, it is emphasis. Data-first treats immutability
as the load-bearing principle, because generic data with no wall around
it is only safe if nobody can mutate it. Type-first can lean on
constructors as well.

## Principle 4 — separate schema from representation

The description of a shape lives outside the shape, as its own value: a
schema you can store in a database row, compose, generate from a
specification, and hand to a validator at the boundary. The data itself
stays generic and carries no schema with it.

**This conflicts hardest** with
[making-illegal-states-unrepresentable](../../making-illegal-states-unrepresentable/SKILL.md),
whose whole method is to fuse the constraint into the representation so
the constraint cannot be skipped.

The trade is explicit on both sides:

| Fusing them (type-first)          | Splitting them (data-first)     |
| --------------------------------- | ------------------------------- |
| Constraint cannot be bypassed     | Constraint can be forgotten     |
| Changing a rule is a deployment   | Changing a rule is a row update |
| One shape per concept             | One validator over many shapes  |
| Reader learns rules from the type | Reader must find the schema     |
| Compiler proves exhaustiveness    | Tests stand in for the compiler |

This pack already crosses the line for one case: policies that change
faster than the code should be data, per
[when-to-validate-instead.md](../../making-illegal-states-unrepresentable/references/when-to-validate-instead.md).
Data-oriented programming makes that the general rule rather than the
exception.

## The lineage

**Hickey on complecting.** Two things are complected when they are
braided together such that you cannot have one without the other. His
charge against types-per-concept is that they complect the value with its
interpretation: to read the value you must accept the type's view of it.
The data-first answer is to keep values plainly readable and layer
interpretation on top, separately, as needed.

**Out of the Tar Pit** makes the same move architecturally. It splits a
system into essential state (relations of plain data), essential logic
(derivations over those relations), and accidental state and control
(caches, order, performance work). The relations are generic data on
purpose: any derivation can read any relation, so logic composes without
the walls. See
[essential-and-accidental.md](../../diagnosing-complexity/references/essential-and-accidental.md).

## Why the schools disagree about where they are

Each school is strongest where the other's tooling is weakest.

Data-first was argued from Clojure and JavaScript, where a distinct type
buys almost nothing enforceable, and where the schema has to be a runtime
value anyway. In that setting the wall costs you generic operations and
returns very little, so tearing it down is straightforwardly correct.

Type-first was argued from F# and its relatives, where a distinct type is
free to declare, checked everywhere, and proves exhaustiveness. In that
setting the wall is nearly free and returns a great deal.

Neither is wrong about its own setting. Both are wrong when they
generalise. That is why this pack keeps one default and one list of
observable exceptions rather than picking a side per language: real
projects span both, and the same project has values of both kinds.

## What both schools agree most codebases get wrong

Worth stating, because it is where the agreement is largest and the
practice is worst:

1. Untrusted input is parsed once, at the edge, into something the rest
   of the code trusts. Not checked repeatedly, defensively, inward.
2. Data does not mutate. Not "mostly", not "except for the cache".
3. Behaviour is not attached to data. Functions take data, return data.
4. Optional fields are not a substitute for representing a choice.

A codebase doing those four is well designed under either school. A
codebase doing none of them is not saved by choosing a school.
