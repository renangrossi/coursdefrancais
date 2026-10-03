"""
Narrate content/readings/{level}/{slug}.json to
assets/audio/reading/{level}/{slug}.mp3 with edge-tts.

It narrates the same "passage" the page renders, so the audio cannot drift
from the text.
"""
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

# The pause between paragraphs is about 0.97s and CANNOT be changed from here.
#
# edge-tts takes plain text and builds its own SSML, so there is no <break> to
# ask for, and the obvious tricks do not work: a line holding a full stop, an
# ellipsis, a dash, a row of commas and four blank lines were each measured
# against this separator on a real three-paragraph passage, and all seven
# produced byte-identical timing. The service discards punctuation-only lines.
# Writing "(pause)" does change it, by reading the word out loud.
#
# A short artificial sample DOES respond to those tricks, which is how this was
# got wrong once already: two one-sentence paragraphs gave 0.43s plain and
# 1.03s with dot lines. Real paragraphs do not behave that way.
PARAGRAPH_BREAK = "\n\n"


def narration_text(d):
    """What the narrator reads: the title, then the passage.

    Asterisks around a title ("*Browder v. Gayle*") are typographic markup for
    the page, not something to say out loud, so they come off here."""
    paras = [re.sub(r"\*([^*\n]+)\*", r"\1", p) for p in d["passage"]]
    return PARAGRAPH_BREAK.join([d["title"].rstrip(".") + "."] + paras)


class Narrator:
    def __init__(self, site):
        self.site = site
        self.cfg = site.cfg
        self.manifest_path = site.audio_dir / "manifest.json"

    # Staleness is decided by the narration text, not by file timestamps.
    # Editing a title, an exercise or a duration label does not change what the
    # narrator says, and an mtime comparison would report those edits as stale
    # and burn a regeneration on every one of them. Hashing the exact string
    # sent to edge-tts (plus the voice and rate) means audio is rebuilt when,
    # and only when, it no longer matches the text.
    def load_manifest(self):
        if self.manifest_path.exists():
            return json.loads(self.manifest_path.read_text(encoding="utf-8"))
        return {}

    def save_manifest(self, m):
        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        self.manifest_path.write_text(
            json.dumps(m, indent=1, sort_keys=True) + "\n", encoding="utf-8")

    def fingerprint(self, d, voice, rate):
        h = hashlib.sha256()
        h.update(narration_text(d).encode("utf-8"))
        h.update(f"|{voice}|{rate}".encode("utf-8"))
        return h.hexdigest()[:16]

    def voice_and_rate(self, level, slug, d):
        a = d.get("audio", {})
        voice = a.get("voice") or self.site.pick_voice(slug, d.get("narrator"))
        rate = a.get("rate") or self.site.rate(level)
        return voice, rate

    def is_stale(self, level, slug, d=None, manifest=None):
        a = self.site.audio_path(level, slug)
        if not a.exists():
            return "missing"
        if d is None:
            return None
        manifest = self.load_manifest() if manifest is None else manifest
        voice, rate = self.voice_and_rate(level, slug, d)
        key = f"{level}/{slug}"
        if manifest.get(key, {}).get("fingerprint") != self.fingerprint(d, voice, rate):
            return "stale"
        return None

    @staticmethod
    def find_tts(explicit=None):
        if explicit:
            return explicit
        for c in ("edge-tts", "/tmp/rl-venv/bin/edge-tts"):
            p = shutil.which(c) or (c if Path(c).is_file() else None)
            if p:
                return p
        return None

    def generate(self, level, slug, d, tts):
        voice, rate = self.voice_and_rate(level, slug, d)
        out = self.site.audio_path(level, slug)
        out.parent.mkdir(parents=True, exist_ok=True)
        cmd = [tts, "--voice", voice, "--rate", rate,
               "--write-media", str(out), "--text", narration_text(d)]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        if r.returncode != 0 or not out.exists() or out.stat().st_size < 2000:
            raise RuntimeError(f"edge-tts failed for {level}/{slug}: {r.stderr.strip()[:300]}")

        # edge-tts can return 0 and still write a file that stops part-way
        # through the text -- it happened once to a B1 text, which came out at
        # 1:56 for a passage that needs 3:31, and nothing caught it because the
        # old guard only rejected files under 2 KB. The threshold is
        # deliberately loose: it is here to catch gross truncation, not to
        # police normal variation between voices, and it is per-language
        # because average word length is not the same in two languages.
        floor = float(self.cfg.get("AUDIO_MIN_KB_PER_WORD", 1.4))
        words = sum(len(p.split()) for p in d["passage"]) or 1
        kb_per_word = (out.stat().st_size / 1024) / words
        if kb_per_word < floor:
            raise RuntimeError(
                f"{level}/{slug}: narration looks truncated -- "
                f"{out.stat().st_size // 1024} KB for {words} words "
                f"({kb_per_word:.2f} KB/word, expected >= {floor}). Delete the "
                f"file and run again; this is usually a transient edge-tts failure.")
        return out, voice, rate

    # ------------------------------------------------------------------ ---
    def measure(self, level, slug):
        """The narration's length as "M:SS", or None if it cannot be measured.

        ffprobe is the only thing here that is not pure Python, and it is not
        worth a hard dependency for a cosmetic label -- so a machine without
        ffmpeg installed simply skips stamping rather than failing a build.
        """
        a = self.site.audio_path(level, slug)
        if not a.exists() or not shutil.which("ffprobe"):
            return None
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(a)],
            capture_output=True, text=True, timeout=60)
        try:
            secs = float(r.stdout.strip())
        except ValueError:
            return None
        return f"{int(secs) // 60}:{int(round(secs)) % 60:02d}"

    def stamp_duration(self, level, slug):
        """Write the measured duration into the source JSON.

        This is the one place the engine writes to a site's content, so it is
        opt-in (--stamp-durations) and it changes exactly one field. The
        narration fingerprint does not cover audio.duration_label, so stamping
        it never makes the file it describes look stale.
        """
        label = self.measure(level, slug)
        if not label:
            return None
        path = self.site.src_path(level, slug)
        d = json.loads(path.read_text(encoding="utf-8"))
        if d.get("audio", {}).get("duration_label") == label:
            return label
        d.setdefault("audio", {})["duration_label"] = label
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
        return label
