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
<meta name="description" content="DustBusters — flat-rate house, Airbnb, and office cleaning in Nashville, TN. Background-checked W-2 pros, same team every visit, instant online quotes, and a free 24-hour re-clean guarantee.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%2330CAEC' d='M12 2.2C7.2 2.2 3.8 6 3.8 10.9v12.2q2.05-2.5 4.1 0 2.05 2.5 4.1 0 2.05-2.5 4.1 0 2.05 2.5 4.1 0V10.9C20.2 6 16.8 2.2 12 2.2Z'/%3E%3Ccircle cx='9.3' cy='10.6' r='1.4' fill='%23fff'/%3E%3Ccircle cx='14.7' cy='10.6' r='1.4' fill='%23fff'/%3E%3C/svg%3E">
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
