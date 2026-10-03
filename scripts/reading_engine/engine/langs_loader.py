"""
Importing a language plugin, wherever this engine happens to be sitting.

In the engine repo the plugins are reading/langs/<lang>.py and the package is
importable as `langs`. Vendored into a site they are
scripts/reading_engine/langs/<lang>.py. Loading by file path rather than by
package name works in both without the site needing anything on sys.path.
"""
import importlib.util
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
_CACHE = {}


def get(lang):
    if lang in _CACHE:
        return _CACHE[lang]
    path = PKG / "langs" / f"{lang}.py"
    if not path.exists():
        raise FileNotFoundError(
            f"no morphology plugin for {lang!r} at {path}. Every language needs "
            f"one -- see reading/langs/__init__.py for what it must export.")
    spec = importlib.util.spec_from_file_location(f"_reading_lang_{lang}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    _CACHE[lang] = mod
    return mod
