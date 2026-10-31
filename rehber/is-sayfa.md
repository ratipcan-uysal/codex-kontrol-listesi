# Görsel sorundan doğrulanmış yayına

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

**Kurgu iş:** Atölye'nin etkinlik sayfasındaki kart telefonda taşıyor. Kullanıcı mevcut metinleri ve görsel yönü seviyor; yalnız dar ekranda okunabilirlik istiyor. Bu rehber için gerçekten üretilmiş iki küçük HTML dosyası üzerinden ilerliyoruz. Bir müşteri sitesinin çalışma kaydı veya mağaza dağıtımı değil.

[Taşan örneği aç](ornekler/sayfa-once.html) · [Düzeltilmiş örneği aç](ornekler/sayfa-sonra.html). Anlatıcı sayfayı daraltıp aynı içeriği karşılaştırabilir. Dinleyicinin kurulum veya kod yazma yapması gerekmez.

**Gözlenen sorundan istenen hedefe ilerle**

1. **Belirti:** Dar ekranda taşma
2. **Müdahale:** Genişliği kapsayıcıya uyarla
3. **Kontrol:** Aynı ekran + bağlantı
4. **Teslim:** İstenen yerel veya canlı hedef

<a id="1-gozledigin-sorunu-ver-cozumu-erkenden-dayatma"></a>

## 1. Gözlediğin sorunu ver, çözümü erkenden dayatma

> Bu yerel sayfada etkinlik kartı dar ekranda taşıyor. 390 ve 320 pikselde tekrar et. Metni, tarihleri ve renkleri koruyarak düzelt. Önce taşmanın hangi öğeden geldiğini göster; sonra aynı koşullarda sonucu kontrol et.

İlk istekte “yazıları küçült” demek yanlış çözümü peşinen seçebilir. Örneğimizde sorun yazı boyutu değil; kartın sabit genişliği. Aşağıdaki görüntü 390 piksel genişlikte açılan **önce** dosyasının gerçek tarayıcı görüntüsüdür.

![Sabit genişlik dar ekranda taşıyor; kurgu Atölye etkinlik sayfasının 390 piksel tarayıcı görünümü.](assets/lesson-before.png)

**Sabit genişlik dar ekranda taşıyor.** Bu rehber için üretilen örnek HTML’nin gerçek tarayıcı görüntüsü. Metin ve tarih kurgudur; Codex uygulaması ekranı değildir. [Tam boyut](assets/lesson-before.png) · Kurgu örnek HTML’nin gerçek tarayıcı görüntüsü · [Kaynak](ornekler/sayfa-once.html) · 2026-10-29.

1. **Nereye bak:** Kartın sağ kenarına ve Programı gör bağlantısına.
2. **Ne yap:** Aynı içerik ve ekran genişliğinde önce/sonra karşılaştır.
3. **Ne gör:** Taşma giderildi mi, metin ve bağlantı korundu mu?

Bu görüntüden “buton çalışmıyor” sonucu çıkmaz. Görünen sorun sağ kenarın taşmasıdır. Önce etkilenen öğeyi ve tekrar koşulunu netleştirmek, gereksiz yeniden tasarımı önler.

<a id="2-tarayicida-bolgeyi-goster-degisecek-boyutu-yaz"></a>

## 2. Tarayıcıda bölgeyi göster, değişecek boyutu yaz

![Yerleşik tarayıcıda hedefli yorum. Sağdaki grafikte işaretlenen alan, soldaki sohbete bağlam olarak taşınıyor. Görsel sorunu doğrudan yerinde göstermek, hangi öğenin değişeceğini netleştirir.](assets/browser.png)

**Yerleşik tarayıcıda hedefli yorum.** Sağdaki grafikte işaretlenen alan, soldaki sohbete bağlam olarak taşınıyor. Görsel sorunu doğrudan yerinde göstermek, hangi öğenin değişeceğini netleştirir. [Tam boyut](assets/browser.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/browser) · 2026-10-29.

1. **Nereye bak:** Sağdaki grafikte mavi işaretli alana ve soldaki yorum bağlamına.
2. **Ne yap:** Annotate ile öğeyi işaretle, sorunu ve korunacak boyutu yaz, sohbette uygulat.
3. **Ne gör:** Düzeltme aynı öğede görünür; başka kartlar gerekçesiz değişmez.

Resmî gösterimde işaretlenen öğe bir grafik. Atölye örneğinde aynı yöntemi taşan kart için kullanırsın: araç çubuğunda **Annotate** seç, öğeyi veya bölgeyi işaretle, yorumunu kaydet, ardından sohbette yorumun uygulanmasını iste. İşaretlemek tek başına değişikliğin tamamlandığı anlamına gelmez. [Tarayıcıda yorum](https://learn.chatgpt.com/docs/browser)

> İşaretlediğim kart ekranın dışına çıkıyor. Kartın içerik sırası ve tipografisi aynı kalsın. Genişliği kapsayıcısına uyarlayarak düzelt.

Yeni yön istemediğin için iki farklı tasarım prototipi üretmeye gerek yok. Eğer sorun “bu sayfa sıkıcı” olsaydı, önce bilgi sırası ve görsel yönü konuşmak gerekirdi. Bizim rehberdeki “yeşil background beni boğdu” düzeltmen ise belirli bir görsel katmanı tarif etti: düzeni koruyup paleti değiştirdik. [Gerçek vaka C09](deneyimler.md#c09)

<a id="3-kucuk-degisikligin-butun-etkisini-gor"></a>

## 3. Küçük değişikliğin bütün etkisini gör

Örnek dosyalarda değişen tek CSS değeri şudur:

```css
/* Önce */
.event-card { width: 440px; }

/* Sonra */
.event-card { width: 100%; }
```

Kart zaten `max-width: 520px` olan bir ana alanın içinde; `box-sizing: border-box` iç boşluk ve kenarlığı genişliğe dahil ediyor. Bu bağlam yüzünden yüzde yüz genişlik uygun. Her taşma için aynı iki satır evrensel çözüm değildir: uzun kesintisiz metin veya grid alt öğesi başka bir neden olabilir.

Anlatıcı [kaynak farkını](ornekler/sayfa-degisikligi.md) gösterir. Tarih, başlık, renk ve bağlantı aynı kaldı. Büyük bir dosyanın tamamının değişmesi gerekmiyordu.

<a id="4-kod-farkini-ve-gorunen-sonucu-birlikte-oku"></a>

## 4. Kod farkını ve görünen sonucu birlikte oku

![Aynı kart kapsayıcıya sığıyor; kurgu Atölye etkinlik sayfasının 390 piksel tarayıcı görünümü.](assets/lesson-after.png)

**Aynı kart kapsayıcıya sığıyor.** Bu rehber için üretilen örnek HTML’nin gerçek tarayıcı görüntüsü. Metin ve tarih kurgudur; Codex uygulaması ekranı değildir. [Tam boyut](assets/lesson-after.png) · Kurgu örnek HTML’nin gerçek tarayıcı görüntüsü · [Kaynak](ornekler/sayfa-sonra.html) · 2026-10-29.

1. **Nereye bak:** Kartın sağ kenarına ve Programı gör bağlantısına.
2. **Ne yap:** Aynı içerik ve ekran genişliğinde önce/sonra karşılaştır.
3. **Ne gör:** Taşma giderildi mi, metin ve bağlantı korundu mu?

Bu da aynı 390 piksel görünümde **sonra** dosyasının gerçek görüntüsü. Kart kapsayıcıya sığıyor ve içerik okunuyor. Sayfayı açıp Programı gör bağlantısını kullanmak, görselin tek başına anlatamayacağı etkileşimi kontrol eder. İlgili 320 piksel koşulu da ayrıca sınanır.

Bir Git projesinde `/review` ile değişiklikleri inceletebilirsin. İnceleme bulgusu seçili dosya farkına dayanır; tarayıcıda okunabilirliği kontrol etmenin yerine geçmez. [Kod inceleme](https://learn.chatgpt.com/docs/code-review)

Bizim başka bir prototipimizde klavye konum testi geçtiği hâlde ikinci metin satırı örtülüyordu. Düzen değişikliği ve son görüntünün açılmasıyla sorun kapandı. Bu örnek, “test geçti” sözünü davranış ve görüntüyle eşleştirmemize neden oldu; gerçek cihaz veya üretim yayını bu kaydın kapsamı değildi. [Gerçek vaka C03](deneyimler.md#c03)

<a id="5-sohbetin-yonunu-hangi-aracla-degistirirsin"></a>

## 5. Sohbetin yönünü hangi araçla değiştirirsin?

| Yeni ihtiyacın | Bu işte seçeceğin yol | Neden? |
|---|---|---|
| “Rengi değiştirme, yalnız genişliği düzelt” | Aynı sohbeti yönlendir | Mevcut hedefin sınırını düzeltiyorsun |
| “Bu CSS ifadesi ne demek?” | `/side` | Ana işi kesmeden kavram açıklaması istiyorsun |
| “Aynı geçmişten farklı bir tasarım deneyeyim” | `/fork` | Ayrı yön istiyorsun; dosya yalıtımını ayrıca seçmelisin |
| “Bambaşka bir rapora başlayacağım” | `/new` | Aynı çalışma alanında boş sohbet istiyorsun |

Komutların erişimi ortama bağlıdır. `/fork` sohbeti dallandırır; aynı klasördeki dosyaları otomatik olarak iki bağımsız ürün yapmaz. Gerekiyorsa ayrı Git çalışma kopyası olan worktree seçilir. [Masaüstü komutları](https://learn.chatgpt.com/docs/reference/slash-commands)

<a id="6-yayin-istegi-gelince-hedefi-degistir"></a>

## 6. Yayın isteği gelince hedefi değiştir

“Yerelde düzelt” isteğinin bitişi yerel sonuçtur. Kullanıcı ayrıca “onaylanan değişikliği GitHub ve canlı sayfaya al” derse teslim zinciri uzar:

> İlgili kontrolleri tamamla, değişikliği belirtilen depoya gönder ve dağıtımı bekle. Sonra canlı adresi açıp aynı düzeltmenin orada olduğunu doğrula. Bekleyen aşamayı tamamlandı sayma.

Bu rehberin kendisi üzerinde gerçekten yapılan yayınlarda yerel test, uzak commit, Pages dağıtımı ve canlı dosya karşılaştırması ayrı kaydedildi. [Yayın kayıtları](../DOGRULAMA.md). Atölye örneğinin GitHub'a ayrı bir uygulama olarak yayımlandığı iddia edilmiyor; örnek dosyaları rehberin içinde açılıyor.

**Başka işte kullanacağın ders:** Belirtiyi tarif et, korunacak boyutları söyle, kaynağı ve görünümü aynı koşulda kontrol et. Sonra kullanıcının istediği hedefte bitir. Bu yaklaşım bir slayttaki taşan başlık veya belgedeki kırık tablo için de uygulanabilir.


**Eğitimde sıradaki:** [Yöntemi ikinci işte kullan](10-baglantilar-skills.md)

[İçindekiler](README.md) · [← Dağınık tablodan güvenilir rapora](is-veri.md) · [Yöntemi ikinci işte kullan →](10-baglantilar-skills.md)
