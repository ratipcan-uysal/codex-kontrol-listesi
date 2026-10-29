# 6. Bağlam, bellek ve devamlılık

Belge kontrolü: 2026-10-29.

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
| Aynı sonucun bir bölümünü düzeltmek | Mevcut sohbette devam et | Kararlar ve son çıktı |
| Çalışan işi kesmeden kavram sormak | `/side` | Ana işin devamı |
| Aynı geçmişten farklı yön denemek | `/fork` | Başlangıç bağlamı; dosya yalıtımı ayrıca seçilir |
| Bağımsız işe başlamak | `/new` | Aynı çalışma alanı, boş konuşma |
| Uzayan konuşmanın bağlamını sıkıştırmak | `/compact` | Çalışmaya yarayan özet; eksiksiz arşiv değil |

Bu seçimleri bir sayfa düzeltmesi içinde [yan yana görebilirsin](is-sayfa.md#5-sohbetin-yonunu-hangi-aracla-degistirirsin). Komutların yüzey ve erişim koşulları [masaüstü belgesinde](https://learn.chatgpt.com/docs/reference/slash-commands) açıklanır. Kaynak dosya, kesin alıntı veya test günlüğü yerine sohbet özetini kullanma.

> Bu işin kararlarını proje notlarına geçir. Hangi dosyada çalıştığımızı, son doğrulanan sonucu ve açık kalan soruları kaydet. Ayrıntıları kopyalamak yerine ilgili kaynağa bağla.

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

Atölye için hazırlanan etkinlik takvimine iki hafta sonra dönüyorsun. Eski sohbette bütçe 20 kişiye göreydi; şimdi 35 kişi var. İyi bir başlangıç:

> Önceki kararları oku. Katılımcı sayısı artık 35; bu bilgi eski 20 kişilik varsayımın yerini alıyor. Mekân kapasitesi ve bütçe hesabında etkilenen yerleri bul. Diğer kararları gerekmedikçe yeniden açma.

Böylece değişiklik hem güncel işte kullanılır hem de sonraki dönüşte eski sayı yeniden canlanmaz.

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
