#!/usr/bin/env python3
"""Assemble ShineNova deliverables from src/site.html:
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
<meta name="description" content="ShineNova — flat-rate house, Airbnb, and office cleaning in Nashville, TN. Background-checked W-2 pros, same team every visit, instant online quotes, and a free 24-hour re-clean guarantee.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23FFDF00' d='M12 1.5Q13.8 10 22.5 12 13.8 14 12 22.5 10.2 14 1.5 12 10.2 10 12 1.5Z'/%3E%3Ccircle cx='10.2' cy='11' r='1.2' fill='%2312304A'/%3E%3Ccircle cx='13.8' cy='11' r='1.2' fill='%2312304A'/%3E%3Cpath d='M10.3 13.4q1.7 1.5 3.4 0' fill='none' stroke='%2312304A' stroke-width='1.1' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="canonical" href="https://www.shinenova.com/">
<meta property="og:title" content="{title}">
<meta property="og:description" content="Flat-rate house, Airbnb, and office cleaning in Nashville, TN — instant online quotes, same trusted team every visit.">
<meta property="og:url" content="https://www.shinenova.com/">
<meta property="og:type" content="website">
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
