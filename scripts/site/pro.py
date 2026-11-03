# Generates public/pro.html: the Estimate & Invoice Maker Pro sales page.
# Run from repo root: python3 scripts/site/pro.py public && python3 scripts/site/seo_tags.py public
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import header, footer, headlinks

os.chdir(sys.argv[1] if len(sys.argv) > 1 else "public")
ARROW = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<span class="pr-y" aria-label="Included">&#10003;</span>'
DASH = '<span class="pr-n" aria-label="Not included">&ndash;</span>'
BUY = f'<a class="btn btn-acc" href="#buy" data-demand-click="maker-pro" data-root="">Get Pro &middot; $9/month {ARROW}</a>'

FEATURES = [
 ("Only your name on the PDF", "Free PDFs end with a small &ldquo;Made with&rdquo; line. Pro removes it, so the estimate your customer reads carries your business and nothing else."),
 ("Your business profile, filled in every time", "Name, license number, phone, email, address, default tax rate, deposit and payment terms, plus your logo, saved once and placed on every new estimate and invoice."),
 ("Unpaid invoice tracker with reminder text", "See which invoices are unpaid and how many days late each one is. One click copies a polite, ready-to-send reminder with the amount and invoice number, for your email or text app."),
 ("Backup and move to a new device", "Download all your customers, saved prices and documents as one file and restore them on a new phone, laptop or browser. Your data still never sits on our server."),
 ("Help by email", "Questions about the maker or a document go to the front of the queue at hello@cleverloopdigital.com."),
]
ROWS = [
 ("Unlimited estimates and invoices", CHECK, CHECK),
 ("Your logo, PDF download, sales tax and deposit", CHECK, CHECK),
 ("18 trade starting points and price calculators", CHECK, CHECK),
 ("Saved customers, saved prices, document history (this device)", CHECK, CHECK),
 ("&ldquo;Made with&rdquo; line at the bottom of the PDF", "Yes", "Removed"),
 ("Business profile and logo filled in automatically", DASH, CHECK),
 ("Unpaid invoice tracker and reminder text", DASH, CHECK),
 ("Backup file to move everything to another device", DASH, CHECK),
 ("Priority email help", DASH, CHECK),
 ("Sign-up or account needed", "No", "No"),
 ("Price", "$0", "$9 a month"),
]
FAQ = [
 ("Can I buy Pro today?", "Not yet. Checkout opens soon. We are counting how many contractors click Get Pro before we switch payments on, so every click helps open it sooner. The free maker works fully in the meantime, with no sign-up, and you can preview the Pro tools at the bottom of the maker: it already counts your unpaid invoices from the ones you save."),
 ("Will the free version stay free?", "Yes. Unlimited estimates and invoices, your logo, PDF download, saved customers, saved prices and document history stay free. Pro adds the extras listed on this page; nothing that is free today will be moved behind Pro."),
 ("How will Pro work without an account?", "Your documents stay in your own browser, as they do now. After checkout you receive a Pro activation link by email; opening it switches on Pro in that browser. Use the backup file to bring your data and Pro to another device."),
 ("How do I cancel?", "Cancel any time from the link in your receipt email, or email hello@cleverloopdigital.com. Pro keeps working until the end of the month you paid for, and you are not charged again. Your documents stay on your device either way."),
 ("What is the refund policy?", "If Pro is not right for you, email us within 14 days of your first payment for a full refund, no questions asked."),
 ("Is sales tax added?", "Prices are in US dollars. Where the law requires it, sales tax or VAT is calculated and shown at checkout before you pay."),
 ("Where is my data stored?", "Only in your browser on your device. Nothing you type, including customer names, prices and your logo, is sent to our server. The only data we will hold for Pro is your email address and payment record, kept by the payment provider."),
]

def faq_ld(items):
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a.replace("&ldquo;", '"').replace("&rdquo;", '"')}} for q, a in items]})

product_ld = json.dumps({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Estimate & Invoice Maker Pro", "url": "https://cleverloopdigital.com/pro.html", "applicationCategory": "BusinessApplication", "operatingSystem": "Any (web browser)", "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD"}, {"@type": "Offer", "name": "Pro", "price": "9.00", "priceCurrency": "USD", "availability": "https://schema.org/PreOrder"}]})

CSS = """<style>
.pr-hero{padding:56px 0 28px}.pr-hero h1{max-width:20ch}
.pr-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:24px 0}
.pr-card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:20px 20px 16px}
.pr-card h3{margin:0 0 6px;font-size:1.08rem}.pr-card p{margin:0;color:var(--mut)}
table.pr-t{border-collapse:collapse;width:100%;background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:16px 0;font-size:.97rem}
table.pr-t th,table.pr-t td{padding:11px 14px;border-bottom:1px solid var(--line);text-align:left}
table.pr-t td+td,table.pr-t th+th{text-align:center;width:22%}
table.pr-t tr:last-child>*{border-bottom:0}table.pr-t thead th{background:var(--bg,#f6f7f9)}
.pr-y{color:#0f8a5f;font-weight:800}.pr-n{color:var(--mut)}
.pr-guar{display:flex;gap:16px;align-items:flex-start;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:20px;margin:24px 0}
.pr-guar b{display:grid;place-items:center;flex:0 0 46px;height:46px;border-radius:14px;background:#e3f6ee;color:#0f8a5f;font-size:1.4rem}
.pr-cta{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin:20px 0}
@media (max-width:560px){table.pr-t{font-size:.9rem}table.pr-t th,table.pr-t td{padding:9px 8px}}
</style>"""

rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in ROWS)
cards = "".join(f'<div class="pr-card"><h3>{t}</h3><p>{d}</p></div>' for t, d in FEATURES)
faq = '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ) + "</div>"

body = f'''<section class="phead pr-hero"><div class="w"><p class="crumbs"><a href="index.html">Home</a> / <a href="maker/">Estimate &amp; Invoice Maker</a> / <span>Pro</span></p>
<p class="eyebrow" data-demand-view="maker-pro">Estimate &amp; Invoice Maker Pro</p>
<h1>Estimates that carry only your name. $9 a month.</h1>
<p class="lede">The free maker already does unlimited estimates and invoices. Pro is for contractors who send them every week: your business details filled in automatically, no &ldquo;Made with&rdquo; line on the PDF, a list of unpaid invoices with reminder text, and a backup you can move to any device. Still no sign-up, still no data on our server.</p>
<div class="pr-cta">{BUY}<a href="maker/">Keep using it free</a></div>
<p class="muted" style="color:var(--mut);font-size:.92rem;margin:0">Checkout opens soon. Cancel any time. 14-day money-back guarantee.</p></div></section>
<main class="w page">
<h2>What Pro adds</h2>
<div class="pr-grid">{cards}</div>
<h2>Free vs Pro</h2>
<table class="pr-t"><thead><tr><th scope="col">Feature</th><th scope="col">Free</th><th scope="col">Pro</th></tr></thead><tbody>{rows}</tbody></table>
<h2>Why $9 is enough</h2>
<p>Popular contractor estimate and field-service apps list plans from about $10 to $49 a month, and their cheapest plans often cap you at a handful of documents a month (published pricing pages, checked November 2026). They run a cloud account for every customer. We do not: your documents live in your browser, so there is no server bill to pass on to you.</p>
<p>That also means honest limits. Pro does not sync live between devices (use the backup file), does not take card payments for you, and does not schedule crews. If you need those, a full field-service app is the better buy.</p>
<div class="pr-guar"><b aria-hidden="true">&#10003;</b><div><h3 style="margin:0 0 4px">14-day money-back guarantee</h3><p style="margin:0">Email <a href="mailto:hello@cleverloopdigital.com">hello@cleverloopdigital.com</a> within 14 days of your first payment and we refund it in full. Cancel any time after that; you keep Pro until the end of the paid month.</p></div></div>
<h2>Frequently asked questions</h2>
{faq}
<h2 id="buy">Get Pro</h2>
<p>$9 a month in US dollars, cancel any time. Checkout opens soon: we are measuring interest first, and every click counts toward opening it.</p>
<div class="pr-cta">{BUY}<a href="maker/">Open the free maker</a></div>
<p><small>Built and sold by Erkan Bedir, trading as Clever Loop Digital, United Kingdom (<a href="about.html">about us</a>). Pro is a software tool, not accounting, tax or legal advice. See the <a href="terms.html">terms</a> and <a href="privacy.html">privacy policy</a>.</small></p>
</main>'''

open("pro.html", "w").write(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Estimate &amp; Invoice Maker Pro: $9/month, No Sign-Up | Clever Loop Digital</title>
<meta name="description" content="Pro for the free contractor estimate and invoice maker: no branding line on PDFs, business profile filled in automatically, unpaid invoice reminders, device backup. $9/month, cancel any time, 14-day refund.">
<link rel="canonical" href="https://cleverloopdigital.com/pro.html">
{headlinks("")}
<link rel="stylesheet" href="site-v3.css"><link rel="stylesheet" href="app-v1.css">{CSS}
<script type="application/ld+json">{product_ld}</script>
<script type="application/ld+json">{faq_ld(FAQ)}</script>
<script src="js/demand.js" defer></script>
</head><body>
{header("", "pro")}
{body}
{footer("")}
</body></html>
''')
print("pro.html written")
