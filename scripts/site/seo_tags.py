"""Add Open Graph/Twitter tags and BreadcrumbList JSON-LD to every page that lacks them. Usage: python3 scripts/site/seo_tags.py public"""
import glob,re,html,json,os,sys
os.chdir(sys.argv[1] if len(sys.argv)>1 else "public")
n=0
for f in glob.glob("**/*.html",recursive=True):
    s=open(f).read()
    if 'property="og:title"' in s or 'noindex' in s: continue
    t=re.search(r"<title>(.*?)</title>",s).group(1); d=re.search(r'name="description" content="([^"]*)"',s).group(1)
    u=re.search(r'rel="canonical" href="([^"]*)"',s).group(1)
    typ="article" if f.startswith("guides/") and not f.endswith("index.html") else "website"
    og=(f'<meta property="og:type" content="{typ}"><meta property="og:site_name" content="Clever Loop Digital">'
        f'<meta property="og:title" content="{t.split(" | ")[0]}"><meta property="og:description" content="{d}">'
        f'<meta property="og:url" content="{u}"><meta property="og:image" content="https://cleverloopdigital.com/og-image.png">'
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">')
    m=re.search(r'<p class="crumbs">(.*?)</p>',s); bc=""
    if m:
        items=[]
        for a in re.finditer(r'<a href="([^"]*)">(.*?)</a>|<span>(.*?)</span>',m.group(1)):
            if a.group(1):
                href=os.path.normpath(os.path.join(os.path.dirname(f),a.group(1))); href="" if href=="index.html" else href[:-10] if href.endswith("/index.html") else href
                url="https://cleverloopdigital.com/"+href; name=html.unescape(a.group(2))
            else: url=u; name=html.unescape(a.group(3))
            items.append({"@type":"ListItem","position":len(items)+1,"name":name,"item":url})
        bc='\n<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items},ensure_ascii=False)+'</script>'
    s=s.replace(f'<link rel="canonical" href="{u}">',f'<link rel="canonical" href="{u}">\n{og}{bc}',1)
    open(f,"w").write(s); n+=1
print("tagged",n)
