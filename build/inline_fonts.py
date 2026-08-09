#!/usr/bin/env python3
"""Inline latin-subset woff2 fonts as base64 — one @font-face per unique file (variable fonts)."""
import base64, re, sys, urllib.request, pathlib

src = pathlib.Path(__file__).parent / "fonts" / "fonts.css"
out = pathlib.Path(__file__).parent / "fonts" / "fonts_inline.css"

css = src.read_text()
blocks = re.findall(r"/\* ([a-z0-9-]+) \*/\s*(@font-face\s*\{[^}]*\})", css)

seen: dict[str, dict] = {}
order = []
for subset, block in blocks:
    if subset != "latin":
        continue
    url = re.search(r"url\((https://[^)]+)\)", block).group(1)
    fam = re.search(r"font-family:\s*'([^']+)'", block).group(1)
    style = re.search(r"font-style:\s*(\w+)", block).group(1)
    weights = [int(w) for w in re.search(r"font-weight:\s*([\d ]+);", block).group(1).split()]
    weight_lo, weight_hi = min(weights), max(weights)
    if url not in seen:
        data = urllib.request.urlopen(url).read()
        print(f"fetched {fam} {style} {len(data)//1024}KB", file=sys.stderr)
        seen[url] = dict(fam=fam, style=style, lo=weight_lo, hi=weight_hi,
                         b64=base64.b64encode(data).decode())
        order.append(url)
    else:
        seen[url]["lo"] = min(seen[url]["lo"], weight_lo)
        seen[url]["hi"] = max(seen[url]["hi"], weight_hi)

faces = []
for url in order:
    f = seen[url]
    faces.append(
        "@font-face{font-family:'%s';font-style:%s;font-weight:%d %d;font-display:swap;"
        "src:url(data:font/woff2;base64,%s) format('woff2');}"
        % (f["fam"], f["style"], min(f["lo"], 400), max(f["hi"], 700), f["b64"])
    )

out.write_text("\n".join(faces))
print(f"wrote {out} ({out.stat().st_size//1024}KB, {len(faces)} faces)")
