# Site build scripts (run from repo root)
- `python3 scripts/site/pages.py public` regenerates index.html, tools/index.html, guides/index.html, ventures/sheets.html (header/footer/tiles come from common.py).
- `python3 scripts/site/tpl.py public` regenerates templates/contractor-estimate-template.html.
- After regenerating, run `python3 scripts/site/seo_tags.py public` (generators drop Open Graph + BreadcrumbList tags); check `grep -L og:title public/**/*.html`.
- Product files: `toolkit.py`, `estimate.py` (need openpyxl in a venv; run from scripts/site).
- New tool/guide: add it to TOOLS/GUIDES in common.py, rerun pages.py, add to sitemap.xml.
- Page-view counter: every page loads `/js/pv.js` (cookie-free; sends path + referrer domain to `public/api/pv.php`, which stores only daily totals in `<repo root>/data/pv/YYYY-MM.json`, git-ignored). `seo_tags.py` adds the tag automatically (via `pv_tag.py`); new hand-made pages get it on the next `seo_tags.py` run. Report: `GET https://cleverloopdigital.com/api/pv.php?days=7` (JSON: humanViews, botViews, perDay, topPages, topReferrers).
- Pro sales page: `python3 scripts/site/pro.py public` writes public/pro.html (then run seo_tags.py). Footer and maker Pro cards link to it.
