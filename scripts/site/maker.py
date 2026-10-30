"""Generate the Estimate & Invoice Maker page and per-trade landing pages. Usage: python3 scripts/site/maker.py public"""
import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common import *
os.chdir(sys.argv[1])
ARROW='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
TRADES={
 "general-contractor":("General Contractor","general contractors and remodelers",["Split demolition, labor, materials and permits into separate lines so changes are easy to price.","Put the permit and inspection costs on their own line; customers accept them more easily when they see them.","Use a 30% deposit line and a valid-until date when material prices are moving."]),
 "plumbing":("Plumbing","plumbers",["List the fixture or water heater separately from labor so the customer sees what they are paying for.","Add haul-away of the old unit as its own line instead of hiding it in labor.","For service calls, a trip or diagnostic charge line avoids arguments later."]),
 "electrical":("Electrical","electricians",["Show the permit as a separate line; many jobs need one.","Price devices (outlets, breakers, fixtures) per unit so add-ons are easy.","Keep labor in hours so a change order can reuse the same rate."]),
 "painting":("Painting","painters",["Price walls, ceilings and trim by square or linear foot; customers compare those numbers.","Put paint and supplies on one line so a color change does not reprice the whole job.","Note how many coats are included in the description."]),
 "roofing":("Roofing","roofers",["Price per square (100 sq ft): tear-off and installation on separate lines.","Underlayment, flashing and ventilation belong on their own lines.","Add the dumpster and disposal so the total has no surprises."]),
 "landscaping":("Landscaping","landscapers and lawn care pros",["Price recurring work per visit and one-off work per job or cubic yard.","Mulch, soil and plants are easiest to adjust when quantity and unit are visible.","Add yard waste removal as its own line."]),
 "cleaning":("Cleaning","house cleaners and cleaning companies",["Price the main clean per job, then add-ons (oven, fridge, windows) per item.","Customers pick add-ons more often when each has its own price.","Say what is included in the description: rooms, bathrooms, supplies."]),
 "handyman":("Handyman","handymen",["Labor in hours plus a materials line covers most small jobs.","A trip charge line makes small jobs worth the drive.","Group several small tasks on one estimate to raise the job size."]),
 "hvac":("HVAC","HVAC technicians",["List parts and refrigerant per unit (each, lb) so the bill is easy to check.","A tune-up or diagnostic line sets the base price of the visit.","Offer repair options as separate estimates rather than one long list."]),
 "flooring":("Flooring","flooring installers",["Material quantity should include waste: install 400 sq ft, order about 420.","Keep removal, underlayment and installation on separate lines.","Transitions and stair nosing are easy to forget; give them their own line."]),
 "drywall":("Drywall","drywall contractors",["Price patches per patch and new drywall per square foot.","Texture matching takes time; give it its own line.","Note the finish level in the description."]),
 "pressure-washing":("Pressure Washing","pressure washing businesses",["Price house, driveway and deck per square foot on separate lines.","Customers often add a second surface when each has a visible price.","Mention the cleaning solution and any plant protection in the notes."]),
 "carpentry":("Carpentry","carpenters and finish carpenters",["Price trim and baseboard per linear foot and doors per unit; hourly labor covers the custom work.","Keep lumber and fasteners on one materials line so a wood species change is a one-line edit.","Say in the description whether paint or stain is included; it is the most common surprise."]),
 "concrete":("Concrete","concrete contractors",["Price the slab per square foot and state the thickness (4 in for patios and walks, often 5-6 in for driveways).","Excavation, gravel base and rebar or forms belong on their own lines; they change with site conditions.","Note the finish (broom, stamped, exposed aggregate) and whether sealing is included."]),
 "fencing":("Fencing","fence installers",["Price the fence per linear foot and gates per unit; customers compare those numbers between bids.","Removal of the old fence is its own line, and so are post holes in concrete if you charge for them.","Mention who calls 811 to locate utilities and who handles the HOA or permit approval."]),
 "tile":("Tile","tile setters",["Price installation per square foot and demolition separately; old tile removal varies a lot from job to job.","Backer board and waterproofing get their own line in showers so nobody skips them to cut the price.","Large-format, mosaic and herringbone layouts take longer; price them at a higher per-foot rate."]),
 "junk-removal":("Junk Removal","junk removal and hauling businesses",["Price by truck volume (quarter, half, full load) so the customer can picture what they pay for.","Mattresses, tires and appliances often carry disposal fees; show them per item.","A stairs or long-carry line covers the extra labor without arguments on site."]),
 "window-cleaning":("Window Cleaning","window cleaners",["Price per window (or per pane) and list interior and exterior on separate lines; many customers want only the outside.","Screens and tracks are easy add-ons when each has its own price.","Note any second-story or ladder work and hard-water stain removal as extras."]),
}
APP=lambda: '''<div class="wide mk">
<div class="mk-form">
<div class="mk-sec"><h2>Document <span class="seg" role="group" aria-label="Document type"><button type="button" data-settype="estimate">Estimate</button><button type="button" data-settype="invoice">Invoice</button></span></h2>
<div class="g3"><div><label for="f-number">Number</label><input id="f-number"></div><div><label for="f-date">Date</label><input id="f-date" type="date"></div><div><label for="f-due" id="lbl-due">Valid until</label><input id="f-due" type="date"></div></div></div>
<div class="mk-sec"><h2>Your business</h2>
<label for="f-biz">Business name</label><input id="f-biz" autocomplete="organization">
<label for="f-bizInfo">Address, phone, email, license #</label><textarea id="f-bizInfo" rows="3"></textarea>
<div class="logo-drop"><img id="logo-prev" alt="Your logo" hidden><div><label for="logo" style="margin-top:0">Logo (optional, stays on your device)</label><input id="logo" type="file" accept="image/png,image/jpeg,image/svg+xml,image/webp"><div id="logo-msg" class="prev-note" style="margin:4px 0 0"></div></div></div></div>
<div class="mk-sec"><h2>Customer</h2>
<label for="f-client">Customer name</label><input id="f-client">
<label for="f-clientInfo">Job address, phone, email</label><textarea id="f-clientInfo" rows="2"></textarea></div>
<div class="mk-sec"><h2>Line items</h2>
<div class="prev-note" style="margin:0">Start from a trade (example prices, replace with yours):</div><div class="preset-row" id="presets"></div>
<div class="items-h" aria-hidden="true"><span>Description</span><span>Qty</span><span>Unit</span><span>Rate $</span><span></span></div>
<div class="items" id="items"></div><button type="button" class="addrow" id="add">+ Add line</button>
<div class="g3" style="margin-top:6px"><div><label for="f-tax">Sales tax %</label><input id="f-tax" inputmode="decimal"></div>
<div id="wrap-deposit"><label for="f-deposit">Deposit %</label><input id="f-deposit" inputmode="decimal"></div>
<div id="wrap-paid" hidden><label for="f-paid">Already paid $</label><input id="f-paid" inputmode="decimal"></div></div></div>
<div class="mk-sec"><h2>Notes &amp; terms</h2><textarea id="f-notes" rows="3" aria-label="Notes and terms"></textarea></div>
<div class="mk-actions"><button type="button" class="btn btn-acc" id="pdf">Download PDF</button><button type="button" class="btn btn-plain" id="reset">Start over</button>
<a class="btn btn-plain" href="#pro" data-demand-click="maker-pro" data-root="ROOT">Save &amp; reuse clients <span class="pro-tag">PRO</span></a></div>
<p class="prev-note" style="margin:0">Your draft is saved only in this browser. Nothing you type is sent to us. "Download PDF" opens your browser's print window: choose "Save as PDF".</p>
</div>
<div class="mk-prev"><div class="paper" id="paper" aria-label="Document preview"></div><p class="prev-note">Live preview. This is exactly what your customer receives.</p></div>
</div>'''
PRO='''<section class="sec alt no-print" id="pro"><div class="wide">
<div class="sec-head center"><p class="eyebrow">Pricing</p><h2>Free forever. Pro when you need more.</h2><p>The maker is free with no sign-up. Pro is for businesses that send estimates every week.</p></div>
<div class="plans">
<div class="plan"><h3>Free</h3><div class="price">$0</div><ul><li>Unlimited estimates and invoices</li><li>Your logo, PDF download</li><li>18 trade starting points</li><li>Small &ldquo;Made with&rdquo; line on the PDF</li></ul><a class="btn btn-plain" href="#top">Use it free</a></div>
<div class="plan hot"><span class="pill">Coming soon</span><h3>Pro</h3><div class="price">$9<small>/month</small></div><ul><li>Everything in Free, no branding line</li><li>Saved customers and price list</li><li>Turn an estimate into an invoice in one click</li><li>Document history on your device</li></ul><a class="btn btn-acc" href="#pro" data-demand-click="maker-pro" data-root="ROOT">Get Pro {A}</a></div>
</div></div></section>'''
def faq_html(items): return '<div class="faq">'+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)+'</div>'
def faq_ld(items): return json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]})
def app_ld(name,url): return json.dumps({"@context":"https://schema.org","@type":"WebApplication","name":name,"url":url,"applicationCategory":"BusinessApplication","operatingSystem":"Any (web browser)","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}})
def write(path,p,title,desc,canon,body,lds,trade="",typ=""):
    attrs=(f' data-trade="{trade}"' if trade else "")+(f' data-type="{typ}"' if typ else "")
    head="".join(f'\n<script type="application/ld+json">{x}</script>' for x in lds)
    open(path,"w").write(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cleverloopdigital.com/{canon}">
{headlinks(p)}
<link rel="stylesheet" href="{p}site-v2.css"><link rel="stylesheet" href="{p}app-v1.css">{head}
<script src="{p}js/demand.js" defer></script><script src="{p}js/maker-v2.js" defer></script>
</head><body id="top"{attrs}>
{header(p,"maker")}
{body}
{footer(p)}
</body></html>
''')
GEN_FAQ=[("Is the estimate and invoice maker really free?","Yes. Make as many estimates and invoices as you like, add your logo and download them as PDF. There is no sign-up and no watermark across the page; a small line at the bottom says which free tool made it."),
("Where is my data stored?","Only in your own browser on this device. Nothing you type, including your logo and customer details, is sent to our server. Clearing your browser data removes the draft."),
("How do I save the estimate as a PDF?","Click Download PDF. Your browser's print window opens; choose Save as PDF as the destination. On a phone, use Share or Print and then Save to Files."),
("What is the difference between an estimate and an invoice?","An estimate tells the customer what a job will cost before you start; an invoice asks for payment after the work (or a stage of it) is done. Switch between them with the Estimate / Invoice toggle."),
("How should I price the line items?","Start from your real costs and the margin you want. The free job price calculator divides cost by (1 minus your target margin), so a $700 job at a 25% margin is $933.33, not $875.")]
# main maker page
body=f'''<section class="phead"><div class="wide"><p class="crumbs"><a href="../index.html">Home</a> / <span>Estimate &amp; Invoice Maker</span></p><p class="eyebrow">Free online tool</p><h1>Free Estimate &amp; Invoice Maker for Contractors</h1><p class="lede">Fill in the form, watch the document build itself, download a clean PDF. Your logo, your line items, tax and deposit worked out for you. No sign-up.</p></div></section>
<main class="mk-main">
{APP().replace("ROOT","../")}
<div class="w no-print" style="padding-bottom:20px">
<h2>Made for the trades</h2>
<p>Pick a starting point and the line items fill in with typical work for that trade. Prices are examples; replace them with yours.</p>
<div class="tiles">{"".join(f'<a class="tile" href="{k}.html"><b>{v[0]} estimate template</b><span>Online estimate and invoice maker for {v[1]}.</span></a>' for k,v in TRADES.items())}</div>
<h2>Frequently asked questions</h2>
{faq_html(GEN_FAQ)}
</div>
</main>
{PRO.replace("ROOT","../").replace("{A}",ARROW)}'''
write("maker/index.html","../","Free Estimate &amp; Invoice Maker for Contractors (PDF) | Clever Loop Digital",
 "Make a professional contractor estimate or invoice online in minutes: your logo, line items, sales tax, deposit, PDF download. Free, no sign-up, data stays in your browser.",
 "maker/",body,[faq_ld(GEN_FAQ),app_ld("Estimate & Invoice Maker","https://cleverloopdigital.com/maker/")])
# trade pages
for k,(name,who,tips) in TRADES.items():
    faq=[(f"Is this {name.lower()} estimate template free?",f"Yes. The online maker is free with no sign-up. It starts with typical {name.lower()} line items, which you can edit, and downloads as a PDF."),
         (f"What should a {name.lower()} estimate include?","Your business details and license number if your state requires one, the customer and job address, a clear description of the work, line items with quantity, unit and price, tax, total, deposit, how long the price is valid, and a signature line."),
         ("Can I turn it into an invoice?","Yes. Switch the toggle at the top from Estimate to Invoice. The same line items carry over, and you can enter what the customer already paid to show the balance due.")]
    b=f'''<section class="phead"><div class="wide"><p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Estimate &amp; Invoice Maker</a> / <span>{name}</span></p><p class="eyebrow">Free {name.lower()} template</p><h1>Free {name} Estimate Template</h1><p class="lede">An online estimate and invoice maker for {who}. It starts with typical {name.lower()} line items; change anything, add your logo and download a PDF. Free, no sign-up.</p></div></section>
<main class="mk-main">
{APP().replace("ROOT","../")}
<div class="w no-print" style="padding-bottom:20px">
<h2>Tips for {name.lower()} estimates</h2>
<ul>{"".join(f"<li>{t}</li>" for t in tips)}</ul>
<p>Not sure what to charge? Use the <a href="../tools/job-price-calculator.html">job price calculator</a> and read <a href="../guides/how-to-price-a-contractor-job.html">how to price a contractor job</a>.</p>
<h2>Frequently asked questions</h2>
{faq_html(faq)}
<h2>Other trades</h2>
<p>{" &middot; ".join(f'<a href="{o}.html">{v[0]}</a>' for o,v in TRADES.items() if o!=k)}</p>
</div>
</main>
{PRO.replace("ROOT","../").replace("{A}",ARROW)}'''
    write(f"maker/{k}.html","../",f"Free {name} Estimate Template &amp; Invoice Maker | Clever Loop Digital",
      f"Free {name.lower()} estimate template you fill in online: typical {name.lower()} line items, your logo, tax and deposit, PDF download. Also makes invoices. No sign-up.",
      f"maker/{k}.html",b,[faq_ld(faq),app_ld(f"{name} Estimate Maker",f"https://cleverloopdigital.com/maker/{k}.html")],trade=k)
print("pages",1+len(TRADES))
