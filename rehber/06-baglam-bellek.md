# 6. Bağlam, bellek ve devamlılık

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Codex'in bir bilgiyi daha önce duymuş olması, o bilginin şu anda eksiksiz ve güncel biçimde elinde olduğu anlamına gelmez. Devamlılık için bilginin nerede tutulduğunu bilmek gerekir.

<a id="bes-farkli-bilgi-kaynagi"></a>

## Beş farklı bilgi kaynağı

| Kaynak | Ne işe yarar? | Sınırı |
|---|---|---|
| Açık sohbet | Bu işin istekleri, kararları ve araç sonuçları | Uzun geçmiş özetlenebilir; her ayrıntı etkin bağlamda kalmaz |
| Otomatik bellek | Önceki işlerden yararlı tercih ve bağlamı geri getirir | Anında ve eksiksiz kayıt değildir; eski bilgiyi taşıyabilir |
| Proje dosyaları | Kod, veri, kaynak ve mevcut ürün durumunu gösterir | Dosyanın varlığı çalıştığını kanıtlamaz |
| `AGENTS.md` | Tekrarlanan çalışma talimatını tanımlar | Değişen olayların günlük kaydı için uygun değildir |
| Devir notu | Son durum, kanıt ve açık işi yeni sohbete taşır | Yazıldığı tarihin fotoğrafıdır; güncelliği kontrol edilir |

Masaüstündeki Codex belleği ile ChatGPT web belleği aynı kayıt sistemi değildir. Codex belleği uygun geçmiş konuşmalardan arka planda oluşturulur. Settings → Personalization ve desteklenen `/memories` denetimleri kullanım ve katkı tercihlerini yönetir. Menülerin kapsamı hesabına bağlıdır. [Bellek](https://learn.chatgpt.com/docs/customization/memories)

<a id="ayni-sohbet-mi-yeni-sohbet-mi"></a>

## Aynı sohbet mi, yeni sohbet mi?

| İhtiyaç | Seçim | Korumak istediğin şey |
|---|---|---|
| Sunumun yalnız başlığını düzeltmek | Mevcut sohbette devam et | Son dosya ve kararlar korunur |
| Site üretilirken “worktree ne demek?” diye sormak | `/side` | Yan açıklama için ana işin yönünü değiştirme |
| Aynı brief’ten farklı tasarım yönü denemek | `/fork` | Geçmiş kopyalanır; aynı dosyaya yazmayı önlemek için ortamı ayrıca seç |
| Etkinlik sitesinden bağımsız kitap özetine geçmek | `/new` | Uygun olduğunda aynı yerel çalışma alanında boş sohbet; gerekli dosyayı yeniden belirt |
| Aynı işi uzun konuşmadan sürdürmek | `/compact` | Önce önemli kararları dosyaya geçir; özet tam arşiv değildir |

Bu seçimleri bir sayfa düzeltmesi içinde [yan yana görebilirsin](is-sayfa.md#5-sohbetin-yonunu-hangi-aracla-degistirirsin). Komutların yüzey ve erişim koşulları [masaüstü belgesinde](https://learn.chatgpt.com/docs/reference/slash-commands) açıklanır. Kaynak dosya, kesin alıntı veya test günlüğü yerine sohbet özetini kullanma.

> Bu işin kararlarını proje notlarına geçir. Hangi dosyada çalıştığımızı, son doğrulanan sonucu ve açık kalan soruları kaydet. Ayrıntıları kopyalamak yerine ilgili kaynağa bağla.

<a id="devir-notunu-ve-yeni-baslangici-yan-yana-gor"></a>

## Devir notunu ve yeni başlangıcı yan yana gör

[Örnek devir notunu](ornekler/devir-notu.md) aç. Bu, Atölye araştırmasının kurgu devam kaydıdır:

| Notta saklanan | Yeni sohbette karşılığı |
|---|---|
| Kayıt B koşullu öneri; hesapsız kayıt zorunlu | Eski kararın nedenini bilir |
| Ek ücret bilinmiyor | Satın alma tamamlandı demez |
| Kaynak paketi ve karar notunun yolları | Özet yerine gerekince asıl dosyayı okur |
| Sonraki adım: ek ücreti doğrula | Araştırmayı baştan başlatmaz |

> Devir notunu ve bağlı kaynakları oku. Hesap açma koşulu artık kabul ediliyor; önceki zorunluluğun yerini bu karar alıyor. B ve C’yi yeniden değerlendir, diğer ölçütleri koru.

**Gösterilecek sonuç:** C yeniden aday olur; ek ücretler hâlâ bilinmediğinden kesin toplam maliyet uydurulmaz. Notta “hesapsız kayıt zorunlu” kararının değiştiği belirtilir. Bu örnek, belleğin bütün sohbeti hatırlamasına ihtiyaç duymadan devamı gösterir.

`/status` ile bağlam durumunu gördüğünde evrensel bir yüzde eşiği arama. Önemli kararlar yalnız uzun geçmişte kaldıysa önce bu kısa notu kaydet. `/compact` bir özetleme hareketidir; notun kaynaklara bağlanması ayrı iştir.

<a id="eski-bilgiye-dogru-soru-sor"></a>

## Eski bilgiye doğru soru sor

Bellek “ilk kullanım ekranı yok” diyebilir. Bugünkü kaynakta bu ekran eklenmiş olabilir. Güvenilir yaklaşım, belleği arama başlangıcı yapmak ve mevcut kodla karşılaştırmaktır.

Gerçek bir ürün incelememizde eski “onboarding yok” notu güncel kaynakla uyuşmadı. İlk kullanım akışı vardı; Debug ve Release koşulları farklıydı. Başka bir bulguda içerik çevrilmişti, fakat uygulama paketine aktarılmamıştı. İki durumda da eski görevi yeniden yapmak yanlış çözüm olurdu. [Vaka C02](deneyimler.md#c02)

<a id="computer-history-appshots-ve-bellek"></a>

## Computer History, Appshots ve bellek

Computer History, desteklenen macOS kurulumlarında isteğe bağlı bilgisayar etkinliği bağlamıdır. Bellek ve uygun hesap/kurum koşulları gerekir. Açık onayla etkinleşir; uygulama/site kapsamı, duraklatma ve silme denetimleri vardır. Belgeler bunun sürekli ekran görüntüsü veya ses kaydı olmadığını belirtir. Appshots ise belirli anda ön plandaki pencereyi sohbete ekleme yoludur. Bunları birbirinin adı gibi kullanma. [Computer History](https://learn.chatgpt.com/docs/customization/computer-history) · [Appshots](https://learn.chatgpt.com/docs/appshots)

Bu özellikleri öğrenmek için açmak zorunda değilsin. Kaynak dosyalar ve kısa proje notları birçok işte yeterlidir.

<a id="kurgu-senaryo-iki-hafta-sonra-donus"></a>

## Kurgu senaryo: iki hafta sonra dönüş

Atölye takvimine döndüğünde katılımcı sayısı 20’den 35’e çıkmışsa yalnız “devam” demek yetmez. “35 kişi eski varsayımın yerini alıyor; kapasite ve bütçede etkilenen yerleri güncelle” de. Yukarıdaki devir yönteminin ikinci kullanımı budur; diğer kararları yeniden açman gerekmez.


**Eğitimde sıradaki:** [Ayrı denemeyi ana işe taşı](08-ortamlar.md)


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [2.1 Farklı sonuçlar için ayrı sohbetler aç.](../codex-kontrol-listesi.md#m-2-1)
- [2.3 Konu değiştiğinde temiz bir sohbet kullan.](../codex-kontrol-listesi.md#m-2-3)
- [2.4 Geniş araştırmayı gerektiğinde ayrı bağlama taşı.](../codex-kontrol-listesi.md#m-2-4)
- [2.5 Büyük logu dosyada tut, ilgili kısmını oku.](../codex-kontrol-listesi.md#m-2-5)
- [2.6 Sıkıştırmadan önce kritik kararları dosyaya geçir.](../codex-kontrol-listesi.md#m-2-6)
- [2.7 Devam etme, dallandırma ve temiz başlangıcı ayır.](../codex-kontrol-listesi.md#m-2-7)
- [18.1 Yeni bilgiyi geçerli olduğu katmana yaz.](../codex-kontrol-listesi.md#m-18-1)
- [18.2 Ertelenen işi kaybolmayacak bir durum kaydına geçir.](../codex-kontrol-listesi.md#m-18-2)

[İçindekiler](README.md) · [← İş sürerken yönü yönetmek](05-yonetmek.md) · [Model, düşünme seviyesi, hız ve kullanım →](07-model-hiz-kullanim.md)
