#!/usr/bin/env python3
"""
Construit levels/{niveau}/test-yourself.html : tous les blocs d'exercices
de toutes les leçons de ce niveau, regroupés sous le titre de leur leçon,
sur une seule page — "plus de questions, mélangées, avec un retour
instantané", exactement ce que promet l'appel à l'action "Teste-toi" de
chaque leçon. Généré directement depuis curriculum/{niveau}/*.json (via
lesson_nav_map.json pour l'ordre) plutôt qu'écrit à la main, pour ne
jamais se désynchroniser des leçons qu'il révise.

Usage :
    python3 scripts/build_test_yourself.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = "../../"
LEVELS = [
    ("Pre-A1", "pre-a1"), ("A1", "a1"), ("A2", "a2"), ("B1", "b1"),
    ("B2", "b2"), ("C1", "c1"), ("C2", "c2"),
]


def topic_section(lesson):
    blocks = "".join(
        f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex, ensure_ascii=False)}</script></div>'
        for ex in lesson["exercises"]
    )
    slug = lesson["id"].split("-", 1)[1] if "-" in lesson["id"] else lesson["id"]
    return f"""<section id="{slug}" class="section section--tight ty-topic" aria-labelledby="ty-{slug}-heading">
        <div class="section__inner">
            <p class="eyebrow">{lesson['level']}</p>
            <h2 id="ty-{slug}-heading"><a href="{slug}.html">{lesson['title']}</a></h2>
            <p style="color:var(--color-text-muted);max-width:60ch;margin-bottom:var(--space-md);">{lesson['subtitle']}</p>
            {blocks}
        </div>
    </section>"""


def build(level_code, level_slug):
    nav_map = json.loads((REPO_ROOT / "scripts" / "lesson_nav_map.json").read_text(encoding="utf-8"))
    lessons_order = nav_map.get(level_slug, [])

    sections = []
    toc_links = []
    for entry in lessons_order:
        lesson_path = REPO_ROOT / "curriculum" / level_slug / f"{entry['slug']}.json"
        lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
        sections.append(topic_section(lesson))
        toc_links.append(f'<a href="#{entry["slug"]}">{lesson["title"]}</a>')

    if not sections:
        sections.append(f"""<section class="section section--tight" aria-labelledby="ty-empty-heading">
            <div class="section__inner">
                <h2 id="ty-empty-heading" class="visually-hidden">Niveau à venir</h2>
                <p style="max-width:56ch;font-size:var(--step-0);color:var(--color-text-muted);">Ce niveau n'a pas encore de leçons publiées, donc il n'y a pas encore d'exercices à réviser ici. Reviens bientôt, ou commence dès maintenant par le niveau Pre-A1.</p>
            </div>
        </section>""")

    title = f"Teste-toi : {level_code} — Révision Mixte — Renan le Professeur"
    description = f"Tous les points de grammaire de {level_code} dans une révision mixte, avec un retour instantané à chaque question."
    breadcrumb = (
        f'<li><a href="{REL}index.html">Accueil</a></li>'
        f'<li aria-current="page">Niveaux</li>'
        f'<li><a href="../{level_slug}.html">{level_code}</a></li>'
        f'<li aria-current="page">Teste-toi</li>'
    )

    page_header = f"""<div class="page-header">
        {site_chrome.STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{level_code} &middot; Révision Mixte</p>
                <h1>Teste-toi : {level_code}</h1>
                <p class="page-header__lede">Tous les exercices de toutes les leçons de {level_code}, réunis sur une seule page. Entraîne-toi autant que tu veux, dans l'ordre que tu préfères.</p>
            </div>
        </div>
    </div>"""
    toc = f'<div class="level-toc"><div class="level-toc__inner">{"".join(toc_links)}</div></div>' if toc_links else ""

    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=["exercises", "lessons"]))
    out.append(site_chrome.header(REL, level_code, breadcrumb, active_top="levels"))
    out.append(page_header)
    out.append(toc)
    out.extend(sections)
    out.append(site_chrome.footer(REL, extra_scripts=["exercises.js", "mastery.js"]))

    out_dir = REPO_ROOT / "levels" / level_slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "test-yourself.html"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Built {out_path.relative_to(REPO_ROOT)} ({len(sections)} topics)")


if __name__ == "__main__":
    for code, slug in LEVELS:
        build(code, slug)
