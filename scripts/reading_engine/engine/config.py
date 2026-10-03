"""
Loading a site's reading-library configuration.

A vendored copy carries its own strings/<lang>.json and langs/<lang>.py next
to it, plus a one-line site.json saying which language it is. Running from
the engine repo instead, config.load("fr") reads the canonical files.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent            # reading/ in the engine, scripts/reading_engine/ in a site


def _first_existing(*paths):
    for p in paths:
        if p.exists():
            return p
    return None


def site_lang(default=None):
    """The language code this vendored copy was generated for."""
    f = PKG / "site.json"
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))["lang"]
    if default:
        return default
    raise RuntimeError("no site.json beside the engine; pass a language explicitly")


class Config:
    def __init__(self, lang, strings):
        self.lang = lang
        self.s = strings

    def __getitem__(self, key):
        try:
            return self.s[key]
        except KeyError:
            raise KeyError(
                f"{self.lang}.json has no string {key!r} -- add it to "
                f"reading/strings/{self.lang}.json and re-apply") from None

    def get(self, key, default=None):
        return self.s.get(key, default)

    @property
    def morphology(self):
        """The language plugin module."""
        from . import langs_loader
        return langs_loader.get(self.lang)


def load(lang=None):
    lang = lang or site_lang()
    f = _first_existing(PKG / "strings" / f"{lang}.json")
    if not f:
        raise FileNotFoundError(f"no strings file for {lang!r} under {PKG / 'strings'}")
    data = json.loads(f.read_text(encoding="utf-8"))
    return Config(lang, {k: v for k, v in data.items() if not k.startswith("_")})
