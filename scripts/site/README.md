# Site build scripts (run from repo root)
- `python3 scripts/site/pages.py public` regenerates index.html, tools/index.html, guides/index.html, ventures/sheets.html (header/footer/tiles come from common.py).
- `python3 scripts/site/tpl.py public` regenerates templates/contractor-estimate-template.html.
- After regenerating, run `python3 scripts/site/seo_tags.py public` (generators drop Open Graph + BreadcrumbList tags); check `grep -L og:title public/**/*.html`.
- Product files: `toolkit.py`, `estimate.py` (need openpyxl in a venv; run from scripts/site).
- New tool/guide: add it to TOOLS/GUIDES in common.py, rerun pages.py, add to sitemap.xml.
