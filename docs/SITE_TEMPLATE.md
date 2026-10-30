# Site template (30 Oct 2026 redesign)

New pages must reuse the shared design so the site stays consistent:
- `<head>`: `<link rel="icon" href="../favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#0d2240">` + `../style.css`. No inline `<style>` needed for forms/tables.
- Header/footer: copy them exactly from an existing page in the same folder (e.g. `public/guides/how-to-price-a-change-order.html`). Set `aria-current="page"` on the current nav link.
- Title band: `<section class="phead"><div class="w"><p class="crumbs">Home / Section / Page</p><p class="eyebrow">Guide | Free calculator</p><h1>..</h1><p class="lede">..</p></div></section>` then `<main class="w page">`.
- Calculator result: `<div class="card result" aria-live="polite"><table id="out"></table></div>`; the key row uses `class='big'`.
- Product call-out at the end of guides: `<div class="card promo-card">`.
- When adding a tool or guide, also add a tile on `index.html`, `tools/index.html` or `guides/index.html`, and add it to `sitemap.xml`.
