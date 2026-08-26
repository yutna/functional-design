#!/usr/bin/env python3
"""Routing keyword coverage for the functional-design skills pack.

Scores each symptom in evals/routing-cases.md against every skill's
discovery text -- the `name` and `description` an agent sees before it
opens anything -- and reports where the expected skill ranked.

Coverage is the gate. It catches false negatives: a skill that should
have answered a symptom and did not reach the top ranks, which means its
description is missing words people actually use.

Noise is reported but does NOT gate. It counts how often a skill reaches
the top ranks for symptoms it does not own. That was built as a
false-positive gate and then measured: giving a skill a deliberately
vague description raises its noise by almost nothing and instead makes it
fail coverage, because inverse document frequency already gives common
words almost no weight. There is no second hole to plug, so the number
ships as a diagnostic for whoever adds the next skill, not as a check
that can fail. See evals/README.md.

Both are keyword lints for descriptions, not oracles for routing. A clean
run does not prove an agent routes correctly.

Usage:
  scripts/eval-routing.py            summary, plus every miss
  scripts/eval-routing.py --report   full ranking for every case
  scripts/eval-routing.py --noise    per-skill noise, worst first
  scripts/eval-routing.py --profile full   also score the When-to-use text
"""

import math
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
CASES = os.path.join(ROOT, "evals", "routing-cases.md")
TOP_N = 3

STOP = set(
    """a an the or of to in for is are be been being that this it its and with on
    at by from as into not no nor but if then than so such use used using when
    where while what which who whom how why can could should would may might will
    shall do does did done have has had i we you they them their our your my me
    all any each every some most more less other another same only just also very
    there here about after before between during over under again once
    """.split()
)


def stem(word):
    """Strip the few suffixes that would otherwise split one concept in
    two: skill/skills, document/documentation, mutate/mutating/mutated."""
    for suffix in ("ations", "ation", "ingly", "ing", "ies", "ers", "er",
                   "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            base = word[: -len(suffix)]
            if suffix == "ies":
                base += "y"
            return base
    return word


def terms(text):
    return [stem(w) for w in re.findall(r"[a-z]+", text.lower())
            if len(w) > 2 and w not in STOP]


def load_skills(profile):
    skills = {}
    for name in sorted(os.listdir(SKILLS)):
        path = os.path.join(SKILLS, name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        text = open(path, encoding="utf-8").read()
        front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not front:
            continue
        desc = re.search(r"^description:\s*(.+)$", front.group(1), re.M)
        desc = desc.group(1).strip() if desc else ""
        # what an agent sees before opening the file
        words = terms(name.replace("-", " ")) * 2 + terms(desc)
        if profile == "full":
            section = re.search(r"## When to use\n(.*?)\n## ", text, re.S)
            if section:
                words += terms(section.group(1))
        skills[name] = Counter(words)
    return skills


def load_cases():
    text = open(CASES, encoding="utf-8").read()
    block = re.search(r"```text\n(.*?)```", text, re.S)
    if not block:
        sys.exit("no ```text case block found in evals/routing-cases.md")
    cases = []
    for line in block.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if " -> " not in line:
            sys.exit("case line missing ' -> ': " + line)
        symptom, _, expected = line.rpartition(" -> ")
        cases.append((symptom.strip(), expected.strip()))
    return cases


def rank(skills, idf, symptom):
    scored = []
    for name, counts in skills.items():
        total = 0.0
        for term in terms(symptom):
            if term in counts:
                total += (1 + math.log(counts[term])) * idf.get(term, 0.0)
        scored.append((total, name))
    scored.sort(key=lambda pair: (-pair[0], pair[1]))
    return scored


def main():
    report = "--report" in sys.argv
    show_noise = "--noise" in sys.argv
    profile = "full" if "--profile" in sys.argv and "full" in sys.argv else "desc"

    skills = load_skills(profile)
    cases = load_cases()

    doc_freq = Counter()
    for counts in skills.values():
        for term in counts:
            doc_freq[term] += 1
    n = len(skills)
    idf = {t: math.log(n / df) for t, df in doc_freq.items()}

    unknown = [e for _, e in cases if e not in skills]
    if unknown:
        sys.exit("unknown skill named in cases: " + ", ".join(sorted(set(unknown))))

    top1 = 0
    misses = []
    noise = Counter()
    owned = Counter()
    zero_scoring = []
    for symptom, expected in cases:
        scored = rank(skills, idf, symptom)
        names = [name for _, name in scored]
        pos = names.index(expected) + 1
        if pos == 1:
            top1 += 1
        if pos > TOP_N:
            misses.append((symptom, expected, pos, names[:TOP_N]))
        owned[expected] += 1
        zero_scoring.append(sum(1 for score, _ in scored if score == 0.0))
        # A skill that shares no term with the symptom scores zero. Most
        # skills do, for most symptoms, and rank breaks those ties by
        # name -- so counting them would rank noise alphabetically rather
        # than by description quality. Only a skill that actually matched
        # some of the symptom's words can mislead by keyword.
        for score, name in scored[:TOP_N]:
            if name != expected and score > 0.0:
                noise[name] += 1
        if report:
            mark = "ok  " if pos == 1 else f"#{pos:<3}"
            print(f"{mark} {expected:38} {symptom[:52]}")

    total = len(cases)
    passed = total - len(misses)
    print(f"\nrouting: {passed}/{total} cases place the expected skill in "
          f"the top {TOP_N}  (top-1: {top1}/{total})")

    if noise:
        loudest, count = noise.most_common(1)[0]
        print(f"noise:   {loudest} is in the top {TOP_N} for {count} cases it "
              f"does not own  (diagnostic, not a gate)")
    median_zero = sorted(zero_scoring)[len(zero_scoring) // 2]
    print(f"ties:    a median of {median_zero} of {len(skills)} skills score "
          f"zero per case, so places below the first are often alphabetical")

    if show_noise:
        print(f"\n{'skill':38s} {'noise':>5s} {'owns':>5s}")
        for name, count in noise.most_common():
            print(f"{name:38s} {count:5d} {owned[name]:5d}")

    if misses:
        print("\nDescriptions missing the words these symptoms use:")
        for symptom, expected, pos, beaten_by in misses:
            print(f"  {expected} ranked #{pos}")
            print(f"    symptom: {symptom}")
            print(f"    outranked by: {', '.join(beaten_by)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
