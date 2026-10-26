"""Turn the public-domain Bible JSON files from github.com/scrollmapper/bible_databases
(formats/json/KJV.json and BSB.json) into the compact files the live page uses:
src/bible/<CODE>.json.gz holding [[[verse text, ...] per chapter] per book].
Run: python3 tools/make_bibles.py path/to/KJV.json path/to/BSB.json"""
import gzip
import json
import re
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "src" / "bible"


def clean(text):
    text = text.replace("[", "").replace("]", "")       # KJV marks added words with [brackets]
    text = re.sub(r"^[א-ת]\s+[A-Z]+\.\s*", "", text)  # Psalm 119 acrostic headings
    return re.sub(r"\s+", " ", text).strip()


def main(paths):
    OUT.mkdir(parents=True, exist_ok=True)
    for p in map(Path, paths):
        data = json.loads(p.read_text())
        books = [[[clean(v["text"]) for v in ch["verses"]] for ch in b["chapters"]] for b in data["books"]]
        assert len(books) == 66
        raw = json.dumps(books, ensure_ascii=False, separators=(",", ":")).encode()
        (OUT / (p.stem.upper() + ".json.gz")).write_bytes(gzip.compress(raw, 9, mtime=0))
        print(p.stem, len(raw), "bytes")


if __name__ == "__main__":
    main(sys.argv[1:])
