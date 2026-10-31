# 15. Otomasyon ve tekrar eden işler

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Otomasyon, iyi tanımlanmış işi tekrar eder. Belirsiz işi zamanlamak, belirsizliği düzenli aralıklarla yeniden üretir. Önce bir gerçek örnekte yöntemi çalıştır, sonra takvime bağla.

<a id="ayni-sohbeti-takip-etmek-ve-bagimsiz-rutin"></a>

## Aynı sohbeti takip etmek ve bağımsız rutin

Aynı sohbette takip, mevcut işteki bir durumun değişmesini beklemek için uygundur: derlemenin sonucu, incelemenin tamamlanması veya geri dönülecek açık konu. Bağımsız rutin ise her çalışmada ayrı çıktı üretir: haftalık kaynak özeti, depo sağlık kontrolü, günlük rapor. Uygulamada Scheduled bölümündeki seçenekler ve doğal dil isteği üzerinden kurulabilir; adlar ve seçenekler istemciye göre değişir. [Otomasyon](https://learn.chatgpt.com/docs/automations)

> Bu sohbetin açık kontrolünü yarın yeniden değerlendir. Durum değişmediyse bildirim üretme; tamamlandığında, hata oluştuğunda veya benden karar gerektiğinde haber ver.

> Her pazartesi seçtiğim proje için geçen haftanın değişikliklerini yeni bir raporda özetle. Kaynak commit bağlantılarını ekle; değişiklik yoksa bunu kısa belirt.

İlk örnek mevcut işin devamını, ikincisi bağımsız tekrar eden sonucu tarif eder. Kurulduğunu, zamanlama ve hedefi geri okuyarak doğrula.

<a id="ne-zaman-zamanlamaya-hazir"></a>

## Ne zaman zamanlamaya hazır?

İlk raporun güzel görünmesi yeterli olmayabilir. Atölye’de ikinci haftanın yeni `yedek` durumu, henüz kararlaştırılmamış kuralı ortaya çıkarıyor. Önce bu kararı ver; sonra aynı yöntemi takvime bağla.

| Gözlediğin durum | Uygun sonraki adım |
|---|---|
| Her raporda ne istediğini baştan değiştiriyorsun | Normal sohbette yöntemi oturt |
| Yöntem sabit, her seferinde elle çağırıyorsun | Skill veya betikle tekrar kullan |
| Yöntem sabit, girdi ve zaman belli | Otomasyon kur; ilk gerçek koşumun çıktısını aç |
| Yalnız mevcut yayının bitmesini bekliyorsun | Kalıcı haftalık rutin yerine bu sohbeti takip et |

**Eksik girdi için somut kural:** Yeni haftanın dosyası gelmediyse geçen haftanın raporunu bu haftaymış gibi sunmasın; eksik kaynağı belirtip o koşumu sonlandırsın. Bu, sıklığı artırmaktan daha yararlı bir otomasyon kararıdır.

<a id="i-lk-rapordan-calisan-rutine"></a>

## İlk rapordan çalışan rutine

Aynı veri örneğini sürdür. Önce [ikinci hafta raporunu](ornekler/hafta-2-raporu.md) aç: yeni `yedek` etiketi görünür. Yöntem doğruysa zamanlama isteğine geç:

> Bu raporu her pazartesi 09.00 Europe/Istanbul saat diliminde, seçtiğim yerel projede bağımsız rutin olarak hazırla. Haftanın dosyası yoksa bunu bildir. Aynı haftanın raporu varsa güncelle. Yeni durum etiketi veya eksik tahsilat varsa belirt; dışarıya gönderme.

| Ekranda veya çıktıda görülecek | Anlatıcının kararı |
|---|---|
| Oluşturulan görevde saat, proje ve hedef | Yanlış saat dilimini çalışmadan düzelt |
| Scheduled içindeki ilk koşum ve rapor bağlantısı | Zamanlama kaydıyla gerçekten oluşan dosyayı ayır |
| Raporda yeni `yedek` etiketi | “Yedek ayrı kategori olarak kalacak” kararını yönteme ekle |
| Sonraki koşumda aynı hafta anahtarı | Çift rapor oluşmadan mevcut çıktı güncellendi mi? |
| Etkinlik bitti | İlgili rutini durdur ve durumunu geri oku |

[Kurgu koşum günlüğü](ornekler/otomasyon-gunlugu.md) bu zinciri gösterir. Gerçek zamanlayıcı kurulmadı; örnek rapor betikle üretildi. Ürün ekranı gösterilecek eğitimde Scheduled’ın o hesaptaki görünümü kullanılmalı. Görev ve son koşumları izleme, doğal dille güncelleme yolları [resmî belgede](https://learn.chatgpt.com/docs/automations) açıklanır. Webdeki olay tetikleyicilerini masaüstü denetimleri diye gösterme.

<a id="yerel-kosullar-devam-eder"></a>

## Yerel koşullar devam eder

Yerel otomasyonda uygulama ve bilgisayarın çalışması, proje klasörüne erişim ve gerekli araçların bulunması önemlidir. Bir takvim satırı eklemek bilgisayarı her koşulda uyandıracağı anlamına gelmez. Worktree kullanan rutin için kurulum ve çıktıların ana projeye nasıl döneceği ayrıca belirlenir.

Gmail, Slack veya GitHub olaylarıyla tetiklenen bazı akışlar web yüzeyinde belgelenmiştir; aynı olay tetikleyicisini masaüstü, CLI veya IDE özelliği gibi anlatma. Önce hangi ortamın çalıştıracağını seç. [Yüzey ve çalışma koşulları](https://learn.chatgpt.com/docs/automations)

<a id="tekrar-guvenligi"></a>

## Tekrar güvenliği

Aynı görevin iki kez çalışması iki kayıt, iki e-posta veya iki yayın üretmemeli. Buna tekrar güvenliği denir; teknik adı idempotency'dir. Örneğin raporu tarih ve proje anahtarıyla bulup güncellemek, her seferinde yeni kopya açmaktan daha uygundur. Gönderim sonucunun belirsiz olduğu durumda yeniden göndermeden önce hedefi kontrol etmek gerekir.

Otomasyon tanımı şu soruları cevaplamalı: Hangi girdiyi okuyacak? Çıktı nereye gidecek? Ne zaman duracak? Hata olduğunda ne yapacak? Hangi değişiklik haber vermeye değer? Görev metnindeki içerik yöntemi ile bildirim tercihini mümkün olduğunca ayrı tut.

<a id="kurgu-senaryo-dusuk-degerli-bildirimleri-azaltmak"></a>

## Kurgu senaryo: düşük değerli bildirimleri azaltmak

Atölye sayfasının kayıt bağlantısı takip ediliyor. Her kontrolde “hâlâ çalışıyor” mesajı gelmesi kullanıcıyı yorabilir.

> Kayıt bağlantısını belirtilen aralıkta kontrol et. Önceki durumla aynıysa sessiz kal. Erişim hatası kalıcı görünürse veya hedef URL değişirse haber ver; geçici tek ağ hatasını kesin site arızası diye sunma. İşlem yapma, yalnız kontrol et. Etkinlik tarihi geçince dur.

Bu kurgu örnek bir izleme mantığını öğretir; burada gerçek otomasyon oluşturulmaz. Kontrol aralığı, yerel çalışma koşulu ve durma tarihi gerçek kurulumda açıkça seçilmelidir.

<a id="otomasyon-sonuclarini-degerlendirmek"></a>

## Otomasyon sonuçlarını değerlendirmek

“Zamanlandı”, “çalıştı” ve “istenen çıktı hedefte oluştu” farklı aşamalardır. İlk koşumun sonucunu incele. Yanlış kaynak, gereksiz bildirim veya tekrar kayıt varsa yöntem düzelmeden daha sık çalıştırma. Otomasyonun öneri üretmesi, önerileri otomatik yayınlama yetkisi vermez.

**Eğitimde sıradaki:** [Sonraki işte neyi koruyacağını seç](18-iyilestirmek.md)


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [13.2 Gözetimsiz işin çalışma koşullarını önceden kontrol et.](../codex-kontrol-listesi.md#m-13-2)
- [14.1 Zamanlayıcıyı ihtiyaca uygun yüzeyde kur.](../codex-kontrol-listesi.md#m-14-1)
- [14.3 Sessizliği başarı sayma.](../codex-kontrol-listesi.md#m-14-3)
- [14.5 Aynı sohbete dönen takibi bağımsız rutinden ayır.](../codex-kontrol-listesi.md#m-14-5)

[İçindekiler](README.md) · [← Büyük işleri ve paralel çalışmayı yönetmek](14-buyuk-isler.md) · [İzinler, gizlilik ve güvenlik →](16-izinler-guvenlik.md)
