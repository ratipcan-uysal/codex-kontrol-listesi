# Komutlar ve kısayollar

İçerik güncellemesi: 2026-10-30. Kaynak kontrol tarihleri kaynak dizinindedir.

Bir komutun başındaki işaret, nerede kullanılacağını değiştirir. Masaüstü mesaj alanındaki `/review`, işletim sistemi terminalindeki `codex review` ve doğal dilde “incele” aynı giriş biçimi değildir. Önce doğru yüzeyi seç.

<a id="baslarken-hangi-komutlar-isine-yarar"></a>

## Başlarken hangi komutlar işine yarar?

Bütün komutları ezberlemek gerekmez. Önce ihtiyacı tanı:

- İş belirsizse `/plan`: yaklaşımı ve kararları netleştir. Planın ardından uygulama isteğini ver.
- Aynı projede başka işe başlayacaksan `/new`: boş sohbet açar, dosyaları sıfırlamaz.
- Mevcut konuşmadan başka yön deneyeceksen `/fork`: geçmişten dallanırsın; dosya yalıtımını ayrıca seçersin.
- Ana işi kesmeden açıklama istiyorsan `/side`: yan soru açar.
- Kod değişti ve kusur arıyorsan `/review`: incelemenin hangi dosya/dal farkını kapsadığını seç.
- Kullanım veya bağlam durumunu anlamak için `/status`; kullanım ayarları için `/usage`.

Örneğin önce `/plan` ile bir tablo dönüşümünün belirsizliğini çözebilir, sonra “bu planı uygula” diyebilir, çalışırken `/side` ile bir terimi sorabilirsin. Komut seçmek, o komuttan sonra yazacağın görev tarifinin yerini tutmaz.

<a id="masaustu-mesaj-alani-belgelenmis-komutlarin-tamami"></a>

## Masaüstü mesaj alanı: belgelenmiş komutların tamamı

Mesaj alanına `/` yazıp listeden seç. Ortam ve hesap uygun değilse bazı komutlar görünmez. Aşağıdaki envanter 29 Ekim 2026'da açılan [masaüstü slash command belgesindeki](https://learn.chatgpt.com/docs/reference/slash-commands) 28 komutu kapsar; hepsi bu hesapta çalıştırılmış değildir.

| Komut | Ne zaman işe yarar? | Önemli ayrım |
|---|---|---|
| `/approve` | Otomatik incelemenin reddettiği işlem için bir yeniden denemeyi onaylama | Genel, sınırsız izin açmaz; etkin auto-review koşulu gerekir |
| `/archive` | Mevcut sohbeti aktif listeden kaldırma | Dosya temizliği veya kalıcı silme değildir |
| `/chat` | Yeni iş için projesiz sohbet seçme | Proje dosyalarını otomatik bağlamaz |
| `/cloud` | Uygun işi bulut ortamında yürütme | Hesap ve bulut erişimi gerekir |
| `/cloud-environment` | Kullanılacak bulut ortamını seçme | Yerel araç ve oturumları otomatik taşımaz |
| `/compact` | Uzayan sohbet bağlamını sıkıştırma | Eksiksiz arşiv veya devir belgesi yerine geçmez |
| `/fast` | Desteklenen modelin hızlı hizmet katmanını açma/kapatma | Model kataloğu ve kullanım koşullarına bağlıdır |
| `/feedback` | Sorunu ve isteğe bağlı logları geri bildirim penceresinde iletme | Göndereceğin tanı verisini gözden geçir |
| `/fork` | Yerel sohbetten ayrı sohbet veya worktree yönü açma | Dosya yalıtımı seçilen ortama bağlıdır |
| `/goal` | Süren bir hedef başlatma | Önce hedefi `/plan` ile netleştirmek yararlı olabilir |
| `/ide-context` | Paylaşılan IDE bağlamını açma/kapatma | Yalnız desteklenen editör bağlamını kapsar |
| `/init` | Proje için `AGENTS.md` başlangıcı üretme | Üretilen talimatlar projeye göre incelenmelidir |
| `/local` | Seçili yerel projede çalışmayı seçme | Doğru bilgisayar ve klasörü kontrol et |
| `/mcp` | Bağlı MCP sunucularının durumunu görme | Durum ekranı görev yetkisi vermez |
| `/memories` | Sohbetin bellek kullanma/üretme tercihini yönetme | Özellik erişimi gerekir; ChatGPT web belleğinden ayrıdır |
| `/model` | Mevcut sohbetin modelini seçme | Görünen modeller hesap ve istemciye bağlıdır |
| `/new` | Aynı yerel çalışma alanında boş sohbet açma | Mevcut dosyaları geri almaz |
| `/pet` | Masaüstü pet'ini gösterme/gizleme | İsteğe bağlı durum/giriş yüzeyidir |
| `/pin` | Sohbeti sabitleme veya sabitlemeyi kaldırma | Erişimi kolaylaştırır; bellek garantisi değildir |
| `/plan` | Çok adımlı iş için plan modunu açma/kapatma | Uygulama isteğiyle plan isteğini karıştırma |
| `/project` | Yeni sohbet için proje seçme | Başlangıç klasörü ve bağlamı etkiler |
| `/reasoning` | Düşünme çabasını seçme | Her model aynı seviyeleri sunmayabilir |
| `/rename` | Sohbete anlaşılır ad verme | Sonuç odaklı ad aramayı kolaylaştırır |
| `/review` | Kaydedilmemiş değişiklikleri veya taban dala farkı inceletme | Git kapsamını seç; inceleme düzeltmeyle aynı iş değildir |
| `/side` | Ana sohbeti kesmeden geçici yan soru açma | Kalıcı karar çıkarsa ana işe aktar |
| `/status` | Sohbet kimliği, bağlam kullanımı ve sınırları görme | Ücret faturasıyla aynı gösterge değildir |
| `/usage` | Kullanım ve faturalama ayarlarını açma | ChatGPT girişi ve özellik erişimine bağlıdır |
| `/worktree` | Ayrı Git çalışma kopyasında işe başlama | Git deposu ve başlangıç durumu gerekir |

Etkin skill'ler de komut listesinde görünebilir. `$` ile skill çağırabilir, desteklenen özel prompt'lara `/prompts:<ad>` yoluyla erişebilirsin. Bunlar yukarıdaki sabit komut sayısına dahil değildir; kurulumunun ekledikleridir.

<a id="goals-masaustu-ve-cli-farki"></a>

### Goals: masaüstü ve CLI farkı

Masaüstünde `/goal` hedefi başlatır. Hedef etkinleşince mesaj alanının üzerindeki ilerleme satırındaki düğmelerle duraklatma, sürdürme, metni düzenleme ve temizleme yapılır. Resmî masaüstü belgesi bu işlemler için yeni slash komutu yazmak yerine düğmeleri tarif ediyor. CLI Goals kılavuzundaki `/goal pause`, `/goal resume`, `/goal clear` örneklerini masaüstü komutları diye öğretme. [Masaüstü](https://learn.chatgpt.com/docs/reference/slash-commands) · [CLI Goals örnekleri](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)

<a id="terminal-tanilama-ve-otomasyon-komutlari"></a>

## Terminal: tanılama ve otomasyon komutları

Bu tablo bütün CLI bayraklarını öğretmeyi hedeflemez. Masaüstü kullanıcısının terminale geçtiğinde en çok ihtiyaç duyacağı ayrımları gösterir. Önce `codex --version`, sonra ilgili `--help` çıktısını oku. PATH'teki ikili uygulamanın kullandığından farklı olabilir. [CLI komutları](https://learn.chatgpt.com/docs/developer-commands) · [Canlı arama](https://learn.chatgpt.com/docs/web-search)

| Komut / giriş | Kullanım alanı | Beklenen sonuç |
|---|---|---|
| `codex --version` | Hangi sürümü çağırdığını öğrenmek | Sürüm bilgisi |
| `codex --search` | O terminal çalıştırmasında canlı web araması | Değişen bilgi için web erişimi; masaüstü slash komutu değil |
| `codex --help` | Kurulu komut ve seçenekleri görmek | O ikilinin yardım çıktısı |
| `codex` | Etkileşimli terminal oturumu açmak | Terminal içi sohbet |
| `codex resume` | Kayıtlı CLI sohbetine dönmek | Seçilen geçmişle devam |
| `codex fork` | CLI sohbetinden ayrı yön açmak | Yeni sohbet; dosya yalıtımı ayrıca seçilir |
| `codex review` | Terminalden kod incelemesi istemek | Belirtilen kapsamın bulguları |
| `codex exec` | Betikten etkileşimsiz görev çalıştırmak | Komut sonucu ve seçilen çıktı biçimi |
| `codex exec --help` | JSONL/şema/son mesaj seçeneklerini kontrol etmek | Desteklenen otomasyon sözleşmesi |
| `codex mcp --help` | MCP yönetim yollarını görmek | Sunucu yönetimi seçenekleri |
| `codex plugin --help` | Plugin yönetimini incelemek | Kurulu sürümün alt komutları |
| `codex doctor` | Belgelenmiş tanılama yolu | Kurulu sürüm destekliyorsa ortam bulguları |
| `codex login --help` | Giriş yöntemini öğrenmek | Hesap/API seçenekleri; giriş işlemi ayrı |

Etkileşimli CLI içindeki `/statusline`, `/hooks`, `/permissions`, `/skills`, `/plugins`, `/resume`, `/ps` ve `/diff` gibi komutların masaüstünde aynı adla bulunduğunu varsayma. CLI `/status`, masaüstü `/status` ile farklı ayrıntılar gösterebilir. Güncel tam liste için terminalde `/` menüsünü ve [CLI referansını](https://learn.chatgpt.com/docs/developer-commands) kullan.

`codex exec` otomasyonu için insanın okuyacağı son mesaj ile olay akışı ayrılır. JSONL, satır başına bir JSON olayı demektir. Süreç çıkış kodu, modelin son metni ve hedef dosyanın gerçek durumu birlikte değerlendirilmelidir. [Etkileşimsiz çalışma](https://learn.chatgpt.com/docs/non-interactive-mode)

<a id="dogal-dil-komutlari-arayuz-sozdizimi-degildir"></a>

## Doğal dil komutları: arayüz sözdizimi değildir

> Açık işi durdur; değişmiş dosyaları geri almadan mevcut durumu raporla.

> Bu taslağı kaynak metinle anlam ve atıf açısından karşılaştır. Yeni araştırma yalnız eksik iddia için gerekirse yap.

> Bu işte yerel düzeltmeleri tamamla. Sonucu gerçek hedefte gözlemeden yayınlandı deme.

Bu cümleler görev tarifidir. `/` komutları gibi sabit program arayüzü değillerdir; gerçek araç erişimi ve görev yetkisi içinde yorumlanırlar.

<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [14.2 Headless koşumun çıktısını ve dış sınırını belirle.](../codex-kontrol-listesi.md#m-14-2)

[İçindekiler](README.md)
