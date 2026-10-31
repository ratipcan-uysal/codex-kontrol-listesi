# 10. Bağlantılar, MCP, plugin ve skill

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Codex'e yeni bir yetenek eklerken önce eksik olanı adlandır: veriye erişim mi, doğru yöntemi bilmek mi, tekrarlı işlemi yürütmek mi? Her ihtiyaç için yeni plugin kurmak gerekmez.

<a id="dort-kavrami-ayir"></a>

## Dört kavramı ayır

| Kavram | Ne sağlar? | Tek başına ne sağlamaz? |
|---|---|---|
| Bağlantı / connector | Bir hizmetteki hesabına kontrollü erişim | Her veriye veya her işleme sınırsız yetki |
| MCP | Araç ve veri kaynaklarını modele sunan ortak protokol | Model kalitesi, kalıcı bellek veya görev onayı |
| Skill | Belirli işi ne zaman ve nasıl yapacağını anlatan yönerge ve yardımcı kaynaklar | Gerekli hesabın bağlı olması |
| Plugin | Skill, araç ve bağlantıları paketleyebilen kurulum birimi | İçindeki her yeteneğin her yüzeyde çalışması |

[MCP](https://learn.chatgpt.com/docs/extend/mcp) · [Skill ve plugin](https://learn.chatgpt.com/docs/skills-and-plugins) · [Plugin kullanımı](https://learn.chatgpt.com/docs/plugins)

Örneğin takvim bağlantısı etkinlikleri okuyabilir; bir toplantı hazırlık skill'i hangi bilgileri birleştireceğini söyler. Kullanıcının “taslak çıkar” isteği, takvime etkinlik yazma yetkisi vermez.

<a id="kesfetme-baglama-ve-cagirma"></a>

## Keşfetme, bağlama ve çağırma

Plugins bölümünde gereken yeteneği bul, hangi hesabın ve izinlerin gerektiğini incele, bağlantıyı tamamla. Kurulumdan sonra araçların kullanılabilirliğini yeni sohbet veya ilgili menü üzerinden kontrol etmek gerekebilir. Codex'te `$` menüsünden skill seçmek ya da adını açıkça yazmak, ilgili yöntemin kullanılmasını netleştirir. Bazı diğer yüzeylerde aynı çağrı `@` ile sunulur; sözdizimini yüzeye göre oku.

Bir plugin'in masaüstü etiketi varsa web veya mobilde aynı aracı bekleme. Güncel belgeler plugin paketleriyle IDE'de kullanılan bağımsız skill/MCP yollarını da ayırır. “Bilgisayarımda kurulu” ile “bu sohbetin araçları arasında” farklı durumlardır.

<a id="uc-kaynaktan-bir-toplanti-notu"></a>

## Üç kaynaktan bir toplantı notu

**Kurgu iş:** Takvimdeki Atölye toplantısı, bağlı belgedeki önceki karar ve yerel katılım raporu tek hazırlık notunda birleşecek. [Örnek kaynak ve çıktı](ornekler/toplanti-hazirligi.md) her cümlenin nereden geldiğini gösterir.

> Bağlı takvimde 14 Kasım Atölye toplantısını bul. Önceki karar belgesini ve yerel katılım raporunu oku. Gündemi, açık soruyu ve dayanak bağlantısını içeren tek hazırlık notu oluştur. Aynı adlı iki kayıt varsa ayır. Gönderim veya takvim değişikliği yapma.

Burada takvim zamanı, karar belgesi seçimi, rapor eksik tahsilatı sağlar. Bir kaynak diğerinin boşluğunu tahminle doldurmaz. Anlatıcı üç açık kaynaktan tek notun hangi satırlarının oluştuğunu gösterir. Gerçek hesaplara erişim yoksa bu dosyalarla yöntem anlatılır; bağlı araçlar çalıştırılmış gibi sunulmaz.

<a id="i-yi-skill-neyi-saklar"></a>

## İyi skill neyi saklar?

Tekrar tekrar açıklamak zorunda kaldığın yöntemi saklar. Örneğin “kaynaklı makale yaz” sürecinde kaynak iddiası, yorum ve alıntı sınırını ayırabilir; gereken dosya şablonunu gösterebilir. Her olası işi üstlenen belirsiz bir skill ise yanlış zamanda devreye girer.

`SKILL.md` dosyasında kısa ad/açıklama, ne zaman uygulanacağı, önemli iş akışı ve gerekirse yardımcı dosyalar bulunur. Ayrıntı ihtiyaç oldukça yüklenir. Kullanım açıklamasını gereksiz uzatmak keşfi zorlaştırabilir. [Skill oluşturma](https://learn.chatgpt.com/docs/build-skills)

> `$skill-creator` kullanarak, kaynaklı Türkçe incelemeleri hazırlama yöntemimizi skill'e dönüştür. Kaynak toplama, alıntı sınırı ve son kontrolü tanımla. Yalnız yazım düzeltmesi istendiğinde bu süreci başlatmasın.

Bu kurgu örnekte beklenen çıktı yalnız uzun bir talimat değildir: doğru tetiklenen, ilgisiz işte devreye girmeyen, kaynakları belli bir paket gerekir.

<a id="skill-dosyadan-kullanilabilir-yonteme-nasil-gecer"></a>

## Skill dosyadan kullanılabilir yönteme nasıl geçer?

Yerel projeye ait örnek için `SKILL.md`, proje kökündeki `.agents/skills/atolye-raporu/` klasörüne konur. Başındaki `name` ve `description` alanları yöntemin adını ve ne zaman seçileceğini tanımlar. Bu yapı, sıradan bir metin dosyasını yalnız sohbete eklemekten farklıdır. [Yerel skill keşfi](https://learn.chatgpt.com/docs/build-skills)

1. Skills görünümünde veya mesaj alanındaki `$` seçicisinde **atolye-raporu** adını bul. Görünmüyorsa yanlış proje, klasör, ad/açıklama veya devre dışı bırakılma ihtimalini kontrol et. Kurulum değişikliği görünmüyorsa uygulamayı yeniden başlatmak resmî sorun giderme adımıdır.
2. Adı seçip girdi dosyasını belirt: “İkinci haftayı bu yöntemle raporla.” Otomatik seçime güvenmek yerine ilk gösterimde açık çağrı kullan.
3. Sonuçta yöntemin kritik davranışını ara: yeni `yedek` durumu saklandı mı, boş tahsilat korunuyor mu? Menüde görünmesi başarılı uygulamanın kanıtı değildir.

Codex masaüstündeki `$` çağrısını diğer yüzeylere aynen taşımadan o yüzeyin seçicisini kontrol et. [Masaüstü çağrı yolu](https://learn.chatgpt.com/docs/reference/slash-commands)

<a id="yontem-ikinci-haftada-neyi-koruyor"></a>

## Yöntem ikinci haftada neyi koruyor?

[Örnek skill metni](ornekler/rapor-skill.md), [ikinci haftanın girdisi](ornekler/katilim-hafta-2.csv) ve [üretilmiş ikinci rapor](ornekler/hafta-2-raporu.md) yan yana durur. Skill örneği, kurulacak paketin `SKILL.md` içeriğidir; indirmek tek başına kurmaz.

İlk haftada öğrendiğimiz yöntem: kimliği koru, boş tutarı boş bırak, yeni durum etiketini sessizce düzeltme. İkinci haftada yeni `yedek` durumu geldi:

| Yeni girdi | Yöntemin ürettiği sonuç |
|---|---|
| K07, durum `yedek` | Yeni durum olarak işaretlenir; katıldı diye çevrilmez |
| K08, tahsilat boş | Bilinmeyen tutar olarak kalır |
| K09, bekliyor, 600 TL | Durum ve tahsilat ayrı tutulur |

Kurulum yapılan desteklenen ortamda `$` menüsünden **atolye-raporu** seçip “İkinci haftayı aynı yöntemle raporla” de. Buradaki rapor dosyası, örnek kuralları uygulayan betikle gerçekten üretildi; bir skill’in otomatik seçildiğine dair oturum kaydı değildir. [Skill oluşturma ve kullanım](https://learn.chatgpt.com/docs/build-skills)

Anlatıcı, uzun ilk isteğin yerine kısa çağrıyı ve korunan üç kararı gösterir. Yalnız başlıkta yazım düzeltmesi istenince tüm rapor sürecinin başlamaması da skill’in kapsamının parçasıdır.

<a id="betik-mi-skill-mi-ozel-arac-mi"></a>

## Betik mi, skill mi, özel araç mı?

Aynı kuralla bin dosya adı değişiyorsa betik daha uygundur. Kaynak kalitesini tartıp makale yapısını seçmek yorum gerektirir; skill bu yöntemi yönlendirir. Mevcut araçların erişemediği kurumsal veriye kontrollü erişim gerekiyorsa özel MCP/araç geliştirmek anlamlı olabilir. Önce hazır araçla küçük işi tamamla; soyut bir ihtiyaca büyük entegrasyon kurma.

<a id="record-replay"></a>

## Record & Replay

Desteklenen macOS kurulumunda Plugins → + → Record a skill yolu bilgisayarda gösterdiğin akıştan skill üretmeye yardımcı olur. Computer Use kurulumu gerekir. Kaydı durdurduktan sonra oluşan yönergeleri incele: sabit kişi adı, tarih, dosya yolu veya tek seferlik tıklama genel kurala dönüşmüş olabilir. Replay, değişen ekranda araçlarla yürütülen akıştır; her pikseli aynı sırayla basan kusursuz makro garantisi değildir. [Record & Replay](https://learn.chatgpt.com/docs/extend/record-and-replay)


**Kısa kurgu örneği:** Kaydedilen adım “Ekim raporunu indir” ise kasımda aynı kaydı körlemesine oynatmak yanlış ayı getirebilir. Yöntemi “istenen ayı seç, başlıkta aynı ayı doğrula, sonra indir” diye genelleştir. Çağrıdaki ay kasım olduğunda beklenen gözlem dosya başlığında kasımdır; yalnız indirme düğmesine basılması başarı değildir. Kaydı skill'e dönüştürme sırasında sabit ayrıntıyı değişkene çevirmenin değeri budur.

<a id="arac-dogru-calisti-cevap-dogru-mu"></a>

## Araç doğru çalıştı; cevap doğru mu?

Kurulumdan sonraki okuma denemesi yalnız başlangıçtır. Araç sonucunu, Codex’in seçimini ve son cevabı ayrı incele. Kontrollü araç testinin başarısı, gerçek uygulamadaki talimatlar ve araç erişimiyle aynı davranışın oluşacağını garanti etmez. [Plugin değerlendirmesi](https://developers.openai.com/cookbook/examples/partners/harness_aware_plugin_evals/harness_aware_plugin_evals)

**Kurgu takvim örneği:** “Yarınki Atölye toplantısının saatini söyle.”

| Kontrol | Doğru davranış | Kaçabilecek hata |
|---|---|---|
| Araç | Seçilen günün kayıtlarını getirir. | Yanlış tarih veya saat dilimi kullanılır. |
| Araç seçimi | Doğru takvimi ve ilgili kaydı seçer. | Aynı adlı iki toplantıdan birini gerekçesiz seçer. |
| Son cevap | Seçilen kaydın 14.00 saatini doğru aktarır. | Araç 14.00 döndürdüğü hâlde cevap 15.00 der. |

> Aynı isteği bu sohbette sınayalım. Hangi kaydı seçtiğini ve araçtaki saatle son cevabın eşleştiğini göster. İki kayıt ayırt edilemiyorsa gerekli ayrımı sor; kayıt bulunmazsa saat uydurma. Takvimi değiştirme.

İlk örneği özellikle belirsiz veya sonuçsuz bir durumla karşılaştır. Bir aracın çağrılmış olması, doğru kullanıldığına tek başına kanıt değildir. Genel kanıt ölçütleri [doğrulama bölümünde](12-dogrulama.md).

<a id="baglanti-calismiyorsa"></a>

## Bağlantı çalışmıyorsa

Önce kurulum, hesap bağlantısı, izin kapsamı ve o sohbette araç keşfini ayrı kontrol et. Araç görünüyorsa küçük bir okuma denemesi yap. Ağ erişimi hatasını doğrudan yanlış parola diye yorumlama. Başka hesaba geçmek veya erişimi genişletmek, hata kanıtı olmadan ilk çözüm olmamalı.

**Eğitimde sıradaki:** [Yeni sohbette kararı koru](06-baglam-bellek.md)


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [9.2 Tekrarlanan yöntemi dar bir skill’e dönüştür.](../codex-kontrol-listesi.md#m-9-2)
- [9.3 Skill açıklamasına gerçek kapsam ve sınır yaz.](../codex-kontrol-listesi.md#m-9-3)
- [9.4 Yan etki yetkisini skill’in bulunabilirliğinden ayır.](../codex-kontrol-listesi.md#m-9-4)
- [9.5 Dış uygulama için önce amaca uygun aracı dene.](../codex-kontrol-listesi.md#m-9-5)
- [9.6 Taşınacak yeteneği Codex plugin biçiminde paketle.](../codex-kontrol-listesi.md#m-9-6)
- [9.7 MCP bağlantısını gerçek bir okuma işlemiyle sınayarak başla.](../codex-kontrol-listesi.md#m-9-7)

[İçindekiler](README.md) · [← İnternet, tarayıcı ve bilgisayar kullanımı](09-web-tarayici-bilgisayar.md) · [Talimatları ve kişisel çalışma düzenini kurmak →](11-talimatlar.md)
