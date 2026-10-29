# Araştırmadan karar ve sunuma

İçerik güncellemesi: 2026-10-30. Kaynak kontrol tarihleri kaynak dizinindedir.

**Kurgu iş:** Atölye, 60 kişilik ücretsiz bir buluşma için kayıt sistemi seçecek. Katılımcıya hesap açtırmak istemiyor; katılımcı listesini CSV olarak indirebilmesi gerekiyor. Etkinlik başına bütçe 3.000 TL. Aşağıdaki platform adları, fiyatlar ve belge parçaları eğitim için uyduruldu. Gerçek bir ürün karşılaştırması veya yapılmış satın alma yok.

Bu işin sonunda iki şey görünmeli: seçimin dayanağı olan kısa karar notu ve aynı kararı anlatan sunum taslağı. Araştırma, taslak ve görsel düzeltme tek bir iş içinde birbirini besliyor.

**Karar bilgisini biçimler arasında koru**

1. **Girdi:** Ölçüt + kaynak paketi
2. **Seçim:** Zorunlu koşulla ele
3. **Karar:** Gerekçeyi ve sınırı yaz
4. **Çıktı:** Aynı bilgiden sunum

<a id="1-i-stekten-once-kararin-olcusunu-kur"></a>

## 1. İstekten önce kararın ölçüsünü kur

“En iyi platformu bul” demek araştırmanın nereye kadar süreceğini açık bırakır. Bu işte kaliteyi üç koşul belirliyor: hesapsız kayıt, CSV dışa aktarma ve bütçe. Renk veya yüzlerce entegrasyon ancak bu koşulları sağlayan seçenekler arasında fark yaratıyorsa önemli.

> Atölye'nin 60 kişilik etkinliği için kayıt sistemi seçiyoruz. Hesapsız kayıt ve CSV dışa aktarma zorunlu; bütçe etkinlik başına 3.000 TL. Önce bu ölçütlerle bir karşılaştırma çıkar, sonra tek öneri ve öneriyi değiştirecek koşulu yaz. Henüz hesap açma veya satın alma yapma.

İş belirsizse `/plan` ile ölçütleri birlikte netleştirebilirsin. Burada ölçütler zaten belli olduğundan doğrudan uygulama isteği yeterli. Bir planın varlığı ayrıca karar kalitesini garanti etmez. [Plan komutu](https://learn.chatgpt.com/docs/reference/slash-commands)

<a id="2-kaynak-yiginini-karsilastirilabilir-kanita-donustur"></a>

## 2. Kaynak yığınını karşılaştırılabilir kanıta dönüştür

Anlatıcı [kurgu kaynak paketini](ornekler/arastirma-kaynaklari.md) açar. Üç kısa belge parçası şöyle bir karşılaştırmayı destekliyor:

| Kurgu seçenek | Etkinlik bedeli | Hesapsız kayıt | CSV | İlk karar |
|---|---|---|---|---|
| Kayıt A | 0 TL | Var | Yok | Zorunlu dışa aktarma koşulunu karşılamıyor |
| Kayıt B | 2.500 TL | Var | Var | Üç koşulu da sağlıyor |
| Kayıt C | 1.700 TL | Yok | Var | Katılımcı hesabı zorunlu |

Gerçek işte bu tabloyu güncel resmî sayfalarla kurdur. Kaynak URL'sini, okunan koşulu ve kontrol tarihini birlikte tut. “CSV var” ifadesinin seçtiğin pakete mi, daha pahalı bir pakete mi ait olduğunu sor. Açılmayan sayfayı tahminle tamamlama. Araştırma yolu seçimi [web ve tarayıcı bölümünde](09-web-tarayici-bilgisayar.md).

**Kurgu ara hata:** İlk taslak C'yi en ucuz ücretli seçenek olduğu için öneriyor. Sorun yetersiz yaratıcılık veya düşük düşünme seviyesi değil; zorunlu koşulun sıralamaya katılmaması.

> C daha ucuz, fakat katılımcıya hesap açtırmama koşulunu karşılamıyor. Zorunlu koşulları önce eleme ölçütü yap. Uygun seçenekler arasında maliyeti karşılaştır. Kaynak paketini değiştirme.

Bu düzeltme bir sıfatı değiştirmiyor, karar yöntemini düzeltiyor. B'nin bütçenin altında kalan payı 500 TL; bu sayının rahatlık payı mı yoksa başka masraflara yetecek bütçe mi olduğu ayrı bir değerlendirme. Örnekte ek vergi veya ödeme komisyonu bilgisi yok; toplam maliyetin bunları içerdiği varsayılmıyor.

<a id="3-secimi-tek-cumleye-sigdir-gerekceyi-kaybetme"></a>

## 3. Seçimi tek cümleye sığdır, gerekçeyi kaybetme

İyi karar notu bütün araştırmayı tekrar anlatmaz. [Örnek karar notunda](ornekler/karar-notu.md) öneri, gerekçe, elenen seçenekler ve açık koşul birlikte duruyor:

> Kurgu belgelerdeki koşullara göre Kayıt B öneriliyor: hesapsız kayıt ve CSV gereksinimlerini karşılıyor, listelenen 2.500 TL bedel bütçenin altında. Ek ücretler doğrulanmalı. Hesap açma koşulu kabul edilirse C yeniden değerlendirilebilir.

Öneriyi değiştirecek koşulu yazmak, kararın hangi varsayıma dayandığını görünür yapar. Kullanıcı daha sonra “hesap açmak sorun değilmiş” derse bütün araştırmayı baştan yapmak gerekmez; değişen ölçütle sıralama yenilenir.

Bizim gerçek işimizde de yanlış katmanda çözüm üretme riski görüldü: İngilizce içerik kaynakta vardı ama uygulama paketine ulaşmamıştı. Sıfırdan çeviri istemek yerine aktarım zincirine bakmak gerekiyordu. Bu, araştırmayı tekrarlamadan önce eksik olanın bilgi mi, aktarım mı olduğunu ayırmayı öğretiyor. [Gerçek vaka C02](deneyimler.md#c02)

<a id="4-dogrulanmis-nottan-yeni-bicimler-uret"></a>

## 4. Doğrulanmış nottan yeni biçimler üret

> Bu karar notunu ana kaynak kabul et. Karar, dayanak ve açık koşulu taşıyan üç slaytlık sunum taslağı hazırla. Yeni fiyat veya özellik ekleme. Ayrıca aynı kararı 100 kelimeyi geçmeyen ekip duyurusuna dönüştür.

Anlatıcı [örnek sunum taslağını](ornekler/sunum-taslagi.md) açar. Aynı B önerisi, aynı 2.500 TL ve aynı ek ücret belirsizliği korunuyor. Slayt için daha kısa yazılması, “ek ücretler bilinmiyor” cümlesinin silinmesini haklı çıkarmaz.

![Sohbetin yanında sunum önizlemesi. Solda üretim isteği ve dosya bağlantısı, sağda slayt listesi ve seçili slayt var. Dosyayı yalnız teslim mesajından değerlendirmek yerine önizlemede incele.](assets/preview.png)

**Sohbetin yanında sunum önizlemesi.** Solda üretim isteği ve dosya bağlantısı, sağda slayt listesi ve seçili slayt var. Dosyayı yalnız teslim mesajından değerlendirmek yerine önizlemede incele. [Tam boyut](assets/preview.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/artifacts-viewer) · 2026-10-29.

1. **Nereye bak:** Soldaki output.pptx bağlantısına, sağdaki slayt listesine.
2. **Ne yap:** Sorunlu slaytı seç; yalnız o parçanın değişmesini, sayıların korunmasını iste.
3. **Ne gör:** Son dosyada aynı karar ve verilerle daha okunur bir slayt.

Resmî görselde farklı bir sunum gösteriliyor; Atölye için çalıştırılmış oturum ekranı değil. Buradan öğrenilecek hareket, üretim mesajından dosyanın önizlemesine geçmek. Bir slayt kalabalıksa bütün sunumu yeniden yazdırmadan “yalnız ikinci slaytı sadeleştir; karar, sayı ve kaynakları koru” diye belirt. Desteklenen önizlemelerde işaretlenen alan bağlam olarak gönderilebilir. [Dosya önizleme ve yorum](https://learn.chatgpt.com/docs/artifacts-viewer)

<a id="5-i-sin-bittigini-hangi-ciktida-gorursun"></a>

## 5. İşin bittiğini hangi çıktıda görürsün?

Bu örnekte teslim, karar notu ve sunum taslağıdır. Bir satın alma veya herkese açık duyuru yok. Gerçek işte PPTX istersen oluşturulan dosyayı açıp slaytları incelet; bu sayfadaki indirilebilir Markdown taslağını PPTX dosyası sanma.

**Başka işte kullanacağın ders:** Önce karar ölçütünü sabitle, sonra uygun kaynakları araştır. Doğrulanmış ana metni yeni biçimlere dönüştürürken iddiaları sabit tut. Her biçim değişikliğini yeni araştırmaya çevirmek, onaylanmış bilgiye gereksiz değişken ekler.

Sonraki örnek aynı yaklaşımı sayısal veriye taşır: [tablodan güvenilir rapora](is-veri.md).

[İçindekiler](README.md) · [Dağınık tablodan güvenilir rapora →](is-veri.md)
