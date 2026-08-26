# Functional Design Skills

A portable pack of agent skills that distils three books into executable
design rules for codebases written in a functional style:

- **Functional Design: Principles, Patterns, and Practices** —
  Robert C. Martin
- **Domain Modeling Made Functional** — Scott Wlaschin
- **A Philosophy of Software Design, 2nd edition** — John Ousterhout

Three further works fill gaps those three leave, each labelled where it
appears rather than folded in silently:

- **Refactoring, 2nd edition** — Martin Fowler, for the smell catalogue
  and the tactical moves
- **Out of the Tar Pit** — Ben Moseley and Peter Marks, for essential
  versus accidental complexity
- **Data-Oriented Programming** — Yehonathan Sharvit, for the data-first
  school this pack otherwise argues against

The skills are language-agnostic. Core skills describe designs in a
neutral notation; separate language packs translate them into JavaScript,
TypeScript, React and Next.js, and Elixir and Phoenix.

## Install

Every skill is a directory holding `SKILL.md` plus optional `references/`.
Both Claude Code and Codex read that layout, from different paths.

```sh
# Claude Code (project scope)
mkdir -p /path/to/project/.claude/skills
cp -R skills/* /path/to/project/.claude/skills/

# Codex (repository scope)
mkdir -p /path/to/project/.agents/skills
cp -R skills/* /path/to/project/.agents/skills/
```

For user scope instead of project scope, copy into `~/.claude/skills/` or
`~/.agents/skills/`.

## Pick only what the project needs

Copy the 34 core skills plus the language packs that match the stack.
Codex truncates its skill list at roughly 8,000 characters, so unused
packs cost real discovery budget. All 40 skills together come to about
7,000 characters, so a project with skills of its own should copy only
the packs it uses.

| Stack            | Language pack to copy              |
| ---------------- | ---------------------------------- |
| JavaScript       | `functional-javascript`            |
| TypeScript       | `functional-typescript`            |
| Effect           | `functional-typescript-effect`     |
| ts-pattern       | `functional-typescript-ts-pattern` |
| React or Next.js | `functional-react-nextjs`          |
| Elixir, Phoenix  | `functional-elixir-phoenix`        |

Copy the core skills in every case. A React or Next.js project wants the
TypeScript pack alongside the React pack.

Core is every directory under `skills/` whose name does not start with
`functional-` — plus `functional-design` itself, which is the index.

## Tell the agent the pack is there

Paste this into the project's `CLAUDE.md` or `AGENTS.md`:

```markdown
## Design rules

This codebase follows functional design. Start with the
`functional-design` skill: its calibration table says how much design a
task warrants, which for a small change is often almost none. Follow the
full design loop only for a new module, workflow, or bounded context.
Before finishing a change of any size, run the checklist in
`reviewing-functional-design`. Use the language pack that matches this
project for concrete syntax.
```

## Start here

Read [skills/functional-design/SKILL.md](skills/functional-design/SKILL.md)
first. It carries the calibration table — how much of this pack a given
task actually warrants — the symptom-to-skill routing, and the notation
the core skills use.

## Layout

```text
skills/                     copied into the target project
  functional-design/        index: design loop, calibration, routing
  <core skills>/            one design rule each
  functional-<stack>/       language packs
    SKILL.md                the rule, short enough to always read
    references/*.md         depth, loaded only when needed

evals/                      stays here; not copied
scripts/                    stays here; not copied
```

Only `skills/` is installed. `evals/` and `scripts/` maintain the pack
and have no meaning inside a target project.

Cross-references between skills are sibling-relative
(`../other-skill/SKILL.md`), which resolves correctly under both
`.claude/skills/` and `.agents/skills/`.

## Constraints this pack honours

- Frontmatter carries only `name` and `description`, the two fields both
  runtimes require. No runtime-specific keys.
- Every `description` is at most 160 characters and states triggers only,
  never a summary of the skill's steps.
- No instruction names a runtime-specific tool, so the same file works in
  either agent.
- Every markdown file passes `markdownlint` under its default rules, with
  no configuration file, no inline directives, and no custom rules.

## Maintenance

```sh
./scripts/verify.sh                     # all six checks
python3 scripts/eval-routing.py         # routing coverage only
python3 scripts/eval-routing.py --report  # rank for every case
python3 scripts/eval-routing.py --noise   # whose territory each description overlaps
```

`verify.sh` runs six checks and fails on any of them: markdownlint under
default rules with no config file and no inline directives; frontmatter
carrying exactly `name` and `description`; the Codex list budget;
relative link resolution; description hygiene, meaning length, opening
and a kebab-case name matching the folder; and routing keyword coverage.
It needs network access on first run to fetch `markdownlint-cli`, which
is pinned so a new default rule cannot break the build unannounced.

Adding a skill means adding routing cases for it in
[evals/routing-cases.md](evals/routing-cases.md), then running the
scorer. `--noise` is worth a look at that point: it shows which existing
descriptions the new one overlaps.

See [evals/README.md](evals/README.md) for what the routing check does
and does not prove, why one of its two measures deliberately does not
gate, and the scenarios to run against a real agent.

## Attribution

The rules here are restatements and syntheses of ideas from the works
above, credited at chapter level inside each skill. Material from the
three supporting sources says so where it appears, and never claims
chapter provenance in the primary three. No book text is reproduced. Read
the originals: the skills are a working checklist, not a substitute.

See [AUDIT.md](AUDIT.md) for the coverage matrix against all three books,
and for what the supporting sources contributed.

## Licence

MIT, in [LICENSE](LICENSE). Copy `skills/` into any project, including
commercial work; keep the copyright notice.

The licence covers the wording in this repository and nothing else. The
ideas belong to the authors of the books, who are credited per chapter
inside each skill, and nothing here licenses their text.
