"""
Search-index entries for the reading library.

Each site builds its own assets/data/search-index.json and they do not agree on
how -- so the engine does not write that file. It hands back the entries for
its own texts in the shape the family's search.js already reads, and a site
adds them with one line in its build_search_index.py:

    from reading_engine.engine import common, search
    entries.extend(search.entries(common.Site()))

A site with no content/readings/ yet gets an empty list, so the call is safe to
add before any text is authored.
"""


def entries(site, include_index=True):
    """[{type, level, title, desc, url, keywords}] for every reading text."""
    cfg = site.cfg
    rd = cfg["READING_DIR"]
    out = []
    n = 0
    for level, slug, d in site.all_sources():
        n += 1
        kw = [k for k in (d.get("topic"), *(d.get("grammar") or [])) if k]
        # The glossary headwords are the words a student is most likely to
        # search for, and they are already the text's own vocabulary list.
        kw += [v["term"] for v in (d.get("vocabulary") or [])]
        out.append({
            "type": "exercise",
            "level": d["level"],
            "title": d["title"],
            "desc": d.get("subtitle", ""),
            "url": f"{rd}/{level}/{slug}.html",
            "keywords": kw,
        })
    if include_index and n:
        out.append({
            "type": "extra",
            "level": "",
            "title": cfg["INDEX_TITLE"],
            "desc": cfg["INDEX_LEDE"].replace("{n}", str(n)),
            "url": f"{rd}/index.html",
            "keywords": [cfg["INDEX_EYEBROW"].lower()],
        })
    return out
