# 9. İnternet, tarayıcı ve bilgisayar kullanımı

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Web araştırması, tarayıcı kontrolü ve bilgisayar kullanımı üç farklı iştir. Bir sayfanın metnini bulmak için bütün bilgisayarı kontrol etmeye gerek yoktur. Bir düğmenin gerçekten çalıştığını görmek için de yalnız kaynak metni yeterli olmaz.

<a id="hangi-yol-hangi-soruya-cevap-verir"></a>

## Hangi yol hangi soruya cevap verir?

| İhtiyaç | Başlangıç yolu | Kanıtın sınırı |
|---|---|---|
| Güncel ürün özelliğini öğrenmek | Web araması ve resmî sayfayı açma | Sayfanın iddiasını doğrular; hesabındaki erişimi değil |
| Bağlı takvim veya belgeyi okumak | İlgili plugin/bağlı araç | Bağlantının izin verdiği veriyle sınırlıdır |
| Yerel sayfadaki taşmayı görmek | Yerleşik tarayıcı | Açılan URL ve ekran boyutundaki görünümü gösterir |
| Kendi tarayıcındaki oturumla çalışmak | Desteklenen tarayıcı eklentisi | Seçilen sekme ve alan izinlerine bağlıdır |
| Yerel uygulamada işlem yapmak | Bilgisayar kullanımı | Platform, uygulama ve işletim sistemi izinlerine bağlıdır |

Bu sıralama bir başlangıç önerisidir. Kullanıcı belirli bir araç istediğinde veya görsel inceleme gerektiğinde yolu ona göre seç.

<a id="guncel-bilgi-istediginde-arama-bicimini-de-netlestir"></a>

## Güncel bilgi istediğinde arama biçimini de netleştir

Yerel Codex için belgelenmiş varsayılan web araması, OpenAI'nin tuttuğu önbellekli dizinden sonuç getirebilir. Bugünkü fiyat, son sürüm veya yeni düzenleme sorusunda güncellik isteğini açıkça yaz: “Güncel resmî sayfayı aç; gördüğün tarihi belirt.” Önbellekli sonuç eski olabilir, canlı arama da her sayfaya erişmeyi garanti etmez.

Yapılandırmada `web_search = "live"` canlı aramayı, `"disabled"` kapatmayı seçer. Terminalde `codex --search` o çalıştırma için canlı arama yoludur. Bunlar masaüstü mesajına yazılan slash komutları değildir. Hazır web aracı ile terminalde ağ bağlantısı farklı kanallardır; birinin çalışıp diğerinin engellenmesi mümkün. [Web araması](https://learn.chatgpt.com/docs/web-search)

Derin kaynak sentezi için hesabında mevcutsa **Work → Plugins → Deep research → Try now** yolu da var. Bu, genel bir “araştır” isteğinden farklı ürün akışıdır; Codex mesaj alanında `/deepresearch` komutu varmış gibi kullanma. Kısa bir resmî belge kontrolünde normal web araştırması çoğu zaman yeterli. Aynı kaynakta yüzey ve erişim koşulları açıklanır.

<a id="cok-baglanti-kac-bagimsiz-dayanak"></a>

## Çok bağlantı, kaç bağımsız dayanak?

Atölye araştırmasındaki B seçeneği için “CSV dışa aktarma var” iddiasını düşün. **Kurgu araştırma uzantısı:** Aynı cümleyi üç yerde bulduğunu varsayalım; bu yeni bir gerçek ürün araştırması değildir.

| Bulunan sayfa | Bilginin geldiği yer | İddiaya katkısı |
|---|---|---|
| B'nin özellik belgesi | Ürünün kendi açıklaması | Özelliğin belgede nasıl ve hangi koşullarla sunulduğunu gösterir |
| B'yi tanıtan haber | Aynı özellik belgesini aktarıyor | Aynı dayanağın ikinci aktarımı; ayrı bir deneme değil |
| B'yi karşılaştıran liste | Haberdeki cümleyi yeniden kullanıyor | Üçüncü URL, üçüncü bağımsız doğrulama değil |

**Önce:** “Üç kaynak CSV desteğini doğruluyor.” **Daha doğru sonuç:** “Üç sayfa aynı ürün açıklamasına dayanıyor; hesabımızdaki dışa aktarmayı henüz denemedik.”

> Önemli iddiaları ilk dayanağına kadar izle. Aynı açıklamadan türeyen sayfaları birlikte göster. Kaynağın söylediği şey ile bağımsız deneyim veya bizim gözlediğimiz sonucu ayır.

Bağımsız bir kullanıcı denemesi de her plan ve sürüm için kanıt değildir; tarihini ve koşulunu kontrol et. Resmî belgeyi sırf tek kaynak diye değersiz sayma: hangi iddiayı desteklediğine bak. Atölye'de CSV'ye erişim seçimi belirliyorsa uygun hesaptaki küçük dışa aktarma denemesi, aynı cümleyi tekrarlayan yeni sayfalar toplamaktan daha açıklayıcı olabilir. Araştırmanın nerede duracağını [kararı değiştiren boşluk](is-arastirma.md#siradaki-arastirmayi-karari-degistirecek-bosluga-ver) belirler.

<a id="yerlesik-tarayici"></a>

## Yerleşik tarayıcı

Yeni tarayıcı sekmesi açıp URL'ye gidebilir, sohbetten `@Browser` referansı verebilirsin. Yerel geliştirici sunucusu çalışıyorsa önizlemeyi aynı panelde incelemek yararlıdır. Tarayıcı profili, normal Chrome oturumunla aynı değildir; başka tarayıcıda giriş yapmış olman burada da girişli olduğunu göstermez. [Tarayıcı](https://learn.chatgpt.com/docs/browser)

Annotate ile bir öğeyi veya bölgeyi işaretlemek “şu boşluğu azalt” isteğinin hedefini netleştirir. Önizlemede yapılan geçici stil ayarı, kaynak dosyaya kaydedildiği veya canlıya çıktığı anlamına gelmez. Kaynak değişikliği ve hedef görünümü ayrı doğrula.

Belge kontrol tarihinde yerleşik tarayıcıda otomatik dosya yükleme desteklenmiyor. Bir yükleme adımı varsa desteklenen başka araç veya tarayıcı yolunu kullanmak gerekir. Bu sınırı bütün tarayıcı araçlarına genelleme.

![Yerleşik tarayıcıda hedefli yorum. Sağdaki grafikte işaretlenen alan, soldaki sohbete bağlam olarak taşınıyor. Görsel sorunu doğrudan yerinde göstermek, hangi öğenin değişeceğini netleştirir.](assets/browser.png)

**Yerleşik tarayıcıda hedefli yorum.** Sağdaki grafikte işaretlenen alan, soldaki sohbete bağlam olarak taşınıyor. Görsel sorunu doğrudan yerinde göstermek, hangi öğenin değişeceğini netleştirir. [Tam boyut](assets/browser.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/browser) · 2026-10-29.

1. **Nereye bak:** Sağdaki grafikte mavi işaretli alana ve soldaki yorum bağlamına.
2. **Ne yap:** Annotate ile öğeyi işaretle, sorunu ve korunacak boyutu yaz, sohbette uygulat.
3. **Ne gör:** Düzeltme aynı öğede görünür; başka kartlar gerekçesiz değişmez.

Görseldeki gibi bir alanı işaretledikten sonra “yalnız bu grafiğin bilgi kutusu kesiliyor; renkleri ve veriyi koruyarak düzelt” demek, bütün sayfayı belirsiz biçimde değiştirtmekten daha hedefli bir geri bildirimdir.

<a id="chrome-ve-diger-desteklenen-tarayicilar"></a>

## Chrome ve diğer desteklenen tarayıcılar

Resmî eklenti Chrome, Edge, Brave, Opera ve Vivaldi için belgelenmiştir. Sekme referansı ve kontrol ile tarayıcı içi yan sohbet aynı kapsamda değildir; örneğin Opera için yan sohbet desteği farklıdır. Kurulumda hem Codex tarafındaki plugin hem tarayıcı eklentisi gerekir. Alan adı izinlerini Manage üzerinden sınırlandırabilirsin. [Tarayıcı eklentisi](https://learn.chatgpt.com/docs/chrome-extension)

YouTube altyazısından zaman damgalı metin almak, videonun bütün görsel içeriğini incelemek demek değildir. Görsel bir iddiayı altyazıya dayandırma. Oturum açılan hesabı da işleme başlamadan kontrol et; aynı sitenin kişisel ve kurumsal hesabı farklı hedeflerdir.

<a id="bilgisayar-kullanimi-ve-ekran-baglami"></a>

## Bilgisayar kullanımı ve ekran bağlamı

macOS ve Windows yollarının çalışma şekli farklıdır. Windows'ta bilgisayar kullanımı etkin ve kilidi açık masaüstü koşullarına bağlıdır; desteklenen macOS akışları farklı arka plan davranışları sunabilir. Ekran kaydı ve erişilebilirlik gibi işletim sistemi izinleri, Codex'in kendi araç izninden ayrıdır. [Bilgisayar kullanımı](https://learn.chatgpt.com/docs/computer-use)

Appshots ön plandaki pencereyi belirli anda sohbete ekler. macOS'ta iki Command, Windows'ta iki Alt tuşu varsayılan giriş yolları arasındadır; atama değişebilir. Görünen görüntüye ek erişilebilirlik metni de gelebilir. Paylaşılmasını istemediğin bilgiyi önce kapat. Sesli sohbette ekran bağlamı ise desteklenen ayarla o konuşmaya bağlanır; sürekli her şeyi gören bir ajan varsayımı yanlıştır. [Appshots](https://learn.chatgpt.com/docs/appshots) · [Ses](https://learn.chatgpt.com/docs/features/voice)

Dikte, konuşmanı metin girdisine dönüştürür. Sesli sohbet ise karşılıklı, kesilebilen konuşma akışıdır. Mikrofon/hesap desteği ve aynı anda etkin oturum sınırlarını mevcut uygulamada kontrol et.

<a id="kurgu-senaryo-form-basari-mesaji-yeterli-mi"></a>

## Kurgu senaryo: form başarı mesajı yeterli mi?

Atölye'nin etkinliğine bir deneme kaydı gönderildiğini düşün. Ekranda “Başarılı” yazması, doğru hesapta doğru kaydın oluştuğunu tek başına kanıtlamaz. Yetkili denemede hedef listede kaydı tekrar açıp bilgileri doğrula. Çift kayıt yaratmamak için belirsiz sonuçta yeniden göndermeden önce hedefi oku. İnceleme için gönderim gerekmiyorsa formu doldurup göndermeden görünümü değerlendirmek yeterlidir.

[İçindekiler](README.md) · Konu sırasıyla oku: [← Dosyalar ve çalışma ortamları](08-ortamlar.md) · [Bağlantılar, MCP, plugin ve skill →](10-baglantilar-skills.md)
