# 7. Model, düşünme seviyesi, hız ve kullanım

Belge kontrolü: 2026-10-29.

En yüksek düşünme ayarı her işin en iyi seçimi değildir. İyi seçim, görevin hangi kısmının zor olduğuna bağlıdır: karar vermek, kaynak bulmak, dosya düzenlemek veya uzun süren bir aracı beklemek.

## Birbirinden ayrı üç tercih

**Model**, görevi yorumlayan ve araçları kullanan sistemdir. **Düşünme seviyesi**, karar için ayrılan çabayı etkiler. **Hız seçeneği**, desteklenen modellerde hizmet hızını ve kullanım tüketimini etkileyebilir. Model seçmek bir tarayıcı eklentisi kurmaz; düşünmeyi yükseltmek eksik kaynak erişimini açmaz. [Modeller](https://learn.chatgpt.com/docs/models) · [Hız](https://learn.chatgpt.com/docs/agent-configuration/speed)

Güncel resmî rehber, en zor işler için Astra'yı; geniş günlük kullanım için Sol'u; yazı, görsel ve bilgisayar kullanımı ağırlıklı işler için Terra'yı; daha dar ve tekrarlı işler için Luna'yı başlangıç noktaları olarak sunuyor. Bunlar bizim karşılaştırmalı ölçümümüz değil. Kullanılabilir model ve düşünme seçeneklerini kendi mesaj alanında kontrol et; isimler ve hesap erişimi değişebilir.

| İş | Mantıklı başlangıç | Seçimi ne değiştirir? |
|---|---|---|
| Tek dosyada açık yazım hatası | Hızlı, düşük çabalı çalışma | Hata birçok dil veya üretim zincirine yayılıyorsa kapsam büyür |
| Belirsiz ürün kararı | Daha fazla düşünme, önce seçenekler | Gerçek kullanıcı verisi yoksa model gücü boşluğu kapatmaz |
| Zor hata ayıklama | Güçlü model, somut tekrar adımı | Log ve ortam eksikse önce onları toplamak gerekir |
| Çok sayıda aynı dönüşüm | Küçük örneği doğrula, sonra betik | Her satır ayrı yorum gerektiriyorsa otomatik dönüşüm uygun olmaz |
| Estetik yön arama | Referanslar ve karşılaştırılabilir prototipler | Daha uzun açıklama yerine görsel seçim gerekir |

Tablo bir kullanım önerisidir; evrensel hız veya kalite sıralaması değildir.

## “Yavaş” olan kısmı ayır

Modelin yanıt üretmesi, araç çağrısı, dosya indirme, derleme, test, kuyruk ve onay beklemesi farklı sürelerdir. On dakikalık derleme sırasında daha hızlı model seçmek derleyiciyi hızlandırmaz. İlerleme mesajından neyin beklendiğini öğren:

> Beklemenin kaynağını ayır: model çalışması mı, araç mı, derleme mi, ağ mı? Aynı kontrol yeniden yapılıyorsa nedenini açıkla. Önceki geçerli kanıtı kullan.

Bu istek performans ölçümü başlatmak zorunda değildir; gereksiz tekrarın yerini bulmaya yarar.

## Kullanım göstergelerini doğru oku

Hesap kullanım penceresi, tek sohbetin token sayısı ve API faturalaması ayrı kavramlardır. Bir sınır penceresinde kullanılan yüzdeyi toplam para harcaması gibi yorumlama. API anahtarıyla çalışan yolların faturalaması abonelikten ayrı olabilir. Fast ve daha yüksek hız katmanlarının hesap/model koşulları ve tüketimi değişebilir; güncel fiyat ve hesap ekranını esas al. [Kullanım ve fiyatlandırma](https://learn.chatgpt.com/docs/pricing)

“Bu işi kaç liraya yaparsın?” sorusunun yanıtı kullanılan yol, gerçek ölçüm ve tarife bilinmeden kesinleştirilemez. Bunun yerine “Mevcut kullanım bilgisini göster; bilinmeyen maliyeti tahmin edilmiş gerçek gibi yazma” denebilir.

## Ultra, paralellik ve görev kapsamı

Bazı güç ayarları daha yoğun çalışma biçimleri sunar. Bu seçenekler her istemcide aynı araçlara veya alt ajan politikasına sahip olduğun anlamına gelmez. Paralel çalışma bağımsız alt işler olduğunda yarar sağlar; ortak dosyayı aynı anda değiştiren üç çalışma yeni sorun yaratabilir. Ayrıntı 14. bölümde.

## Kurgu senaryo: modeli yükseltmeden sorunu çözmek

Atölye için 200 satırlık etkinlik verisi temizleniyor. Codex her satırı tek tek yeniden yorumlayıp yavaş ilerliyor. Sorun muhakeme zorluğu değil, tekrarlı dönüşüm. Önce tarih biçimi ve boş alan kurallarını birkaç temsilî satırda netleştir; sonra aynı kuralları betikle uygulat. Beklenen çıktı, kaynak satır sayısını koruyan ve değişen alanları gösteren bir dönüşüm raporudur. Örnekler başarısızsa bütün dosyaya geçilmez.

## Kontrol listesinde karşılığı

- [2.2 Bağlam ve kullanım göstergelerini kontrol et.](../codex-kontrol-listesi.md#m-2-2)
- [5.1 Alt ajan modelini göreve göre belirle.](../codex-kontrol-listesi.md#m-5-1)
- [5.2 Model adını erişilebilir katalogdan seç.](../codex-kontrol-listesi.md#m-5-2)
- [5.3 Düşünme seviyesini işin güçlüğüne göre değiştir.](../codex-kontrol-listesi.md#m-5-3)
- [5.4 Kullanımı ve bekleme nedenini ayrı kaydet.](../codex-kontrol-listesi.md#m-5-4)
- [5.5 Hız modunu ve güçlü ikinci görüşü seçerek kullan.](../codex-kontrol-listesi.md#m-5-5)

[İçindekiler](README.md) · [← Bağlam, bellek ve devamlılık](06-baglam-bellek.md) · [Dosyalar ve çalışma ortamları →](08-ortamlar.md)
