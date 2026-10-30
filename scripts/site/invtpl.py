import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from common import *
exec(open(os.path.dirname(__file__)+"/pages.py").read().split("# HOME")[0].split("os.chdir(sys.argv[1])")[1])
os.chdir(sys.argv[1])
DL='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'
U="https://cleverloopdigital.com/templates/contractor-invoice-template.html"
T="Free Contractor Invoice Template (Excel &amp; Google Sheets)"
D="Download a free contractor invoice template for Excel and Google Sheets: line items, change orders, sales tax, deposit received and balance due, all calculated automatically. No sign-up."
faq=[("What should a contractor invoice include?","Your business name, contact details and license number if your state requires one; the word Invoice, an invoice number, invoice date and due date; the customer and job address; the work completed as line items, including any signed change orders; subtotal, sales tax, total, payments already received and the balance due; and how to pay."),
("How do I show the deposit on the final invoice?","List the full job as line items so the invoice total matches the agreed price plus any change orders, then subtract the deposit already received on its own line. The template does this for you and shows the balance due."),
("What payment terms should a contractor use?","Common terms are due on receipt or net 15 / net 30 (payment due 15 or 30 days after the invoice date). Use what your contract says, put the due date on the invoice, and check your state's rules before adding late fees."),
("Is this invoice template really free?","Yes. Download the .xlsx file, open it in Excel or import it into Google Sheets (File > Import > Upload) and replace the yellow example cells with your own details. No sign-up.")]
ld='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['+",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'%(q,a) for q,a in faq)+']}'
bc='{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://cleverloopdigital.com/"}, {"@type": "ListItem", "position": 2, "name": "Contractor Invoice Template", "item": "%s"}]}'%U
og=f'<meta property="og:type" content="website"><meta property="og:site_name" content="Clever Loop Digital"><meta property="og:title" content="{T}"><meta property="og:description" content="{D}"><meta property="og:url" content="{U}"><meta property="og:image" content="https://cleverloopdigital.com/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">'
rows=[("Labor","16 hr","$1,200.00"),("Materials (see list)","1 lot","$1,200.00"),("Equipment rental","1 day","$150.00"),("Disposal / dump fee","1 load","$95.00"),("Change order #1 (signed)","1","$822.00")]
tr="".join(f'<tr class="in"><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in rows)
body=f'''<section class="phead"><div class="wide promo">
<div><p class="crumbs"><a href="../index.html">Home</a> / <span>Contractor Invoice Template</span></p>
<span class="pill">Free download &middot; Excel &amp; Google Sheets</span>
<h1 style="margin-top:14px">Free Contractor Invoice Template</h1>
<p class="lede">Bill the finished job in minutes: line items, signed change orders, sales tax, the deposit you already took and the balance due. Every total calculates itself. No sign-up.</p>
<p style="margin-top:22px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-acc" href="contractor-invoice-template.xlsx" download>{DL} Download the template (.xlsx)</a><a class="btn btn-ghost" href="contractor-estimate-template.html">Need the estimate first?</a></p></div>
<div class="sheet" role="img" aria-label="Preview of the invoice template: 5 line items, invoice total $3,467.00, deposit received $793.50, balance due $2,673.50">
<div class="bar-top"><i></i><i></i><i></i></div>
<table>
<tr class="tot"><td>[Your Business Name]</td><td></td><td>INVOICE #2001</td></tr>
<tr class="h"><td>Item</td><td>Qty</td><td>Amount</td></tr>
{tr}
<tr><td>Sales tax (0%)</td><td></td><td>$0.00</td></tr>
<tr><td>Invoice total</td><td></td><td>$3,467.00</td></tr>
<tr><td>Less deposit received</td><td></td><td>&minus;$793.50</td></tr>
<tr class="tot"><td>Balance due</td><td></td><td>$2,673.50</td></tr>
</table></div>
</div></section>
<main class="w page">
<p class="card" style="margin-top:0">Rather fill it in online? Use the free <a href="../tools/invoice-maker.html">invoice &amp; estimate maker</a>: type, then save as PDF. No spreadsheet needed.</p>
<h2>What is in the template</h2>
<ul>
<li>Header for your business name, address, phone, email and license number</li>
<li>Invoice number, invoice date, due date and the estimate number it relates to</li>
<li>Bill-to customer, job address and a line for the work completed</li>
<li>12 line-item rows (quantity &times; unit price), with room for signed change orders</li>
<li>Subtotal, sales tax on the taxable amount, invoice total, deposit and other payments received, and the balance due, all automatic</li>
<li>Editable payment instructions; prints on one page</li>
</ul>
<h2>How to invoice a finished job</h2>
<ol>
<li><strong>Start from the signed estimate.</strong> Copy the line items from your <a href="contractor-estimate-template.html">estimate</a> so the invoice matches what the customer agreed to.</li>
<li><strong>Add every signed change order.</strong> Extra work goes on its own line with the price the customer signed. See <a href="../guides/how-to-price-a-change-order.html">how to price a change order</a>.</li>
<li><strong>Apply sales tax only where it applies.</strong> Enter the taxable amount and your rate; rules differ by state and by trade. The <a href="../tools/job-sales-tax-calculator.html">job sales tax calculator</a> shows the math.</li>
<li><strong>Subtract what you already received.</strong> Enter the deposit and any progress payments; the template shows the balance due.</li>
<li><strong>Set a clear due date and how to pay.</strong> If you accept cards, check what the fee costs you with the <a href="../tools/invoice-processing-fee-calculator.html">invoice processing fee calculator</a>.</li>
<li><strong>Follow up on time.</strong> If your contract allows a late fee, the <a href="../tools/late-payment-fee-calculator.html">late payment fee calculator</a> estimates it.</li>
</ol>
<h2>Worked example</h2>
<table>
<tr><td>Original estimate (labor, materials, rental, disposal)</td><td>$2,645.00</td></tr>
<tr><td>Change order #1 (signed)</td><td>$822.00</td></tr>
<tr><th>Invoice total (no sales tax)</th><th>$3,467.00</th></tr>
<tr><td>Less deposit received (30% of $2,645)</td><td>&minus;$793.50</td></tr>
<tr><th>Balance due</th><th>$2,673.50</th></tr>
</table>
<h2>Frequently asked questions</h2>
<div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)}</div>
<div class="card promo-card">
<h2>Make sure the price was right before you bill it</h2>
<p>The <a href="../ventures/sheets.html">Contractor Quote &amp; Margin Sheet</a> prices each job from your costs and target margin, and includes this invoice and the estimate as tabs, plus hourly rate, change order and job profit log tabs.</p>
</div>
<p><small>Template for general business use. Check your state's rules on invoicing, sales tax and late fees. Not legal, tax or accounting advice.</small></p>
</main>'''
page("templates/contractor-invoice-template.html","../","",T+" | Clever Loop Digital",D,"templates/contractor-invoice-template.html",body,
 extra_head=f'\n{og}\n<script type="application/ld+json">{bc}</script>\n<script type="application/ld+json">{ld}</script>')
print("ok")
