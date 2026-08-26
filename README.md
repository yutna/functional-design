# Functional Design Skills

A portable pack of agent skills that distils three books into executable
design rules for codebases written in a functional style:

- **Functional Design: Principles, Patterns, and Practices** —
  Robert C. Martin
- **Domain Modeling Made Functional** — Scott Wlaschin
- **A Philosophy of Software Design, 2nd edition** — John Ousterhout

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

Copy the 33 core skills plus the language packs that match the stack.
Codex truncates its skill list at roughly 8,000 characters, so unused
packs cost real discovery budget. All 39 skills together come to about
6,700 characters, so a project with skills of its own should copy only
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
./scripts/verify.sh                    # everything
python3 scripts/eval-routing.py        # routing coverage only
```

`verify.sh` checks markdownlint compliance, frontmatter shape, the Codex
list budget, relative link resolution, description hygiene, and whether
each skill's description contains the words people use for the problem
it solves. It needs network access on first run to fetch
`markdownlint-cli`.

See [evals/README.md](evals/README.md) for what the routing check does
and does not prove, and for the scenarios to run against a real agent.

## Attribution

The rules here are restatements and syntheses of ideas from the three
books above, credited at chapter level inside each skill. No book text is
reproduced. Read the originals: the skills are a working checklist, not a
substitute.

See [AUDIT.md](AUDIT.md) for the coverage matrix against all three books.
