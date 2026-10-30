import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from common import *
exec(open(os.path.dirname(__file__)+"/pages.py").read().split("# HOME")[0].split("os.chdir(sys.argv[1])")[1])
os.chdir(sys.argv[1])
DL='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'
faq=[("What is the difference between an estimate, a quote and a bid?","Usage varies by trade and state, but an estimate is usually an approximate price that can change if the job changes, a quote is a fixed price for a defined scope, and a bid is a price submitted to compete for a project. Label your document clearly and say what happens if the scope changes."),
("What should a contractor estimate include?","Your business name, contact details and license number if your state requires one; the customer and job address; a clear description of the work; line items with quantity, unit and price; subtotal, any sales tax, total, deposit and balance; how long the price is valid; payment terms; and a signature line."),
("Is this estimate template really free?","Yes. Download the .xlsx file, open it in Excel or import it into Google Sheets (File > Import > Upload) and replace the yellow example cells with your own details. No sign-up."),
("How do I price the line items?","Price each job from your real costs and the margin you want, not from a guess. The free job price calculator does this in seconds: cost divided by (1 minus your target margin).")]
ld='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['+",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'%(q,a) for q,a in faq)+']}'
rows=[("Labor","16","hr","$75.00","$1,200.00"),("Materials (see list)","1","lot","$1,200.00","$1,200.00"),("Equipment rental","1","day","$150.00","$150.00"),("Disposal / dump fee","1","load","$95.00","$95.00")]
tr="".join(f'<tr class="in"><td>{a}</td><td>{b} {c}</td><td>{e}</td></tr>' for a,b,c,d,e in rows)
body=f'''<section class="phead"><div class="wide promo">
<div><p class="crumbs"><a href="../index.html">Home</a> / <span>Contractor Estimate Template</span></p>
<span class="pill">Free download &middot; Excel &amp; Google Sheets</span>
<h1 style="margin-top:14px">Free Contractor Estimate Template</h1>
<p class="lede">A clean, professional estimate you can send today: line items, sales tax, deposit, balance, terms and a signature line. Totals calculate themselves. No sign-up.</p>
<p style="margin-top:22px;display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-acc" href="contractor-estimate-template.xlsx" download>{DL} Download the template (.xlsx)</a><a class="btn btn-ghost" href="../tools/job-price-calculator.html">Price the job first</a></p></div>
<div class="sheet" role="img" aria-label="Preview of the estimate template: 4 line items, subtotal $2,645.00, 30% deposit $793.50, balance $1,851.50">
<div class="bar-top"><i></i><i></i><i></i></div>
<table>
<tr class="tot"><td>[Your Business Name]</td><td></td><td>ESTIMATE #1001</td></tr>
<tr class="h"><td>Item</td><td>Qty</td><td>Amount</td></tr>
{tr}
<tr><td>Subtotal</td><td></td><td>$2,645.00</td></tr>
<tr><td>Sales tax (0%)</td><td></td><td>$0.00</td></tr>
<tr class="tot"><td>Total</td><td></td><td>$2,645.00</td></tr>
<tr><td>Deposit due to start (30%)</td><td></td><td>$793.50</td></tr>
<tr><td>Balance on completion</td><td></td><td>$1,851.50</td></tr>
</table></div>
</div></section>
<main class="w page">
<h2>What is in the template</h2>
<ul>
<li>Header for your business name, address, phone, email and license number</li>
<li>Estimate number, date and &ldquo;valid until&rdquo; date</li>
<li>Customer, job address and a short job description</li>
<li>12 line-item rows: quantity &times; unit price calculates each amount</li>
<li>Subtotal, sales tax on the taxable amount, total, deposit and balance, all automatic</li>
<li>Editable terms and a customer signature line; prints on one page</li>
</ul>
<h2>How to fill out a contractor estimate</h2>
<ol>
<li><strong>Add your details once.</strong> Replace the yellow header cells with your business name, contact details and license number, then save it as your master copy.</li>
<li><strong>Describe the job in plain words.</strong> One or two sentences the customer will recognise: &ldquo;Replace 180 sq ft of rotted deck boards and railings.&rdquo;</li>
<li><strong>List the work as line items.</strong> Labor, materials, rentals, disposal and permits on separate lines make the price easier to accept and to change later.</li>
<li><strong>Price from cost and margin.</strong> Work out the price with the <a href="../tools/job-price-calculator.html">job price calculator</a> so the total carries the margin you want. See <a href="../guides/how-to-price-a-contractor-job.html">how to price a contractor job</a>.</li>
<li><strong>Set the deposit and the expiry date.</strong> The template splits the total into the deposit and the balance. A &ldquo;valid until&rdquo; date protects you when material prices move.</li>
<li><strong>Get it signed.</strong> Anything added later goes on a signed change order; see <a href="../guides/how-to-price-a-change-order.html">how to price a change order</a>. When the job is done, bill it with the free <a href="contractor-invoice-template.html">contractor invoice template</a>.</li>
</ol>
<h2>Worked example</h2>
<table>
<tr><td>Labor: 16 h &times; $75</td><td>$1,200.00</td></tr>
<tr><td>Materials</td><td>$1,200.00</td></tr>
<tr><td>Equipment rental: 1 day</td><td>$150.00</td></tr>
<tr><td>Disposal: 1 load</td><td>$95.00</td></tr>
<tr><th>Total (no sales tax)</th><th>$2,645.00</th></tr>
<tr><td>Deposit: 30% of $2,645</td><td>$793.50</td></tr>
<tr><td>Balance on completion</td><td>$1,851.50</td></tr>
</table>
<h2>Frequently asked questions</h2>
<div class="faq">{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faq)}</div>
<div class="card promo-card">
<h2>Want the price worked out for you too?</h2>
<p>The <a href="../ventures/sheets.html">Contractor Quote &amp; Margin Sheet</a> prices each job from your costs and target margin, and includes this estimate as a tab, plus hourly rate, change order and job profit log tabs.</p>
</div>
<p><small>Template for general business use. Check your state's rules for required wording on estimates and contracts. Not legal, tax or accounting advice.</small></p>
</main>'''
page("templates/contractor-estimate-template.html","../","", "Free Contractor Estimate Template (Excel &amp; Google Sheets) | Clever Loop Digital",
 "Download a free contractor estimate template for Excel and Google Sheets: line items, sales tax, deposit, balance, terms and signature line. Totals calculate automatically. No sign-up.",
 "templates/contractor-estimate-template.html",body,extra_head=f'\n<script type="application/ld+json">{ld}</script>')
print("ok")
