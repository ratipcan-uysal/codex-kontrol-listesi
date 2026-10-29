# İleri teknik ayrıntılar

Belge kontrolü: 2026-10-29.

Bu ek, ana anlatıyı kesmeden geliştirici ve yoğun kullanıcıların ihtiyaç duyacağı ayrıntıları toplar. Gereken yerde başvur; başlangıç için hepsini kurmak zorunda değilsin.

<a id="hook-larin-gercekten-uygulandigini-gostermek"></a>

## Hook'ların gerçekten uygulandığını göstermek

Hook dosyasının varlığı, yüklendiğini veya engelleme davranışının çalıştığını kanıtlamaz. Güncel belgede kaynak keşfi, güven, etkinleştirme ve olay sözleşmesi ayrı adımlardır. CLI `/hooks` üzerinden kaynakları, yeni/değişmiş hook güvenini ve yönetilmeyen hook'ların etkinliğini incelemek mümkündür. Yönetilen kurum hook'larının davranışı farklıdır. [Hook referansı](https://learn.chatgpt.com/docs/hooks)

Olumlu girdi, engellenmesi gereken girdi ve bozuk girdiyle kontrol yap. Örneğin yalnız belirli dosya türünde biçim kontrolü gerekiyorsa, ilgili olmayan dosyada çalışmadığını da göster. `PreToolUse`, `PostToolUse`, `SessionStart`, `PreCompact` veya `Stop` gibi olay adlarını kurulu sürümün belgesinden seç. Hook'un çıkış kodu ve çıktısının anlamını o olayın sözleşmesine göre yorumla.

Engellemesi gereken kontrol arka planda çalışıp asıl işlemin tamamlanmasından sonra cevap veriyorsa güvenlik sınırı kurulmuş sayılmaz. Birden çok hook arasında açıkça belgelenmeyen sıra varsayma. Eksik araç, bozuk JSON ve zaman aşımı durumunda fail-open (işe izin ver) veya fail-closed (işi durdur) kararını etkisine göre seç. Her hook'a aynı politika uygun değildir.

<a id="i-zin-ve-komut-oneki"></a>

## İzin ve komut öneki

Bir komuta verilen onay, seçilen önek çok genişse başka argümanlarla farklı işlere de kapı açabilir. Kapsamı iş için gereken düzeyde tut. Ağ kuralının web aramasına mı, shell içindeki bağlantıya mı, plugin'e mi uygulandığını belgeyle kontrol et. Bir kanaldaki engeli başka kanalda da var sayma. [İzinler](https://learn.chatgpt.com/docs/permissions) · [Kurallar](https://learn.chatgpt.com/docs/agent-configuration/rules)

Shell komutuna kullanıcı metni yerleştirmek kod ile veriyi karıştırabilir. Metni uygun dosyaya veya yapılandırılmış argümana taşı; tırnak içine almak her komut yorumlamasını kendiliğinden güvenli kılmaz. Çok satırlı yayın açıklamalarında metin dosyası ve `--body-file` benzeri desteklenen yollar okunabilirliği korur.

<a id="makineye-aktarilacak-cikti"></a>

## Makineye aktarılacak çıktı

Bir sonraki programın okuyacağı çıktı için alanları ve türleri belirle. Serbest metindeki “tamam” sözcüğünü başarı bayrağı yapmak kırılgandır. JSON şemasında durum, üretilen dosya ve doğrulama sonucunu ayrı alanlarda tut. Şemaya uymak, alanların doğru olduğu anlamına gelmez; hedefi yine kontrol et. [Etkileşimsiz çalışma](https://learn.chatgpt.com/docs/non-interactive-mode)

Kurgu veri dönüşümünde sonuç şu alanları taşıyabilir: `status`, `input_rows`, `output_rows`, `unresolved_rows`, `output_file`. Bu alanlar eğitim örneğidir, ürünün zorunlu API'si değildir. Çıktı parse edilemiyorsa başarı varsayılanı kullanma.

<a id="tekrar-baslatilabilir-uzun-isler"></a>

## Tekrar başlatılabilir uzun işler

İşi ara çıktılarla böl: indirilen kaynak, temizlenmiş veri, doğrulanmış taslak, üretilmiş çıktı. Her aşamanın girdisi ve geçerli sürümü belli olsun. Kesinti sonrası hangi aşamanın tekrar gerektiğini buradan anlarsın. Aynı dış işlemi yeniden yürütmeden önce hedef durumunu oku.

Arka plan işlemi başlatmak tamamlamak değildir. Sürecin son durumu ve çıktısı beklenmeden görevi kapatma. Kaynak taramasında hizmetin hız ve erişim koşullarına uy; gereksiz tekrarları yerel kayıtla azalt. Sessiz günlük, başarılı koşum kanıtı değildir.

<a id="mobil-gelistirme-ve-simulator-kaniti"></a>

## Mobil geliştirme ve simülatör kanıtı

Simülatör, fiziksel cihazın bütün özelliklerini temsil etmez. Bildirim, kamera, gerçek erişilebilirlik veya dağıtım davranışı için gereken cihaz kontrolü ayrıca belirtilir. Türkçe karakter girişinde otomasyon katmanının yaptığı hata ile uygulama hatasını ayır; ham girdi ve görünen sonucu karşılaştır.

Geçici simülatör oluşturulduysa adını, kesin UDID'sini ve görev sahibini kaydet. Kanıtı cihaz dizininin dışında koru; iş bittiğinde yalnız bu görevin cihazını kapatıp tam kimliğiyle sil. Silindiğini cihaz listesinden doğrula. Kullanıcının önceden var olan cihazına dokunma. Bu yöntem proje çalışma tercihidir; Codex'in bütün kurulumlarda otomatik yaptığı garanti değildir.

<a id="kaynak-ve-disk-temizligi"></a>

## Kaynak ve disk temizliği

Tarayıcı otomasyon sürecini, test sunucusunu ve derleme klasörünü göreve özel kimlikle izlemek yanlış kaynağı kapatma riskini azaltır. Bir REPL'i sıfırlamak, onu barındıran Node sürecinin çıktığını kanıtlamaz. Paylaşılan MCP altyapısını sırf eski göründüğü için sonlandırma; desteklenen oturum kapatma yolunu kullan.

Derleme önbelleğiyle yayın arşivi aynı klasör ağacında bulunabilir. Klasör adına bakıp bütün `build` dizinini silme. Gerekli test günlüklerini ve dağıtım ürünlerini koru; yalnız sahipliği ve kullanımının bittiği bilinen geçici hedefleri kaldır. Disk alanı kazancı ancak ölçüldüyse sayı olarak raporlanır.

<a id="baska-ajandan-ice-aktarma"></a>

## Başka ajandan içe aktarma

Settings → Import, yoksa General → Import other agent setup yolu desteklenen kurulumlarda başka ajanların proje, talimat ve çalışma malzemelerini seçerek taşır. Masaüstü belgesi Claude Code, Claude Cowork ve Cursor'u; CLI yolu Claude Code ve Cursor'u listeler. Bağlantılara yeniden giriş veya Finish adımı gerekebilir. [İçe aktarma](https://learn.chatgpt.com/docs/import)

Aktarılan talimat, hook ve izinleri incele. Başka ürünün komutunu birebir Codex komutu sayma. Otomatik eşitleme seçeneği varsa değişikliklerin hangi kaynaktan geldiğini bil; iki bağımsız kural kopyasının sessizce ayrışmasını önle.

<a id="space-belge-ve-urun-yuzeyleri"></a>

## Space, belge ve ürün yüzeyleri

Space sayfaları, slaytlar ve tabloları bulutta düzenleyip paylaşma alanıdır. Yerel proje klasörü ve Git deposuyla aynı şey değildir. Bağlı dosyanın özgün izni korunabilir; o dosyadan sayfaya kopyalanan özet ise sayfanın okuyucularına görünür. Desteklenen araçlarla aynı çıktıya bağlanmak ve yeni kopya oluşturmak farklı işlemlerdir. [Space](https://learn.chatgpt.com/docs/space)

Masaüstünde belge önizlemek, her Space özelliğinin her Codex hesabında bulunduğunu göstermez. CLI, IDE ve web yollarını gerektiği kadar öğren: ortak model ve araç kavramlarını paylaşabilirler, fakat menüleri, oturumları ve izin kapsamları aynı değildir.

<a id="pets-mini-ve-micro"></a>

## Pets, Mini ve Micro

Pets ve Mini, başka uygulamada çalışırken sohbet durumuna ulaşmak için isteğe bağlı yüzeylerdir. Settings → Pets içinden seçip `/pet` ile gösterip gizleyebilirsin. Mini, hayvan karakteri olmadan denetimleri sunar. Buradan başlayan sohbet proje dışında açılır; proje bağlamı gerekiyorsa ana penceredeki projeden başla. Özel pet yerelde saklanabilir ve web yüzeyine kendiliğinden eşitlenmeyebilir. Görünüm tercihi modelin iş kalitesini değiştirmez.

Codex Micro, uyumlu fiziksel donanımla sohbet ve komut kontrolü sunan ayrı bir seçenektir. Temel kullanım için gerekmez. [Pets](https://learn.chatgpt.com/docs/pets) · [Micro](https://learn.chatgpt.com/docs/features/codex-micro)


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [6.2 Yıkıcı komut için açık komut kuralı kullan.](../codex-kontrol-listesi.md#m-6-2)
- [6.3 Onaylanan komut önekini daralt.](../codex-kontrol-listesi.md#m-6-3)
- [6.4 Çalıştırma yolunu basit ve belirgin tut.](../codex-kontrol-listesi.md#m-6-4)
- [6.7 Ağ kuralının hangi aracı kapsadığını kontrol et.](../codex-kontrol-listesi.md#m-6-7)
- [7.6 Politika hook’unu kapsamlı savunmanın bir parçası say.](../codex-kontrol-listesi.md#m-7-6)
- [8.1 Başlangıç bağlamını gerekiyorsa SessionStart ile ekle.](../codex-kontrol-listesi.md#m-8-1)
- [8.2 Biçim kontrolünü yalnız ilgili dosyalara uygula.](../codex-kontrol-listesi.md#m-8-2)
- [8.3 Bağlam uyarısını gerçek ölçüme bağla.](../codex-kontrol-listesi.md#m-8-3)
- [8.4 Hook’u olumlu, olumsuz ve bozuk girdilerle sınayıp kanıtla.](../codex-kontrol-listesi.md#m-8-4)
- [8.5 Hook hata politikasını görevine göre belirle.](../codex-kontrol-listesi.md#m-8-5)
- [8.6 Engellemesi gereken hook’u arka plana atma.](../codex-kontrol-listesi.md#m-8-6)
- [8.7 Birden çok hook arasında çalışma sırası varsayma.](../codex-kontrol-listesi.md#m-8-7)
- [13.3 Uzun işi tekrar başlatılabilir adımlara ayır.](../codex-kontrol-listesi.md#m-13-3)
- [14.4 Tarama yükünü kaynak kurallarına göre yönet.](../codex-kontrol-listesi.md#m-14-4)
- [14.6 Makineye aktarılacak sonucu şemayla tanımla.](../codex-kontrol-listesi.md#m-14-6)
- [17.1 Simülatör kullanımını görev kimliğiyle izole et.](../codex-kontrol-listesi.md#m-17-1)
- [17.2 Tekrarlanan kullanıcı akışını davranış testine çevir.](../codex-kontrol-listesi.md#m-17-2)
- [17.3 Türkçe girdi sorununu ürün hatasıyla karıştırma.](../codex-kontrol-listesi.md#m-17-3)
- [17.4 Riskli yerleşimi desteklenen dar görünümde erken dene.](../codex-kontrol-listesi.md#m-17-4)
- [17.5 İşi biten görev cihazını kanıtı koruyup tam UDID ile sil.](../codex-kontrol-listesi.md#m-17-5)
- [19.4 İzin, hook ve kurulum farklarını sürüm değişiminde kontrol et.](../codex-kontrol-listesi.md#m-19-4)
- [19.6 Geçici derleme dosyalarını kanıttan ayırarak temizle.](../codex-kontrol-listesi.md#m-19-6)

[İçindekiler](README.md)
