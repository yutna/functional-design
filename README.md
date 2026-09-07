# Functional Design Skills

A portable pack of agent skills carrying executable design rules for
codebases written in a functional style. It covers:

- Diagnosing complexity, and telling what a design costs from what it
  looks like
- Modelling a domain in types so illegal values cannot be built
- Composing workflows out of total functions, with errors as values
- Module boundaries, information hiding, and interface depth
- Immutability, state, effects at the edges, and reliability across a
  process boundary
- Refactoring imperative or object-oriented code toward all of the above

The skills are language-agnostic. Core skills describe designs in a
neutral notation; separate language packs translate them into JavaScript,
TypeScript, React and Next.js, and Elixir and Phoenix.

## What it changes

The smallest example of the whole method. A type that permits states the
business forbids:

```text
type Shipment = {
  status: String,
  trackingNumber: Option<String>,
  shippedAt: Option<Date>,
  deliveredAt: Option<Date>,
  failureReason: Option<String>,
}
```

Five fields, four of them optional, so the type admits sixteen
combinations of presence for any status. Reports break on the ones nobody
meant. After:

```text
type Shipment =
  | Pending
  | Shipped of { trackingNumber: TrackingNumber, shippedAt: Date }
  | Delivered of { trackingNumber: TrackingNumber, deliveredAt: Date }
  | Failed of { reason: FailureReason }
```

Each case carries exactly the data that case has, so there is nothing to
check for absence. The gain is not tidiness: every consumer that used to
branch on a status string and then test a field for `null` now handles
four cases and cannot forget one.

## What it costs

A skill's `description` is always in the agent's list; its body is read
only when the skill is selected. So the standing cost is the descriptions
and nothing else.

| Installed               | Descriptions |
| ----------------------- | ------------ |
| 34 core only            | 5,883 chars  |
| core plus TypeScript    | 6,057 chars  |
| core, TypeScript, React | 6,241 chars  |
| all 40                  | 6,951 chars  |

Codex truncates its skill list at roughly 8,000 characters, silently. All
40 therefore fit only if the project's own skills total under about 1,050
characters, which is around ten skills. A project with more of its own
needs to copy only the packs it uses.

When a skill is selected, its `SKILL.md` averages 6,886 bytes, roughly
1,700 tokens. `functional-design/SKILL.md` is the largest at 10,690
bytes, which is why nothing below tells the agent to open it every
session. The 90 reference files average 4,548 bytes and load only when a
skill links into one.

## Pick only what the project needs

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
`functional-`, plus `functional-design` itself, which is the index. That
is 34 of the 40.

## Install

Every skill is a directory holding `SKILL.md` plus optional `references/`.
Both Claude Code and Codex read that layout, from different paths.

```sh
# Claude Code, project scope, a TypeScript project
DEST=/path/to/project/.claude/skills
mkdir -p "$DEST"
find skills -mindepth 1 -maxdepth 1 -type d \
  ! -name 'functional-*' -exec cp -R {} "$DEST" \;
cp -R skills/functional-design \
      skills/functional-typescript "$DEST"
```

For Codex, the only change is `DEST=/path/to/project/.agents/skills`. For
user scope instead of project scope, use `~/.claude/skills` or
`~/.agents/skills`.

A pack you did not copy leaves a few links pointing nowhere: its entry in
the index's "Language packs" list, and any cross-reference to it from a
skill you did copy. Installing core plus TypeScript leaves nine such
links. That is expected and harmless -- they are reading suggestions, not
a manifest.

## Tell the agent the pack is there

Paste this into the project's `CLAUDE.md` or `AGENTS.md`, with the last
line naming whichever language pack you copied:

```markdown
## Design rules

This codebase follows functional design. The skills in
`.claude/skills/` carry the rules, and `functional-design` is the index.

- This project's own conventions win. The pack decides what they leave
  open, and a pack red flag is a place to look, not a finding.
- Before designing a new module, workflow, endpoint, or bounded
  context, read `functional-design` and follow its design loop.
- For anything smaller, use its calibration table to decide how much
  design the task warrants. For one function in a module that already
  exists, that is an honest signature and a precise name, nothing more.
- Before finishing a change that added or reshaped a type, a signature,
  or a module boundary, run the checklist in
  `reviewing-functional-design`.
- Use `functional-typescript` for concrete syntax.
```

The first line matters more than it looks. A project that installs the
pack without it has told the agent nothing about what outranks what, and
the agent will read a deliberate convention as a defect.

## Check it took

Start a session in the target project and ask one question whose right
answer names a skill:

> we have four nullable fields that only make sense in some combinations

Expect the agent to reach `making-illegal-states-unrepresentable`. If it
answers from general knowledge without naming a skill, the files are in
the wrong directory for that runtime.

## If it over-engineers

The symptom is a wrapper type on a throwaway script, a new error union
for a one-line change, or a review finding against something the team
decided on purpose. The cause is the agent applying a heavier rule than
the task warrants. Three things fix it, in order of how much they buy:

1. **Say what outranks what**, as in the snippet above. Most
   over-application is an agent with no stated precedence treating every
   rule as binding.
2. **Name the calibration row out loud** in the session: "this is one
   function in a module that already exists". The row is the pack's own
   answer and the agent will take it.
3. **Scope the rules to the code they apply to.** In Claude Code, a rule
   file under `.claude/rules/` takes a `paths:` key in its frontmatter,
   so a codebase that is only partly functional can point these rules at
   the part that is. The Codex equivalent has not been verified here.

## Updating

Record what you copied, so the next person can tell. A file beside the
skills, or a section in the project's own docs, holding:

```text
Upstream   https://github.com/yutna/functional-design
Version    v1.0.0
Commit     <sha>
Copied     <date>
Licence    MIT
```

Re-run the install block to update. Two things to know:

- **`cp -R` does not delete.** A skill removed upstream survives in the
  target project until someone removes it by hand. Check `git status`
  for directories the copy did not touch.
- **Copying overwrites local edits.** Do not edit the skills in place.
  Project-specific decisions belong outside the pack, in the project's
  own rule files, which is also what keeps an update a copy rather than a
  merge. To confirm a copy is still unmodified:
  `diff -rq skills/<name> /path/to/project/.claude/skills/<name>`.

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

## Further reading

- [skills/functional-design/SKILL.md](skills/functional-design/SKILL.md)
  is the index: the calibration table, the symptom-to-skill routing, and
  the notation the core skills use.
- [CONTRIBUTING.md](CONTRIBUTING.md) is how to change the pack, and the
  constraints a change has to keep.
- [evals/README.md](evals/README.md) is what the routing check does and
  does not prove, and the scenarios to run against a real agent.
- [AUDIT.md](AUDIT.md) is what the pack covers, how it was verified, and
  what it does not establish.

## Licence

MIT, in [LICENSE](LICENSE). Copy `skills/` into any project, including
commercial work; keep the copyright notice.

The licence covers the wording in this repository and nothing else. The
design principles it states are long-established and belong to nobody
here.
