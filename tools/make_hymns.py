#!/usr/bin/env python3
"""Build src/hymns.json from the Open Hymnal Project (public domain hymns).

Usage:
  git clone --depth 1 https://github.com/mzealey/openhymnal /tmp/openhymnal
  python3 tools/make_hymns.py /tmp/openhymnal

Each hymn becomes {t, a (words by), s: [one slide per verse, refrain as its own slide]}.
Only files whose header says "copyright: public domain" are used.
"""
import json, os, re, sys

MAX_LINE = 34  # characters per line on a slide, roughly


def clean(syl):
    t = syl
    t = re.sub(r"^\s*\d+\.\s*~?", "", t)          # verse number "1.~"
    t = t.replace("\\-", "\u2014")                 # a real dash
    t = t.replace("~", " ").replace("_", " ").replace("*", " ").replace("|", " ")
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"-\s*", "", t)                     # syllables "a- new" -> "anew"
    return t.strip()


# Words that are capitalized inside a line, so they don't start a new line.
KEEP_CAP = set("I God Lord Christ Jesus Jesus' Thee Thou Thy Thine He His Him Spirit Father Son Savior Saviour King Lamb O Oh Zion Israel Bethlehem Heaven Holy Ghost Word Love Name Calvary Jordan Mary Lord's God's Christ's Son's King's Emmanuel Immanuel Alleluia Hallelujah Amen".split())


def to_lines(text):
    # Hymn lines start with a capital letter: break there, and after strong punctuation.
    words, lines, cur = text.split(" "), [], []
    for w in words:
        bare = re.sub(r"^[\"'\u2018\u201c(]+", "", w)
        starts = bare[:1].isupper() and bare.rstrip(",;:.!?\"'\u2019\u201d)") not in KEEP_CAP
        if cur and (starts and len(" ".join(cur)) >= 12 or re.search(r"[.!?;:]$", cur[-1]) and len(" ".join(cur)) >= 12):
            lines.append(" ".join(cur)); cur = []
        cur.append(w)
    if cur:
        lines.append(" ".join(cur))
    out = []
    for ln in lines:  # long lines: split at a comma near the middle, else at a space
        while len(ln) > MAX_LINE + 6:
            mid = len(ln) // 2
            cuts = [m.end() for m in re.finditer(r",\s", ln)]
            cut = min(cuts, key=lambda c: abs(c - mid)) if cuts else ln.rfind(" ", 0, mid + 6) + 1
            if cut <= 0:
                break
            out.append(ln[:cut].strip()); ln = ln[cut:].strip()
        out.append(ln)
    return "\n".join(out)


def parse(path):
    b = open(path, "rb").read()
    try:
        raw = b.decode("utf-8")
    except UnicodeDecodeError:
        raw = b.decode("cp1252", errors="replace")
    if not re.search(r"copyright:\s*public domain", raw, re.I):
        return None
    lines = raw.splitlines()
    title = next((l[2:].strip() for l in lines if l.startswith("T:")), None)
    words_by = next((re.sub(r"^C:\s*Words:\s*", "", l).strip().rstrip(".") for l in lines if re.match(r"C:\s*Words:", l)), "")
    blocks, cur = [], []
    extra, stanza = [], []
    for l in lines:
        if l.startswith("w:"):
            cur.append(clean(l[2:]))
            continue
        if cur:
            blocks.append(cur); cur = []
        if l.startswith("W:"):
            t = l[2:].strip()
            if not t:
                if stanza:
                    extra.append(" ".join(stanza)); stanza = []
            else:
                stanza.append(clean(t))
    if cur:
        blocks.append(cur)
    if stanza:
        extra.append(" ".join(stanza))
    if not blocks:
        return None
    n = max(len(b) for b in blocks)
    verses, refrain = [""] * n, []
    for b in blocks:
        if len(b) == 1 and n > 1:
            refrain.append(b[0])  # one line under the music for every verse: the refrain
        else:
            for i, t in enumerate(b):
                verses[i] = (verses[i] + " " + t).strip()
    verses = [v for v in verses if v] + [v for v in extra if v]
    ref = " ".join(refrain).strip()
    slides = []
    for v in verses:
        slides.append(to_lines(v))
        if ref:
            slides.append(to_lines(ref))
    if not slides:
        return None
    return {"t": title, "a": words_by, "s": slides}


def main(root):
    out, seen = [], set()
    base = os.path.join(root, "Complete")
    for d in sorted(os.listdir(base)):
        files = sorted(f for f in os.listdir(os.path.join(base, d)) if f.endswith(".abc"))
        for f in files:
            h = parse(os.path.join(base, d, f))
            if h and h["t"] and h["t"].lower() not in seen:
                seen.add(h["t"].lower()); out.append(h); break
    out.sort(key=lambda h: re.sub(r"^(the|a|o)\s+", "", h["t"].lower()))
    dest = os.path.join(os.path.dirname(__file__), "..", "src", "hymns.json")
    json.dump(out, open(dest, "w"), ensure_ascii=False, separators=(",", ":"))
    print(len(out), "hymns ->", os.path.normpath(dest), os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "/tmp/openhymnal")
