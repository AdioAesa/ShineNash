# ShineNova ✦

Marketing website for **ShineNova** — flat-rate house, Airbnb, and office cleaning in Nashville, TN.

**Live preview:** the site is a single self-contained `index.html` (fonts embedded, no external requests) — open it locally or host it on any static host.

## Highlights

- Instant on-screen quote calculator (beds / baths / sq ft / frequency → flat rate)
- The **Encore Guarantee** — free 24-hour re-clean
- 55-Point Shine List with per-room tabs
- "Your home is not a gig" comparison vs. gig cleaning apps
- Nashville neighborhoods + Middle TN suburbs service-area coverage
- Light + dark theme, fully responsive, zero dependencies

## Design

Bold DTC direction: electric cobalt `#2038EE` + acid lime `#D9F64F`, Bricolage Grotesque display type, Instrument Sans body, hard offset shadows, sticker cards, scrolling marquee.

## Development

Edit `src/site.html` only, then rebuild:

```bash
python3 build/build.py        # regenerates index.html and dist/artifact.html
```

Fonts are inlined as base64 data URIs; to change fonts, update the Google Fonts URL fetch in `build/fonts/` and run `python3 build/inline_fonts.py` first.

## Before launch

- Replace placeholder phone `(615) 555-0199` and `hello@shinenova.com`
- Replace aspirational stats/testimonials with real ones
- Wire the booking form to a backend (currently demo-only)
- Calibrate calculator pricing in the `quote()` function in `src/site.html`
