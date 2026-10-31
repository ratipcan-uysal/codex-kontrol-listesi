# 7. Model, düşünme seviyesi, hız ve kullanım

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

En yüksek düşünme ayarı her işin en iyi seçimi değildir. İyi seçim, görevin hangi kısmının zor olduğuna bağlıdır: karar vermek, kaynak bulmak, dosya düzenlemek veya uzun süren bir aracı beklemek.

<a id="birbirinden-ayri-uc-tercih"></a>

## Birbirinden ayrı üç tercih

**Model**, görevi yorumlayan ve araçları kullanan sistemdir. **Düşünme seviyesi**, karar için ayrılan çabayı etkiler. **Hız seçeneği**, desteklenen modellerde hizmet hızını ve kullanım tüketimini etkileyebilir. Model seçmek bir tarayıcı eklentisi kurmaz; düşünmeyi yükseltmek eksik kaynak erişimini açmaz. [Modeller](https://learn.chatgpt.com/docs/models) · [Hız](https://learn.chatgpt.com/docs/agent-configuration/speed)

<a id="hangi-ise-hangi-modelle-baslamali"></a>

## Hangi işe hangi modelle başlamalı?

31 Ekim 2026’da kontrol edilen resmî rehberin dört güncel modeli aşağıda. Model rolleri belgeye, Atölye örnekleri bizim kullanım önerimize dayanır; karşılaştırmalı performans testi yapmadık. Kendi hesabında görünen seçenekleri esas al. [Güncel modeller](https://learn.chatgpt.com/docs/models)

| Model | İyi başlangıç olduğu işler | Atölye’de örnek istek |
|---|---|---|
| **GPT-6 Luna** | Dar kapsamlı düzenleme, bilgi çıkarma, tekrarlı işler | “Bu onaylı programdan tarih ve saatleri çıkar; bulunmayanı ekleme.” |
| **GPT-6.1 Terra** | Kaynağa dayalı yazı, görsel yorumlama, sonucu belirli bilgisayar işleri | “Karar notunu kısa ekip duyurusuna dönüştür; belirsiz ücretleri koru.” |
| **GPT-6.1 Sol** | Karmaşık, birden çok dosya veya çıktı içeren, revizyon gerektiren işler | “Bu brief’ten etkinlik sitesini üret; dar ekranı ve kayıt bağlantısını kontrol et.” |
| **GPT-6 Astra** | Zor muhakeme, geniş bağlam ve sıkı gereksinimleri uzlaştırma | “Birbirini tutmayan koşulları çöz; hangi seçeneğin neden elendiğini göster.” |

Bu tablo görev yasağı değildir: Terra sınırlı kod düzeltmesi, Astra kısa yazı da yapabilir. Seçimi “kod mu, yazı mı?” kadar belirsizlik ve birbirine bağlı kararların sayısı belirler. Eski sürüm adlarını bu dört adla eşanlamlı sayma; sürüm değişince aynı işi yeniden karşılaştır. [Seçim rehberi](https://learn.chatgpt.com/docs/model-selection)

<a id="model-dusunme-ve-hizi-uygulamada-sec"></a>

## Model, düşünme ve hızı uygulamada seç

Mesaj alanının altındaki model/düşünme kontrolünü aç. Masaüstünde `/model` model seçer, `/reasoning` düşünme çabasını değiştirir; `/fast` desteklenen Fast hizmet katmanını açıp kapatır. Bunları mesajın içine süslü bir talimat olarak yazmak yerine komut menüsünden seç. Görünür seçenekler ortama ve erişime bağlıdır. [Komutların kapsamı](https://learn.chatgpt.com/docs/reference/slash-commands)

Resmî başlangıç örnekleri: dar bir düzenleme için **Luna · Low**, revize edilecek çok parçalı teknik iş için **Sol · Medium**, zor analiz ve sıkı koşullar için **Astra · Extra high**. Emin değilsen varsayılan çabayla başla; gerekli bilgi elindeyken karar kalitesi yetersiz kalıyorsa yükselt. Bunlar her iş için zorunlu ayarlar değil. [Model ve çaba seçimi](https://learn.chatgpt.com/docs/model-selection)

Fast bir hizmet hızı tercihidir; aynı şey daha güçlü model veya daha yüksek düşünme seviyesi demek değildir. Kullanım tüketimini artırabilir. Model beklemesini azaltmakla dosya yükleme veya derleme süresini azaltmayı ayır. [Hız ve kullanım](https://learn.chatgpt.com/docs/agent-configuration/speed)

**Üç ayrı seçim, tek iş**

1. **İşin güçlüğü:** Dar işlem mi, birçok kararı birleştiren iş mi? Modeli buna göre seç.
2. **Karar kalitesi:** Bilgi tamam ama muhakeme yetmiyorsa düşünme çabasını değiştir.
3. **Bekleme:** Model yanıtını bekliyorsan hız seçeneğini değerlendir; araç beklemesini ayrı tut.
4. **Sonuç:** Aynı kaynak ve kabul koşullarıyla karşılaştır; yeterli sonucu veren seçimi koru.

**Anlatıcı gösterimi:** Modelin adını, seçili düşünme seviyesini ve varsa hız tercihini ayrı ayrı işaret et. Sonra [karar ve sunum işine geç](is-arastirma.md). Dinleyicinin bütün seçenekleri ezberlemesi gerekmiyor; aynı işi yeniden değerlendirirken hangi tercihi değiştirdiğini bilmesi gerekiyor.

<a id="ayni-is-buyuyunce-secim-nasil-degisir"></a>

## Aynı iş büyüyünce seçim nasıl değişir?

**Kurgu karşılaştırma:** Onaylı nottan beş tarih çıkarmak dar bir iştir; Luna ile başlanabilir. Aynı notu farklı kitleye anlatmak için Terra denenebilir. Not, site ve sunumu birlikte güncelleyip tutarlılığını korumak Sol için uygun bir başlangıçtır. Kaynaklar birbiriyle çelişiyor ve seçim birçok koşula bağlıysa Astra’dan güçlü bir ikinci görüş alınabilir.

Her aşamada model değiştirmek zorunda değilsin. Mevcut modelin sonucu yeterliyse devam et. Karşılaştıracaksan aynı kaynakları ve kabul koşullarını ver: “Tarihleri korudu mu, açık ücreti kesinmiş gibi yazdı mı, istenen dosyayı üretti mi?” Daha uzun cevap otomatik olarak daha iyi sonuç değildir. [Karşılaştırma yöntemi](18-iyilestirmek.md)

<a id="yavas-olan-kismi-ayir"></a>

## “Yavaş” olan kısmı ayır

Modelin yanıt üretmesi, araç çağrısı, dosya indirme, derleme, test, kuyruk ve onay beklemesi farklı sürelerdir. On dakikalık derleme sırasında daha hızlı model seçmek derleyiciyi hızlandırmaz. İlerleme mesajından neyin beklendiğini öğren:

> Beklemenin kaynağını ayır: model çalışması mı, araç mı, derleme mi, ağ mı? Aynı kontrol yeniden yapılıyorsa nedenini açıkla. Önceki geçerli kanıtı kullan.

Bu istek performans ölçümü başlatmak zorunda değildir; gereksiz tekrarın yerini bulmaya yarar.

<a id="kullanim-gostergelerini-dogru-oku"></a>

## Kullanım göstergelerini doğru oku

Hesap kullanım penceresi, tek sohbetin token sayısı ve API faturalaması ayrı kavramlardır. Bir sınır penceresinde kullanılan yüzdeyi toplam para harcaması gibi yorumlama. API anahtarıyla çalışan yolların faturalaması abonelikten ayrı olabilir. Fast ve daha yüksek hız katmanlarının hesap/model koşulları ve tüketimi değişebilir; güncel fiyat ve hesap ekranını esas al. [Kullanım ve fiyatlandırma](https://learn.chatgpt.com/docs/pricing)

“Bu işi kaç liraya yaparsın?” sorusunun yanıtı kullanılan yol, gerçek ölçüm ve tarife bilinmeden kesinleştirilemez. Bunun yerine “Mevcut kullanım bilgisini göster; bilinmeyen maliyeti tahmin edilmiş gerçek gibi yazma” denebilir.

<a id="ultra-paralellik-ve-gorev-kapsami"></a>

## Ultra, paralellik ve görev kapsamı

Resmî model belgesi, Ultra modunu tek ajanlı çalışmanın ötesinde alt ajanlardan yararlanan bir seçenek olarak anlatır. Bu yüzden yalnız “biraz daha uzun düşünme” diye tanıtma. Ultra ile hız katmanı Ultrafast farklı tercihlerdir. Görünen seçenekler ve alt ajan politikası istemciye bağlıdır. [Ultra](https://learn.chatgpt.com/docs/models) · [Hız katmanları](https://learn.chatgpt.com/docs/agent-configuration/speed)

Paralel çalışma bağımsız alt işler olduğunda yarar sağlar; ortak dosyayı aynı anda değiştiren üç çalışma yeni sorun yaratabilir. Ayrıntı 14. bölümde.

<a id="kurgu-senaryo-modeli-yukseltmeden-sorunu-cozmek"></a>

## Kurgu senaryo: modeli yükseltmeden sorunu çözmek

Atölye’nin aynı kuralla işlenecek 200 satırında yavaşlık varsa [veri işindeki](is-veri.md#2-zor-orneklerde-yontemi-gorunur-yap) temsilî satır → sabit kural → betik yolunu kullan. Buradaki model kararı şudur: eksik erişimi ve mekanik tekrarı daha fazla düşünme ayarıyla çözmeye çalışma. Token, modelin işlediği metin parçasıdır; doğrudan kelime veya para birimi değildir.

<a id="baska-uygulama-da-ayni-kullanim-hakkini-tuketebilir"></a>

## Başka uygulama da aynı kullanım hakkını tüketebilir

**Sign in with ChatGPT** ile üçüncü taraf uygulamaya giriş yapmak ve o uygulamanın plan kullanım hakkını tüketmesine izin vermek ayrı seçimlerdir. Desteklenen Plus/Pro bağlantılarında dış uygulama, Codex/Work ile paylaşılan mevcut kotadan kullanabilir. Bu yeni bir kota sağlamaz; uygulamanın ayrıca kendi ücreti olabilir.

Kullanımını anlamaya çalışırken yalnız açık Codex sohbetlerini sayma. Settings → Usage → App limits içinde bağlı uygulamaların kullanım sınırları görünüyorsa bunları da incele. Yüzdelik üst sınır, uygulama için ayrılmış veya garantilenmiş kota değildir. Plan kullanma izni sohbet geçmişine ve belleğe erişim izni de vermez. [ChatGPT ile giriş ve plan kullanımı](https://learn.chatgpt.com/docs/sign-in-with-chatgpt)


<a id="modeli-degistirmeden-once"></a>

## Modeli değiştirmeden önce

Kötü sonucu tek bir “model zayıf” açıklamasına bağlama. Aşağıdaki müdahaleler aynı maliyeti ve aynı sonucu üretmez:

| Gözlenen sorun | İlk müdahale | Söylenebilecek kısa istek |
|---|---|---|
| Kaynak veya erişim eksik | Girdiyi tamamla | “Hangi bilgiye erişemediğini belirt; tahminle kapatma.” |
| Bilgi doğru, amaç yanlış anlaşılmış | Ölçütü düzelt | “En ucuzu değil, hesapsız kayıt ve CSV koşullarını karşılayanı seç.” |
| Bilgi yeterli, çoklu koşullar kaçıyor | Çabayı artır veya güçlü ikinci görüş al | “Bu üç koşulu birlikte değerlendir; öneriyi kaynaklara karşı yeniden incele.” |
| Aynı mekanik işlem tekrarlanıyor | Kuralı sabitle, betikle uygula | “Önce üç zor satırda yöntemi göster; sonra aynı kuralı uygula.” |
| Araç sonucu bekleniyor | Beklenen işlemi teşhis et | “Model mi, derleme mi bekliyor? Çalışan işi gereksiz yeniden başlatma.” |
| Sonuç doğru, anlatım yetersiz | Hedefli editoryal revizyon yap | “Kararı ve belirsizliği koru; teknik terimleri ilk kullanımda açıkla.” |

[Araştırma örneğinde](is-arastirma.md) düzelen şey eleme ölçütüydü. Buna karşılık gerekli kaynaklar verildiği hâlde birbiriyle ilişkili koşullar sürekli kaçıyorsa daha güçlü muhakemeyi denemek anlamlıdır. Hangi müdahalenin işe yaradığını görmek için her denemede tek ana değişkeni değiştir.


**Eğitimde sıradaki:** [Araştırmadan karar ve sunuma](is-arastirma.md)


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [2.2 Bağlam ve kullanım göstergelerini kontrol et.](../codex-kontrol-listesi.md#m-2-2)
- [5.1 Alt ajan modelini göreve göre belirle.](../codex-kontrol-listesi.md#m-5-1)
- [5.2 Model adını erişilebilir katalogdan seç.](../codex-kontrol-listesi.md#m-5-2)
- [5.3 Düşünme seviyesini işin güçlüğüne göre değiştir.](../codex-kontrol-listesi.md#m-5-3)
- [5.4 Kullanımı ve bekleme nedenini ayrı kaydet.](../codex-kontrol-listesi.md#m-5-4)
- [5.5 Hız modunu ve güçlü ikinci görüşü seçerek kullan.](../codex-kontrol-listesi.md#m-5-5)

[İçindekiler](README.md) · Konu sırasıyla oku: [← Bağlam, bellek ve devamlılık](06-baglam-bellek.md) · [Dosyalar ve çalışma ortamları →](08-ortamlar.md)
