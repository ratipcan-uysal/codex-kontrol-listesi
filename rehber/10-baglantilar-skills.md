# 10. Bağlantılar, MCP, plugin ve skill

Belge kontrolü: 2026-10-29.

Codex'e yeni bir yetenek eklerken önce eksik olanı adlandır: veriye erişim mi, doğru yöntemi bilmek mi, tekrarlı işlemi yürütmek mi? Her ihtiyaç için yeni plugin kurmak gerekmez.

## Dört kavramı ayır

| Kavram | Ne sağlar? | Tek başına ne sağlamaz? |
|---|---|---|
| Bağlantı / connector | Bir hizmetteki hesabına kontrollü erişim | Her veriye veya her işleme sınırsız yetki |
| MCP | Araç ve veri kaynaklarını modele sunan ortak protokol | Model kalitesi, kalıcı bellek veya görev onayı |
| Skill | Belirli işi ne zaman ve nasıl yapacağını anlatan yönerge ve yardımcı kaynaklar | Gerekli hesabın bağlı olması |
| Plugin | Skill, araç ve bağlantıları paketleyebilen kurulum birimi | İçindeki her yeteneğin her yüzeyde çalışması |

[MCP](https://learn.chatgpt.com/docs/extend/mcp) · [Skill ve plugin](https://learn.chatgpt.com/docs/skills-and-plugins) · [Plugin kullanımı](https://learn.chatgpt.com/docs/plugins)

Örneğin takvim bağlantısı etkinlikleri okuyabilir; bir toplantı hazırlık skill'i hangi bilgileri birleştireceğini söyler. Kullanıcının “taslak çıkar” isteği, takvime etkinlik yazma yetkisi vermez.

## Keşfetme, bağlama ve çağırma

Plugins bölümünde gereken yeteneği bul, hangi hesabın ve izinlerin gerektiğini incele, bağlantıyı tamamla. Kurulumdan sonra araçların kullanılabilirliğini yeni sohbet veya ilgili menü üzerinden kontrol etmek gerekebilir. Codex'te `$` menüsünden skill seçmek ya da adını açıkça yazmak, ilgili yöntemin kullanılmasını netleştirir. Bazı diğer yüzeylerde aynı çağrı `@` ile sunulur; sözdizimini yüzeye göre oku.

Bir plugin'in masaüstü etiketi varsa web veya mobilde aynı aracı bekleme. Güncel belgeler plugin paketleriyle IDE'de kullanılan bağımsız skill/MCP yollarını da ayırır. “Bilgisayarımda kurulu” ile “bu sohbetin araçları arasında” farklı durumlardır.

## İyi skill neyi saklar?

Tekrar tekrar açıklamak zorunda kaldığın yöntemi saklar. Örneğin “kaynaklı makale yaz” sürecinde kaynak iddiası, yorum ve alıntı sınırını ayırabilir; gereken dosya şablonunu gösterebilir. Her olası işi üstlenen belirsiz bir skill ise yanlış zamanda devreye girer.

`SKILL.md` dosyasında kısa ad/açıklama, ne zaman uygulanacağı, önemli iş akışı ve gerekirse yardımcı dosyalar bulunur. Ayrıntı ihtiyaç oldukça yüklenir. Kullanım açıklamasını gereksiz uzatmak keşfi zorlaştırabilir. [Skill oluşturma](https://learn.chatgpt.com/docs/build-skills)

> `$skill-creator` kullanarak, kaynaklı Türkçe incelemeleri hazırlama yöntemimizi skill'e dönüştür. Kaynak toplama, alıntı sınırı ve son kontrolü tanımla. Yalnız yazım düzeltmesi istendiğinde bu süreci başlatmasın.

Bu kurgu örnekte beklenen çıktı yalnız uzun bir talimat değildir: doğru tetiklenen, ilgisiz işte devreye girmeyen, kaynakları belli bir paket gerekir.

## Betik mi, skill mi, özel araç mı?

Aynı kuralla bin dosya adı değişiyorsa betik daha uygundur. Kaynak kalitesini tartıp makale yapısını seçmek yorum gerektirir; skill bu yöntemi yönlendirir. Mevcut araçların erişemediği kurumsal veriye kontrollü erişim gerekiyorsa özel MCP/araç geliştirmek anlamlı olabilir. Önce hazır araçla küçük işi tamamla; soyut bir ihtiyaca büyük entegrasyon kurma.

## Record & Replay

Desteklenen macOS kurulumunda Plugins → + → Record a skill yolu bilgisayarda gösterdiğin akıştan skill üretmeye yardımcı olur. Computer Use kurulumu gerekir. Kaydı durdurduktan sonra oluşan yönergeleri incele: sabit kişi adı, tarih, dosya yolu veya tek seferlik tıklama genel kurala dönüşmüş olabilir. Replay, değişen ekranda araçlarla yürütülen akıştır; her pikseli aynı sırayla basan kusursuz makro garantisi değildir. [Record & Replay](https://learn.chatgpt.com/docs/extend/record-and-replay)

## Bağlantı çalışmıyorsa

Önce kurulum, hesap bağlantısı, izin kapsamı ve o sohbette araç keşfini ayrı kontrol et. Araç görünüyorsa küçük bir okuma denemesi yap. Ağ erişimi hatasını doğrudan yanlış parola diye yorumlama. Başka hesaba geçmek veya erişimi genişletmek, hata kanıtı olmadan ilk çözüm olmamalı.

## Kontrol listesinde karşılığı

- [9.2 Tekrarlanan yöntemi dar bir skill’e dönüştür.](../codex-kontrol-listesi.md#m-9-2)
- [9.3 Skill açıklamasına gerçek kapsam ve sınır yaz.](../codex-kontrol-listesi.md#m-9-3)
- [9.4 Yan etki yetkisini skill’in bulunabilirliğinden ayır.](../codex-kontrol-listesi.md#m-9-4)
- [9.5 Dış uygulama için önce amaca uygun aracı dene.](../codex-kontrol-listesi.md#m-9-5)
- [9.6 Taşınacak yeteneği Codex plugin biçiminde paketle.](../codex-kontrol-listesi.md#m-9-6)
- [9.7 MCP bağlantısını gerçek bir okuma işlemiyle sınayarak başla.](../codex-kontrol-listesi.md#m-9-7)

[İçindekiler](README.md) · [← İnternet, tarayıcı ve bilgisayar kullanımı](09-web-tarayici-bilgisayar.md) · [Talimatları ve kişisel çalışma düzenini kurmak →](11-talimatlar.md)
