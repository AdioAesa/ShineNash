# ShineNova — website

Static site (plain HTML/CSS/JS, no build step). Open `index.html` or host the folder anywhere
(Netlify, Vercel, Cloudflare Pages, GoDaddy/cPanel).

## Pages
index.html · services.html · about.html · areas.html · faq.html · contact.html

## Before launch — things to replace
- **Phone / email / hours** — now (615) 290-1866 · info@shinenova.net · Mon–Fri 8am–5pm. To change, search for `(615) 290-1866`, `+16152901866`, and `info@shinenova.net` in all `.html` files.
- **Lead forms** — connected to Web3Forms (key in the hidden `access_key` input in `index.html` and `contact.html`); requests are emailed to info@shinenova.net.
- **Reviews (hidden)** — the Reviews page, homepage testimonials, the "4.9 / 180+ Google reviews" badge and the About-page stats were sample content, so they were removed before launch. Copies are in `.backup-reviews/` (don't upload that folder). Bring them back with real reviews only.
- **About story & stats** — `about.html` has a bracketed placeholder for the founder story.
- **Social links** — hidden (commented out in each page footer) until real Instagram/Facebook/Google profiles exist.
- **Prices** — "From $149 / $249 / $349" appear on `index.html` and `services.html`.
- **Privacy / Terms** — footer links hidden (commented out) until those pages exist.

## Brand
- Logo: `assets/logo.svg` (horizontal), `assets/mark.svg` (icon), `assets/favicon.svg`
- Colors: turquoise `#18B3AB`, dusty pink `#E4AEB3`, sage `#7EA98B`, ink `#173331`, mint `#F3FAF8`
- Fonts (Google Fonts): Bricolage Grotesque (headlines), Instrument Sans (body)
- Photos: `images/` — AI-generated, 1600px JPEGs
- Hero video: `video/hero-1080.mp4` (desktop) and `video/hero-720.mp4` (phones), H.264. Plays once (messy to clean) and holds on the clean room. `hero-before.jpg` / `hero-after.jpg` are its first and last frames; visitors with reduced motion see the "after" frame.
- `.backup-v2/` holds a rejected redesign (Archivo font, full-width video hero). `images/svc-*.jpg`, `images/room-*.jpg` and `assets/logo-light.svg` belong to it and are unused. Don't deploy `.backup-v1/` or `.backup-v2/`.
