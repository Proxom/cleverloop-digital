# Site build scripts (run from repo root)
- `python3 scripts/site/pages.py public` regenerates index.html, tools/index.html, guides/index.html, ventures/sheets.html (header/footer/tiles come from common.py).
- `python3 scripts/site/tpl.py public` regenerates templates/contractor-estimate-template.html.
- After regenerating, re-add Open Graph + BreadcrumbList tags: the generator pages need them (see git history of run 47 for the tagging snippet) — check `grep -L og:title public/**/*.html`.
- Product files: `toolkit.py`, `estimate.py` (need openpyxl in a venv; run from scripts/site).
- New tool/guide: add it to TOOLS/GUIDES in common.py, rerun pages.py, add to sitemap.xml.
