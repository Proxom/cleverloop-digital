# Dağıtım işi 008 — Payhip listeleme paketi (kopyala-yapıştır, ~10 dk)

Amaç: Erkan Payhip'te ürünü 10 dakikada açabilsin; her alan aşağıda hazır. Ajan hesap açmaz, şartları kabul etmez, ödeme bilgisi girmez.
Ürün dosyası: `docs/distribution/product/contractor-quote-margin-sheet.csv` (örnek: 1.200$ malzeme + 24sa×35$ = 840$ işçilik + 300$ taşeron = 2.340$; %12 genel gider 280,80$ → maliyet 2.620,80$; %30 marj → teklif 3.744$, kâr 1.123,20$; elle doğrulandı).

## Erkan'ın adımları
1. payhip.com → ücretsiz hesap (Clever Loop Digital adına, kişisel e-posta veya hello@cleverloopdigital.com). Ödeme alma: PayPal veya Stripe bağla (Proxom Ltd Stripe'ını DEĞİL).
2. CSV'yi Google Sheets'e içe aktar (Dosya > İçe aktar > Yükle), B5:B12 hücrelerini sarıya boya, Dosya > İndir > Microsoft Excel (.xlsx). Hem .xlsx'i hem aşağıdaki "README" metnini .txt olarak yükle.
3. Add Product → Digital Product → alanları aşağıdan yapıştır → Publish.
4. Ürün linkini dashboard'da strategy notuna veya onay notuna yaz; ajan bir sonraki çalıştırmada sitedeki butona ekler.

## Alanlar (EN, aynen yapıştır)
**Product name:** Contractor Quote & Margin Sheet (Google Sheets / Excel)

**Price:** $9 (USD)

**Description:**
Price every job with the margin you actually want.

One spreadsheet page for home-service pros: plumbers, electricians, roofers, painters, handymen and similar trades. Type in materials, labor hours, your labor rate, subcontractor or rental costs, overhead and your target margin. The sheet gives you:

- Quote price before and after sales tax on materials
- Profit on the job, markup on cost and profit per labor hour
- The deposit to ask for up front
- What your margin becomes if the client negotiates 10% off
- Your break-even price

Yellow cells are inputs; everything else is formulas. No macros, no add-ons, no subscription. Works in Google Sheets and Excel.

Worked example included: $1,200 materials, 24 labor hours at $35, $300 rental and 12% overhead at a 30% target margin gives a $3,744 quote and $1,123.20 profit.

Want to try the math first? Free calculator: https://cleverloopdigital.com/tools/job-price-calculator.html

Figures are estimates. This is a spreadsheet tool, not accounting, tax or legal advice. Questions: hello@cleverloopdigital.com

**Tags:** contractor quote template, job pricing spreadsheet, profit margin calculator, markup vs margin, plumber pricing, electrician estimate, handyman pricing, Google Sheets template

**Refund line (opsiyonel):** If the sheet does not work for you, email hello@cleverloopdigital.com within 14 days for a refund.

## README.txt (ürünle birlikte yüklenecek)
Contractor Quote & Margin Sheet — how to use
1. Google Sheets: File > Import > Upload this file, or open the .xlsx in Excel.
2. Fill only the yellow cells in column B (rows 5-12).
3. Read the results under CALCULATIONS and CHECK.
Margin = profit / price. Markup = profit / cost. A 30% margin needs about a 42.9% markup.
Questions: hello@cleverloopdigital.com. Figures are estimates, not tax or legal advice.

## Satış çıkınca ilk paylaşım (Erkan gönderir; kural izin veriyorsa, gerçek bir soruya cevap olarak)
"I kept getting margin and markup mixed up when quoting, so I put the math in one sheet: materials, labor, overhead and target margin in, quote price, profit and deposit out. Free calculator version here: https://cleverloopdigital.com/tools/job-price-calculator.html — the full sheet is $9 if it is useful."

Not: Gumroad da olur (aynı alanlar). İki platformun komisyonları bu çalıştırmada doğrulanmadı; hesap açarken fiyat sayfasına bak.

## UPDATE 30 Oct (run 45): upload the .xlsx instead of the CSV
File to upload on Payhip: `docs/distribution/product/contractor-pricing-toolkit.xlsx` (5 tabs: Start Here, Quote & Margin, Hourly Rate, Change Order, Job Profit Log). Download it from GitHub (open the file > "Download raw file").
Add to the description: "Includes 3 bonus tabs: Hourly Rate, Change Order and Job Profit Log." Price stays $9 (launch price).


> NOT (30 Ekim): Paylaşım metni bölümü kullanılmaz (outreach yok). Yalnızca Payhip ürün kurulumu geçerli.
