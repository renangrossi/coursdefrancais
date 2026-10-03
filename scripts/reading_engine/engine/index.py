"""
Build the reading library's own index page: {READING_DIR}/index.html.

Why the library gets its own page rather than a section spliced into each
site's exercises hub: those hubs are generated wholesale by each site's own
build_static_pages.py / build_exercises_hub.py, which differ across the family
and would overwrite anything the engine wrote into them. A page the engine owns
end to end needs no cooperation from seven different hub builders -- the site
only has to link to it once, from wherever it likes.

The cards use .card, .grid, .grid--3, .eyebrow and .badge, which every site in
the family already defines. Everything specific to this page is scoped under
.reading-index in assets/css/reading.css.
"""
from .page import REL as PAGE_REL, STARS_ROW, esc

REL = "../"


class IndexBuilder:
    def __init__(self, site, chrome):
        self.site = site
        self.cfg = site.cfg
        self.chrome = chrome

    def card(self, level, slug, d):
        # The index sits at {READING_DIR}/index.html and the texts one level
        # below it, at {READING_DIR}/{level}/{slug}.html -- so the href needs
        # the level segment. Without it every card 404s.
        topic = self.site.topic_label(d.get("topic"))
        dur = (d.get("audio") or {}).get("duration_label")
        meta = " &middot; ".join(x for x in (esc(topic) if topic else "", dur) if x)
        return f"""<article class="card reading-card">
                    <p class="eyebrow">{esc(d["level"])}{f' &middot; {meta}' if meta else ''}</p>
                    <h3 class="reading-card__title"><a href="{esc(level)}/{esc(slug)}.html">{esc(d["title"])}</a></h3>
                    <p class="reading-card__blurb">{esc(d.get("subtitle", ""))}</p>
                </article>"""

    def level_section(self, level, rows):
        cards = "\n                ".join(self.card(level, slug, d) for slug, d in rows)
        n = len(rows)
        count = self.cfg["INDEX_COUNT"].replace("{n}", str(n))
        return f"""<section class="section section--tight" aria-labelledby="lv-{level}-heading">
        <div class="section__inner">
            <p class="eyebrow">{count}</p>
            <h2 id="lv-{level}-heading">{esc(rows[0][1]["level"])}</h2>
            <div class="grid grid--3 reading-index">
                {cards}
            </div>
        </div>
    </section>"""

    def build(self):
        by_level = {}
        for lv, slug, d in self.site.all_sources():
            by_level.setdefault(lv, []).append((slug, d))
        if not by_level:
            return None
        for rows in by_level.values():
            # "order" sorts within a level; a text without one sorts last, by
            # title, so adding a text never reshuffles the ones already there.
            rows.sort(key=lambda r: (r[1].get("order", 10**6), r[1]["title"]))

        total = sum(len(r) for r in by_level.values())
        sections = [self.level_section(lv, by_level[lv])
                    for lv in self.site.cfg["LEVEL_ORDER"] if lv in by_level]

        header = f"""<div class="page-header">
        {STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{esc(self.cfg["INDEX_EYEBROW"])}</p>
                <h1>{esc(self.cfg["INDEX_TITLE"])}</h1>
                <p class="page-header__lede">{esc(self.cfg["INDEX_LEDE"].replace("{n}", str(total)))}</p>
            </div>
        </div>
    </div>"""

        breadcrumb = (
            f'<li><a href="{REL}index.html">{esc(self.cfg["BREADCRUMB_HOME"])}</a></li>'
            f'<li aria-current="page">{esc(self.cfg["BREADCRUMB_READING"])}</li>')

        out = [
            self.chrome.head(REL, f'{self.cfg["INDEX_TITLE"]} — {self.cfg["PRINT_BRAND"]}',
                             self.cfg["INDEX_LEDE"].replace("{n}", str(total)),
                             page_path=f'{self.cfg["READING_DIR"]}/index.html',
                             extra_css=["reading"]),
            self.chrome.header(REL, None, breadcrumb, body_class="reading-index-page"),
            header,
            *sections,
            self.chrome.footer(REL),
        ]
        p = self.site.page_dir / "index.html"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(out), encoding="utf-8")
        return p
