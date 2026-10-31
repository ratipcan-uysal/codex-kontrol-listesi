# 17. Teslim, yayın ve geri dönüş

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Bir işin tamamlanma noktası, kullanıcının istediği hedefte tanımlanır. Yerel dosya üretimi, canlı yayın isteyen bir görev için ara adımdır. Taslak isteyen görevde ise yayın yapmak kapsamı aşar.

<a id="durumlari-birbirine-karistirma"></a>

## Durumları birbirine karıştırma

| Durum | Ne oldu? | Henüz neyi göstermiyor? |
|---|---|---|
| Yerel değişiklik | Çalışma dosyası değişti | Git geçmişine kaydedildiğini |
| Commit | Değişiklik Git geçmişine kaydedildi | Uzak depoya gittiğini |
| Push | Commit uzak depoya gönderildi | Site veya uygulamanın dağıtıldığını |
| Deployment | Hedefe dağıtım süreci çalıştı | Doğru sürümün kullanıcıya göründüğünü |
| Upload | Dosya bir sisteme yüklendi | Doğru kayda atandığını veya yayımlandığını |
| Atama / submission | Varlık hedef kayda veya incelemeye bağlandı | Onaylandığını veya kamuya açıldığını |
| Hedefte doğrulama | İstenen sürüm/kayıt orada tekrar gözlendi | Ölçülmemiş kullanıcı etkisini |

Örneğin uygulama paketi TestFlight'a yüklenmiş olabilir; App Store'da yayınlanması ayrı süreçtir. Eğitimde bu ayrımı yalnız yazılımla sınırlama: belgeyi hazırlamak, e-postaya eklemek ve göndermek de ayrı sonuçlardır.

<a id="git-degisikliklerini-incele"></a>

## Git değişikliklerini incele

Review panelinde dosya ve değişiklik parçalarını görebilir, desteklenen akışlarda stage, revert, commit, push ve pull request işlemlerini yönetebilirsin. Stage, bir sonraki commit'e hangi değişikliğin gireceğini seçmektir. Revert/geri alma işleminin kapsamını okumadan topluca uygulama; depoda kullanıcının başka işi bulunabilir. [Git ve inceleme](https://learn.chatgpt.com/docs/code-review)

Pull request, değişikliğin inceleme önerisidir. Oluşturulması birleştiği anlamına gelmez. GitHub/GitLab hesabı ve depo erişimi ilgili bağlantıya bağlıdır. Bir PR'ı okumak, yorum göndermek, onaylamak ve merge etmek farklı yetkiler gerektirir. Bazı inceleme alanlarında yorum gönderme anında gerçekleşebilir; metnin taslakta kalacağını varsayma. [GitHub](https://learn.chatgpt.com/docs/third-party/github) · [GitLab](https://learn.chatgpt.com/docs/third-party/gitlab)

<a id="kucuk-farki-okuyarak-dogru-isi-teslim-et"></a>

## Küçük farkı okuyarak doğru işi teslim et

**Kurgu örnek:** Değişiklik görünümünde `sayfa.css` kart genişliğini, `program.md` kullanıcının tarih düzeltmesini içeriyor. Kırmızı satır kaldırılanı, yeşil satır ekleneni gösterir. Bu görev yalnız kartı düzeltmişse tarih değişikliğini kendine ait sayma.

> Bu göreve ait farkları göster. Kullanıcının önceden yaptığı değişiklikleri ayır. Seçilen düzeltmeyi teslim et; ilgisiz dosyayı geri alma veya commit’e ekleme.

[Sayfa örneğinin tek satırlık farkını](ornekler/sayfa-degisikligi.md) açıp sonucu önizlemeyle eşleştir. Yanlış düzeltmeyi geri alırken de aynı dosya/iş kapsamını kullan. Commit bir kayıt noktasıdır; başka sistemde gönderilmiş mesajı geri almaz.

<a id="sonucu-hedefte-geri-oku"></a>

## Sonucu hedefte geri oku

Yetkili dış işlemde araç “başarılı” dönünce hedefi tekrar kontrol et. Doğru depo/dal, dosya, hesap ve sürüm mü? Ağ sonucu belirsizse işlemi yeniden yapmadan önce hedefi oku. Özellikle e-posta ve kayıt oluşturma gibi işlemlerde tekrar denemek çift sonuç üretebilir.

> Teslimi hedefte doğrula. Yerel dosya, commit, uzak depo ve canlı görünüm durumlarını ayrı yaz. Doğrulayamadığın aşamayı tamamlandı sayma.

Bu bir rapor formatı talebi olmanın yanında işin nerede biteceğini açıklar.

<a id="geri-donusun-siniri"></a>

## Geri dönüşün sınırı

Sohbette önceki mesaja dönmek, yapılmış dış işlemleri geri almayabilir. Git de yalnız kaydettiği içerik için geri dönüş sağlar; gönderilmiş e-posta, uzak veritabanı ve izlenmeyen dosya ayrı sistemlerdir. Riskli işlemden önce hangi geri dönüşün gerçekten var olduğunu bil.

Worktree arşivleme akışları kaydedilmiş durumu kurtarmaya yardımcı olabilir; yok sayılan büyük dosyaların ve yerel sırların korunduğunu otomatik varsayma. [Worktree yaşam döngüsü](https://learn.chatgpt.com/docs/environments/git-worktrees)

<a id="gorev-kaynaklarini-kapat"></a>

## Görev kaynaklarını kapat

İş bitince yalnız bu görevin oluşturduğu ve artık kullanılmayan geçici kaynakları kapat. Test kanıtını, sürüm paketini ve kullanıcıya ait oturumları koru. Süreç, simülatör ve derleme dosyalarının güvenli temizliği [ileri ekte](ileri-teknik.md#kaynak-ve-disk-temizligi) açıklanır.

<a id="kullanacagin-bicimde-teslim-al"></a>

## Kullanacağın biçimde teslim al

Çıktıyı nerede kullanacağını başta söyle. Düzenlenecek metinde DOCX, sunumda PPTX, hesaplama sürecek tabloda XLSX yararlı olabilir. Markdown sade metin ve GitHub için, PDF sabit görünümle paylaşım için uygundur. Dosyanın yapısını ve hangi değişikliği yapabilmek istediğini de belirt. [Dosya yapısı ve inceleme ölçütleri](https://learn.chatgpt.com/docs/artifacts-viewer)

<a id="uzanti-degil-yapabilecegin-degisiklik"></a>

### Uzantı değil, yapabileceğin değişiklik

[Atölye tablosunun görüntüsünü](assets/atolye-slayt-2.png) ve [düzenlenebilir sunumu](ornekler/atolye-karar.pptx) karşılaştır. Görüntüde fiyat okunabilir; sunumda fiyatın bulunduğu tablo hücresi ayrı düzenlenebilir. Bir resmi PPTX içine koymak da PPTX dosyası üretir, ama tablonun hücrelerini düzenlenebilir yapmaz.

| Teslim beklentisi | Yetersiz kalan çıktı | İstenecek kontrol |
|---|---|---|
| Sunumda fiyatı değiştirmek | Bütün slayt tek resim | Metni veya tablo hücresini ayrı seçip değiştirebilmek |
| Tahsilat değişince toplamın güncellenmesi | XLSX içinde elle yazılmış sabit toplam | Kopyada bilinen bir tutarı değiştirip hesap ve bağlı grafiği kontrol etmek |
| Metni düzenleyip PDF paylaşmak | Kaynak belgesi olmayan PDF | Düzenlenebilir kaynak ve onunla aynı içerikte son PDF |

> Sunum metinlerini ve tablolarını ayrı düzenlenebilir bırak. Hesaplama sürecek tabloda formülleri ve gerekli grafik bağlantılarını koru. Son dosyayı hedef uygulamada açıp bu düzenlemeyi yapabildiğini kontrol et; yalnız dosya uzantısını kanıt sayma.

**Atölye için hesap kontrolü — kurgu teslim ölçütü:** İlk haftanın çalışma kopyasında bilinen 600 TL tutarlardan birini 700 TL yaparsan bilinen tahsilat 1.800'den 1.900 TL'ye çıkmalı; K04'ün bilinmeyen tutarı hâlâ açık kalmalı. Bu değişikliği asıl kayda uygulama. Rehberin indirilebilir veri örneği CSV'dir; bu cümle formüllü bir XLSX'in üretilip sınandığı iddiası değildir.

Dosyayı yeniden adlandırmak gerçek biçim dönüşümü değildir. Tek bir son sürüm bağlantısı ve gerekiyorsa düzenlenebilir kaynak verilsin. Çok sayıda dosyayı adlandırırken [toplu değişiklik önizlemesini](08-ortamlar.md#toplu-islemden-once-degisiklik-listesini-gor) kullan.

Kurgu Atölye'nin program sayfasında teslim hedefi canlı URL ise uzak sürüm ve canlı görünüm kontrolü gerekir. Yaratıcı kalite ve teslim ayrımının gerçek örneği [C04 vakasında](deneyimler.md#c04) bulunur.


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [11.2 Commit öncesi index’i ve dosya kapsamını incele.](../codex-kontrol-listesi.md#m-11-2)
- [13.4 Arka plan sürecini sonuçla uzlaştırmadan işi kapatma.](../codex-kontrol-listesi.md#m-13-4)
- [13.5 Yalnız görevin açtığı kaynakları temizle.](../codex-kontrol-listesi.md#m-13-5)
- [15.1 Git kapsamını ve commit yetkisini açıklaştır.](../codex-kontrol-listesi.md#m-15-1)
- [15.2 Sohbet geri dönüşünün dosya geri dönüşü olmadığını bil.](../codex-kontrol-listesi.md#m-15-2)
- [15.3 Push, deploy ve mağaza yayınını ayrı teslimler say.](../codex-kontrol-listesi.md#m-15-3)
- [15.4 Commit kimliği ve atfı için gerçek Git sonucunu incele.](../codex-kontrol-listesi.md#m-15-4)
- [19.2 Eski worktree ve büyük çıktıları sahiplik bilgisiyle temizle.](../codex-kontrol-listesi.md#m-19-2)

[İçindekiler](README.md) · Konu sırasıyla oku: [← İzinler, gizlilik ve güvenlik](16-izinler-guvenlik.md) · [Kendi kullanımını sürekli iyileştirmek →](18-iyilestirmek.md)
