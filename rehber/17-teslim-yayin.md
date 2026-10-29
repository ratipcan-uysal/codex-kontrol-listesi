# 17. Teslim, yayın ve geri dönüş

Belge kontrolü: 2026-10-29.

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

Çıktıyı nerede kullanacağını başta söyle. Düzenlenecek raporda DOCX, sunumda PPTX, hesaplama sürecek tabloda XLSX yararlı olabilir. Markdown, sade metin ve GitHub yayını için uygundur. PDF sabit görünümle paylaşımı kolaylaştırır ama düzenlenebilir kaynağın yerini her işte tutmaz.

> Raporu düzenlenebilir DOCX ve paylaşmalık PDF olarak teslim et. İkisindeki metin ve tablolar aynı olsun. Kaynak dosyayı sakla; son PDF'yi açıp sayfa taşmalarını kontrol et.

Dosya uzantısını değiştirmek gerçek biçim dönüşümü değildir. Dosyayı hedef uygulamada açtırıp doğrulat. Tek bir “son sürüm” bağlantısı ve gerekiyorsa kaynak dosya vermek, adında final bulunan çok sayıda kopya bırakmaktan daha kolay takip edilir.

Kurgu Atölye'nin program sayfasında teslim hedefi canlı URL ise, yerel önizlemenin ardından uzak sürüm ve canlı sayfa kontrolü gerekir. Yaratıcı kalite ve teslim ayrımının gerçek örneği [C04 vakasında](deneyimler.md#c04) bulunur.


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

[İçindekiler](README.md) · [← İzinler, gizlilik ve güvenlik](16-izinler-guvenlik.md) · [Kendi kullanımını sürekli iyileştirmek →](18-iyilestirmek.md)
