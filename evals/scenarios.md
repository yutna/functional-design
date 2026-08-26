# Scenarios

Fifteen problems in the form someone would actually bring them, each
with what a correct response has to contain. Paste one as the whole
prompt into an agent session with the pack installed.

The "must contain" lists are deliberately about substance, not wording.
An answer that reaches the same place by another route passes.

## 1. Optional fields that correlate

> Our `Shipment` type has a status string plus `trackingNumber`,
> `shippedAt`, `deliveredAt` and `failureReason`, all nullable. Reports
> keep breaking on combinations nobody expected. What should we do?

Must contain: a choice type with one case per state; the data moved
inside the case that owns it; the observation that consumers stop
checking. Should reach `making-illegal-states-unrepresentable`.

## 2. A rule in three places

> The rule that a discount code is four to sixteen upper-case characters
> is implemented in the orders module, the billing module and the admin
> importer. They have drifted.

Must contain: one owner for the rule; a wrapper type built through a
parser; downstream code receiving an already-valid value. Should reach
`constraining-primitive-values`, possibly via `hiding-information`.

## 3. Untestable pricing

> Testing our pricing rules needs a database, a clock and a fake mail
> server. The tests take four minutes and nobody runs them.

Must contain: separating the decision from the effects; the decision
becoming a pure function of values; capabilities passed as parameters;
tests with no infrastructure. Should reach
`separating-pure-core-from-shell`.

## 4. How much design for a script

> I need a one-off script that reads a CSV, calls an API for each row and
> writes the results. It runs once, then I delete it. How should I
> structure it?

Must contain: recognition that this needs almost none of the pack.
A correct answer does **not** propose branded types, a workflow pipeline
or an aggregate. Should reach the calibration guidance in
`functional-design`.

## 5. A charge that may have happened

> Our checkout calls the payment provider, then writes the order, then
> publishes an event. Last week a timeout meant we charged a customer and
> have no order for it.

Must contain: a client-supplied command identity; an idempotent charge
adapter; state and event written in one transaction and relayed
afterwards. Should reach `making-effects-reliable`.

## 6. A status column driving everything

> Every function in our booking module starts with a switch on
> `booking.status`. Adding a state means finding all of them.

Must contain: states as a choice type; transitions as functions taking
the specific source state; illegal transitions becoming unwriteable.
Should reach `modeling-state-machines`.

## 7. A too-eager extraction

> A reviewer says my forty-line function should be split. I tried, and
> the six helpers each need four parameters from the parent.

Must contain: the observation that this is conjoined functions and worse
than the original; the criterion that an extracted part must be
independently meaningful; leaving it long if there is no natural
boundary. Should reach `splitting-and-joining-code`.

## 8. Errors everywhere

> Our service has a try/catch in almost every function and the error
> handling is longer than the logic. Half of it just rethrows.

Must contain: an attempt to define errors away or mask them before
handling them; aggregation at the edge; `Result` for what remains.
Should reach `defining-errors-out-of-existence`, then
`handling-errors-with-results`.

## 9. A dashboard that is slow

> The appointment board reconstructs two hundred aggregates every thirty
> seconds and one bad legacy row blanks the whole screen.

Must contain: a view type for the screen; querying storage directly on
the read path; tolerating imperfect stored data rather than failing.
Should reach `crossing-io-boundaries` and its read-model example.

## 10. A legacy service

> We have a 300-line `OrderService` class doing validation, pricing,
> saving and emailing. We want to move to a functional style without
> stopping feature work.

Must contain: incremental moves rather than a rewrite; one move per
commit with tests green between; an order that starts with types and
`Result` before extracting the pure decision. Should reach
`refactoring-toward-functional-design`.

## 11. Naming failure

> I have a function that validates an order, prices it and saves it, and
> I cannot think of a name for it.

Must contain: treating the naming difficulty as a design finding, not a
naming problem; splitting along the three jobs. Should reach
`choosing-precise-names`, then `splitting-and-joining-code`.

## 12. An incident nobody could diagnose

> A booking silently failed for three hours. The logs have "error"
> forty thousand times and none of them say which booking.

Must contain: deciding the questions before the fields; events as the
source; correlation identifiers carried from the edge; not logging
inside pure functions. Should reach `designing-what-to-observe`.

## 13. Two ways to say customer

> Billing calls it a customer and means an account with tax details.
> Support calls it a customer and means a person. We have one shared
> `Customer` class with fields for both.

Must contain: two bounded contexts; a type per context holding only what
that context needs; translation at the border rather than a shared
model. Should reach `capturing-the-domain`.

## 14. A wide dependency

> Our `placeOrder` takes an `OrderRepository` with twenty-two methods and
> uses two. Every test needs a mocking framework.

Must contain: narrowing to the function types actually used; naming them
in the domain's words; the test becoming two one-line functions. Should
reach `applying-solid-functionally` or `parameterizing-dependencies`.

## 15. A schema as the domain model

> We generate our TypeScript types from the database schema and use them
> everywhere. Adding a nullable column changed forty files.

Must contain: two type families with a mapping between them; the domain
type freed from storage; the inward mapping returning a result. Should
reach `crossing-io-boundaries`.

## 16. Functions that will not chain

> `parseUser` returns a Result, and `enrichUser` takes a User and also
> returns a Result. I cannot chain them without nested ifs, and I keep
> changing my mind about which argument goes first.

Must contain: composing fallible functions with bind rather than
nesting; totality as the precondition for composition; dependencies and
configuration first, data last. Should reach `composing-functions`.

## 17. Correct but unreadable

> My module passes every test and two reviewers still said they could
> not tell what mattered in it. It exports fourteen names.

Must contain: deciding explicitly which facts a caller needs; hiding the
rest rather than merely de-emphasising it; the point that obviousness is
measured by the reader, not the author. Should reach
`deciding-what-matters`.

## 18. Three nested loops

> I have three nested loops building a map of totals per customer per
> month with four mutable variables. It works and nobody dares touch it.

Must contain: recognising the accumulator as a fold; naming the
accumulator type first; a pure combining function; preferring a named
operation such as groupBy where one exists. Should reach
`folding-over-data`.

## 19. A lost update

> Our in-memory cart service mutates the cart object. Under load, two
> adds sometimes produce one item, so we wrapped it in a lock.

Must contain: returning a new value instead of mutating; keeping the one
mutable cell in a single place; an atomic swap or compare-and-set rather
than a lock; readers needing no lock at all. Should reach
`managing-state-immutably`.

## 20. What to look for before merging

> I am about to merge a pull request that adds a new module. What should
> I actually look for, and in what order?

Must contain: an ordered pass rather than ad hoc reading; types and
signatures before names and style; ranking findings by what they cost;
proposing the smallest fix. Should reach `reviewing-functional-design`.

## 21. Three layers, one vocabulary

> Our API handler calls a service that calls a repository. All three
> have the same method names and pass the same types. Adding one field
> means editing three files.

Must contain: each layer must change the abstraction; deleting
pass-throughs; the test for whether a layer earns its place. Should
reach `separating-layers`.

## 22. About to write a strategy interface

> I need to support CSV, JSON and PDF export. I was going to define an
> ExportStrategy interface with three implementations.

Must contain: passing a function instead of defining an interface; or a
choice type if the set of formats is fixed; no class hierarchy. Should
reach `translating-gof-patterns`.

## 23. Does this need comments

> My team says my code needs more comments. I think it is
> self-documenting. Who is right?

Must contain: both are half right; a comment must carry what the code
cannot; interface comments stating what a caller must guarantee; the
suggestion to write them before the implementation. Should reach
`writing-useful-comments`.

## 24. Interchangeable ids in TypeScript

> In TypeScript, how do I stop OrderId and CustomerId being swapped by
> accident, and how do I make sure a switch handles every case?

Must contain: branded types with a parser as the only constructor;
discriminated unions; exhaustiveness through `never`; strict compiler
settings. Should reach `functional-typescript`.

## 25. Effect services and layers

> We use the Effect library. Where do I declare a dependency and where
> do I provide it? Should my pure pricing function return an Effect?

Must contain: the service declared by the domain, provided by a layer at
the composition root; pure functions staying plain rather than being
wrapped; running the effect only at the edge. Should reach
`functional-typescript-effect`.

## 26. otherwise at the end of a match

> We use ts-pattern. My match ends with `.otherwise()` and a colleague
> said that is wrong. Is it?

Must contain: `.exhaustive()` instead, because the compile error is the
thing of value; the narrow cases where `.otherwise()` is legitimate.
Should reach `functional-typescript-ts-pattern`.

## 27. Unions without a type checker

> Plain JavaScript, no TypeScript and no plans for it. How do I do a
> union type and be sure I handled every case?

Must contain: one tag key used consistently; construction only through
constructor functions; a dispatch whose default throws; a test driven by
the list of tags. Should reach `functional-javascript`.

## 28. Three useState and a flicker

> My component has isLoading, error and data as three useState, plus a
> useEffect that sets data from a fetch. The screen flickers.

Must contain: one state union instead of three booleans; not deriving
state inside an effect; moving the fetch to the edge. Should reach
`functional-react-nextjs`.

## 29. Ecto schemas as the domain

> In Elixir, our Ecto schemas are the domain model everywhere, and each
> context reaches into other contexts' schemas.

Must contain: schemas as boundary artefacts mapped into structs with
enforced keys; contexts as bounded contexts that do not alias each
other's schemas; translation at the edge. Should reach
`functional-elixir-phoenix`.
