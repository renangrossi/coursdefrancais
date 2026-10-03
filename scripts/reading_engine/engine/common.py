"""
Paths, levels, voices and source loading -- the things every reading script
needs and none of them should define twice.
"""
import json
from pathlib import Path

from . import config as _config

PKG = Path(__file__).resolve().parent.parent
# reading/ in the engine repo has no site around it; scripts/reading_engine/
# in a site sits two levels under the repo root.
REPO_ROOT = PKG.parent.parent

LEVELS = ["pre-a1", "a1", "a2", "b1", "b2", "c1", "c2"]


class Site:
    """One site's reading library: its config, its paths, its sources."""

    def __init__(self, lang=None, repo_root=None):
        self.cfg = _config.load(lang)
        self.lang = self.cfg.lang
        self.root = Path(repo_root) if repo_root else REPO_ROOT
        self.src_dir = self.root / "content" / "readings"
        self.page_dir = self.root / self.cfg["READING_DIR"]
        self.audio_dir = self.root / "assets" / "audio" / "reading"
        self.img_dir = self.root / "assets" / "img" / "reading"

    # -- paths ---------------------------------------------------------------
    def src_path(self, level, slug):
        return self.src_dir / level / f"{slug}.json"

    def page_path(self, level, slug):
        return self.page_dir / level / f"{slug}.html"

    def audio_path(self, level, slug):
        return self.audio_dir / level / f"{slug}.mp3"

    def audio_href(self, level, slug, rel="../../"):
        return f"{rel}assets/audio/reading/{level}/{slug}.mp3"

    def page_url(self, level, slug):
        return (f'{self.cfg["SITE_URL"]}/{self.cfg["READING_DIR"]}'
                f'/{level}/{slug}.html')

    # -- sources -------------------------------------------------------------
    def load(self, level, slug):
        return json.loads(self.src_path(level, slug).read_text(encoding="utf-8"))

    def all_sources(self):
        """Every reading source JSON, as (level, slug, data)."""
        for lv in LEVELS:
            d = self.src_dir / lv
            if not d.is_dir():
                continue
            for f in sorted(d.glob("*.json")):
                yield lv, f.stem, json.loads(f.read_text(encoding="utf-8"))

    # -- narration -----------------------------------------------------------
    def pick_voice(self, slug, narrator):
        """narrator: "male" | "female" | None. Deterministic per slug, so a
        rebuild does not silently reassign a voice (and thus invalidate
        audio)."""
        f, m = self.cfg["VOICES_F"], self.cfg["VOICES_M"]
        roster = m if narrator == "male" else f if narrator == "female" else f + m
        return roster[sum(ord(c) for c in slug) % len(roster)]

    def rate(self, level):
        return self.cfg["LEVEL_RATE"][level]

    def topic_label(self, topic):
        return self.cfg["TOPIC_LABELS"].get(topic or "", "")
