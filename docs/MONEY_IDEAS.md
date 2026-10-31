# Para kazanma fikirleri (sıralı backlog) — her çalıştırmada güncellenir

## ANA ÜRÜN (30 Ekim, Erkan'ın örnek siteleri: Tally, HeadshotPro, Senja, ShipFast...)
Ders: tek kişilik başarılı siteler TEK dar işi kusursuz yapar, hero'da ürünü çalışırken gösterir, "ücretsiz başla" ile çeker, programatik SEO sayfalarıyla (şablon/meslek sayfaları) trafik toplar, sonra ücretli plana çevirir.
Bizim karşılığımız: **Estimate & Invoice Maker** (/maker/) — tarayıcıda çalışan ücretsiz teklif/fatura oluşturucu, 12 meslek sayfası (/maker/<trade>.html). Ücretli plan: **Pro $9/ay** (markasız PDF, kayıtlı müşteri/fiyat listesi, teklif→fatura tek tık, belge geçmişi). Talep: `maker` (görüntüleme, PDF indirme) + `maker-pro` (Pro tıklaması) panelde.
**KARAR v3 (30 Ekim 17:30):** her meslek için hesapla→teklif aracı (1. boya, 2. basınçlı yıkama, 3. çit, 4. roofing, 5. flooring, 6. drywall, 7. concrete, 8. mulch: YAPILDI). Sıra: cleaning. Yeni ince şablon sayfası yok.
Sıradaki büyüme işleri (yalnızca ürün + SEO):
1. (DURDURULDU, karar v3) Daha fazla meslek sayfası — 51. çalıştırmada 6 eklendi (carpentry, concrete, fencing, tile, junk removal, window cleaning; toplam 18). Sırada: cabinet, moving, pest control, pool, gutter, appliance repair, masonry, siding.
2. "Invoice" odaklı meslek sayfaları (/maker/<trade>-invoice.html, data-type="invoice").
3. Ürün: tahmini-faturaya çevir, birden çok taslak, para birimi seçimi (CAD/AUD/GBP), kalem kütüphanesi.
4. Karşılaştırma/rehber içerikleri: "how to write an estimate", "estimate vs quote vs bid", "what to put on an invoice".


Durum: 30 Ekim (Erkan'ın 12 örnek sitesi incelendi → docs/BENCHMARKS.md; kapsam yazılım/AI dahil genişledi). Gelir £0. Tek darboğaz: ödeme altyapısı (Payhip/Gumroad/Stripe hesabı Erkan'da). Aşağıdakilerin hepsi gerçek kanıt istenen tahminlerdir; uydurma rakam yok.

| # | Fikir | Alıcı | Fiyat | Kanal | Engel | Sonraki adım |
|---|-------|-------|-------|-------|-------|--------------|
| 1 | Contractor Pricing Toolkit (.xlsx, 5 sekme) | ABD esnaf (tesisatçı, boyacı, tamirci) | $9 lansman | SEO: satış sayfası + rehber/araç sayfalarından iç link | Payhip hesabı (Erkan) | HAZIR: docs/distribution/product/contractor-pricing-toolkit.xlsx; Erkan Payhip'e yükleyince butona link |
| 3 | Niş paketler: temizlikçi / bahçıvan / boyacı için fiyatlama şablonu | Her meslek ayrı arama yapar | $9-15 | SEO: meslek bazlı fiyatlama rehberleri + araçlar | #1 ile aynı | Toolkit'ten meslek varyantları üret (kare metre / oda bazlı fiyat) |
| 4 | Bundle: Toolkit + teklif (estimate) & fatura şablonu | Teklif yazan esnaf | $19 | SEO: "estimate template" / "invoice template" sayfaları | #1 | YAPILDI: estimate + invoice ücretsiz şablon/SEO sayfaları, pakete 2 sekme. Sırada: "change order form template" sayfası + ücretsiz form |
| 5 | Affiliate: esnaf yazılımları (Jobber, Housecall Pro vb.) karşılaştırma sayfaları | Yazılım arayan esnaf | Komisyon | SEO | Affiliate kaydı Erkan'da; İSTEME. Önce komisyonsuz, tarafsız SEO karşılaştırma sayfası | Karşılaştırma sayfası (resmi fiyat sayfalarından) |

Öldürülen (30 Ekim, Erkan'ın modeli: yalnızca ürün + SEO): Etsy listeleme (yeni hesap isteği), "fiyat kontrolü" e-posta hizmeti (insanlara ulaşma/e-posta), forum/sosyal paylaşımlar.

| 6 | Meslek bazlı ücretsiz şablon sayfaları (painting estimate, handyman invoice vb.) | Mesleğe özel arayan esnaf | Ücretsiz → $9 paket | SEO (uzun kuyruk) | Yok | Yeni fikir (48. çalıştırma): mevcut şablon motoru ile meslek varyantları |

| 7 (fence YAPILDI 31 Ekim, 65. çalıştırma; sırada painting, roofing) | Meslek başına "pricing guide" sayfaları (ör. "how much to charge for fence installation per foot") + maker'a link | Fiyat araştıran esnaf | Ücretsiz → Pro $9/ay | SEO (uzun kuyruk, ticari niyet) | Yok; fiyat aralıkları için okunmuş kaynak gerekir | Yeni fikir (51. çalıştırma): kaynaklı 1 rehberle başla |

Kural: Kanal YALNIZCA SEO. Erkan'dan yeni bir şey istenmez.

| 8 (YAPILDI 31 Ekim, 64. çalıştırma) | "Pressure washing pricing guide" / "how to price pressure washing per square foot" rehberi (kaynaklı fiyat aralıkları) + hesaplayıcıya link | Yeni başlayan basınçlı yıkama işletmeleri | Ücretsiz → Pro | SEO (uzun kuyruk) | Okunmuş fiyat kaynakları gerekir | Yeni fikir (54. çalıştırma) |
