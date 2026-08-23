# DustBusters (formerly ShineNash) — Nashville cleaning company website

Single-file marketing site for "DustBusters" (house / Airbnb / commercial cleaning, Nashville TN).
Renamed from ShineNash 2026-08-23; repo dir is still `~/shinenash`.

## Brand / logo (2026-08-23)
- Mascot: "a ghost doing the cleaning" — cute smiling ghost gripping a pink-handled mop, sparkles; inline SVG `#ghost` symbol in src/site.html (header + footer + favicon in build.py)
- Standalone assets in `logo/`: `dustbusters-mark.svg` (canonical vector mark), `dustbusters-lockup.png` (mark + wordmark), `canva-ghost-A/B/C.png` (Canva AI alternates, editable in user's Canva account: DAHTHoWPsjY / DAHTHgFolEA / DAHTHg6W18E)
- Wordmark: "Dust" ink + "Busters" blue, Baloo 2 700
- CAUTION flagged to user: "DustBuster" is a Black & Decker trademark (handheld vacs) and the ghost concept evokes Ghostbusters — name is common among local cleaners but worth a check before signage/LLC filing
- Placeholder email is now hello@dustbustersnashville.com (domain not registered)

## Layout
- `src/site.html` — the ONLY file to edit (title + CSS + markup + JS, artifact/body format; `/*__FONTS__*/` placeholder)
- `build/build.py` — assembles deliverables. Run after every edit: `python3 build/build.py`
  - `index.html` — full standalone document (fonts inlined, ~240KB, fully portable)
  - `dist/artifact.html` — Artifact-publish format (no doctype/head wrapper)
- `build/fonts/` — `inline_fonts.py` downloads + base64-inlines Google Fonts latin subsets → `fonts_inline.css` (rerun only if changing fonts)
- Published Artifact preview: https://claude.ai/code/artifact/1037c3e2-1548-4936-8231-963b3ae23cfc (republish `dist/artifact.html` to update same URL from the original conversation, or pass `url` from others)

## Design system (v3 — 2026-08-23, modeled on www.musiccitymaidservice.com at user's request: "this is the look we would like to have, theme, colors, the logic")
- Direction: playful/friendly maid-service look — bright cyan hero `#30CAEC` with floating CSS bubbles + SVG wave dividers; candy CTAs: pink `#EE046E` (primary/book), yellow `#FFDF00` w/ dark text (quote), green `#24D53C` (call/text); blue `#2097FC`/`#0170B9` accents; white sections + light-blue tint cards `#F0F8FC`; dotted-pattern stats band; sticky blue bottom CTA bar (call/text + Get a Quote + Book Online); buttons uppercase Poppins 600, 5px radius
- Fonts (embedded data URIs): Baloo 2 variable 400–800 (rounded display, ProximaSoft stand-in) + Poppins 400/500/600/700 (body). `inline_fonts.py` now emits real per-face weights (was clamping to 400–700)
- Dual theme via CSS tokens: `@media (prefers-color-scheme: dark)` + `:root[data-theme=…]` overrides; dark = deep navy `#0A1620`, same candy accents
- Conversion logic (from MCMS): dual path everywhere — instant on-screen quote (#pricing calculator) AND "Book in 60 seconds" (#book); reference site's exact colors were extracted live from their CSS (they run Astra/WP + BookingKoala)
- v2 (cobalt+lime neobrutalist) retired 8/23; v1 cream/serif remains banned

## ZenMaid (booking backend — user will subscribe)
- `#book` section renders a ZenMaid booking-form iframe when `ZENMAID_BOOKING_URL` (top of the `<script>` in src/site.html) is set; until then a fallback card shows (request-slot form + call/text)
- Once the ZenMaid account exists: ZenMaid → Settings → Booking Forms → copy the embed/share link → paste into `ZENMAID_BOOKING_URL` → rebuild. Quote-form leads should also be pointed into ZenMaid (email lead intake or manual entry)

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
