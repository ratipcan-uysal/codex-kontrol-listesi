# 2. Uygulamanın tamamını tanımak

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Uygulamayı öğrenmenin pratik yolu, bir işin nerede başladığını, hangi kaynaklara dayandığını ve çıktısının nerede incelendiğini takip etmek. Menüler bu akış içinde anlam kazanır.

<a id="i-lk-acilis-ve-dogru-calisma-yuzeyi"></a>

## İlk açılış ve doğru çalışma yüzeyi

Resmî indirme sayfasından masaüstü uygulamasını kur, hesabınla giriş yap ve ürün seçicisinden Codex'i aç. Güncel belgelerde ortak uygulama ChatGPT desktop app adıyla geçiyor. Chat, Work ve Codex'in görünümü ve geçmişi aynı şey değildir. Codex'te geliştirici ayrıntıları, Git değişiklikleri ve inceleme araçları görünür. Aynı yüzeyde belge ve araştırma işleri de yapabilirsin. [Kurulum](https://learn.chatgpt.com/docs/app) · [Yüzey seçimi](https://learn.chatgpt.com/docs/use-chatgpt)

<a id="i-lk-dosyani-uret-ac-duzelt"></a>

## İlk dosyanı üret, aç, düzelt

Kod yazmak veya Git kurmak ilk belge işi için gerekmez. Git, dosyaların sürüm geçmişini tutan araçtır; kod projeleri ve değişiklik yönetiminde daha sonra işimize yarayacak.

1. Bilgisayarında bu iş için bir klasör seç. Uygulamada **Projects → +** ile bu klasörü yerel proje olarak ekle. Proje ekleme yolu arayüzünde farklı görünüyorsa komut menüsünde “project” ara.
2. O projenin içinde yeni sohbet aç. İlk dosya işinde **Local / Work locally** ortamını seç. Bu, işin kendi bilgisayarındaki proje klasöründe yürütülmesidir.
3. Kaynak notu mesaj alanına ekle veya proje içindeki dosyayı adıyla belirt. “Bu nottan `program-taslagi.md` oluştur. Kesinleşmemiş tarihleri açık sorulara ayır. Dosyayı önizlemede aç” de. `.md`, düz metin olarak da açılan Markdown belge biçimidir.
4. Yanıttaki dosya bağlantısını aç. Bağlantı görünmüyorsa “Oluşturduğun dosyayı uygulamanın panelinde aç” diye iste. Taslağın gerçekten kaydedildiği konumu ve içeriğini görebilirsin.
5. Aynı sohbette “Açık soruları en alta taşı; tarih ve isimleri değiştirme” de. Son dosyayı yeniden açıp istediğin kısmın değiştiğine bak.

Dosya henüz yoksa ilk istekte “Boş proje klasöründe, kurgu bir etkinlik için program taslağı oluştur; bütün tarih ve isimlerin örnek olduğunu yaz” diyebilirsin. Bu yol herhangi bir hesabı bağlamadan üretim–önizleme–düzeltme döngüsünü gösterir. [Başlangıç ve proje akışı](https://learn.chatgpt.com/docs/projects) · [Yerel çalışma](https://learn.chatgpt.com/docs/environments/modes)

Bu noktada CLI (terminalden kullanılan istemci), IDE (kod editörü) veya MCP kurman gerekmiyor. Bunlar ihtiyaca göre öğreneceğin ek yollar. Dosya üretmek için bir servise yükleme veya yayınlama da gerekmez.

**Anlatıcı gösterimi:** Solda proje klasörünü, sağda açılan dosyayı göster. “Açık soruları sona taşı” dedikten sonra aynı dosyadaki değişikliği göster. Bu üç hareketi tamamlayınca [işe göre model seçimine geç](07-model-hiz-kullanim.md#hangi-ise-hangi-modelle-baslamali); aşağıdaki menüler ihtiyaç anında başvurmak için duruyor.

<a id="platform-ayrintisina-ihtiyac-duyarsan"></a>

### Platform ayrıntısına ihtiyaç duyarsan

macOS, Windows ve Linux için kurulum yolları farklıdır. Özellikle bilgisayar kullanımı gibi yeteneklerde her platformda eşit destek bekleme. Bir seçeneği göremiyorsan önce hesap, uygulama sürümü, çalışma yüzeyi ve kurum politikası ayrımını yap. Başka platformun menüsünü aramak sonuç vermez. [Windows](https://learn.chatgpt.com/docs/windows/windows-app) · [Linux](https://learn.chatgpt.com/docs/linux/linux-app)

Windows uygulaması PowerShell (Windows komut ortamı) veya WSL2 (Windows içinde Linux ortamı) ile çalışabilir. Terminal tercihini değiştirmek açık oturumu kendiliğinden değiştirmeyebilir. Linux sürümü belge kontrol tarihinde önizleme durumunda; dağıtım ve işlemci mimarisine uygun paket seçmek gerekir. İndirme ve destek listesini yukarıdaki platform bağlantılarından kontrol et.

<a id="proje-ve-sohbet-duzeni"></a>

## Proje ve sohbet düzeni

Proje, ilgili işleri bir arada tutar. Yerel projeye klasör bağladığında Codex o dosyalarla çalışabilir. Birden fazla klasör varsa birincil klasörün seçimi önemlidir: yeni sohbetin çalışma dizini ve otomatik proje talimatı keşfi buradan başlar. İkincil klasörün erişilebilir olması, içindeki bütün talimatların otomatik yüklendiğini göstermez. [Projeler](https://learn.chatgpt.com/docs/projects)

Sohbetleri “web sitesi”, “notlar”, “test” gibi geniş adlar yerine sonuçlarıyla adlandır: “Etkinlik sayfasının mobil taşması”, “Mayıs programı kaynak kontrolü”. Sabitleme yalnız görünürlüğü değiştirir. Arşivleme, sohbeti aktif listeden kaldırır. Dosyalarının yedeği için ayrı bir yöntem gerekir. Arşivlenmiş sohbetlere Settings içinden dönebilirsin.

![Proje ve sohbetleri bulmak. Soldaki listede sabitlenmiş sohbet, diğer sohbetler ve Projects başlığı altındaki klasörleri ayırt et. Bir sohbet adı ile bağlı proje klasörü farklı öğelerdir.](assets/projects.png)

**Proje ve sohbetleri bulmak.** Soldaki listede sabitlenmiş sohbet, diğer sohbetler ve Projects başlığı altındaki klasörleri ayırt et. Bir sohbet adı ile bağlı proje klasörü farklı öğelerdir. [Tam boyut](assets/projects.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/projects) · 2026-10-29.

1. **Nereye bak:** Projects altındaki klasörlere ve üstteki sohbet adlarına.
2. **Ne yap:** Dosya işi için ilgili yerel projeyi seç; sohbeti sonuç adıyla adlandır.
3. **Ne gör:** Yeni konuşmanın hangi proje kaynaklarıyla başlayacağı anlaşılır olur.

**Yerel proje ile ChatGPT projesi farklı kaynakları bağlar.** Yerel proje bilgisayarındaki klasörlerle çalışır. ChatGPT projesindeki Sources ise yüklenen veya bağlanan bulut kaynaklarıdır; bilgisayarındaki klasöre otomatik erişim vermez. İki yerde aynı proje adını görmek dosyaların ortak olduğu anlamına gelmez.

Eski işi bulmak için kenar çubuğundaki **Search chats** alanında ayırt edici bir ifade veya dal adı ara. ⌘F / Ctrl+F ise açık sohbetin içinde arar. Search chats için belgelenmiş varsayılan kısayol yok; Settings → Keyboard shortcuts üzerinden atanabilir. Quick chat, New chat yanındaki simgeden açılan genel ChatGPT girişidir ve Codex kenar çubuğunda görünmez. Proje dosyası üzerinde işe başlayacaksan projenin kendi yeni sohbetini kullan. [Sohbetleri bulma ve düzenleme](https://learn.chatgpt.com/docs/projects)

<a id="mesaj-alani-ve-baglam-ekleme"></a>

## Mesaj alanı ve bağlam ekleme

Bir dosyayı eklemek, ekran görüntüsü vermek ve açık tarayıcı sekmesini referans göstermek farklı bağlam türleridir. Mesajda hangisinin ne işe yaradığını yaz. Birden fazla görüntüde “ilk görüntü hedef, ikincisi mevcut sonuç” gibi bir ayrım, ters yönde düzeltme riskini azaltır. Masaüstünde görseli Shift basılı sürükleme yolu belgelenmiştir. [Görsel girdiler](https://learn.chatgpt.com/docs/image-inputs)

`@` menüsünde bulunan bir uygulama veya sekmeyi seçerek hedefi netleştirebilirsin. `$` ile kullanılabilir bir skill (belirli işi yürütme yöntemi) seçebilirsin. Hedefi menüdeki öğeden seç. Yazdığın bir araç adı listede yoksa bağlantı kurulmuş sayılmaz. Model ve düşünme ayarı mesaj alanının altındaki denetimlerden seçilir.

**Mesaj önerisi ile gönderme aynı hareket değildir.** Composer predictions erişimin açıksa Codex yanıtından sonra bir sonraki mesaj için öneri gösterebilir. Tab öneriyi düzenlenebilir taslağa alır; kendiliğinden göndermez. Taslağın istediğin işi tarif ettiğini okuyup sonra gönder. Ayar: Settings → General → Composer → Show predictions. Belge tarihinde kişisel Pro hesabı, 18 yaş ve üzeri kullanıcı, desteklenen bölge/model ve yerel veya SSH ile bağlı uzak bilgisayardaki sohbet koşulları var; herkeste görünmesi beklenmez. [Mesaj önerileri](https://learn.chatgpt.com/docs/features/composer-predictions)

<a id="yan-panelleri-sonuc-incelemek-icin-kullan"></a>

## Yan panelleri sonuç incelemek için kullan

Dosya önizlemesi, tarayıcı ve terminal sohbetin yanında açılabilir. Desteklenen belge, tablo, sunum ve PDF çıktılarında dosyayı önizleyip belirli bir alana yorum bırakabilirsin. HTML dosyasının kaynağıyla ekranda oluşturulmuş görünümünü karşılaştırabilirsin. LaTeX adlı bilimsel belge biçimini düzenlerken de kaynak ve derlenen PDF yan yana incelenebilir. Son başarılı PDF'nin ekranda kalması, son düzenlemenin derlendiğini kanıtlamaz. [Dosyalarla çalışma](https://learn.chatgpt.com/docs/artifacts-viewer)

Terminal, komutların çalıştığı paneldir. New tab → Terminal ile açılır. Çalışan sunucunun çıktısı ve hataları burada görünür. Codex'ten terminaldeki son hatayı açıklamasını isteyebilirsin. Terminali açmak bir sunucuyu kendiliğinden başlatmaz. [Terminal](https://learn.chatgpt.com/docs/integrated-terminal)

![Sohbetin yanında sunum önizlemesi. Solda üretim isteği ve dosya bağlantısı, sağda slayt listesi ve seçili slayt var. Dosyayı yalnız teslim mesajından değerlendirmek yerine önizlemede incele.](assets/preview.png)

**Sohbetin yanında sunum önizlemesi.** Solda üretim isteği ve dosya bağlantısı, sağda slayt listesi ve seçili slayt var. Dosyayı yalnız teslim mesajından değerlendirmek yerine önizlemede incele. [Tam boyut](assets/preview.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/artifacts-viewer) · 2026-10-29.

1. **Nereye bak:** Soldaki output.pptx bağlantısına, sağdaki slayt listesine.
2. **Ne yap:** Sorunlu slaytı seç; yalnız o parçanın değişmesini, sayıların korunmasını iste.
3. **Ne gör:** Son dosyada aynı karar ve verilerle daha okunur bir slayt.

Ekranda bir sunum görünse de aynı alışkanlık rapor ve tablo için geçerli: dosyayı aç, sorunlu bölgeyi tarif et, değişikliği aynı çıktı üzerinde iste. “Yeni dosya üret” demediğin sürece hangi dosyanın son sürüm olduğu belli kalsın.

<a id="gunluk-iste-degerli-kisayollar"></a>

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

<a id="az-gorunen-ama-ise-yarayan-ayarlar"></a>

## Az görünen ama işe yarayan ayarlar

Settings → General içindeki gönderme tercihi, uzun mesajı Enter ile yanlışlıkla göndermeyi önleyebilir. Follow-up behavior, çalışma sürerken gönderdiğin mesajın mevcut işi yönlendirmesini veya sonraki turu beklemesini belirler. Bildirim ayarı, işin tamamlanmasını takip etmeye yarar. Desteklenen sistemlerde uyku önleme seçeneği yerel uzun işlerde kullanılabilir. Açılır ayrı sohbet penceresi ve Always on top, başka uygulamayla karşılaştırma yaparken yararlıdır. [Ayarlar](https://learn.chatgpt.com/docs/reference/settings)

Appearance içindeki tema ve yazı tipi tercihleri uzun okumayı kolaylaştırabilir. Open için varsayılan editör veya uygulama seçimi, dosyayı hangi programda açacağını belirler. Projeye özel tercih genel tercihin önüne geçebilir. Bu ayarlar modelin talimat dosyasından ayrı arayüz tercihleridir.

![Görünümü ayarlamak. Appearance içindeki Light, Dark ve System seçimiyle başla. Tema rengi, yazı tipi ve boyut denetimleri uygulamanın görünümünü değiştirir; modelin çalışma talimatlarını değiştirmez.](assets/settings.png)

**Görünümü ayarlamak.** Appearance içindeki Light, Dark ve System seçimiyle başla. Tema rengi, yazı tipi ve boyut denetimleri uygulamanın görünümünü değiştirir; modelin çalışma talimatlarını değiştirmez. [Tam boyut](assets/settings.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/reference/settings) · 2026-10-29.

1. **Nereye bak:** Appearance içindeki Theme ve UI font size alanlarına.
2. **Ne yap:** Okuma rahatlığını tema ve yazı boyutundan ayarla.
3. **Ne gör:** Arayüz değişir; modelin görev talimatı veya düşünme seviyesi değişmez.

<a id="i-s-bitti-mi-benden-yanit-mi-bekliyor"></a>

## İş bitti mi, benden yanıt mı bekliyor?

Kenar çubuğundaki zil, **Activity** görünümünü açar. Çalışan işleri ve senden yanıt bekleyenleri buradan ayırabilirsin. macOS'ta ⌘⌥U, Windows'ta Ctrl+Alt+U belgelenmiş kısayollardır. Her sessizlik “model hâlâ düşünüyor” anlamına gelmez; bekleyen soru veya izin olabilir.

Settings içindeki bildirim tercihlerinde tur bitişi için Never, When in background veya Always seçenekleri bulunur. Soru ve izin bildirimleri ayrı denetlenebilir. İşletim sisteminin uygulamaya bildirim izni de açık olmalı. Birden fazla iş yürütürken yalnız arka plandaki bitiş bildirimlerini almak, sürekli pencere değiştirmenin önüne geçer. [Bildirimler ve Activity](https://learn.chatgpt.com/docs/notifications)

İsteğe bağlı Pets, Mini ve Micro yüzeyleri [ileri ekte](ileri-teknik.md#pets-mini-ve-micro) anlatılır. İlk işin için gerekli değiller.

<a id="kurgu-senaryo-ayni-oturumda-uc-gorunum"></a>

## Kurgu senaryo: aynı oturumda üç görünüm

Atölye'nin program sayfasını düzenlerken solda sohbet, sağda yerel sayfa, altta terminal açık olsun. Görsel taşmayı sayfada işaretle, düzeltme isteğini sohbette ver, sunucu hatası varsa terminal çıktısına bak. Üç görünüm aynı sorunun farklı kanıtlarını sağlar. Kod değişikliği görünümüne geçerek değişikliğin beklediğin dosyada olduğunu ayrıca kontrol edebilirsin.

**Eğitimde sıradaki:** [İşe göre model ve düşünme seç](07-model-hiz-kullanim.md)

[İçindekiler](README.md) · [← Codex ile neler yapabilirsin?](01-olanaklar.md) · [Codex gerçekte nasıl çalışıyor? →](03-calisma-mantigi.md)
