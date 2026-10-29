# 11. Talimatları ve kişisel çalışma düzenini kurmak

İçerik güncellemesi: 2026-10-30. Kaynak kontrol tarihleri kaynak dizinindedir.

Kalıcı talimat, aynı düzeltmeyi tekrar söyleme ihtiyacını azaltır. Ancak her başarısızlığın ardından yeni bir yasak eklemek, kısa işi uzun bir prosedüre çevirebilir. İyi kural belirli bir sürtüşmeyi çözer.

<a id="talimati-dogru-yere-koy"></a>

## Talimatı doğru yere koy

Global talimat, projeler arasında değişmeyen tercih içindir: kullanılan dil, kanıt standardı, dış işlem sınırı gibi. Proje kökündeki `AGENTS.md`, o projenin çalışma ve doğrulama bilgisini tutar. Alt dizindeki talimat daha dar alanın gereğini açıklayabilir. Dosyanın kapsamı ve uygulanan öncelik zinciri önemlidir; farklı yerlerde aynı kuralı çoğaltmak çelişki riskini artırır. [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Codex'in yapılandırma dosyası `config.toml`, arayüz tercihleri ve çalışma politikalarının başka bir katmanıdır. Her ayar doğal dil talimatıyla aynı etkiye sahip değildir. Proje güveni, kullanıcı ayarı, yönetilen kurum ayarı ve çalışma sırasında verilen seçenekler farklı kapsamlar taşır. Belgedeki katman sırasını esas al; rastgele kopyalanmış bir dosyanın yüklendiğini varsayma. [Yapılandırma](https://learn.chatgpt.com/docs/config-file/config-basic) · [Ayar katmanları](https://learn.chatgpt.com/docs/configuration)

**Dosya adı ile uygulama özelliğini ayır.** Bazı Cookbook örnekleri `PLANS.md`, `GOALS.md` ve `PROMPTS.md` kullanır. Bunlar isteğe bağlı belge düzenidir: `GOALS.md` yazmak `/goal` başlatmaz, `PLANS.md` oluşturmak plan modunu açmaz. Mevcut karar ve ilerleme notların aynı işi görüyorsa yeni kopyalar üretme. [Çalışma düzeni örneği](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex)

<a id="zayif-ve-ise-yarayan-kural"></a>

## Zayıf ve işe yarayan kural

| Belirsiz kural | Uygulanabilir kural |
|---|---|
| “Her şeyi test et.” | “İçerik değişince üreticiyi ve bağlantı denetimini çalıştır; etkileşim değişince tarayıcı regresyonunu da çalıştır.” |
| “Asla hata yapma.” | “İddianın kanıtı yoksa gözlem, çıkarım ve açık soruyu ayır.” |
| “Hiç soru sorma.” | “Geri alınabilir ayrıntıları çöz; yayın hedefi veya veri kaybı değişiyorsa karar iste.” |
| “Bütün bilgiyi hatırla.” | “Kalıcı kararları proje notlarına yaz; eski karar değişince yenisinin öncekini geçersiz kıldığını belirt.” |

Bu kuralların değeri uzunluklarında değil, yanlış davranışın yerine ne koyduklarında.

<a id="kurgu-ornegi-kucuk-proje-talimati"></a>

## Kurgu örneği: küçük proje talimatı

```text
İçeriğin kaynağı kaynak/content.py. Üretilen HTML'yi elle düzenleme.
Mevcut madde kimliklerini ve kullanıcı işaretlerini koru.
İçerik değişince üretici ve kaynak testlerini çalıştır.
Etkileşim değişince tarayıcı testini çalıştır ve görüntüyü aç.
Teslimde yerel değişiklik, push ve canlı yayın durumunu ayrı yaz.
```

Bu örnek, bu rehberin üretim biçimine benzer bir proje için yazılmıştır. Başka projeye aynen yapıştırmak yerine gerçek kaynak ve komutlarla değiştir.

<a id="kurallar-sandbox-ve-hook-ayni-sey-degildir"></a>

## Kurallar, sandbox ve hook aynı şey değildir

Talimat modelin davranışını yönlendirir. Sandbox teknik erişimi sınırlar. Komut kuralları belirli işlemlerin nasıl onaylanacağını tanımlayabilir. Hook, belirli yaşam döngüsü olayında çalışan programdır. Bir Markdown cümlesi, işletim sisteminde dosya erişimini kapatmaz. [Komut kuralları](https://learn.chatgpt.com/docs/agent-configuration/rules) · [Hook](https://learn.chatgpt.com/docs/hooks)

Hook'lar örneğin desteklenen olaydan sonra kısa bir yerel kontrol veya bildirim üretmek için kullanılabilir. Her yanıttan sonra tüm projeyi derlemek ise akışı yavaşlatır. Olay adı, veri sözleşmesi ve yüklenme yolu istemci/sürüm belgesinden doğrulanmalı. CLI için anlatılan hook'u masaüstünde aynı adla çalışıyor kabul etme. Hatalı hook kendi hata döngüsünü veya takılı kalan süreci yaratabilir.

<a id="tekrarlanan-isi-kodla"></a>

## Tekrarlanan işi kodla

Her yayında aynı dosyaları üretip bağlantıları sayıyorsan, bu adımları bir üretim betiğine taşı. Codex betiğin amacını ve ne zaman çalışacağını bilsin. Böylece her tur farklı bir dönüşüm icat etmez; değişiklik diff üzerinden incelenebilir.

İşi tamamlayınca “hangi kuralı ekleyelim?” kadar “hangi eski kuralı çıkaralım?” sorusu da değerlidir. Eski kaynak yolunu, artık gerekmeyen kontrolü ve çelişen onay cümlesini kaldır. Gizli anahtarları veya kişisel veriyi talimat dosyasına koyma; bu dosyalar Git'e girebilir.

<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [1.1 Global AGENTS.md’yi davranışı değiştiren kurallarla sınırla.](../codex-kontrol-listesi.md#m-1-1)
- [1.2 Aktif projenin giriş talimatını güncel tut.](../codex-kontrol-listesi.md#m-1-2)
- [1.3 Makineye özgü notu açık bir dosya bağlantısıyla ayır.](../codex-kontrol-listesi.md#m-1-3)
- [1.4 Dizin kuralını alt AGENTS.md ile kapsamlandır.](../codex-kontrol-listesi.md#m-1-4)
- [1.5 Gerekli harici notun yüklendiğini gözle.](../codex-kontrol-listesi.md#m-1-5)
- [1.6 Araçlar arasında ortak kuralın tek kaynağını belirle.](../codex-kontrol-listesi.md#m-1-6)
- [1.7 Ayarın hangi katmandan geldiğini doğrula.](../codex-kontrol-listesi.md#m-1-7)
- [6.5 Tekrarlanan işlemi gözden geçirilebilir betiğe dönüştür.](../codex-kontrol-listesi.md#m-6-5)
- [10.1 Ortak proje ayarıyla kişisel varsayılanı ayır.](../codex-kontrol-listesi.md#m-10-1)
- [10.2 Talimat değişikliğini davranış değişikliği olarak incele.](../codex-kontrol-listesi.md#m-10-2)
- [10.3 Ekip yöntemini ortak kaynakta sürümle.](../codex-kontrol-listesi.md#m-10-3)
- [18.4 Kuralı kısa tut, gerekçeyi gerektiğinde aç.](../codex-kontrol-listesi.md#m-18-4)
- [19.3 Eskimiş AGENTS.md kurallarını periyodik olarak gözden geçir.](../codex-kontrol-listesi.md#m-19-3)

[İçindekiler](README.md) · [← Bağlantılar, MCP, plugin ve skill](10-baglantilar-skills.md) · [Güvenilir sonuç elde etmek →](12-dogrulama.md)
