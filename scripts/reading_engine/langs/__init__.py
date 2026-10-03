"""
Per-language plugins for the shared reading-library engine.

Everything in the reading library that cannot be the same in two languages
lives in exactly one of two places, and nowhere else:

  * reading/strings/<lang>.json  -- what a student reads (section headings,
    button labels, topic chips, the brand line in the print footer).
  * reading/langs/<lang>.py      -- how the language WORKS: the narration
    voices, the reading pace, and above all the morphology that lets a
    glossary headword written in dictionary form find its own inflected
    form in a passage.

The second is the one that cannot be solved with a translation table. A
glossary says "to grind" and the passage says "grinding"; a French glossary
says "se lever" and the passage says "je me leve"; a Latin glossary says
"amare" and the passage says "amaverunt". Each language needs its own rules,
so each gets a module exposing one function:

    surface_forms(head) -> set[str]

given the FIRST word of a headword (already stripped of its article or
infinitive marker by the shared code), return every surface form it might
appear as. Over-generating is free: a form that occurs in no text simply
never matches. Under-generating is what leaves a word defined in the
glossary and never highlighted in the passage that defines it, which is
what check_content.py reports.

A module may also export:

    ARTICLE_RE   -- the leading articles/infinitive markers to strip
                    ("to|a|an|the" in English, "le|la|les|un|une|se|s'" in French)
    IRREGULAR    -- dict of head -> [forms], merged into surface_forms()
    PLURALISES_LAST_WORD -- True where a noun phrase pluralises its final
                    word ("a fitting room" -> "fitting rooms"). False for
                    Romance languages, where the HEAD noun carries number
                    and the modifier agrees with it.
"""
from importlib import import_module

_CACHE = {}


def get(lang):
    """The plugin module for a language code, e.g. "fr"."""
    if lang not in _CACHE:
        _CACHE[lang] = import_module(f"{__name__}.{lang}")
    return _CACHE[lang]


def available():
    from pathlib import Path
    return sorted(p.stem for p in Path(__file__).parent.glob("*.py")
                  if p.stem != "__init__")
