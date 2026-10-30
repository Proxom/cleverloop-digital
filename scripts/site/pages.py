import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from common import *
os.chdir(sys.argv[1])
def page(path,p,cur,title,desc,canon,body,extra_head=""):
    open(path,"w").write(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cleverloopdigital.com/{canon}">
{headlinks(p)}
<link rel="stylesheet" href="{p}site-v2.css">{extra_head}
</head><body>
{header(p,cur)}
{body}
{footer(p)}
</body></html>
''')
ARROW='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
SHEET=lambda p:'''<div class="sheet" role="img" aria-label="Example of the Contractor Quote and Margin Sheet: $2,620.80 total cost at a 30% margin gives a $3,744.00 quote">
<div class="bar-top"><i></i><i></i><i></i></div>
<table>
<tr class="h"><td>Inputs</td><td></td></tr>
<tr class="in"><td>Materials</td><td>$1,200</td></tr>
<tr class="in"><td>Labor: 24 h &times; $35</td><td>$840</td></tr>
<tr class="in"><td>Subcontractor / rental</td><td>$300</td></tr>
<tr class="in"><td>Overhead / target margin</td><td>12% / 30%</td></tr>
<tr class="h"><td>Results</td><td></td></tr>
<tr><td>Total cost</td><td>$2,620.80</td></tr>
<tr class="tot"><td>Quote price</td><td>$3,744.00</td></tr>
<tr><td>Profit on the job</td><td>$1,123.20</td></tr>
<tr><td>Markup on cost</td><td>42.9%</td></tr>
<tr><td>30% deposit to ask for</td><td>$1,123.20</td></tr>
<tr><td>Margin if they negotiate 10% off</td><td>22.2%</td></tr>
</table></div>'''

# HOME
home=f'''<section class="hero"><div class="wide">
<div>
<p class="eyebrow">Free tools for home-service pros</p>
<h1>Quote every job at the margin you <em>meant</em> to make.</h1>
<p class="lede">Pricing calculators and plain-English guides for contractors, cleaners, landscapers and handymen. No sign-up, no cookies. Everything runs in your browser.</p>
<div class="actions"><a class="btn btn-acc" href="tools/job-price-calculator.html">Price a job now {ARROW}</a><a class="btn btn-ghost" href="tools/index.html">See all 12 calculators</a></div>
</div>
<div class="qq-wrap"><span class="chip chip-a"><i></i>Profit <b id="qprof">$233.33</b></span><span class="chip chip-b"><i></i>Markup on cost <b id="qmk">33.3%</b></span>
<div class="qq" id="qq">
<h2>Quick quote <span class="live">LIVE</span></h2>
<div class="grid2"><div><label for="qc">Job cost ($)</label><input id="qc" type="number" min="0" step="10" value="700" inputmode="decimal"></div>
<div><label for="qm">Target margin (%)</label><input id="qm" type="number" min="0" max="90" step="1" value="25" inputmode="decimal"></div></div>
<div class="price" aria-live="polite"><span>Quote this price</span><strong id="qp">$933.33</strong></div>
<p class="warn" id="qw">Adding a 25% markup instead gives <b>$875.00</b>, which is only a <b>20.0%</b> margin.</p>
<a class="more" href="tools/job-price-calculator.html">Add labor, materials and overhead &rarr;</a>
</div></div>
</div></section>
<section class="facts"><ul class="wide">
<li><b>12</b>free calculators</li><li><b>6</b>step-by-step guides</li><li><b>0</b>cookies or trackers</li><li><b>$0</b>no sign-up needed</li>
</ul></section>
<section class="sec"><div class="wide">
<div class="sec-head center"><p class="eyebrow">How it works</p><h2>A confident quote in three steps</h2><p>No spreadsheets to build, no account to create. Open a calculator and type.</p></div>
<ol class="steps">
<li><span class="n">1</span><h3>Enter your costs</h3><p>Materials, labor hours and your real hourly labor cost, plus overhead from your own books.</p></li>
<li><span class="n">2</span><h3>Pick the margin you want</h3><p>The calculator divides by (1 &minus; margin), so the profit you choose is a share of the <em>price</em>.</p></li>
<li><span class="n">3</span><h3>Send the quote</h3><p>See the price, the profit, the markup and the deposit to ask for before you hit send.</p></li>
</ol></div></section>
<section class="sec alt"><div class="wide">
<div class="sec-head"><p class="eyebrow">Calculators</p><h2>Every number behind a profitable quote</h2><p>From the first estimate to the final invoice. Each tool shows its formula and a worked example, so you can check the math yourself.</p></div>
{tool_tiles("")}
</div></section>
<section class="sec"><div class="wide trap">
<div><p class="eyebrow">The margin trap</p><h2 style="margin-top:0">A 25% markup is not a 25% margin</h2>
<p>Margin is the share of the <em>price</em> you keep. Markup is added to <em>cost</em>. Mix them up and every quote leaves money behind. On a $700 job the gap is $58.33, and it grows with every job you win.</p>
<p><a class="btn btn-acc" href="guides/markup-vs-margin-for-contractors.html">Read the markup vs margin guide {ARROW}</a></p></div>
<div class="bars">
<div class="bar"><div class="lbl"><span>Cost + 25% markup</span><span class="num">$875.00</span></div>
<div class="track"><i class="c" style="width:80%">Cost $700</i><i class="p thin" style="width:20%">$175</i></div><small>Margin kept: 20.0%</small></div>
<div class="bar"><div class="lbl"><span>Priced for a 25% margin</span><span class="num">$933.33</span></div>
<div class="track"><i class="c" style="width:75%">Cost $700</i><i class="p" style="width:25%">$233.33</i></div><small>Margin kept: 25.0%</small></div>
</div></div></section>
<section class="sec alt"><div class="wide">
<div class="sec-head"><p class="eyebrow">Guides</p><h2>Learn the method, not just the number</h2><p>Short guides with worked examples you can follow with a calculator in the next tab.</p></div>
{guide_tiles("")}
</div></section>
<section class="sec"><div class="wide promo">
<div><span class="pill">Coming soon &middot; planned price $9</span>
<h2>The Contractor Quote &amp; Margin Sheet</h2>
<p>All of this in one Google Sheets page. Type your materials, hours, rates, overhead and target margin into the yellow cells; get the quote, your profit, the deposit and your walk-away price.</p>
<ul><li>Works in Excel and Google Sheets</li><li>Bonus tabs: hourly rate, change orders, job profit log, customer estimate</li><li>Shows what a 10% or 20% discount does to your margin</li><li>No macros, add-ons or subscription</li></ul>
<p style="display:flex;gap:12px;flex-wrap:wrap;align-items:center"><a class="btn btn-acc" href="ventures/sheets.html">See the sheet {ARROW}</a><a href="templates/contractor-estimate-template.html">Or get the free estimate template</a></p></div>
{SHEET("")}
</div></section>
<section class="sec alt"><div class="w">
<div class="sec-head center"><p class="eyebrow">FAQ</p><h2>Questions, answered</h2></div>
<div class="faq">
<details open><summary>Are the calculators really free?</summary><p>Yes. There is no sign-up and no paywall. Every calculator runs in your browser; nothing you type is stored or sent anywhere.</p></details>
<details><summary>What is the difference between markup and margin?</summary><p>Markup is profit as a share of cost; margin is profit as a share of price. A 25% markup on a $700 job gives $875, which is only a 20% margin. For a true 25% margin you divide by 0.75 and quote $933.33.</p></details>
<details><summary>Who are these tools for?</summary><p>Small home-service businesses in the US: plumbers, electricians, painters, roofers, handymen, cleaners, landscapers and similar trades.</p></details>
<details><summary>Do you use cookies or track me?</summary><p>No. The site sets no cookies and loads no trackers or third-party scripts. See the <a href="privacy.html">privacy notice</a>.</p></details>
<details><summary>Is this financial or tax advice?</summary><p>No. The tools give planning estimates. Check local taxes, licensing rules and your own books before you rely on a number.</p></details>
</div></div></section>
<section class="cta-band"><div class="wide"><div><h2>Your next quote is one tab away.</h2><p>Open the job price calculator and see the number you should be quoting.</p></div><a class="btn btn-acc" href="tools/job-price-calculator.html">Price a job now {ARROW}</a></div></section>
<script>
(function(){{var c=document.getElementById("qc"),m=document.getElementById("qm"),p=document.getElementById("qp"),w=document.getElementById("qw"),
f=new Intl.NumberFormat("en-US",{{style:"currency",currency:"USD"}});
function u(){{var C=Math.max(0,parseFloat(c.value)||0),M=Math.min(90,Math.max(0,parseFloat(m.value)||0)),P=C/(1-M/100),K=C*(1+M/100),km=K>0?(K-C)/K*100:0;
p.textContent=f.format(P);document.getElementById("qprof").textContent=f.format(P-C);document.getElementById("qmk").textContent=(C>0?((P-C)/C*100).toFixed(1):"0.0")+"%";w.innerHTML="Adding a "+M+"% markup instead gives <b>"+f.format(K)+"</b>, which is only a <b>"+km.toFixed(1)+"%</b> margin.";}}
c.addEventListener("input",u);m.addEventListener("input",u);u();}})();
</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"Clever Loop Digital","url":"https://cleverloopdigital.com/","description":"Free pricing calculators and guides for US home-service businesses."}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"Are the calculators really free?","acceptedAnswer":{{"@type":"Answer","text":"Yes. There is no sign-up and no paywall. Every calculator runs in your browser; nothing you type is stored or sent anywhere."}}}},{{"@type":"Question","name":"What is the difference between markup and margin?","acceptedAnswer":{{"@type":"Answer","text":"Markup is profit as a share of cost; margin is profit as a share of price. A 25% markup on a $700 job gives $875, which is only a 20% margin. For a true 25% margin you divide by 0.75 and quote $933.33."}}}}]}}</script>'''
page("index.html","","", "Free Pricing Calculators for Home-Service Pros | Clever Loop Digital",
 "Free job price, hourly rate, markup/margin and break-even calculators for contractors, cleaners and other home-service businesses. No sign-up, no cookies.","",home)

# TOOLS HUB
tb=f'''<section class="phead"><div class="wide"><p class="crumbs"><a href="../index.html">Home</a> / <span>Calculators</span></p><p class="eyebrow">12 free calculators</p><h1>Free Calculators for Home-Service Pros</h1><p class="lede">Simple pricing tools for contractors, cleaners, landscapers and other home-service businesses. No sign-up, no cookies; everything runs in your browser.</p></div></section>
<main class="wide page">
{tool_tiles("../")}
<h2>Not sure where to start?</h2>
<p>Start with the <a href="job-price-calculator.html">job price calculator</a>. If you do not know your overhead or labor cost yet, read <a href="../guides/how-to-price-a-contractor-job.html">how to price a contractor job</a> first, or browse <a href="../guides/index.html">all guides</a>.</p>
<p><small>Estimates for planning only. Not accounting, tax or legal advice.</small></p>
</main>'''
page("tools/index.html","../","tools","Free Calculators for Home-Service Pros | Clever Loop Digital","Free pricing, margin, cost and invoicing calculators for contractors and home-service businesses. No sign-up, no cookies.","tools/index.html",tb)

# GUIDES HUB
gb=f'''<section class="phead"><div class="wide"><p class="crumbs"><a href="../index.html">Home</a> / <span>Guides</span></p><p class="eyebrow">Guides</p><h1>Pricing Guides for Contractors</h1><p class="lede">Plain-English, step-by-step guides with worked examples: pricing a job, markup vs margin, overhead, labor cost, break-even and change orders.</p></div></section>
<main class="wide page">
{guide_tiles("../")}
<h2>Run the numbers</h2>
<p>Every guide links to a matching free tool. See all <a href="../tools/index.html">12 calculators</a>.</p>
<p><small>Figures are illustrative estimates for planning only. Not accounting, tax or legal advice.</small></p>
</main>'''
page("guides/index.html","../","guides","Pricing Guides for Contractors | Clever Loop Digital","Step-by-step pricing guides for contractors and home-service pros: job pricing, markup vs margin, overhead, labor cost, break-even and change orders.","guides/index.html",gb)

# SHEETS
sb=f'''<section class="phead"><div class="wide promo">
<div><p class="crumbs"><a href="../index.html">Home</a> / <span>Quote &amp; Margin Sheet</span></p>
<span class="pill">Launching soon &middot; planned price $9</span>
<h1 style="margin-top:14px">Contractor Quote &amp; Margin Sheet</h1>
<p class="lede">One Google Sheets page for home-service pros (plumbers, electricians, roofers, painters and similar). Enter materials, labor hours, labor rate, subcontractor costs, overhead and the margin you want, and get the quote price, your profit and the deposit to ask for.</p>
<p style="margin-top:22px"><a class="btn btn-acc" href="mailto:hello@cleverloopdigital.com?subject=Quote%20sheet">Tell me when it is out {ARROW}</a></p></div>
{SHEET("../")}
</div></section>
<main class="w page">
<div class="card"><h2>What the sheet calculates</h2><ul>
<li>Quote price before and after sales tax on materials</li>
<li>Profit on the job, markup on cost and profit per labor hour</li>
<li>Deposit due at your chosen percentage</li>
<li>What your margin becomes if the client negotiates 10% or 20% off, and your break-even price</li></ul>
<p>Yellow input cells, everything else is formulas. No macros, no add-ons, no subscription.</p></div>
<div class="card"><h2>Plus four bonus tabs in the same workbook</h2><ul>
<li><strong>Hourly Rate:</strong> the rate to charge for your income goal after overhead and unbillable time</li>
<li><strong>Change Order:</strong> price extra work as labor + disruption allowance + marked-up materials</li>
<li><strong>Job Profit Log:</strong> list finished jobs and see the margin you really made on each, and in total</li>
<li><strong>Customer Estimate:</strong> a clean estimate to send, with line items, tax, deposit and a signature line</li></ul>
<p>One .xlsx file that opens in Excel and imports into Google Sheets (File &gt; Import &gt; Upload).</p></div>
<p>Prefer to try the math first? Use the free <a href="../tools/job-price-calculator.html">job price calculator</a> or see all <a href="../tools/index.html">free tools</a>.</p>
<h2>How to get it</h2>
<p>The checkout is not open yet. To be told when it is, email <a href="mailto:hello@cleverloopdigital.com?subject=Quote%20sheet">hello@cleverloopdigital.com</a> with the subject &ldquo;Quote sheet&rdquo;. We will only write to you about this sheet.</p>
<p><small>The example in the picture uses the sheet's own formulas: $1,200 materials + 24 h &times; $35 + $300 = $2,340 direct cost; + 12% overhead = $2,620.80; &divide; 0.70 = $3,744.00. Figures are estimates. Margin means profit divided by price; markup means profit divided by cost. This is a tool, not accounting, tax or legal advice.</small></p>
</main>'''
page("ventures/sheets.html","../","sheet","Contractor Quote &amp; Margin Sheet | Clever Loop Digital","Contractor Quote &amp; Margin Sheet: a Google Sheets quote, profit and deposit calculator for home-service pros. Launching soon.","ventures/sheets.html",sb)
print("done")
