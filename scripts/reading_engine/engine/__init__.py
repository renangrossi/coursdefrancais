"""
The shared reading-library engine.

Language-neutral. Everything that differs between the family's sites comes
from two places: reading/strings/<lang>.json (what a student reads) and
reading/langs/<lang>.py (how the language inflects). See reading/README.md.

This package is vendored into each site as scripts/reading_engine/ by
reading/apply.py -- it is never edited there. Edit it here and re-apply.
"""
