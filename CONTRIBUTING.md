# Contributing

This file is for changing the pack. For installing and using it, see
[README.md](README.md).

## Constraints this pack honours

- Frontmatter carries only `name` and `description`, the two fields both
  runtimes require. No runtime-specific keys.
- Every `description` is at most 160 characters and states triggers only,
  never a summary of the skill's steps.
- No instruction names a runtime-specific tool, so the same file works in
  either agent.
- Every markdown file passes `markdownlint` under its default rules, with
  no configuration file, no inline directives, and no custom rules.
- Cross-references between skills are sibling-relative
  (`../other-skill/SKILL.md`), which resolves correctly under both
  `.claude/skills/` and `.agents/skills/`.

The first three are what make a copy into a target project a copy rather
than a port. The fourth is what lets a project run one markdown policy
over its own files and the pack together.

## Verifying a change

```sh
npx prettier --write '**/*.md'          # do this first; it fixes most of it
./scripts/verify.sh                     # all six checks
python3 scripts/eval-routing.py         # routing coverage only
python3 scripts/eval-routing.py --report  # rank for every case
python3 scripts/eval-routing.py --noise   # whose territory a description overlaps
```

`verify.sh` runs six checks and fails on any of them: markdownlint under
default rules with no config file and no inline directives; frontmatter
carrying exactly `name` and `description`; the Codex list budget;
relative link resolution; description hygiene, meaning length, opening
and a kebab-case name matching the folder; and routing keyword coverage.
It needs network access on first run to fetch `markdownlint-cli`, which
is pinned so a new default rule cannot break the build unannounced.

markdownlint's default rule set grows between releases. MD060, aligned
table pipes, arrived in 0.49 and would have failed every table in the
pack on an unpinned run. Bump the pin deliberately, then re-run and fix.

## Adding a skill

1. Write `SKILL.md` with a `description` that states triggers only, in
   the vocabulary someone would use for the problem, not the solution.
2. Add routing cases for it in
   [evals/routing-cases.md](evals/routing-cases.md), in the wording
   someone actually said.
3. Run the scorer. `--noise` is worth a look at this point: it shows
   which existing descriptions the new one overlaps.
4. Add a scenario to [evals/scenarios.md](evals/scenarios.md) if the
   skill has a direction that could invert — a rule that could become an
   escape hatch needs a case that must refuse it, not only one that must
   apply it.

## Changing a rule

Before adding a check or tightening a rule, give the pack the defect the
change is meant to catch and confirm it fires. A rule written from
reasoning alone has an even chance of being the wrong shape, and the
routing noise measure is the standing example: it looked like a real
finding and was measuring alphabetical order.

The same applies to guidance form. Over-application is not a discipline
failure, so a prohibition does not fix it. State the rule as a positive
conditional keyed to something observable, and put the exception in its
own conditional rather than appending a clause to the rule.

See [evals/README.md](evals/README.md) for what the routing check does
and does not prove, and why one of its two measures deliberately does
not gate. See [AUDIT.md](AUDIT.md) for the record of what each round
changed and what it did not establish.
