LOGO='<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#ff6a2b"/><path d="M21.5 11.2A7 7 0 1 0 23 16" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/><path d="M17.6 10.6l4.4.4-.6 4.3" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="16" cy="16" r="2.4" fill="#0d2240"/></svg>'

def P(p): return p  # prefix like "" or "../"

def header(p, cur=""):
    def a(href, txt, key, cls=""):
        c = f' class="{cls}"' if cls else ""
        ac = ' aria-current="page"' if key == cur else ""
        return f'<a href="{p}{href}"{c}{ac}>{txt}</a>'
    return ('<header class="site-head"><div class="wide">'
            f'<a class="logo" href="{p}index.html">{LOGO}<span>Clever Loop Digital</span></a>'
            '<nav class="site-nav" aria-label="Main">'
            + a("tools/index.html","Calculators","tools")
            + a("guides/index.html","Guides","guides")
            + a("about.html","About","about")
            + a("maker/","Estimate Maker","maker","cta")
            + '</nav></div></header>')

def footer(p):
    return f'''<footer class="site-foot"><div class="wide cols">
<div><a class="logo" href="{p}index.html">{LOGO}<span>Clever Loop Digital</span></a><p>Free pricing calculators and plain-English guides for US home-service businesses. Everything runs in your browser.</p></div>
<div><h4>Free tools</h4><a href="{p}maker/">Estimate &amp; invoice maker</a><a href="{p}tools/job-price-calculator.html">Job price</a><a href="{p}tools/hourly-rate-calculator.html">Hourly rate</a><a href="{p}tools/markup-margin-calculator.html">Markup vs margin</a><a href="{p}tools/break-even-calculator.html">Break-even</a><a href="{p}tools/index.html">All calculators</a></div>
<div><h4>Guides</h4><a href="{p}guides/how-to-price-a-contractor-job.html">Price a job</a><a href="{p}guides/markup-vs-margin-for-contractors.html">Markup vs margin</a><a href="{p}guides/contractor-overhead-rate.html">Overhead rate</a><a href="{p}guides/how-to-price-a-change-order.html">Change orders</a><a href="{p}guides/index.html">All guides</a></div>
<div><h4>Company</h4><a href="{p}templates/contractor-estimate-template.html">Free estimate template</a><a href="{p}templates/contractor-invoice-template.html">Free invoice template</a><a href="{p}about.html">About</a><a href="{p}ventures/sheets.html">Quote &amp; Margin Sheet</a><a href="mailto:hello@cleverloopdigital.com">hello@cleverloopdigital.com</a><a href="{p}terms.html">Terms</a><a href="{p}privacy.html">Privacy</a></div>
</div><div class="wide legal"><span>&copy; 2026 Erkan Bedir, trading as Clever Loop Digital, United Kingdom.</span><span>No cookies, no trackers. Estimates only, not financial, tax or legal advice.</span></div></footer>'''

def headlinks(p):
    return f'<link rel="preload" href="{p}fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="icon" href="{p}favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#0d2240">'

I = lambda d: f'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
ICONS = {
 "job-price-calculator": I('<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>'),
 "hourly-rate-calculator": I('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "markup-margin-calculator": I('<path d="M19 5L5 19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>'),
 "break-even-calculator": I('<path d="M3 3v18h18"/><path d="M6 17L19 6"/><path d="M6 9h13"/>'),
 "labor-burden-calculator": I('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M17 4.5a3.5 3.5 0 0 1 0 7"/><path d="M19 14a6.5 6.5 0 0 1 2.5 6"/>'),
 "change-order-calculator": I('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/><path d="M12 12v6M9 15h6"/>'),
 "painting-estimate-calculator": I('<rect x="3" y="3" width="15" height="6" rx="1.5"/><path d="M18 6h3v5h-9v3"/><rect x="10" y="14" width="4" height="7" rx="1"/>'),
 "material-waste-calculator": I('<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5"/>'),
 "deposit-payment-schedule-calculator": I('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="M8 15h3"/>'),
 "invoice-processing-fee-calculator": I('<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6.5 15h4"/>'),
 "late-payment-fee-calculator": I('<path d="M6 3h12M6 21h12"/><path d="M7 3c0 5 5 6 5 9s-5 4-5 9M17 3c0 5-5 6-5 9s5 4 5 9"/>'),
 "travel-cost-calculator": I('<path d="M2 6h12v10H2z"/><path d="M14 9h4l4 4v3h-8"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>'),
 "job-sales-tax-calculator": I('<path d="M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2z"/><path d="M9 8h6M9 12h6"/>'),
 "guide": I('<path d="M4 19.5V5a2 2 0 0 1 2-2h13v16H6.5a2.5 2.5 0 0 0 0 5H19"/><path d="M8 7h7M8 11h5"/>'),
}
TOOLS = [  # slug, name, desc, group
 ("job-price-calculator","Job Price Calculator","Price a job from labor, materials and your target margin.","Price the job"),
 ("painting-estimate-calculator","Painting Estimate Calculator","Wall area, gallons of paint, labor and a priced estimate in one go.","Price the job"),
 ("hourly-rate-calculator","Hourly Rate Calculator","Work out the hourly rate you need to hit your income goal.","Price the job"),
 ("markup-margin-calculator","Markup vs Margin Calculator","Convert markup to margin and back, and get the selling price.","Price the job"),
 ("change-order-calculator","Change Order Calculator","Price extra work added mid-job.","Price the job"),
 ("material-waste-calculator","Material Waste Calculator","Add a waste factor and see how much to order.","Price the job"),
 ("travel-cost-calculator","Travel &amp; Drive Time Cost Calculator","Estimate the mileage and drive time cost of a job.","Price the job"),
 ("labor-burden-calculator","Labor Burden Calculator","Real cost and billing rate per employee hour.","Know your costs"),
 ("break-even-calculator","Break-Even Calculator","How many jobs a month cover your fixed costs.","Know your costs"),
 ("deposit-payment-schedule-calculator","Deposit &amp; Payment Schedule Calculator","Split a job into a deposit and milestone payments.","Get paid"),
 ("invoice-processing-fee-calculator","Invoice Processing Fee Calculator","See the card fee on an invoice and what you keep.","Get paid"),
 ("late-payment-fee-calculator","Late Payment Fee Calculator","Estimate the late fee on an overdue invoice.","Get paid"),
 ("job-sales-tax-calculator","Job Sales Tax Calculator","Add sales tax to a job quote and see the invoice total.","Get paid"),
]
GUIDES = [  # slug, title, desc, example
 ("how-to-price-a-contractor-job","How to Price a Contractor Job","Materials, labor, overhead and target margin, step by step.","$2,620.80 cost &rarr; $3,744 quote"),
 ("markup-vs-margin-for-contractors","Markup vs Margin for Contractors","Why a 30% markup is only a 23.1% margin, with a conversion chart.","30% markup = 23.1% margin"),
 ("contractor-overhead-rate","How to Calculate Contractor Overhead","Find your overhead rate and add it to every job.","$48k &divide; $200k = 24%"),
 ("how-to-calculate-labor-cost","How to Calculate Labor Cost for a Bid","Wage, burden and billable hours: the true cost of an hour.","$25 wage &rarr; $42.86/hour"),
 ("contractor-break-even-point","How to Find Your Break-Even Point","How many jobs a month it takes to cover overhead.","$4,000 &divide; $400 = 10 jobs"),
 ("how-to-price-a-change-order","How to Price a Change Order","Labor, disruption and marked-up materials, signed before you start.","6 h + materials = $822"),
]
def tile(href, name, desc, icon, ex=""):
    e = f'<em class="ex">{ex}</em>' if ex else ""
    return f'<a class="tile" href="{href}"><span class="ic">{icon}</span><b>{name}</b><span>{desc}</span>{e}</a>'
def tool_tiles(p, grouped=True):
    out=[]; g=None
    for s,n,d,grp in TOOLS:
        if grouped and grp!=g:
            if g: out.append('</div>')
            out.append(f'<p class="group-title">{grp}</p><div class="tiles">'); g=grp
            if grp=="Get paid" and grouped: out.append(tile(f"{p}maker/","Invoice &amp; Estimate Maker","Make an invoice or estimate and save it as a PDF. Free, no sign-up.",'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/><path d="M8 13h8M8 17h5"/></svg>',"New"))
        out.append(tile(f"{p}tools/{s}.html",n,d,ICONS[s]))
    out.append('</div>'); return "\n".join(out)
def guide_tiles(p):
    return '<div class="tiles">'+"\n".join(tile(f"{p}guides/{s}.html",t,d,ICONS["guide"],ex) for s,t,d,ex in GUIDES)+'</div>'
