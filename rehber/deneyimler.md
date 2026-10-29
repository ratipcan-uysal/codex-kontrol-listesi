# Gerçek deneyimlerden dokuz ders

Belge kontrolü: 2026-10-29.

Bu bölüm, bu rehber hazırlanırken seçili proje raporları ve ilgili konuşma parçaları üzerinden doğrulanan gerçek deneyimleri anonimleştirir. Tüm sohbet geçmişinin eksiksiz tarandığı iddiası yoktur. Özel kayıtlar, hesaplar, yerel yollar ve ham konuşmalar kamuya taşınmaz. Bölümlerdeki “Kurgu senaryo” metinleri bu vakaların kaydı değildir.

<a id="c01"></a>

## C01

<a id="uygulama-yok-iddiasini-duzeltmek"></a>

### “Uygulama yok” iddiasını düzeltmek

**İstenen iş:** Daha önce üzerinde çalışılmış masaüstü uygulamasını başlatmak. İlk bakılan derleme ve uygulama konumlarında hazır paket bulunamadı; mevcut kaynaktan Release derlemesi başladı.

**Senin müdahalen:** “buranın app'i nasıl yok ya test ettik bir ton”. Bu cümle, geçmiş test bilgisini yeniden görünür yaptı ve yokluk iddiasına itiraz etti.

**Neyi değiştirdi?** Konuşma sırası derlemenin bu itirazdan önce başladığını gösteriyor. Bu yüzden “kullanıcı düzeltti, ardından uygulamayı yeniden derledik” diye bir neden–sonuç kurmuyoruz. Düzelen şey raporun kesinliği oldu: ilk bakılan konumlarda paket bulunamaması, uygulamanın hiç var olmadığı anlamına gelmiyordu.

**Gözlenen sonuç:** Kaynak proje üzerinden derleme tamamlandı, uygulama süreci gözlendi. Paketin neden önceki konumlarda bulunmadığı bilinmiyordu. Görünür pencere ve yeni ses işlevleri ayrıca doğrulanmadı. Kontrol tarihi: 28 Ekim 2026.

**Başka işte kullan:** “Aradığın kapsam neydi?” sorusu, modelin gözlemini geniş bir iddiaya dönüştürdüğü noktayı bulur. [Rapor örneğindeki](is-veri.md) bilinen tahsilat/tam toplam ayrımı aynı alışkanlığın veri işindeki karşılığı.

<a id="c02"></a>

## C02

<a id="eksik-gorunen-icerik-icin-yanlis-isi-baslatmamak"></a>

### Eksik görünen içerik için yanlış işi başlatmamak

**Başlangıç:** Ürün incelemesinde eski “ilk kullanım akışı yok” notu ve İngilizce görünümde eksik bağlam sorunu vardı. Eski nota dayanmak yeni bir giriş akışı önermeye, İngilizce eksikliği ise tekrar çeviri yaptırmaya götürebilirdi.

**İncelemenin değiştirdiği karar:** Güncel kaynak açıldı. İlk kullanım akışı vardı; Debug/Release koşulları ayrılıyordu. İngilizce açıklamalar kaynakta bulunuyordu, yerel uygulama paketinde yoktu. Dolayısıyla önce içeriği yeniden üretmek yerine üretim ve paketleme zincirine bakmak gerekiyordu.

**Sonuç ve sınır:** Kanıt, yapılacak işin katmanını değiştirdi. Bu incelemede uygulama onarımı, yeni cihaz testi veya mağaza yayını yapılmadı. Bulguyu belirli bir kullanıcı cümlesi tetiklemiş gibi anlatmıyoruz; kayıt kaynak temelli incelemeyi destekliyor. Kontrol tarihi: 27 Ekim 2026.

**Başka işte kullan:** “Bu bilgi hiç üretilmedi mi, yoksa doğru yere ulaşmadı mı?” diye ayır. [Araştırma örneğinde](is-arastirma.md) onaylanmış karar notunu yeniden araştırmadan sunuma taşıma aynı aktarım disiplinini kullanıyor.

<a id="c03"></a>

## C03

<a id="testin-gecmesiyle-metnin-gorunmesi-farkliydi"></a>

### Testin geçmesiyle metnin görünmesi farklıydı

**İstenen iş:** İki yerel arayüz adayını gerçek içerik uzunlukları ve büyük yazıyla karşılaştırmak. Klavye ile giriş alanının konum kontrolü geçti.

**Yönü değiştiren kanıt:** Ekran görüntüsü açıldığında ikinci metin satırının örtüldüğü görüldü. Bu, kullanıcıdan geldiği kaydedilmemiş bir müdahale; görsel inceleme bulgusu olarak anlatıyoruz. Sayısal konum kontrolü, metnin tamamının okunabilirliğini ölçmüyordu.

**Yapılan değişiklik:** Giriş alanı üste, açılabilir kaynak bağlamı altına alındı. Son kontrol iki satırlık taslağı ve imleci görünür gösterdi. Başarısız önceki görüntüler son kabul diye kullanılmadı.

**Sonuç ve sınır:** Yerel prototipte ilgili durum kapandı. Tasarım seçimi, ana ürüne aktarım, fiziksel cihaz ve gerçek VoiceOver doğrulaması bu sonucun dışında kaldı. Kontrol tarihi: 20 Ekim 2026.

**Başka işte kullan:** Testin hangi iddiayı ölçtüğünü söyle ve gösterilen çıktıyı aç. [Web sayfası örneğinde](is-sayfa.md) aynı koşulda önce/sonra görüntüsü ve bağlantı davranışı ayrı kontrol edilir.

<a id="c04"></a>

## C04

<a id="teknik-teslim-tamamlanirken-yaratici-tercih-acik-kalabilir"></a>

### Teknik teslim tamamlanırken yaratıcı tercih açık kalabilir

**İstenen iş:** Kitap kapaklarından video üretmek; ardından geçiş ritmine uyacak müzik eklemek. Kapak sayısı, benzersizlik ve videonun tam çözümlenmesi kontrol edildi.

**Senin müdahalen:** “sıkıcı bir müzik, daha yaratıcı ol”. Bu, dosyanın teknik bütünlüğüne değil yaratıcı yöne itirazdı. Sonraki isteğin “müziksiz halini bana gmail'e atabilir misin” oldu.

**Neyi değiştirdi?** Son teslim hedefi sessiz sürümün e-postayla gönderilmesine döndü. Kayıt, sessiz teslimi destekliyor; beğenilen yeni bir müziğin bulunup tamamlandığını göstermiyor. Teknik başarı, yaratıcı memnuniyet ve teslim aynı ölçü değildi.

**Başka işte kullan:** Beğenmediğin boyutu seçilebilir yönlere aç: ritim, doku, yoğunluk veya referans. Bu öneri vakadan çıkardığımız yöntemdir; o konuşmada bu çerçeveyle başarılı müzik üretildiğini iddia etmiyoruz. [Yaratıcı yönü tarif etme örneği](13-tasarim.md#kurgu-senaryo-daha-yaratici-muzik-istegini-acmak).

**Sınır:** E-postayla teslim kaydı sosyal platform yayını değildir. Adres ve ileti kimlikleri kamuya alınmadı. Kontrol tarihi: 19 Ekim 2026.

<a id="c05"></a>

## C05

<a id="arama-detaylari-ac-dugmesinin-durumunu-degistirdi"></a>

### Arama, “detayları aç” düğmesinin durumunu değiştirdi

**Gözlenen:** Kontrol listesinde arama ayrıntıları açabiliyordu; genel aç/kapat düğmesi önceki duruma göre davrandığında tutarsızlık oluştu. Düğmenin görünür ayrıntıların gerçek durumundan türetilmesiyle sorun giderildi ve regresyon kontrolü eklendi.

**Ders:** Etkileşim durumunu tek bir önceki tıklamadan çıkarma. Arama, filtre ve toplu işlem aynı durumu etkiliyorsa birlikte sınanmalı.

**Sınır:** Bu belirli sayfa davranışı için kanıttır; her arama uygulaması aynı yapıyı kullanmaz. [Önceki doğrulama raporu](../DOGRULAMA.md), 21 Ekim 2026.

<a id="c06"></a>

## C06

<a id="ayni-sayfada-baglanti-degisimi-ilk-yuklemeyle-ayni-olay-degildir"></a>

### Aynı sayfada bağlantı değişimi, ilk yüklemeyle aynı olay değildir

**Gözlenen:** Maddeye derin bağlantı, sayfa ilk açıldığında çalışırken aynı sayfadaki başka hash bağlantısına geçişte beklenen açılmayı sağlamıyordu. `hashchange` davranışı ele alındı ve kontrol edildi.

**Ders:** Bir bağlantının doğrudan açılması ile gezinme sırasında kullanılması ayrı senaryolardır. Kullanıcının gerçek yolunu test et.

**Sınır:** Sayfa içi bağlantı davranışıdır; uzak yayın veya bütün tarayıcı uyumluluğu kanıtı değildir. [Önceki doğrulama raporu](../DOGRULAMA.md), 21 Ekim 2026.

<a id="c07"></a>

## C07

<a id="ag-engeli-yanlis-kimlik-bilgisi-demek-degildir"></a>

### Ağ engeli, yanlış kimlik bilgisi demek değildir

**Gözlenen:** Kısıtlı ortamda başarısız kimlik kontrolü, uygun erişimle yapılan salt okuma kontrolüyle aynı sonucu vermedi.

**Ders:** Hata metnini nedenin tamamı sayma. DNS/ağ, sandbox, oturum ve hizmet iznini ayrı sınayarak ilerle; kanıt olmadan anahtar değiştirme.

**Sınır:** Bu vaka, bütün kimlik hatalarının ağdan kaynaklandığını söylemez. 21 Ekim 2026 tarihli çalışma kaydı. Özel erişim günlüğü bu kamuya açık rehbere eklenmez.

<a id="c08"></a>

## C08

<a id="ayni-isimli-cli-farkli-ikili-olabilir"></a>

### Aynı isimli CLI, farklı ikili olabilir

**Gözlenen:** PATH üzerinden çağrılan CLI ile masaüstü uygulamasının beraberinde gelen CLI farklı sürümlerdeydi. Seçili komut desteği güncel ikilinin yardım çıktısıyla kontrol edildi.

**Ders:** Sürüm karşılaştırırken çağrılan dosyayı ve yüzeyi belirt. Eski CLI'da komut bulunmaması, uygulamanın tamamında yeteneğin bulunmadığını kanıtlamaz.

**Sınır:** Sürüm numaraları tarihli gözlemdir. Güncel kurulumun `--version` ve `--help` çıktısı yeniden kontrol edilmelidir. [Önceki kaynak denetimi](../KAYNAKLAR.md), 21 Ekim 2026.

<a id="c09"></a>

## C09

<a id="bu-rehberde-daha-iyi-yi-uc-ayri-karara-cevirmek"></a>

### Bu rehberde “daha iyi”yi üç ayrı karara çevirmek

**İstenen iş:** Codex'i başlangıçtan ileri kullanıma anlatan, gerçek deneyimlere dayalı bir eğitim kaynağı. İlk sürüm 18 bölüm, komutlar ve senaryolar içeriyordu; uygulama görseli yoktu.

**Senin müdahalen:** İlk kullanıcı gözüyle yeniden inceleme istedin; görsellerin eksikliğini ve yeşil arka planın bunaltmasını ayrı ayrı belirttin. Böylece içerik, öğretim ve görünüm tek bir belirsiz “iyileştir” isteğinde kalmadı.

**Gözlenen değişiklik:** İlk dosyayı üretme yolu ve eksik kullanım başlıkları eklendi; altı resmî arayüz gösterimi açıklamalarıyla yerleştirildi. Geniş yeşil yüzeyler nötr renklere döndü, düzen korundu. 107 kontrol maddesi ve işaretleme biçimi değişmedi. Bu değişiklikler GitHub ve canlı Pages üzerinde kontrol edildi. [29 Ekim revizyonunun kanıtı](../dogrulama/rehber-revizyon-20261029/INCELEME.md) · [Yayın](../DOGRULAMA.md).

**Sonraki ayrım:** “Yapabileceğimiz en iyi eğitim materyali bu mu?” sorusu, kapsamlı bir başvuru kaynağının eğitim anlatısını tek başına kurmadığını ortaya çıkardı. Şimdi okuduğun örnek işler bu ikinci isteğin uygulaması. Dinleyicilerin daha iyi öğrendiğine ilişkin ölçüm yapılmadı; içerik ve ürün kontrollerini öğrenme başarısı saymıyoruz.

**Başka işte kullan:** Geri bildirimde sorunlu boyutu ayır. Eksik bilgiye içerik, yanlış sıraya anlatı, yetersiz gösterime görsel, bunaltan zemine palet müdahalesi gerekir. Her eleştiride bütün ürünü baştan kurmak zorunda değilsin.

[İçindekiler](README.md)
