# ShineNova — Nashville house-cleaning website

Static six-page site (plain HTML/CSS/JS, no build step). RESIDENTIAL house cleaning only, Nashville TN.
Repo dir is still `~/shinenash` (GitHub AdioAesa/ShineNash); Vercel project `shine-nash`; production domain www.shinenova.net.
Naming history: ShineNash → DustBusters (8/23) → **ShineNova (final, 2026-08-26)**.

## 2026-10-11 — site replaced wholesale with Hilal's launch build
- Source: https://github.com/hilalgoc2-beep/shinenova-website (commit f2e2c84, "ShineNova website, ready for launch"), added here as git remote `hilal`. Local clone at `~/shinenova-website`; browsable copy at `C:\Users\ademirci\claude-work\shinenova-website\`.
- User instruction: "make it exactly the same, 100%" — tree is byte-identical to hilal/main except `vercel.json`, `CLAUDE.md`, `.gitignore`.
- Vercel is connected to the GitHub repo: **a push to `main` auto-deploys production** (no `vercel deploy` needed; the CLI deploy is blocked by the permission classifier anyway).
- Previous single-file build (src/site.html + build/build.py, candy cyan/pink design, ZenMaid hook, quote calculator) is gone — see git history before 13223fc if it's ever needed.

## Pages / layout
index.html · services.html · about.html · areas.html · faq.html · contact.html · `css/style.css` · `js/main.js` · `assets/` (logo.svg, mark.svg, favicon.svg) · `images/` (AI-generated 1600px JPEGs) · `video/hero-1080.mp4` + `hero-720.mp4` (plays once messy→clean; `hero-before/after.jpg` frames).
`images/svc-*.jpg`, `images/room-*.jpg`, `assets/logo-light.svg` belong to a rejected redesign and are unused.

## Brand (Hilal's)
- Colors: turquoise `#18B3AB`, dusty pink `#E4AEB3`, sage `#7EA98B`, ink `#173331`, mint `#F3FAF8`
- Fonts (Google Fonts CDN): Bricolage Grotesque (headlines), Instrument Sans (body)

## Contact / forms
- Phone (615) 290-1866 · email **info@shinenova.net** · Mon–Fri 8am–5pm (search all .html to change; previous site used hilal@shinenova.net)
- Lead forms → Web3Forms (hidden `access_key` input in index.html + contact.html), delivered to info@shinenova.net

## Known content notes
- Copy claims "insured & bonded" and "W-2 employees" (index, about, faq). The earlier rule was NO insurance/W-2 claims (no insurance at launch, 2026-09-10). User chose to ship Hilal's copy verbatim on 2026-10-11 — flag again if asked to edit.
- FAQ says no Airbnbs/offices "yet" — consistent with residential-only.
- Still placeholder per README: founder story in about.html, prices "From $149/$249/$349", reviews + social + privacy/terms links hidden until real.

## Hosting
- `vercel.json` only holds redirects: shine-nash.vercel.app and apex shinenova.net → https://www.shinenova.net
- `.vercel/` (local link) and `.env.local` are git-ignored
