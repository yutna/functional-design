# Evals

Two checks on whether the pack routes a problem to the right skill. They
prove different things, and neither proves what the other does.

## 1. Routing keyword coverage — automated

```sh
python3 scripts/eval-routing.py            # summary, plus any miss
python3 scripts/eval-routing.py --report   # rank for every case
```

Scores each symptom in [routing-cases.md](routing-cases.md) against the
`name` and `description` of every skill — the text an agent sees before
it opens anything — and reports where the expected skill ranked. It runs
in `scripts/verify.sh` and fails the build if any expected skill falls
outside the top three.

**What it proves:** every skill's description contains enough of the
words people actually use for that problem to be a plausible candidate.

**What it does not prove:** that an agent routes correctly. It is a bag
of words with no idea what any of them mean. A description could pass by
containing the right nouns while describing the wrong thing.

Treat a failure as a defect in the description, not in the case. If a
symptom is phrased the way a developer would phrase it and the skill does
not surface, the skill is missing a trigger word.

Two flags worth knowing:

- `--profile full` also scores each skill's "When to use" section. It
  scores _better_ on exact matches and slightly worse on top-three
  coverage, because the extra text adds noise as well as signal. The
  gate uses descriptions only, because that is what discovery sees.
- The scorer stems a few suffixes so `skill` and `skills` are one term.
  Irregular forms such as `broke` and `break` are still two, so phrase
  cases in the present tense where it does not distort them.

## 2. Scenarios — manual, against a real agent

[scenarios.md](scenarios.md) holds fifteen fuller problems, each a
paragraph of realistic context with the response a correct answer must
contain. Run them by hand in an agent session with the pack installed:

1. Install the pack into a scratch project, per the main README.
2. Start a session there and paste one scenario as the whole prompt.
3. Record which skill the agent loaded first and whether the response
   contains the required elements.
4. Note anything the agent did instead, which is usually more
   informative than a pass.

**What it proves:** the pack works end to end for that scenario, with
that agent, on that day.

**What it does not prove:** anything stable. Results move with the model
and with the rest of the session's context, so this is a spot check, not
a regression test. Do not record a score from it as though it were one.

## Adding cases

Add a routing case whenever you catch yourself describing a problem in
words the pack does not contain. Add a scenario when a real task needed
more than one skill and the order mattered.

Keep case wording as it was actually said. A case rewritten until it
passes tests nothing.
