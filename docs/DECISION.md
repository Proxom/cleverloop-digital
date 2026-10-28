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

## Kill criteria and 30-day validation (numeric)
Day 30 after tools go live:
- ≥ 500 organic visits total AND ≥ 25 email sign-ups, else rethink distribution (switch emphasis to backup E or drop D).
- ≥ 1 affiliate program accepted by Erkan and ≥ 3 qualified clicks logged.
- ≥ 1 paid template sale or ≥ 10 pre-order "notify me" sign-ups.
Day 90 kill: < 2,000 monthly visits or < 150 subscribers → stop D, pick next candidate.
Day 180 must-have: ≥ £500/month, else the £5k/month goal needs a different method.

## Red-team notes
(to be filled by the red-team subagent)
