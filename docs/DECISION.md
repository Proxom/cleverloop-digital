# KARAR: Para kazanma yöntemi (Faz 1) — taslak v1, 28 Ekim 2026

## Özet (Türkçe)
- **Semrush:** hesapta API birimi yok (`no_api_units`) → anahtar kelime hacmi ALINAMADI. Talep kanıtı yalnızca web kaynaklarından; hacim doğrulaması yok, bunu karar belirsizliği olarak kabul et.
- **Sert gerçek:** İlk dalga seçimi (şablon + yazılım rehberi) zayıf. Whop verisine göre dijital şablon kategorisinde 6.700 üründen yalnızca 367'si gelir üretiyor, ortalama $70/ay, $5k/ay üstü ürün SIFIR (whoptrends.com/categories/digital_templates). Tek başına şablon satışı £5k/ay hedefine götürmez.
- **Dağıtım gerçeği:** 50 soğuk e-posta = 0 yanıt. Erkan'ın zamanı olmadan ilk 100 müşteriye ulaşmanın tek ölçeklenebilir yolu: arama motoru + ücretsiz araçlar + e-posta listesi. Arama trafiği yayıncılar için düşüyor (~%60, kaynak aşağıda) → bu yüzden tek sayfa/çok sayfa değil, *araç + özgün veri* gerekir.
- **Öneri (kırmızı takım sonrası bkz. aşağıda):** BİRİNCİL = "ABD ev-hizmetleri esnafı için ücretsiz fiyat/kâr hesaplayıcıları + yazılım karşılaştırma (açıklamalı affiliate) + e-posta listesi → ücretli şablon paketi". YEDEK = "Aylık otomatik niş rapor/veri aboneliği" sadece ilk 30 günde birincil eşikleri tutturamazsa.
- Erkan onayı gerekli: docs/APPROVALS.md madde 0.

## Adaylar (English details)
Revenue target: £5k/month ≈ $6.3k (FX 1.27 assumed).

| # | Method | Revenue math (assumptions) | First-100-customer path (no Erkan time) | Verdict |
|---|---|---|---|---|
| A | Template shop (Sheets/Excel) on own site | $19 avg → ~330 sales/mo. Whop: avg $76/mo/product, 1.8% of products > $1k/mo, 0 > $5k | SEO + Pinterest/Etsy-like discovery; Etsy bans bot-made listings | Weak alone; keep as *cross-sell* only |
| B | Software directory + affiliate + paid featured listing | 30 featured × $197 = $5.9k (vendor-blog claim, unverified) or affiliate 20-25% recurring | Needs organic traffic; directories lost traffic in AI era (directorygems case study); cold outreach to vendors = same 0-reply risk | Medium-weak; merge into D as affiliate layer |
| C | Rank-and-rent / pay-per-lead local sites | ~20 leads/mo × $20 = $400/mo per site (dn.org example) → ~15 ranking sites for $6k | Must rank in local SERPs; slow (6-12 mo); buyers are local businesses needing sales calls | Too slow, sales-heavy, reject |
| D | Free calculators/tools + comparison content for US home-service pros, monetised by affiliate + email list + paid template packs | Illustrative: 20k visits/mo × 1.5% email capture = 300 subs; 1% buy $29 = ~$87... realistically needs 100k+ visits for $5k; affiliate adds ~$30-100 per software signup | Search (tools earn links), directory submissions, forum answers (drafts for Erkan), no calls | Primary: only option with compounding distribution, but 12-month path is uncertain |
| E | Monthly niche data report subscription ($29-99/mo) | 100 subs × $49 = $4.9k | Same distribution problem; needs 5-10k niche audience first | Backup; validate with free sample reports from D's audience |
| F | Pure AI affiliate comparison blog | Revenue per page claims (thestacc.com: $1,121/page) are vendor-published, unverified | Google scaled-content-abuse risk | Reject as standalone |

## Sources actually read (search excerpts)
- whoptrends.com/categories/digital_templates (template market stats, Whop only, estimates)
- developers.google.com/search/docs/essentials/spam-policies (scaled content abuse)
- searchengineland.com/small-publisher-search-traffic-drops-data-471974
- etsy.com seller handbook (bot-made listings banned)
- dn.org geo-domain lead-gen article (illustrative numbers)
- thestacc.com programmatic SEO case study (vendor self-report, treated as UNVERIFIED)
- Semrush: NOT available (no API units).

## Legal/platform risks
Affiliate disclosure (FTC), CAN-SPAM for any email, CCPA/state privacy for list, Google spam policy (few pages, real tools), no regulated advice (calculators give estimates only, with disclaimers; no tax/legal advice).

## What must be built (Phase 2)
Home page for "tools for home-service pros", 3 launch calculators (job pricing, hourly rate / profit margin, quote markup) in plain JS (no cookies), comparison pages with disclosed affiliate links (only after Erkan joins programs), email capture (needs provider chosen by Erkan, no account created by me), template pack page (pricing displayed, checkout later), trust pages with Erkan's real details.
Cost: £0 beyond domain/hosting already paid.

## Kill criteria and 30-day validation (numeric, revised after red-team)
Single assumption: 1.5-3% of visits join the email list. Thresholds derive from it.
- Day 45: >= 15 pages indexed AND >= 1,000 Search Console impressions (day-30 traffic is noise on a new domain).
- Day 30-45: willingness-to-pay test: a paid $29-49 sample report/pre-order (paid deposit only; free "notify me" sign-ups do NOT count as demand).
- Day 90: >= 3,000 visits/month, rising >= 30% month on month, and >= $1 affiliate revenue or one paid pre-order.
- Hard checkpoint ~June 2027: >= £1,000/month; stop or pivot if < £300.
- Caps: kill if Erkan's time > 45 min/day or spend > £200. Pause on any Google manual action or affiliate ban.

## Red-team notes (subagent; unverified, no web searches run)
1. Revenue math does not close: 100k visits/mo gives only ~$435/mo from $29 packs; $6.3k needs ~500k-1M visits/mo. "£5k net" also ignores fees, US sales tax/nexus, UK tax, W-8BEN. The "$87" line in row D is a one-off, not monthly.
2. Original thresholds contradicted the model (implied 5-7.5% capture) - fixed above.
3. SEO on a new domain takes 3-6 months; Jobber/ServiceTitan/Housecall Pro own calculator queries; AI Overviews answer them.
4. Thin/AI-run content risk (scaled content abuse): few pages, original data, real sources.
5. Depends on Erkan (affiliate sign-ups, email provider, details); forums ban AI/promo posts; trades audiences respond poorly to email.
Probability of reaching £5k/month by Oct 2027 with D: estimated <= 5% by the red team. Honest view: low; this is a validation bet, not a plan.
Changes adopted: pick high-bounty niche (field-service software $100+/signup, financing) rather than $29 packs; add original state-by-state data (licensing, permits, rates, with sources) as content moat; test paid demand in week 1 via E-style sample report.
