"""Build index.html (GitHub Pages) and dist/artifact.html (claude.ai) from src/quiz.src.html.

The libraries are inlined so the page works without any CDN."""
import pathlib
root = pathlib.Path(__file__).parent
s = (root / "src/quiz.src.html").read_text()
libs = ("<script>" + (root / "vendor/mqtt.min.js").read_text().replace("</script", "<\\/script") + "</script>\n"
        "<script>" + (root / "vendor/qrcode.js").read_text() + "</script>")
s = s.replace("<!--INLINE-LIBS-->", libs)
(root / "dist").mkdir(exist_ok=True)
(root / "dist/artifact.html").write_text(s)
full = ('<!doctype html><html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
        + s.replace("</style>", "</style></head><body>", 1) + "</body></html>")
(root / "index.html").write_text(full)
print("index.html", len(full))
