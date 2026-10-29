# 2. Uygulamanın tamamını tanımak

Belge kontrolü: 2026-10-29.

Uygulamayı öğrenmenin pratik yolu, bir işin nerede başladığını, hangi kaynaklara dayandığını ve çıktısının nerede incelendiğini takip etmek. Menüler bu akış içinde anlam kazanır.

## İlk açılış ve doğru çalışma yüzeyi

Resmî indirme sayfasından masaüstü uygulamasını kur, hesabınla giriş yap ve ürün seçicisinden Codex'i aç. Güncel belgelerde ortak uygulama ChatGPT desktop app adıyla geçiyor. Chat, Work ve Codex'in görünümü ve geçmişi aynı şey değildir. Codex'te geliştirici ayrıntıları, Git değişiklikleri ve inceleme araçları görünür. Aynı yüzeyde belge ve araştırma işleri de yapabilirsin. [Kurulum](https://learn.chatgpt.com/docs/app) · [Yüzey seçimi](https://learn.chatgpt.com/docs/use-chatgpt)

macOS, Windows ve Linux için kurulum yolları farklıdır. Özellikle bilgisayar kullanımı gibi yeteneklerde her platformda eşit destek bekleme. Bir seçeneği göremiyorsan önce hesap, uygulama sürümü, çalışma yüzeyi ve kurum politikası ayrımını yap. Başka platformun menüsünü aramak sonuç vermez. [Windows](https://learn.chatgpt.com/docs/windows/windows-app) · [Linux](https://learn.chatgpt.com/docs/linux/linux-app)

Windows uygulaması yerel PowerShell veya yapılandırılmış WSL2 ortamıyla çalışabilir. Terminal tercihini değiştirmek açık oturumu kendiliğinden değiştirmeyebilir. Linux sürümü belge kontrol tarihinde önizleme durumunda; dağıtım ve işlemci mimarisine uygun paket seçmek gerekir. İndirme ve destek listesini yukarıdaki platform bağlantılarından kontrol et.

## Proje ve sohbet düzeni

Proje, ilgili işleri bir arada tutar. Yerel projeye klasör bağladığında Codex o dosyalarla çalışabilir. Birden fazla klasör varsa birincil klasörün seçimi önemlidir: yeni sohbetin çalışma dizini ve otomatik proje talimatı keşfi buradan başlar. İkincil klasörün erişilebilir olması, içindeki bütün talimatların otomatik yüklendiğini göstermez. [Projeler](https://learn.chatgpt.com/docs/projects)

Sohbetleri “web sitesi”, “notlar”, “test” gibi geniş adlar yerine sonuçlarıyla adlandır: “Etkinlik sayfasının mobil taşması”, “Mayıs programı kaynak kontrolü”. Sabitleme yalnız görünürlüğü değiştirir. Arşivleme, sohbeti aktif listeden kaldırır. Dosyalarının yedeği için ayrı bir yöntem gerekir. Arşivlenmiş sohbetlere Settings içinden dönebilirsin.

## Mesaj alanı ve bağlam ekleme

Bir dosyayı eklemek, ekran görüntüsü vermek ve açık tarayıcı sekmesini referans göstermek farklı bağlam türleridir. Mesajda hangisinin ne işe yaradığını yaz. Birden fazla görüntüde “ilk görüntü hedef, ikincisi mevcut sonuç” gibi bir ayrım, ters yönde düzeltme riskini azaltır. Masaüstünde görseli Shift basılı sürükleme yolu belgelenmiştir. [Görsel girdiler](https://learn.chatgpt.com/docs/image-inputs)

`@` menüsünde bulunan bir uygulama veya sekmeyi seçerek hedefi netleştirebilirsin. `$` ile kullanılabilir bir skill seçebilirsin. Hedefi menüdeki öğeden seç. Yazdığın bir araç adı listede yoksa bağlantı kurulmuş sayılmaz. Model ve düşünme ayarı mesaj alanının altındaki denetimlerden seçilir.

## Yan panelleri sonuç incelemek için kullan

Dosya önizlemesi, tarayıcı ve terminal sohbetin yanında açılabilir. Desteklenen belge, tablo, sunum ve PDF çıktılarında dosyayı önizleyip belirli bir alana yorum bırakabilirsin. HTML dosyasının kaynağıyla render edilmiş görünümünü karşılaştırabilirsin. LaTeX düzenlerken de kaynak ve derlenen PDF yan yana incelenebilir. Son başarılı PDF'nin ekranda kalması, son düzenlemenin derlendiğini kanıtlamaz. [Dosyalarla çalışma](https://learn.chatgpt.com/docs/artifacts-viewer)

Terminal, komutların çalıştığı paneldir. New tab → Terminal ile açılır. Çalışan sunucunun çıktısı ve hataları burada görünür. Codex'ten terminaldeki son hatayı açıklamasını isteyebilirsin. Terminali açmak bir sunucuyu kendiliğinden başlatmaz. [Terminal](https://learn.chatgpt.com/docs/integrated-terminal)

## Günlük işte değerli kısayollar

| İş | macOS | Windows |
|---|---|---|
| Komut menüsü | ⌘K veya ⌘⇧P | Ctrl+K veya Ctrl+Shift+P |
| Ayarlar | ⌘, | Ctrl+, |
| Kısayol listesi | ⌘/ | Ctrl+/ |
| Yeni sohbet | ⌘N | Ctrl+N |
| Dosya ara | ⌘P | Ctrl+P |
| Dosya ağacı | ⌘⇧E | Ctrl+Shift+E |
| Sohbet içinde bul | ⌘F | Ctrl+F |
| Terminal | Ctrl+` | Ctrl+` |
| İnceleme sekmesi | Ctrl+Shift+G | Ctrl+Shift+G |
| Tarayıcı sekmesi | ⌘T | Ctrl+T |

Tablo belgelenmiş varsayılanları gösterir. Odak ve kişisel tuş ataması farklıysa kısayolun davranışı değişebilir. Komut menüsünde işlemin adını aramak, bütün kısayolları ezberlemekten daha kullanışlıdır. [Tam komut listesi](https://learn.chatgpt.com/docs/reference/commands)

## Az görünen ama işe yarayan ayarlar

Settings → General içindeki gönderme tercihi, uzun mesajı Enter ile yanlışlıkla göndermeyi önleyebilir. Follow-up behavior, çalışma sürerken gönderdiğin mesajın mevcut işi yönlendirmesini veya sonraki turu beklemesini belirler. Bildirim ayarı, işin tamamlanmasını takip etmeye yarar. Desteklenen sistemlerde uyku önleme seçeneği yerel uzun işlerde kullanılabilir. Açılır ayrı sohbet penceresi ve Always on top, başka uygulamayla karşılaştırma yaparken yararlıdır. [Ayarlar](https://learn.chatgpt.com/docs/reference/settings)

Appearance içindeki tema ve yazı tipi tercihleri uzun okumayı kolaylaştırabilir. Open için varsayılan editör veya uygulama seçimi, dosyayı hangi programda açacağını belirler. Projeye özel tercih genel tercihin önüne geçebilir. Bu ayarlar modelin talimat dosyasından ayrı arayüz tercihleridir.

Pets ve Mini, başka uygulamada çalışırken sohbet durumuna ulaşmak için isteğe bağlı yüzeylerdir. Settings → Pets içinden seçip `/pet` ile gösterip gizleyebilirsin. Mini, hayvan karakteri olmadan denetimleri sunar. Buradan başlayan sohbet proje dışında açılır; proje bağlamı gerekiyorsa ana penceredeki projeden başla. Özel pet yerelde saklanabilir ve web yüzeyine kendiliğinden eşitlenmeyebilir. Görünüm tercihi modelin iş kalitesini değiştirmez.

Codex Micro, uyumlu fiziksel donanımla sohbet ve komut kontrolü sunan ayrı bir seçenektir. Temel kullanım için gerekmez. [Pets](https://learn.chatgpt.com/docs/pets) · [Micro](https://learn.chatgpt.com/docs/features/codex-micro)

## Kurgu senaryo: aynı oturumda üç görünüm

Atölye'nin program sayfasını düzenlerken solda sohbet, sağda yerel sayfa, altta terminal açık olsun. Görsel taşmayı sayfada işaretle, düzeltme isteğini sohbette ver, sunucu hatası varsa terminal çıktısına bak. Üç görünüm aynı sorunun farklı kanıtlarını sağlar. Kod değişikliği görünümüne geçerek değişikliğin beklediğin dosyada olduğunu ayrıca kontrol edebilirsin.

[İçindekiler](README.md) · [← Codex ile neler yapabilirsin?](01-olanaklar.md) · [Codex gerçekte nasıl çalışıyor? →](03-calisma-mantigi.md)
