"""Build index.html (the slide builder) and live.html (Sunday Live, for running
the service on the projector). Each is one self-contained page (song list,
pictures, Bibles and the PowerPoint library are all inlined), so it works from
GitHub Pages or by double-clicking the file. Run: python3 build.py"""
import base64
import json
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"


def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


HEAD = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>[hidden]{display:none!important}body{margin:0}img{max-width:100%}</style>\n'
        '</head>\n<body>\n')
TAIL = "\n</body>\n</html>\n"


def build():
    page = (SRC / "template.html").read_text()
    images = {
        "welcomeBg": data_uri(SRC / "assets/welcome_bg.jpg", "image/jpeg"),
        "logo": data_uri(SRC / "assets/logo.png", "image/png"),
        "logoWhite": data_uri(SRC / "assets/logo_white.png", "image/png"),
        "church": data_uri(SRC / "assets/church.jpg", "image/jpeg"),
    }
    songs = json.dumps(json.loads((SRC / "songs.json").read_text()), ensure_ascii=False, separators=(",", ":"))
    pptxgen = (ROOT / "vendor/pptxgen.bundle.js").read_text()
    pptxgen = pptxgen.replace("//# sourceMappingURL=pptxgen.bundle.js.map", "")
    page = (page.replace("/*SONGS*/", songs.replace("</", "<\\/"))
                .replace("/*IMAGES*/", json.dumps(images))
                .replace("/*PPTXGEN*/", pptxgen.replace("</script", "<\\/script")))
    (ROOT / "index.html").write_text(HEAD + page + TAIL)

    bibles = {p.name.split(".")[0]: base64.b64encode(p.read_bytes()).decode()
              for p in sorted((SRC / "bible").glob("*.json.gz"), key=lambda p: p.name != "KJV.json.gz")}
    live = (SRC / "live.html").read_text()
    live = (live.replace("/*SONGS*/", songs.replace("</", "<\\/"))
                .replace("/*IMAGES*/", json.dumps(images))
                .replace("/*BIBLES*/", json.dumps(bibles)))
    (ROOT / "live.html").write_text(HEAD + live + TAIL)


if __name__ == "__main__":
    build()
