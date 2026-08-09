#!/usr/bin/env python3
"""Assemble ShineNash deliverables from src/site.html:
  - dist/artifact.html : body-only (Artifact publish format), fonts inlined
  - index.html         : full standalone document, fonts inlined
"""
import pathlib, re

root = pathlib.Path(__file__).parent.parent
src = (root / "src" / "site.html").read_text()
fonts = (root / "build" / "fonts" / "fonts_inline.css").read_text()

content = src.replace("/*__FONTS__*/", fonts)

dist = root / "dist"
dist.mkdir(exist_ok=True)
(dist / "artifact.html").write_text(content)

title = re.search(r"<title>(.*?)</title>", content).group(1)
body = re.sub(r"<title>.*?</title>\s*", "", content, count=1)
index = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="ShineNash — flat-rate house, Airbnb, and office cleaning in Nashville, TN. Background-checked W-2 pros, same team every visit, instant online quotes, and a free 24-hour re-clean Encore Guarantee.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23C9931B' d='M12 2c.9 4.8 2.4 6.3 7.2 7.2v1.6C14.4 11.7 12.9 13.2 12 18c-.9-4.8-2.4-6.3-7.2-7.2V9.2C9.6 8.3 11.1 6.8 12 2z'/%3E%3C/svg%3E">
</head>
<body>
{body}
</body>
</html>
"""
(root / "index.html").write_text(index)
for p in ("dist/artifact.html", "index.html"):
    f = root / p
    print(f"{p}: {f.stat().st_size//1024}KB")
