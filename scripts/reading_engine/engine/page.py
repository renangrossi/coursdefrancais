"""
Build {READING_DIR}/{level}/{slug}.html from content/readings/{level}/{slug}.json.

Deliberately separate from each site's build_lesson.py: that builds the grammar
lessons from curriculum/*.json, and re-running it on an existing lesson
destroys enrichment those built pages hold but their JSON no longer does.
Nothing here touches a site's levels/ or curriculum/.

Page shape (reusing each site's existing components -- the only new CSS is
assets/css/reading.css, which the engine also owns):

    page-header          level eyebrow + print button
    level-toc            jump links
    #listen-and-read     <audio controls> then the passage
    (glossary)           accessible-hidden on screen, printed on paper
    #practice            .exercise-block JSON for assets/js/exercises.js
    #discussion          optional speaking/writing prompts
"""
import html
import json
import re

from .match import surface_patterns

REL = "../../"

STAR = ('<svg class="" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
        '<path d="m12 2 2.9 6.9 7.1.6-5.4 4.7 1.6 7L12 17.5 5.8 21.2l1.6-7L2 9.5l7.1-.6Z"/></svg>')
STARS_ROW = f'<div class="stars-row stars-row--onlight" aria-hidden="true">{STAR * 11}</div>'
PRINTER_SVG = ('<svg class="" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" '
               'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/>'
               '<path d="M6 14h12v8H6Z"/></svg>')


def esc(s):
    return html.escape(str(s), quote=False)


# A title set between asterisks, the way anyone writing plain text marks one.
# The JSON is hand-written, so this is the only markup it is allowed to carry.
EMPHASIS_RE = re.compile(r"\*([^*\n]+)\*")


def _emphasis(escaped):
    """Turn *...* into <em>...</em> in text that has ALREADY been escaped."""
    return EMPHASIS_RE.sub(r"<em>\1</em>", escaped)


def _caption(text):
    return _emphasis(esc(text))


# "Receptionist:", "You:", "Emma:", "La receptionniste :" -- a dialogue turn,
# as opposed to prose that merely contains a colon. French sets a space before
# the colon, which is why the separator is optional-space rather than none.
SPEAKER_RE = re.compile(r"^[^\W\d_][\w .'’À-ſ-]{0,24}\s?:\s")

# A numbered section heading inside a passage -- "1. Booking a room" -- as
# opposed to a sentence that merely starts with a figure.
NUMBERED_HEADING_RE = re.compile(r"^\d+\.\s+\S")


def is_heading(para):
    t = para.strip()
    if not t:
        return False
    if NUMBERED_HEADING_RE.match(t) and len(t) <= 70 and t[-1] not in ".!?:;":
        return True
    # A short titled heading with no number. It has to be short, end without
    # sentence punctuation, and not be a line of dialogue, which is also short
    # and unpunctuated at the end.
    if (len(t) <= 60 and t[-1] not in ".!?:;,”’\"'"
            and not SPEAKER_RE.match(t) and len(t.split()) <= 9):
        return True
    letters = [c for c in t if c.isalpha()]
    return bool(letters) and sum(c.isupper() for c in letters) / len(letters) > 0.6


def annotate(paras, vocab, lang):
    """Bold the first occurrence of each glossary word in the passage and hang
    its definition off it, so the reader can hover (or tap, or tab to) the word
    instead of consulting a separate list.

    Each term is marked at most once, across the whole passage -- marking every
    occurrence would turn a page into a field of underlines."""
    # A glossary entry may pin the exact surface form to highlight via "match".
    # Auto-matching cannot tell senses apart: "to exchange" (return goods)
    # happily attached itself to "exchanges" meaning conversations, so the
    # author needs a way to say which word is meant.
    todo = []
    for i, v in enumerate(vocab or []):
        if v.get("match"):
            pats = [r"(?<![\w-])(" + re.escape(v["match"]).replace(r"\ ", r"\s+") + r")(?![\w-])"]
        else:
            pats = surface_patterns(v["term"], lang)
        todo.append((v["term"], (v["definition"], i), pats))

    out, placed, headings, slot = [], set(), set(), []
    for idx, para in enumerate(paras):
        text = para
        # A section heading inside the passage is not prose, and highlighting a
        # word in one hangs the definition off the heading itself.
        if is_heading(para):
            headings.add(idx)
            out.append(text)
            continue
        while True:
            best = None
            for term, definition, forms in todo:
                if term in placed:
                    continue
                for pat in forms:
                    m = re.search(pat, text, re.I)
                    if m and (best is None or m.start() < best[0].start()):
                        best = (m, term, definition)
                        break
            if best is None:
                break
            m, term, definition = best
            placed.add(term)
            token = f"\x00{len(slot)}\x00"
            slot.append((m.group(1), definition))
            text = text[:m.start()] + token + text[m.end():]
        out.append(text)

    rendered = []
    for text in out:
        t = _emphasis(esc(text))
        for i, (word, (definition, vi)) in enumerate(slot):
            # data-definition drives the CSS tooltip, which only a sighted
            # reader gets; aria-describedby points at the same words in the Key
            # Vocabulary list below, which is what a screen reader reads out.
            t = t.replace(
                f"\x00{i}\x00",
                f'<span class="vocab-term" tabindex="0" role="note" '
                f'aria-describedby="vocab-{vi}" '
                f'data-definition="{html.escape(definition, quote=True)}">{esc(word)}</span>')
        rendered.append(t)
    return rendered, placed, headings


class Builder:
    def __init__(self, site, chrome):
        self.site = site
        self.cfg = site.cfg
        self.chrome = chrome
        self.lang = site.cfg.morphology

    # -- pieces --------------------------------------------------------------
    def print_button(self):
        return (f'<button type="button" class="btn btn--ghost btn--small print-hidden" '
                f'data-print-page>{PRINTER_SVG}{esc(self.cfg["PRINT_BUTTON"])}</button>')

    def page_header(self, d):
        """A thin band: where you are, and the one action the page offers.

        The text's own title belongs immediately above the text, not up here --
        a title separated from its prose by a navigation bar is a title for the
        page rather than for the reading."""
        topic = self.site.topic_label(d.get("topic"))
        eyebrow = f'{d["level"]} &middot; {esc(topic)}' if topic else d["level"]
        return f"""<div class="page-header page-header--slim">
        {STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{eyebrow}</p>
                <p class="page-header__actions print-hidden">{self.print_button()}</p>
            </div>
        </div>
    </div>"""

    def toc(self, ids):
        labels = {"listen-and-read": self.cfg["TOC_READING"],
                  "practice": self.cfg["TOC_PRACTICE"],
                  "discussion": self.cfg["TOC_DISCUSSION"]}
        links = "".join(f'<a href="#{i}">{esc(labels[i])}</a>' for i in labels if i in ids)
        return f'<div class="level-toc"><div class="level-toc__inner">{links}</div></div>'

    def reading_intro(self):
        """One line of instructions, next to the player it is about.

        The demo tooltip is built from the strings rather than written into
        them, so a translator never has to reproduce the span by hand."""
        demo = (f'<span class="vocab-term" tabindex="0" role="note" '
                f'data-definition="{html.escape(self.cfg["READING_INTRO_TOOLTIP"], quote=True)}">'
                f'{esc(self.cfg["READING_INTRO_TERM"])}</span>')
        return esc(self.cfg["READING_INTRO"]).replace("{TERM}", demo)

    def figures(self, d, level, slug):
        """Images belong to the page but not to the passage: they are listed
        separately in the source JSON and slotted in after the paragraph each
        one names. Keeping them out of "passage" means adding a picture never
        changes the narration fingerprint, so it never forces a re-record."""
        out = {}
        for img in (d.get("images") or []):
            # A plain filename lives in this page's own folder. A path with a
            # slash is relative to assets/img/reading/, so several pages split
            # out of one source document can share its image set.
            rel = img["src"] if "/" in img["src"] else f"{level}/{slug}/{img['src']}"
            src = f"{REL}assets/img/reading/{rel}"
            # A picture used under an attribution licence is free only on
            # condition of a credit, so the credit is part of the figure rather
            # than something kept in a file somebody has to go and find.
            credit = ""
            if img.get("licence"):
                who = esc(img["author"]) if img.get("author") else "?"
                lic = esc(self.cfg["LICENCE_LABEL"].get(img["licence"], img["licence"]))
                if img.get("source_url"):
                    lic = f'<a href="{esc(img["source_url"])}" rel="license nofollow">{lic}</a>'
                kind = esc(img.get("credit_prefix") or self.cfg.get("CREDIT_PHOTO", "Photo"))
                credit = f'<span class="reading-figure__credit">{kind}: {who}, {lic}</span>'
            cap_text = _caption(img["caption"]) if img.get("caption") else ""
            cap = f'<figcaption>{cap_text}{credit}</figcaption>' if (cap_text or credit) else ""
            cls = "reading-figure reading-figure--wide" if img.get("wide") else "reading-figure"
            out.setdefault(int(img.get("after", 0)), []).append(
                f'<figure class="{cls}">'
                f'<img src="{src}" alt="{html.escape(img.get("alt", ""), quote=True)}" loading="lazy">'
                f'{cap}</figure>')
        return out

    def listen_and_read(self, d, level, slug):
        """Audio first, then the text. Native <audio controls> is a deliberate
        choice: play/pause, a progress bar, elapsed/total time, keyboard access
        and a playback-speed menu on every modern browser, with no JavaScript
        to fail."""
        marked, _placed, headings = annotate(d["passage"], d.get("vocabulary"), self.lang)

        def ptag(i):
            if i in headings:
                return '<p class="reading-passage__heading">'
            if SPEAKER_RE.match(d["passage"][i]):
                return '<p class="reading-passage__turn">'
            if i == 0:
                # The drop cap hangs on this paragraph, so it has to be long
                # enough to sit beside; under about 200 characters it would
                # overhang whatever follows.
                short = " reading-passage__lead--short" if len(d["passage"][0]) < 200 else ""
                return f'<p class="reading-passage__lead{short}">'
            if (i - 1) in headings:
                return '<p class="reading-passage__opener">'
            return "<p>"

        figs = self.figures(d, level, slug)
        blocks = []
        for i, p in enumerate(marked):
            blocks.append(f"{ptag(i)}{p}</p>")
            blocks.extend(figs.get(i, []))
        paras = "\n            ".join(blocks)

        # The same list serves three readers: somebody skimming before they
        # start, somebody using a screen reader (a CSS tooltip is invisible to
        # one), and somebody holding a printout with nothing to hover over.
        gloss = "".join(
            f'<li id="vocab-{i}"><strong>{esc(v["term"])}</strong> '
            f'<span class="reading-glossary__def">{esc(v["definition"])}</span></li>'
            for i, v in enumerate(d.get("vocabulary") or []))
        gloss_html = (f'<div class="reading-glossary">'
                      f'<h2 class="reading-glossary__heading">{esc(self.cfg["KEY_VOCABULARY"])}</h2>'
                      f'<ul class="reading-glossary__list">{gloss}</ul></div>') if gloss else ""

        href = self.site.audio_href(level, slug, REL)
        return f"""<section id="listen-and-read" class="section" aria-labelledby="lr-heading">
        <div class="section__inner">
            <h1 id="lr-heading" class="reading-title">{esc(d['title'])}</h1>
            <p class="reading-subtitle">{esc(d['subtitle'])}</p>
            <p class="reading-intro print-hidden">{self.reading_intro()}</p>
            <audio controls preload="metadata" src="{href}">
                <p>{esc(self.cfg["AUDIO_FALLBACK"])} <a href="{href}">{esc(self.cfg["AUDIO_DOWNLOAD"])}</a></p>
            </audio>
            <div class="reading-passage">
            {paras}
            </div>
            {gloss_html}
            {self.print_source(d, level, slug)}
        </div>
    </section>"""

    def practice(self, d):
        exs = d.get("exercises") or []
        if not exs:
            return ""
        blocks = "".join(
            '<div class="exercise-block"><script type="application/json" class="exercise-data">'
            f'{json.dumps(ex, ensure_ascii=False)}</script></div>' for ex in exs)
        return f"""<section id="practice" class="section section--surface" aria-labelledby="practice-heading">
        <div class="section__inner">
            <p class="eyebrow">{esc(self.cfg["PRACTICE_EYEBROW"])}</p>
            <h2 id="practice-heading">{esc(self.cfg["PRACTICE_HEADING"])}</h2>
            <p class="reading-section-blurb">{self.cfg["PRACTICE_BLURB"]}</p>
            {blocks}
        </div>
    </section>"""

    def discussion(self, d):
        prompts = d.get("discussion") or []
        if not prompts:
            return ""
        rows = "".join(f"<li>{esc(p)}</li>" for p in prompts)
        return f"""<section id="discussion" class="section section--tight" aria-labelledby="disc-heading">
        <div class="section__inner">
            <p class="eyebrow">{self.cfg["DISCUSSION_EYEBROW"]}</p>
            <h2 id="disc-heading">{esc(self.cfg["DISCUSSION_HEADING"])}</h2>
            <p class="reading-section-blurb">{self.cfg["DISCUSSION_BLURB"]}</p>
            <ul class="summary-list">{rows}</ul>
        </div>
    </section>"""

    def print_source(self, d, level, slug):
        """Printed once at the foot of the handout. A photocopy that has lost
        its first page should still say where it came from and what level."""
        topic = self.site.topic_label(d.get("topic"))
        where = f'{d["level"]} &middot; {esc(topic)}' if topic else d["level"]
        url = self.site.page_url(level, slug)
        return (f'<p class="print-source">{esc(d["title"])} &mdash; {where} &middot; '
                f'{esc(self.cfg["PRINT_BRAND"])} &middot; '
                f'<a href="{url}">{url}</a></p>')

    # -- the page ------------------------------------------------------------
    def build(self, level, slug, d):
        suffix = self.cfg["PAGE_TITLE_SUFFIX"].replace("{level}", d["level"])
        title = f'{d["title"]} — {suffix}'
        description = d.get("description") or f'{d["title"]}: {d["subtitle"]}'
        rd, ex, lv = (self.cfg["READING_DIR"], self.cfg["EXERCISES_PAGE"],
                      self.cfg["LEVELS_DIR"])
        breadcrumb = (
            f'<li><a href="{REL}index.html">{esc(self.cfg["BREADCRUMB_HOME"])}</a></li>'
            f'<li><a href="{REL}{ex}">{esc(self.cfg["BREADCRUMB_READING"])}</a></li>'
            f'<li><a href="{REL}{lv}/{level}.html">{d["level"]}</a></li>'
            f'<li aria-current="page">{esc(d["title"])}</li>'
        )
        body = [self.listen_and_read(d, level, slug), self.practice(d), self.discussion(d)]
        ids = [i for i, s in zip(["listen-and-read", "practice", "discussion"], body) if s]

        out = [
            self.chrome.head(REL, title, description[:300],
                             page_path=f"{rd}/{level}/{slug}.html",
                             # Bare names: every site's head() appends ".css".
                             # "exercises" is needed because a reading page
                             # carries .exercise-block, and several sites do
                             # not load that stylesheet by default.
                             extra_css=self.cfg.get("EXTRA_CSS", ["exercises", "reading"])),
            self.chrome.header(REL, d["level"], breadcrumb),
            self.page_header(d),
            self.toc(ids),
            *[s for s in body if s],
            # Loaded here rather than in <head> because it is an enhancement
            # with nothing to block rendering for, and because not every
            # site's footer() accepts an extra-scripts argument.
            f'<script src="{REL}assets/js/reading.js"></script>',
            self.chrome.footer(REL),
        ]
        p = self.site.page_path(level, slug)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(out), encoding="utf-8")
        return p
