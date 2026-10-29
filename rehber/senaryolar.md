# On iki kurgu kullanım senaryosu

Belge kontrolü: 2026-10-29.

Eğitimde ilk anlatılacak akışlar [araştırma](is-arastirma.md), [veri](is-veri.md) ve [sayfa düzeltme](is-sayfa.md) örnekleridir. Aşağıdaki on iki kısa senaryo farklı işlere uyarlamak için hızlı başvurudur.

Aşağıdaki senaryolar eğitim için üretilmiş kurgulardır. Gerçekte yürütülmüş görev, başarı ölçümü veya müşteri hikâyesi değildir. İstekler kopyalanabilir; dosya, hesap ve hedefleri kendi işine göre seç. Bunlar katılımcı alıştırması değil, anlatıcının bir özelliği somutlaştırabileceği örneklerdir.

<a id="1-arastirmadan-karar-notuna"></a>

## 1. Araştırmadan karar notuna

**Durum:** Küçük bir eğitim topluluğu üç etkinlik platformunu karşılaştırmak istiyor.

> Üç platformu kayıt akışı, veri dışa aktarma ve toplam maliyeti anlamaya yarayan bilgiler açısından karşılaştır. Resmî sayfaları aç. Belgelenmeyen koşulları bilinmiyor diye işaretle. Bizim 60 kişilik ücretsiz etkinliğimiz için önerini ve önerini değiştirecek koşulu yaz.

**Öğrettiği:** Kaynak seçimi, değişen fiyat bilgisi ve karar gerekçesi. Beklenen çıktı, özellik yığını yerine seçimi etkileyen farklardır. Açılmayan fiyat sayfasına uydurma rakam konmaz. Kullanılabilecek yollar: web araştırması, bağlı belge, karar notu.

<a id="2-kod-bilmeden-bozuk-sayfayi-tarif-etmek"></a>

## 2. Kod bilmeden bozuk sayfayı tarif etmek

**Durum:** Telefonda uzun başlık menüyü taşıyor.

> Bu sayfada 320 piksel genişlikte uzun başlık yatay kaydırma yaratıyor. Ekteki görüntü mevcut sorun. Mevcut tasarımı koruyarak düzelt; uzun başlık, kısa başlık ve açık menü durumlarını yerel tarayıcıda kontrol et.

**Öğrettiği:** Gözlenen belirtiyi doğru bağlamla vermek. Beklenen çıktı ilgili kaynak düzeltmesi ve açılmış görünüm kanıtıdır. Ekran görüntüsü, yanlış URL'yi test etme riskini tek başına çözmez. Araçlar: dosya erişimi, yerleşik tarayıcı, değişiklik görünümü.

<a id="3-tabloyu-temizlerken-kimligi-korumak"></a>

## 3. Tabloyu temizlerken kimliği korumak

**Durum:** Aynı isimli katılımcılar ve farklı tarih biçimleri var.

> Kaynak tabloyu koru. Tarihleri tek biçime dönüştür; aynı adları otomatik birleştirme. Kayıt anahtarı yoksa bunu belirt. Belirsiz satırları ayrı göster. Kaynak ve sonuçtaki kayıtları eşleştirip kayıp ve tekrar kontrolü yap.

**Öğrettiği:** Temiz görünen çıktı ile doğru veri arasındaki fark. Beklenen çıktı düzenlenebilir tablo, dönüşüm kuralları ve açık belirsizliklerdir. Araç: dosya veya bağlı tablo; tekrar eden dönüşüm için betik.

<a id="4-kaynagi-dogrulanmis-metni-cevirmek"></a>

## 4. Kaynağı doğrulanmış metni çevirmek

**Durum:** Türkçe makale kaynak bakımından onaylanmış, İngilizce sürüm gerekiyor.

> Bu metni anlamını ve atıflarını koruyarak İngilizceye aktar. Yeni iddia ve kaynak ekleme. Olasılık bildiren cümleleri kesinleştirme. Son kontrolde anlam, alıntı, kişi adları ve bağlantıları kaynakla karşılaştır.

**Öğrettiği:** Görev sınırı. Beklenen çıktı çeviri ve gerekiyorsa kısa anlam sorularıdır; bütün konunun sıfırdan araştırılması değildir. Araç: belge ve uygun yazım skill'i.

<a id="5-yaratici-yonu-secilebilir-yapmak"></a>

## 5. Yaratıcı yönü seçilebilir yapmak

**Durum:** Duyuru sayfası teknik olarak doğru ama sıradan görünüyor.

> Aynı gerçek metin ve görsellerle iki farklı düzen üret. Birinde editoryal okuma, diğerinde program tarama öne çıksın. Renk değiştirerek iki kopya üretme; bilgi sırasını ve kullanım farkını göster. Seçimden önce ana sayfayı değiştirme.

**Öğrettiği:** Karşılaştırılabilir prototip, referans ve karar yetkisi. Beklenen çıktı açılıp incelenen iki yön ve farklarının açıklamasıdır. Araç: HTML/yerel prototip ve tarayıcı.

<a id="6-hata-ayiklarken-cozumu-pesinen-dayatmamak"></a>

## 6. Hata ayıklarken çözümü peşinen dayatmamak

**Durum:** Bildirime dokununca uygulama bazen kapanıyor.

> Hatanın tekrar koşulunu log ve mevcut kaynakla araştır. Açık uygulama, arka plan ve soğuk başlangıç durumlarını ayır. Önce hatayı açıklayan kanıtı bul; ilgili düzeltmeyi yap ve hangi durumun cihazda henüz denenmediğini belirt.

**Öğrettiği:** Hipotez, regresyon ve cihaz kanıtı farkı. Beklenen çıktı gerekçeli düzeltme, ilgili kontroller ve sınırlarıdır. “Bütün mobil senaryolar geçti” gibi kapsamsız sonuç üretilmez.

<a id="7-paralel-arastirma-tek-sonuc"></a>

## 7. Paralel araştırma, tek sonuç

**Durum:** Büyük rehberin hem kaynak hem kullanım açısından incelenmesi gerekiyor.

> İki bağımsız alt ajan kullanmana yetki veriyorum. Biri yalnız ürün iddialarını resmî kaynaklarla kontrol etsin; diğeri başlangıç düzeyi açıklama boşluklarını arasın. Dosyaları değiştirmesinler. Bulguları sen birleştir ve çelişkileri çöz.

**Öğrettiği:** Alt görev sınırı ve entegrasyon sahipliği. Beklenen çıktı iki özetin yapıştırılması değil, önceliklendirilmiş tek incelemedir. Ana görev alt ajan araçlarını desteklemiyorsa yapılmış gibi sunulmaz.

<a id="8-ses-ve-ekran-baglamiyla-hizli-yonlendirme"></a>

## 8. Ses ve ekran bağlamıyla hızlı yönlendirme

**Durum:** Görünen program tablosunda yanlış bölüm fark ediliyor.

> Ekrandaki tabloyu mevcut bağlam olarak kullan. Üstteki tarih başlığı yanlış; veri satırlarını değiştirmeden başlığı düzelt. Hangi dosya veya bağlı belgeyi düzenlediğini belirt.

**Öğrettiği:** Görüntü hedef gösterir; düzenlenecek kaynağın bulunması ayrıca gerekir. Beklenen sonuç desteklenen ses/ekran bağlamıyla hedefli düzeltmedir. Görünmeyen tüm belgelerin otomatik okunduğu varsayılmaz.

<a id="9-tekrarli-raporu-otomasyona-donusturmek"></a>

## 9. Tekrarlı raporu otomasyona dönüştürmek

**Durum:** Haftalık kaynak raporunun yöntemi birkaç gerçek çalışmada tutarlı hâle gelmiş.

> Bu yöntemi haftalık bağımsız rutin olarak kur. Aynı haftaya ait rapor varsa güncelle, ikinci kopya üretme. Kaynak bulunamazsa uydurma özet yerine engeli yaz. Yayın yapma; yalnız belirlenen klasöre taslak üret.

**Öğrettiği:** Zamanlama, tekrar güvenliği ve yayın yetkisi. Beklenen çıktı doğrulanmış zamanlama ve ilk koşumun gözlenen durumudur. Yerel bilgisayarın çalışma koşulu hesaba katılır.

<a id="10-teslimi-gercek-hedefte-bitirmek"></a>

## 10. Teslimi gerçek hedefte bitirmek

**Durum:** Kullanıcı mevcut web sayfasındaki onaylanmış düzeltmenin yayına alınmasını açıkça istiyor.

> Onayladığım değişikliği belirtilen depoya ve canlı ortama yayınla. Önce ilgili kontrolleri tamamla. Dağıtımdan sonra doğru sürümün canlı URL'de göründüğünü doğrula. Başarısız veya bekleyen aşamayı açık bırak.

**Öğrettiği:** Commit, push, deployment ve kamuya açık görünüm ayrımı. Beklenen çıktı hedefte gözlenen sürümdür. Düzeltmeyi yerelde bırakıp “yayında” demek tamamlanma değildir.

<a id="11-belge-ve-sunum-uretimini-incelemek"></a>

## 11. Belge ve sunum üretimini incelemek

**Durum:** Uzun rapordan yönetim toplantısına kısa sunum gerekiyor.

> Kaynak rapordaki karar, dayanak ve belirsizlikleri koruyarak sunum hazırla. Her slayt tek kararı desteklesin. Kaynakta olmayan sayı ekleme. Dosyayı önizle; taşan metin, okunamayan grafik ve kopan kaynak bağlantılarını düzelt.

**Öğrettiği:** Düzenlenebilir çıktı, kaynak sadakati ve görsel kontrol. Beklenen dosya türünü ve hedef uygulamayı belirtmek gerekir. Bir PPTX dosyasının oluşması slaytların incelendiğini göstermez.

<a id="12-eski-isten-guvenilir-devam"></a>

## 12. Eski işten güvenilir devam

**Durum:** Bir ay önce bırakılan değişiklik yeniden açılıyor.

> Proje notlarını ve mevcut Git durumunu karşılaştır. Eski nottaki hangi işin zaten tamamlandığını bul. Bana ait değişiklikleri koru. Geçerli kanıttan devam et; eski yayın yetkisini yeni işlem için varsayma.

**Öğrettiği:** Bellek, devir ve güncel kaynak ilişkisi. Beklenen çıktı, yeniden keşfedilen eski plan değil, bugünkü durumdan başlayan çalışma olur.

[İçindekiler](README.md)
