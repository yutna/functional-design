# The Smell Catalogue, Read Functionally

Fowler's twenty-four smells, each with its one-line test and where to go
in this pack. Read the last two sections first if you already know the
list: several of these smells mean something different in functional
code, and four of them are not smells here at all.

Source: not from the three books. Refactoring, 2nd edition, chapter 3
(Fowler).

## Naming and comments

### Mysterious Name

**Test.** You cannot say what it is from the name.
Go to [choosing-precise-names](../../choosing-precise-names/SKILL.md).

### Comments

**Test.** A comment exists to compensate for code that does not explain
itself. Fowler treats the comment as deodorant for a smell underneath.
Go to [writing-useful-comments](../../writing-useful-comments/SKILL.md),
which parts company with Fowler here: a comment recording _why_, or
recording what the code cannot say, is not deodorant. Only a comment
restating _what_ is.

## Duplication and size

### Duplicated Code

**Test.** The same fact is written down twice.
Go to
[splitting-and-joining-code](../../splitting-and-joining-code/SKILL.md).

### Long Function

**Test.** You must scroll, or hold intermediate state in your head, to
read it.
Go to
[splitting-and-joining-code](../../splitting-and-joining-code/SKILL.md),
and to Split Phase and Extract Function in
[fowler-moves.md](fowler-moves.md). Note the counter-pressure: a function
split into pieces each of which needs the others is worse, not better.

### Large Class

**Test.** A module has too many responsibilities. In functional code this
is a module with an unrelated set of exported functions.
Go to [designing-deep-modules](../../designing-deep-modules/SKILL.md).

### Lazy Element

**Test.** A function or module whose body is as small as its name.
Go to
[splitting-and-joining-code](../../splitting-and-joining-code/SKILL.md);
the move is Inline Function.

### Long Parameter List

**Test.** More arguments than a reader can keep straight, or several that
always travel together.
Go to [modeling-with-algebraic-types](../../modeling-with-algebraic-types/SKILL.md);
the moves are Introduce Parameter Object and Preserve Whole Object.

## Data

### Global Data

**Test.** Data any code can reach and any code can change.
Go to [managing-state-immutably](../../managing-state-immutably/SKILL.md).

### Mutable Data

**Test.** A value changes in place, so its meaning depends on when you
look.
Go to [managing-state-immutably](../../managing-state-immutably/SKILL.md).
This is a smell Fowler softens for performance; functional design does
not.

### Data Clumps

**Test.** The same three or four values appear together everywhere.
Go to
[modeling-with-algebraic-types](../../modeling-with-algebraic-types/SKILL.md).
The clump is a concept the domain has and the code does not.

### Primitive Obsession

**Test.** Domain values carried as raw strings, numbers, or booleans.
Go to
[constraining-primitive-values](../../constraining-primitive-values/SKILL.md).

### Temporary Field

**Test.** A field only set and read during one operation.
Go to
[modeling-state-machines](../../modeling-state-machines/SKILL.md), or
delete the field: it is usually accidental state. See
[essential-and-accidental.md](../../diagnosing-complexity/references/essential-and-accidental.md).

### Data Class

**Test.** A class that is only fields and accessors, with no behaviour.
**Not a smell here.** See the next section.

## Change patterns

### Divergent Change

**Test.** One module is edited for several unrelated reasons.
Go to [diagnosing-complexity](../../diagnosing-complexity/SKILL.md);
Ousterhout's name for the cause is a module with more than one purpose.

### Shotgun Surgery

**Test.** One conceptual change requires edits in many places.
Go to [diagnosing-complexity](../../diagnosing-complexity/SKILL.md);
this is change amplification exactly.

### Speculative Generality

**Test.** Machinery that exists for a requirement nobody has.
Go to
[programming-strategically](../../programming-strategically/SKILL.md).
Delete it; it is accidental complexity with no defender.

## Coupling

### Feature Envy

**Test.** A function is more interested in another module's data than its
own.
Go to [hiding-information](../../hiding-information/SKILL.md). In
functional code this usually means the function belongs in the module
that owns the type.

### Message Chains

**Test.** A caller navigates `a.b.c.d` to reach what it wants.
Go to [designing-deep-modules](../../designing-deep-modules/SKILL.md).
The chain is the shape of what the caller had to know.

### Middle Man

**Test.** A module whose functions only forward to another.
Go to [separating-layers](../../separating-layers/SKILL.md); the flag in
this pack is the pass-through function.

### Insider Trading

**Test.** Two modules quietly depend on each other's internals.
Go to [hiding-information](../../hiding-information/SKILL.md); this is
information leakage.

## Conditionals and inheritance

### Repeated Switches

**Test.** The same set of cases is matched in several places.
**Often not a smell here.** See the next section.

### Loops

**Test.** An explicit loop where a pipeline would say what is happening.
Go to [folding-over-data](../../folding-over-data/SKILL.md). Fowler lists
the loop itself as the smell; here the smell is narrower — a loop
accumulating into a mutable variable.

### Alternative Classes with Different Interfaces

**Test.** Two things do the same job through different names.
Go to
[applying-solid-functionally](../../applying-solid-functionally/SKILL.md).
Mostly evaporates without classes: the functional form is two function
types that should have been one.

### Refused Bequest

**Test.** A subclass inherits what it does not want.
**Does not occur here.** There is no inheritance to refuse. If you see
its shape, it is a sum type whose cases do not belong together: go to
[modeling-with-algebraic-types](../../modeling-with-algebraic-types/SKILL.md).

## Smells that stop being smells here

This is the section that matters if you arrive carrying Fowler's list. An
agent applying it unchanged to functional code misflags exactly these
four, and each misflag pushes the design the wrong way.

| Fowler's smell    | Here                                       |
| ----------------- | ------------------------------------------ |
| Data Class        | The goal. Data has no behaviour by design. |
| Loops             | Only a smell when mutating an accumulator  |
| Repeated Switches | Often the correct trade-off                |
| Refused Bequest   | Cannot occur; no inheritance               |

**Data Class.** Fowler's remedy is to move behaviour into the class until
it stops being a bag of fields. That is the opposite of principle one of
data-oriented design and of this pack's whole notation: data is inert,
behaviour lives in functions over it. A record of fields with a smart
constructor and no methods is a correct functional type. Do not "fix" it.

**Loops.** The smell is not iteration. It is iteration that accumulates
into a mutable variable, which hides what is being computed. A `for` loop
whose body is a fold with no mutation is fine, if less clear than the
fold. Rewrite for clarity, not because a loop appeared.

**Repeated Switches.** Fowler's remedy is polymorphism: push each case
into a subclass so the switch happens once. In a functional design the
same set of cases is matched in every function that consumes the sum
type, and that is the deliberate trade — the expression problem. Matching
in ten functions means adding a case forces you to visit ten places, and
the compiler names all ten. That is a feature. Only reach for a single
dispatch table when the _set of cases_ changes more often than the set of
operations. See
[translating-gof-patterns](../../translating-gof-patterns/SKILL.md).

**Refused Bequest** and **Alternative Classes** are largely artefacts of
inheritance. Their functional residue is a sum type with unrelated cases,
or two function types that should be one.

## Two vocabularies, one diagnosis

Fowler's smells and Ousterhout's symptoms describe the same failures from
opposite ends: Fowler names what the code looks like, Ousterhout names
what it costs you. Resolve them to one diagnosis rather than reporting
both.

| Fowler                    | Ousterhout                 |
| ------------------------- | -------------------------- |
| Shotgun Surgery           | Change amplification       |
| Duplicated Code           | Change amplification       |
| Divergent Change          | Module without one purpose |
| Insider Trading           | Information leakage        |
| Message Chains            | Information leakage        |
| Mysterious Name           | Obscurity                  |
| Temporary Field           | Cognitive load             |
| Long Parameter List       | Cognitive load             |
| Mutable Data, Global Data | Unknown unknowns           |

## Using a smell

A smell is a prompt to look, never a reason to change code. Three rules:

1. **Ask whether the thing should exist at all.** If the requirement,
   stated in the domain's words, never mentions it, delete it instead of
   moving it. See
   [essential-and-accidental.md](../../diagnosing-complexity/references/essential-and-accidental.md).
2. **Name the cost before the fix.** "This is a Long Function" is not a
   finding; "a reader must hold four intermediate values" is.
3. **Check the smell still applies here.** Four of the twenty-four do
   not, and using them anyway makes the design worse.
4. **One move at a time, tests green between each.** See
   [fowler-moves.md](fowler-moves.md).
