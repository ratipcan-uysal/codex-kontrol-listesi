# Editoryal ve kaynak sadakati kontrolü

29 Ekim 2026. Ölçüm kapsamı: 18 bölüm ve 6 yazılmış ek. İlk tam taslak başlangıç kabul edildi. Önceden var olan bir yazar metni yeniden yazılmadı. Ürün iddiaları resmî belgelere, gerçek olaylar seçili asıl proje kayıtlarına dayanır. Kurgu örnekler kullanıcı isteğiyle üretildi ve etiketlendi.

## Tekrarlanabilir ölçüm

Node tabanlı slop-check ölçümü. Son ölçüm girdisi, canonical içerikteki bölüm başlığı ve body alanlarının sırayla birleştirilmesidir. Girdi hash'leri [kayıtta](editorial-inputs.json); [önce](editorial-before.json) ve [sonra](editorial-after.json) sonuçları saklanır. Eşleme, envanter ve kaynak dizini gibi üretilmiş tablolar ölçüme katılmadı. Ölçümün kelime ayıklaması düz boşluk sayımından farklıdır.

| Metric | Before | After |
|---|---|---|
| Em dashes (per 1k words) | 0 | 0 |
| Semicolons (per 1k words) | 12.3 | 10.6 |
| Sentence length spread (stdev, words) | 24.1 | 23.7 |
| Short sentences (% under 6 words) | 18.5 | 18.4 |
| Top sentence opener (% start with "bu") | 4.6 | 4.7 |
| sadece … değil, aynı zamanda (per 1k words) | 0 | 0 |
| -dir / -maktadır ekleri (per 1k words) | 0.1 | 0.1 |
| -ebilir / -abilir yığılması (per 1k words) | 10.1 | 10 |
| Hazır bağlayıcılar (per 1k words) | 0 | 0 |
| Şişmiş ifadeler (per 1k words) | 0 | 0 |
| Üçlü sıfat dizileri (per 1k words) | 5.6 | 5.6 |
| Hazır ibare (per 1k words) | 0.5 | 0.5 |
| Edilgen çatı (per 1k words) | 13.1 | 13.3 |

## Karar: REVISE — ölçüm eşikleri açısından

Üç eşik hâlâ aşılıyor; PASSED olarak sunulmadı. Bunlar teslimi engelleyen üç saptanmış anlam hatası demek değildir. Pasajlar gözden geçirildi:

- Noktalı virgül: 1–4. bölümlerde birden fazla kararı taşıyan cümleler yeniden kuruldu. Kalan “Önce uygulanabilir plan çıkar; bu aşamada dosya değiştirme” ve “Kaynak ve sonuç kayıt sayısını karşılaştır; fark varsa nedenini açıkla” örnekleri, kopyalanabilir istekte görev ve sınırını birlikte tutuyor. Teknik başvuru tablolarındaki kısa koşullar da yoğunluğu artırıyor.
- Üçlü dizi: “Chat, Work ve Codex”, “macOS, Windows ve Linux” gibi gerçekten ayrılması gereken kavram adları var. Regex bunları sıfat dizisi sayabiliyor. Sırf eşiği indirmek için bir kavram çıkarılmadı.
- Edilgen regex: “yapabilir”, “görünür”, “karşılaştırabilir” ve “değişebilir” de eşleşiyor. Özellik erişimi ve hesap koşullarındaki olasılık kipleri kesinlik iddiasına dönüştürülmedi. Gerçek vaka C01'in ilk anlatımında özne açıldı.

## Anlamsal kontrol ve teslim değerlendirmesi

- Kurgu örnekler yaşanmış başarı gibi sunulmuyor. Gerçek vakalarda tamamlanmamış cihaz, görsel seçim ve yayın aşamaları açık kalıyor.
- Ürün bilgisi, gözlem, çıkarım ve öneri ana anlatıda ayrılıyor. Masaüstü Goals düğmeleri ile CLI alt komutlarının farklı olduğu resmî komut sayfasından doğrulandı.
- Mevcut 107 madde aynen korunuyor; [koruma kanıtı](legacy-preservation.json) kaynak alanlarını karşılaştırıyor.
- Metinde sınav, katılımcı ödevi veya atölye görevi yok. Örnek istekler anlatım malzemesi.
- Kaynak metnindeki olasılığı kesinliğe çeviren veya ölçülmemiş başarı ekleyen bir üslup düzeltmesi saptanmadı. Ölçüm doğruluk testi değildir.

Editoryal teslim değerlendirmesi: kullanıma hazır. Kalan regex bayrakları korunmuş koşul ve terim listeleriyle açıklanmıştır. Bütün metriğin sıfırlandığı veya otomatik ölçümün metni kusursuz kıldığı iddia edilmez.
