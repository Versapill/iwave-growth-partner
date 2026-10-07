# iWave Digital website

Marketing site for [iWave Digital](https://www.iwave.digital), the AI growth partner for fast-moving B2B companies.

It's a static site: plain HTML, a compiled Tailwind stylesheet and a little JavaScript. No framework or server is needed, so it can be hosted on GitHub Pages, Netlify, Vercel, Cloudflare Pages or any static host.

## Structure

```
index.html                Homepage
services/*.html           Service pages (generated — see below)
404.html                  Not-found page (uses root paths, so serve the site from the domain root)
assets/
  tailwind.css            Compiled Tailwind styles (generated — see below)
  site.css                Custom styles: marquee, testimonials, team gallery, services list, etc.
  site.js                 Shared header, mobile menu and footer behaviour
  logos/ marks/ team/ testimonials/ case-studies/   Optimised images
  og-image.jpg            Social share image (1200×630)
favicon.ico, favicon-*.png, apple-touch-icon.png, site.webmanifest
robots.txt, sitemap.xml
tools/build_services.py   Generates the service pages
tailwind.config.js        Tailwind theme (brand colours, fonts)
```

## Editing service pages

All six service pages share one template. Their content (copy, stats, case studies, FAQs) lives in `tools/build_services.py`. Edit it there, then regenerate:

```bash
python3 tools/build_services.py
```

The booking link, contact email and live domain are set at the top of that file. The homepage (`index.html`) is edited directly.

## Rebuilding the CSS

After adding or changing Tailwind classes in any HTML file or in the page generator, rebuild the stylesheet:

```bash
npx tailwindcss@3.4.17 -i tools/tailwind.input.css -o assets/tailwind.css --minify
```

## Before going live

- The canonical URLs, sitemap and share tags assume the site is served at `https://www.iwave.digital`. If the domain differs, update `SITE` in `tools/build_services.py`, the URLs in `index.html`, `robots.txt` and `sitemap.xml`, then regenerate.
- Update `<lastmod>` dates in `sitemap.xml` when pages change.
