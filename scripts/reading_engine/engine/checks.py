"""
Checks on the reading sources, language-neutral.

A glossary headword that never matches its own passage is defined and then
never shown to the reader, which is the one content bug in this subsystem that
produces no build error at all -- so it is checked rather than hoped for.
"""
import re

from .match import surface_patterns
from .page import is_heading


def unmatched_vocabulary(d, lang):
    """Headwords that do not occur in their own passage."""
    bad = []
    prose = [p for p in d["passage"] if not is_heading(p)]
    for v in (d.get("vocabulary") or []):
        if v.get("match"):
            pats = [r"(?<![\w-])(" + re.escape(v["match"]).replace(r"\ ", r"\s+") + r")(?![\w-])"]
        else:
            pats = surface_patterns(v["term"], lang)
        if not any(re.search(p, para, re.I) for para in prose for p in pats):
            bad.append(v["term"])
    return bad


REQUIRED = ("id", "level", "slug", "title", "subtitle", "passage")
VALID_PROVENANCE = ("as-published", "edited", "rewritten", "merged", "new")

# Guidance, not a rule: a text with a genuinely technical subject earns more,
# and no text should be padded to reach a number.
VOCAB_RANGE = {"pre-a1": (4, 8), "a1": (5, 8), "a2": (6, 10), "b1": (8, 12),
               "b2": (10, 15), "c1": (10, 16), "c2": (10, 18)}


def check_one(site, level, slug, d, warnings=False):
    """(errors, warnings) for one source file."""
    errs, warns = [], []
    for k in REQUIRED:
        if not d.get(k):
            errs.append(f"missing required field {k!r}")
    if d.get("level", "").lower() != level.lower():
        errs.append(f'level {d.get("level")!r} does not match folder {level!r}')
    if d.get("slug") != slug:
        errs.append(f'slug {d.get("slug")!r} does not match filename {slug!r}')
    if d.get("provenance") and d["provenance"] not in VALID_PROVENANCE:
        errs.append(f'provenance {d["provenance"]!r} not one of {VALID_PROVENANCE}')
    if d.get("topic") and d["topic"] not in site.cfg["TOPIC_LABELS"]:
        errs.append(f'topic {d["topic"]!r} is not a key of TOPIC_LABELS in '
                    f'reading/strings/{site.lang}.json')

    lang = site.cfg.morphology
    for term in unmatched_vocabulary(d, lang):
        errs.append(f'glossary term {term!r} never matches its own passage, so '
                    f'it is defined and never highlighted (pin it with "match")')

    for img in (d.get("images") or []):
        if not img.get("alt"):
            errs.append(f'image {img.get("src")!r} has no alt text')
        # An analogue is a good illustration and a bad photograph, and the
        # caption is what decides which the reader takes it for.
        rel = img.get("relation") or ("depicts" if str(img.get("source", "")).startswith("commons:")
                                      else "analogue")
        if rel == "analogue" and warnings:
            cap = img.get("caption") or ""
            # A caption that is only "*Title* -- Artist, year." tells a reader
            # they are looking at the thing itself.
            if cap.count(".") < 2:
                warns.append(f'image {img.get("src")!r} is an analogue but its '
                             f'caption does not say what it is doing there')
        if img.get("licence") and not img.get("author"):
            errs.append(f'image {img.get("src")!r} is under {img["licence"]} '
                        f'but records no author to credit')

    if warnings:
        n = len(d.get("vocabulary") or [])
        lo, hi = VOCAB_RANGE.get(level, (0, 99))
        if n and not (lo <= n <= hi):
            warns.append(f"{n} glossary entries; {level} guidance is {lo}-{hi}")
        if not d.get("exercises"):
            warns.append("no exercises")
        if not d.get("discussion"):
            warns.append("no discussion prompts")
    return errs, warns
