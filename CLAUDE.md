# ShineNash — Nashville cleaning company website

Single-file marketing site for "ShineNash" (house / Airbnb / commercial cleaning, Nashville TN).

## Layout
- `src/site.html` — the ONLY file to edit (title + CSS + markup + JS, artifact/body format; `/*__FONTS__*/` placeholder)
- `build/build.py` — assembles deliverables. Run after every edit: `python3 build/build.py`
  - `index.html` — full standalone document (fonts inlined, ~240KB, fully portable)
  - `dist/artifact.html` — Artifact-publish format (no doctype/head wrapper)
- `build/fonts/` — `inline_fonts.py` downloads + base64-inlines Google Fonts latin subsets → `fonts_inline.css` (rerun only if changing fonts)
- Published Artifact preview: https://claude.ai/code/artifact/1037c3e2-1548-4936-8231-963b3ae23cfc (republish `dist/artifact.html` to update same URL from the original conversation, or pass `url` from others)

## Design system (v2 — 2026-08-09, replaced v1 cream/serif look at user's request: "be unique, bold, up to date")
- Direction: bold DTC / neobrutalist-lite — electric cobalt `#2038EE` + acid lime `#D9F64F` on cool white `#F3F5FC`; 2px ink strokes, hard offset shadows (`4px 4px 0`), sticker cards with slight rotation, tilted scrolling marquee tape, spinning asterisk motif (`#sprk` symbol)
- Fonts (embedded data URIs): Bricolage Grotesque variable (display, wght 800) + Instrument Sans variable (body)
- Dual theme via CSS tokens: `@media (prefers-color-scheme: dark)` + `:root[data-theme=…]` overrides; dark = near-black navy `#080B18`, brighter cobalt, same lime
- USER FEEDBACK: do NOT use the cream-paper + serif + gold/green "editorial" aesthetic — user explicitly rejected it as the recognizable AI default

## Brand decisions (from Aug 2026 competitive research)
- **Encore Guarantee** = free 24-hr re-clean (Nashville music tie-in; every top competitor has a named guarantee)
- **Transparent flat-rate pricing + on-screen instant quote calculator** — main differentiator; most Nashville competitors hide prices
- **"Your home is not a gig"** enemy positioning vs gig apps (W-2, same-trio crew, $2M insured)
- **55-Point Shine List** checklist (transparency artifact), Airbnb/STR turnovers flagged as Nashville specialty
- Service areas = canonical set: East Nashville, Green Hills, Gulch, Germantown, 12 South… + Brentwood, Franklin, Hendersonville, Mt. Juliet, Murfreesboro

## Placeholders to replace before launch
- Phone `(615) 555-0199`, email `hello@shinenash.com`
- Stats (2,317 homes, 317 reviews, 4.9★) and all testimonials are ASPIRATIONAL COPY — must be made truthful before going live
- Quote form is demo-only (client-side success state, submits nowhere) — wire to a backend/formspree/CRM
- Calculator pricing model in `quote()`: base 95 + 24/bed + 22/bath + sqft adder; deep ×1.65, move ×1.95; airbnb 69+18/bed+14/bath; freq discounts 20/15/10%
