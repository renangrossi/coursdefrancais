"""
Finding a glossary headword inside a passage -- the language-neutral half.

A vocabulary list is written in dictionary form ("to grind", "se lever",
"un journal") and the passage contains the inflected, article-less, separated
thing ("grinding", "je me leve", "les journaux"). The shape of that problem is
the same in every language; the inflections are not. So everything structural
is here, and every fact about a particular language comes from its plugin in
reading/langs/ (see that package's docstring).

A plugin must export surface_forms(head); it may also export ARTICLE_RE,
IRREGULAR, PLURALISES_LAST_WORD, CHAR_CLASSES and tail_forms().
"""
import re

# Placeholders in a dictionary headword that stand for whatever the real
# object is: "cheer someone up" -> "cheer you up", "aider quelqu'un a" ->
# "aider sa soeur a". A literal search can never find these.
PLACEHOLDERS = {
    "something", "someone", "somebody", "sth", "sb",            # en
    "quelquun", "quelque", "quelqu'un", "qqn", "qqch", "quelquechose",  # fr
    "algo", "alguien", "alguno",                                 # es
    "qualcosa", "qualcuno",                                      # it
    "alguem",                                                    # pt
    "aliquid", "aliquem",                                        # la
}


def _folded(form, char_classes):
    """A regex matching `form` with any accented variant of its letters.

    Expanding each letter into a character class keeps the match offsets in
    the ORIGINAL text, which is what lets the builder splice a highlight into
    the passage without having to map positions back from a folded copy.
    """
    if not char_classes:
        return re.escape(form).replace(r"\ ", r"\s+")
    out = []
    for ch in form:
        low = ch.lower()
        if low in char_classes:
            cls = char_classes[low]
            out.append(f"[{cls}{cls.upper()}]")
        elif ch == " ":
            out.append(r"\s+")
        else:
            out.append(re.escape(ch))
    return "".join(out)


def surface_patterns(term, lang):
    """Regexes for the ways a glossary headword can appear in running text,
    longest phrase first.

    Returned patterns each have exactly one capturing group: the text to
    highlight.
    """
    article_re = getattr(lang, "ARTICLE_RE", None)
    char_classes = getattr(lang, "CHAR_CLASSES", None)
    plural_last = getattr(lang, "PLURALISES_LAST_WORD", False)
    tail_forms = getattr(lang, "tail_forms", None)

    pats = []
    for alt in re.split(r"\s*/\s*", term):
        alt = alt.strip().strip("….?!’'\"")
        # A parenthesised aside in a headword -- "It's worth (doing)" -- is a
        # note to the author, not part of the phrase.
        alt = re.sub(r"\s*\(.*?\)\s*", " ", alt).strip()
        if article_re:
            alt = article_re.sub("", alt).strip()
        # Two letters is a real headword ("an ox", "y a"); the word boundaries
        # in the pattern are what stop it claiming the inside of a longer word.
        if len(alt) < 2:
            continue
        words = alt.split()
        head, rest = words[0], words[1:]

        forms = lang.surface_forms(head)

        # The rest of the phrase, with placeholders opened up.
        tail = []
        for w in rest:
            if w.lower().strip(".,").replace("’", "'") in PLACEHOLDERS:
                tail.append(r"\s+\S+")          # whatever the real object is
            elif tail_forms:
                # A modifier that agrees with its head (French, Spanish,
                # Italian, Portuguese, Latin): match any of its agreement
                # forms rather than the dictionary spelling alone.
                alts = sorted(tail_forms(w), key=lambda s: (-len(s), s))
                inner = "|".join(_folded(a, char_classes) for a in alts)
                tail.append(r"\s+(?:" + inner + r")")
            else:
                tail.append(r"\s+" + _folded(w, char_classes))
        tail_re = "".join(tail)

        # Longest first so "checked in" wins over "check", then alphabetically:
        # forms is a set, and sorting on length alone leaves equal-length forms
        # in hash order, which changes per process. The first pattern that
        # matches is the one that claims the word, so that made the build
        # non-reproducible -- rebuilding a page moved highlights between
        # occurrences with no source change.
        for f in sorted(forms, key=lambda w: (-len(w), w)):
            pats.append((len(alt),
                         r"(?<![\w-])(" + _folded(f, char_classes) + tail_re + r")(?![\w-])"))

        # A phrase whose meaning sits in its tail, where the head is a copula
        # contracted onto the subject ("we're out of...", "c'est a dire") and a
        # leading word boundary can never match. Match the tail alone.
        if head.lower() in ("be", "etre", "ser", "estar", "essere", "esse") and rest:
            core = []
            for w in rest:
                if w.lower().strip(".,") in PLACEHOLDERS:
                    break
                core.append(_folded(w, char_classes))
            if core:
                pats.append((len(alt),
                             r"(?<![\w-])(" + r"\s+".join(core) + r")(?![\w-])"))

        # In an English noun phrase it is the LAST word that pluralises, not
        # the first: "a fitting room" appears as "fitting rooms". Romance
        # languages agree the modifier with the head instead, which tail_forms
        # above already covers, so this is opt-in per language.
        if plural_last and rest and not any(r"\S+" in t for t in tail):
            last = rest[-1]
            stem = (r"(?<![\w-])(" + _folded(head, char_classes)
                    + "".join(tail[:-1]) + r"\s+" + _folded(last, char_classes))
            for suf in ("s", "es"):
                pats.append((len(alt), stem + suf + r")(?![\w-])"))

    # Dedupe without losing insertion order, then sort stably. set(pats) here
    # discarded the order the patterns were built in, and the sort key only
    # compares the phrase length, so every pattern from the same headword tied
    # and fell back on the set's hash order -- which differs per process.
    seen = set()
    uniq = [p for p in pats if not (p in seen or seen.add(p))]
    return [p for _, p in sorted(uniq, key=lambda x: -x[0])]
