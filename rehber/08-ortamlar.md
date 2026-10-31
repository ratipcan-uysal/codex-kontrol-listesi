# 8. Dosyalar ve çalışma ortamları

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Bir dosyanın nerede değiştiği, o dosyayla ne yapıldığı kadar önemlidir. “Bende çalışıyor” ifadesinin anlamı çalışma ortamı açıklanınca ortaya çıkar.

<a id="klasor-depo-dal-ve-worktree"></a>

## Klasör, depo, dal ve worktree

**Çalışma dizini**, komutun başlangıç klasörüdür. **Git deposu**, dosyaların sürüm geçmişini tutar. **Dal**, geçmişteki bir gelişim çizgisidir. **Worktree**, aynı Git geçmişine bağlı ayrı bir dosya çalışma kopyasıdır. Sıradan klasörün Git deposu olması zorunlu değildir; worktree için Git gerekir.

| Ortam | Dosyalar nerede? | İyi kullanım | Sık hata |
|---|---|---|---|
| Local | Seçili bilgisayar/proje klasöründe | Mevcut yerel araçlarla çalışma | Başka işin değişikliklerini de kendi işi sanmak |
| Worktree | Ayrı yerel checkout içinde | Bağımsız değişikliği yalıtmak | Ana klasörde açılan uygulamayı yeni değişikliğin testi sanmak |
| Cloud | Görev için sağlanan uzak ortamda | Yerel bilgisayardan bağımsız uygun işler | Yerel oturum, dosya veya VPN erişimini var saymak |
| Remote host | Bağlanılan bilgisayarda | O bilgisayarın kaynaklarını kullanmak | Yerel makineyle aynı izin ve yolları beklemek |

[Ortam türleri](https://learn.chatgpt.com/docs/environments/modes) · [Worktree](https://learn.chatgpt.com/docs/environments/git-worktrees) · [Bulut](https://learn.chatgpt.com/docs/environments/cloud-environments)

<a id="worktree-nin-asil-kazanci"></a>

## Worktree'nin asıl kazancı

Aynı projede bir hata düzeltirken başka tasarımı denemek istiyorsan ayrı dosya alanı yararlıdır. Uygulamada yeni işin ortamını Worktree seçip başlangıç durumunu belirlersin. Uygulamanın yönettiği bazı akışlar mevcut değişiklikleri başlangıca taşıyabilir; düz `git worktree add` komutunun bunu otomatik yaptığını düşünme. Başlangıç commit'i ve taşınan değişiklikleri kontrol et.

Yeni worktree ayrılmış HEAD durumunda başlayabilir: henüz adlandırılmış dala bağlı olmayan bir commit üzerindesindir. Bu veri kaybı demek değildir, ancak kalıcı geliştirme ve paylaşım için dal/commit düzenini bilmek gerekir. Aynı dalın iki checkout'ta eşzamanlı açılmasına ilişkin Git kısıtı da vardır.

Hand off, desteklenen akışlarda sohbeti ve kod durumunu Local ile worktree arasında taşır. Her klasörü elle kopyalamakla aynı işlem değildir. Git tarafından izlenmeyen ve yok sayılan dosyaların taşınma davranışını ayrıca incele. `.worktreeinclude` desteklenen yerel worktree akışlarında seçili yok sayılmış dosyaları kopyalamaya yarar; sırları topluca ekleme. [Worktree ayrıntıları](https://learn.chatgpt.com/docs/environments/git-worktrees)

<a id="ayri-denemeden-ana-calismaya-don"></a>

## Ayrı denemeden ana çalışmaya dön

**Kurgu masaüstü gösterimi:** Ana klasörde etkinlik metni üzerinde çalışıyorsun. Ayrı worktree’de yalnız kart genişliği düzeltildi. Checkout, üzerinde çalışılan dosya kopyasıdır; bu iki kopyanın adresleri farklıdır.

| Aşama | Anlatıcının göstereceği şey | Karar |
|---|---|---|
| Deneme | Worktree’de tek genişlik farkı | Ana klasördeki metin değişikliği bu işe ait değil |
| Önizleme | Denemenin kendi klasöründen açılan sayfa | Görüntü gerçekten denediğimiz koda ait |
| İnceleme | Değişen dosya ve satır | Yalnız seçilen düzeltme taşınacak |
| Dönüş | Sohbet başlığındaki Hand off → Local yolu | Yerel durum ve olası çakışmalar kontrol edilir |

> Bu worktree’deki düzeltmeyi ana çalışmaya taşımadan mevcut değişiklikleri göster. Bana ait metin düzenlemesini koru. Uygun geçişi tamamlayınca ana klasörde aynı sayfayı açıp kontrol et.

Hand off, sohbet ve Git durumunu taşıyan ürün akışıdır; her değişikliği otomatik birleştiren genel merge komutu değildir. Bir çatışma varsa hangi iki değişikliğin karşılaştığını görmeden taraf seçme. [Resmî geçiş yolu](https://learn.chatgpt.com/docs/environments/git-worktrees)

[İki dosya alanının örnek kaydı](ornekler/worktree-gecis.md) bu gösterim için kurgu hazırlanmıştır; gerçek bir kullanıcı projesinde worktree açıldığı iddiası değildir. Ana kaynağa döndükten sonra doğrulama, deneme kopyasının görüntüsünü yeniden kullanmakla bitmez.

<a id="toplu-islemden-once-degisiklik-listesini-gor"></a>

## Toplu işlemden önce değişiklik listesini gör

Atölye dosyalarını yeni tarihe göre adlandırmak istiyorsun. **Kurgu önizleme:** Aşağıdaki üç kaynak için tek bir hedef klasör seçildi. Henüz dosya adı değişmedi.

| Mevcut dosya | Önerilen hedef adı | Önizlemenin yakaladığı sorun |
|---|---|---|
| `taslaklar/program.pdf` | `2026-11-21-program.pdf` | Onaylı programla aynı hedefe gidiyor |
| `onayli/program.pdf` | `2026-11-21-program.pdf` | Taslak ile onaylı dosya çakışıyor |
| `duyuru.pdf` | `2026-11-21-duyuru.pdf` | Hedef klasörde bu adla başka bir dosya var |

> Dosyaları henüz değiştirme. Eski yol → yeni yol listesini çıkar. Aynı hedefe dönüşenleri ve mevcut dosyanın üzerine yazacakları belirt. Sorunları çözen yeni listeyi göster; kaynakları silme.

**Düzeltilmiş karar:** İlk iki hedefe `taslak` ve `onayli` ayrımı eklenir. Duyurunun mevcut hedefle aynı içerik olup olmadığı karşılaştırılır; farklıysa üzerine yazmak yerine açık bir sürüm adı seçilir. Tam liste çakışmasız olduğunda yetkilendirilmiş işlem uygulanır; dosya sayısı, içerik ve yeni yollar kontrol edilir.

Küçük örnekle yöntemi sınamak başka, bütün hedeflerin birbiriyle çakışmadığını görmek başkadır. Gerçek işte 300 dosya varsa önizleme 300 dosyayı kapsamalı; üç örnekte hata çıkmaması tamamı için yeterli değildir. Buna değişiklik yapmadan deneme, teknik adıyla **dry run** denir. “Önizleme” etiketi taşıyan adımın dosya yazmadığından da emin ol.

<a id="ortam-kurulumu-ve-actions"></a>

## Ortam kurulumu ve Actions

Bağımlılıklar, veri dosyaları ve başlatma komutu eksikse kaynak kod tek başına yeterli olmaz. Local environment tanımları yeni worktree hazırlığı için kurulum komutlarını ve tekrar kullanılan Actions işlemlerini düzenleyebilir. Actions, sık kullandığın “uygulamayı aç” veya “önizlemeyi başlat” komutuna hızlı erişim sağlar. [Yerel ortam](https://learn.chatgpt.com/docs/environments/local-environment)

Büyük modeli veya uzun derlemeyi her sohbet başında yeniden kurmak yerine kurulumun mevcut ve geçerli olup olmadığını kontrol ettir. Kullanıcıya ait eski önbellekleri sırf temiz görünmek için silme.

<a id="uzaktan-ve-mobilden-calisma"></a>

## Uzaktan ve mobilden çalışma

Desteklenen Connections akışında başka bilgisayardaki Codex'e bağlanabilirsin. Ana bilgisayarın çevrimiçi olması, ilgili proje ve araçların orada bulunması gerekir. Mobil cihazdan komut vermek, masaüstü derleyicinin telefonda çalıştığı anlamına gelmez. Hesap, çalışma alanı ve dağıtım koşullarını kontrol et. [Uzak bağlantılar](https://learn.chatgpt.com/docs/remote-connections) · [Mobil](https://learn.chatgpt.com/docs/mobile)

Mobil eşleme desteklenen ana bilgisayarda Settings → Connections → Control this Mac or PC yolundan başlar. QR kodu telefonda açıp aynı hesap ve çalışma alanıyla bağlantıyı tamamlarsın. SSH, başka makinedeki projeye güvenli uzak bağlantı kuran ayrı bir yoldur; mobil eşlemeyle aynı kurulum değildir.

Work Cloud içindeki Local computer access ise uygun Work konuşmalarını bulut koordinasyonuyla yerel kaynaklara bağlayan ayrı akıştır. Etkinleştirilmeden önce açılmış her eski sohbetin bu moda geçtiğini varsayma. Ana bilgisayar erişilemiyorsa bulut ortamının onun yerel dosyalarına erişmesi de mümkün değildir.

<a id="kurgu-senaryo-dogru-kod-yanlis-onizleme"></a>

## Kurgu senaryo: doğru kod, yanlış önizleme

Atölye'nin başlık düzeltmesi worktree'de yapılmış, tarayıcı ise ana klasörden çalışan sunucuyu gösteriyor. Değişiklik görünmüyor. Codex'e daha güçlü CSS yazdırmak yerine:

> Önizlemeyi sunan sürecin çalışma klasörünü ve portunu doğrula. Düzenlediğin worktree ile aynı kaynaktan çalıştığını göster. Sonra görsel kontrolü tekrarla.

Bu kontrol, kodun yanlış olduğu varsayımını sınar. Sonuç raporunda klasör, sürüm ve URL birlikte anlam taşır.

**Eğitimde sıradaki:** [Alt işleri tek kararda birleştir](14-buyuk-isler.md)


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [11.1 Çakışan yazarlara ayrı worktree ver.](../codex-kontrol-listesi.md#m-11-1)
- [11.3 Port ve tarayıcı bağlamını göreve bağla.](../codex-kontrol-listesi.md#m-11-3)
- [11.5 Buluta yalnız uygun bağımlılıkları olan işi gönder.](../codex-kontrol-listesi.md#m-11-5)

[İçindekiler](README.md) · [← Model, düşünme seviyesi, hız ve kullanım](07-model-hiz-kullanim.md) · [İnternet, tarayıcı ve bilgisayar kullanımı →](09-web-tarayici-bilgisayar.md)
