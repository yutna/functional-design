#!/usr/bin/env bash
# Verify the functional-design skills pack.
#   1. markdownlint with default rules only
#   2. frontmatter shape
#   3. Codex skill-list character budget
#   4. relative link resolution
#   5. description hygiene
# Usage: ./scripts/verify.sh
set -uo pipefail

cd "$(dirname "$0")/.." || exit 1
FAIL=0
note() { printf '%s\n' "$*"; }
fail() { printf 'FAIL  %s\n' "$*"; FAIL=1; }
pass() { printf 'ok    %s\n' "$*"; }

note '== 1. markdownlint (default rules) =='
if find . -name '.markdownlint*' -not -path './node_modules/*' \
    | grep -q .; then
  fail 'a markdownlint config file exists (overrides are forbidden)'
else
  pass 'no markdownlint config file'
fi

if grep -rIl 'markdownlint-disable\|markdownlint-configure' \
    --include='*.md' . >/dev/null 2>&1; then
  fail 'inline markdownlint directives found'
else
  pass 'no inline markdownlint directives'
fi

LINT=$(npx --yes markdownlint-cli@latest \
  README.md AUDIT.md 'evals/*.md' 'skills/**/*.md' 2>&1)
if [ -n "$LINT" ]; then
  fail 'markdownlint reported problems:'
  printf '%s\n' "$LINT"
else
  pass 'markdownlint clean'
fi

note ''
note '== 2-5. frontmatter, budget, links, hygiene =='
python3 - <<'PY' || FAIL=1
import os, re, sys

root = 'skills'
ok = True
def bad(msg):
    global ok
    print('FAIL  ' + msg)
    ok = False

total = 0
count = 0
targets = []

for name in sorted(os.listdir(root)):
    d = os.path.join(root, name)
    if not os.path.isdir(d):
        continue
    p = os.path.join(d, 'SKILL.md')
    if not os.path.isfile(p):
        bad('%s: missing SKILL.md' % name)
        continue
    text = open(p, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        bad('%s: no YAML frontmatter' % name)
        continue
    block = m.group(1)
    if len(block) > 1024:
        bad('%s: frontmatter %d chars > 1024' % (name, len(block)))
    keys = re.findall(r'^([A-Za-z-]+):', block, re.M)
    if keys != ['name', 'description']:
        bad('%s: keys are %s, want [name, description]' % (name, keys))
        continue
    fname = re.search(r'^name:\s*(.+)$', block, re.M).group(1).strip()
    desc = re.search(r'^description:\s*(.+)$', block, re.M).group(1).strip()
    if fname != name:
        bad('%s: name field is "%s"' % (name, fname))
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', fname):
        bad('%s: name is not kebab-case' % name)
    if len(desc) > 160:
        bad('%s: description %d chars > 160' % (name, len(desc)))
    if not desc.startswith('Use when'):
        bad('%s: description must start with "Use when"' % name)
    total += len(fname) + len(desc) + 3
    count += 1

print('ok    %d skills, Codex list budget %d chars (limit 7200)'
      % (count, total))
if total > 7200:
    bad('Codex list budget exceeded')

link = re.compile(r'\[[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)')
for dirpath, _dirs, files in os.walk(root):
    for f in files:
        if not f.endswith('.md'):
            continue
        p = os.path.join(dirpath, f)
        for href in link.findall(open(p, encoding='utf-8').read()):
            if href.startswith(('http://', 'https://', 'mailto:')):
                continue
            t = os.path.normpath(os.path.join(dirpath, href))
            if not os.path.exists(t):
                bad('%s: broken link -> %s' % (p, href))

if ok:
    print('ok    frontmatter, budget, links, hygiene')
sys.exit(0 if ok else 1)
PY

note ''
note '== 6. routing keyword coverage =='
if ROUTING=$(python3 scripts/eval-routing.py 2>&1); then
  printf 'ok    %s\n' "$(printf '%s' "$ROUTING" | grep '^routing:')"
else
  fail 'routing keyword coverage:'
  printf '%s\n' "$ROUTING"
fi

note ''
if [ "$FAIL" -eq 0 ]; then
  note 'ALL CHECKS PASSED'
else
  note 'VERIFICATION FAILED'
fi
exit "$FAIL"
