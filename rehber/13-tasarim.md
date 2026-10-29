# 13. Tasarım ve yaratıcı üretim

İçerik güncellemesi: 2026-10-30. Kaynak kontrol tarihleri kaynak dizinindedir.

Teknik olarak çalışan bir çıktı, iyi tasarlanmış veya iyi yazılmış olmayabilir. Görsel ve yaratıcı işte beğeniyi somutlaştırmak, model seçmekten önce gelen bir iştir.

<a id="referansin-hangi-yonunu-istedigini-soyle"></a>

## Referansın hangi yönünü istediğini söyle

Bir ekranı “bunun gibi” diye vermek renk, boşluk, içerik yapısı ve etkileşimin birlikte kopyalanmasına yol açabilir. Referansı parçala:

> Bu örneğin sakin tipografisini ve bölüm aralıklarını kullan. Kart yapısını kopyalama; bizim içerik uzun paragraflardan oluşuyor. Başlıkların daha kolay taranmasını istiyorum.

Karşı örnek de yararlıdır: “Büyük tanıtım başlıkları ve boş kartlar istemiyorum; ilk ekranda gerçek içerik görünsün.” Böylece yalnız beğenilen değil, kaçınılacak yön de belli olur.

<a id="sorunu-dogru-katmanda-duzelt"></a>

## Sorunu doğru katmanda düzelt

| Şikâyet | Önce bakılacak katman |
|---|---|
| “Sayfa sıkıcı.” | İçerik seçimi, anlatı sırası, vurgu |
| “Nereye basacağım anlaşılmıyor.” | Görev akışı ve bilgi hiyerarşisi |
| “Her şey aynı görünüyor.” | Tipografik farklar ve görsel ağırlık |
| “Hareket rahatsız ediyor.” | Animasyon gereği, süre, yön ve azaltılmış hareket |
| “Çalışıyor ama ucuz görünüyor.” | Gerçek içerik, boşluk, tutarlılık, durum ayrıntıları |

Her eleştiriye yeni renk, gölge veya animasyon eklemek çözüm değildir. Önce sorunun hangi karar düzeyinde olduğunu bul.

<a id="prototip-neden-degerlidir"></a>

## Prototip neden değerlidir?

Prototip, belirsiz bir kararı görülebilir hâle getirir. İki seçenek aynı içerik, ekran boyutu ve başlangıç durumuyla karşılaştırılırsa fark anlaşılır. Birinde iyi içerik, diğerinde boş kutular varsa tasarım karşılaştırması yanıltıcıdır.

> Aynı örnek içerikle iki farklı okuma düzeni göster. Biri uzun okumayı, diğeri hızlı taramayı öne çıkarsın. Açıp inceleyebileceğim prototipler üret; hangisinin ana ürüne gireceğine görüntüler üzerinden karar vereceğim.

Bu kurgu istek yeni yönü seçmeden üretime taşıma yetkisi vermez. Mevcut kabul edilmiş yöndeki küçük taşma ve hizalama düzeltmeleri ise yeni tasarım seçimi gerektirmeyebilir.

<a id="gorsel-uretimi-ayri-bir-aractir"></a>

## Görsel üretimi ayrı bir araçtır

Görsel girdisi, elindeki görüntüyü modele göstermek içindir. Görsel üretimi/düzenleme aracı yeni görüntü yaratır veya mevcut görüntüyü değiştirir. Referans, hedef boyut, kullanılacak alan ve korunacak öğeleri belirtmek sonucu iyileştirir. Şeffaf arka plan gerekiyorsa açıkça iste. Oluşan dosyayı açmadan yalnız üretim komutunun başarılı olduğuna dayanarak görsel kalite iddiasında bulunma. [Görsel üretimi](https://learn.chatgpt.com/docs/image-generation) · [Görsel girdileri](https://learn.chatgpt.com/docs/image-inputs)

Sites gibi yayın odaklı araçlar ve HTML prototipler farklı teslim yollarıdır. Önizleme, yayımlanmış site ve kendi depondaki uygulama aynı çıktı değildir. Hangi kaynağın daha sonra düzenleneceğini baştan bil. [Sites](https://learn.chatgpt.com/docs/sites)

<a id="tek-afis-yerine-yeniden-kullanilabilir-parcalar"></a>

### Tek afiş yerine yeniden kullanılabilir parçalar

**Kurgu kampanya:** Atölye için aynı illüstrasyon hem açık renkli web sayfasında hem koyu sunumda kullanılacak. İllüstrasyonu şeffaf dosya, başlıkları düzenlenebilir metin, zemini ayrı katman olarak istemek sonraki değişikliği kolaylaştırır. Tarih değiştiğinde bütün afişi yeniden çizdirmek gerekmez.

> İllüstrasyonu yazısız ve şeffaf arka planlı ayrı PNG olarak üret. Başlık ve tarihi sayfada düzenlenebilir metin tut. Aynı görseli açık ve koyu zeminde göster; kenarlarda beyaz hale veya kesilmiş ayrıntı var mı incele.

Damalı arka planın resme çizilmiş olması gerçek şeffaflık değildir. Dosyada şeffaflığı taşıyan **alfa kanalı** bulunmalı; yarı saydam kenarlar ve ince ayrıntılar kullanılacağı zeminlerde incelenmeli. [Şeffaf görsel örnekleri](https://developers.openai.com/cookbook/examples/multimodal/transparent-image-assets-for-campaigns-and-presentations)

<a id="sayisal-grafik-bir-resimden-daha-fazla-dogruluk-ister"></a>

### Sayısal grafik bir resimden daha fazla doğruluk ister

Görsel üretim aracına doğru sayıları vermek, çizilen çubukların oranlarını veya etiketleri otomatik olarak doğrulamaz. Hassas raporda grafiği kaynak veriden programla çizdir; illüstrasyonu ayrı üret. [Grafik üretiminin sınırı](https://developers.openai.com/cookbook/examples/multimodal/transparent-image-assets-for-campaigns-and-presentations)

Bizim [veri örneğindeki](is-veri.md) 3 katıldı, 2 iptal, 1 bekliyor dağılımında hem etiketler hem çubuk uzunlukları 3:2:1 oranını taşımalı. Güzel bir görsel uğruna yeni sayı veya tahsilat iddiası eklenmemeli.

<a id="gercek-deneyim-teknik-basari-yaratici-kararin-yerini-tutmadi"></a>

## Gerçek deneyim: teknik başarı, yaratıcı kararın yerini tutmadı

Bir kitap videosunda kapak sayısı, benzersizlik ve video çözümleme kontrolü geçti. Müzik için yapılan öneri ise kullanıcıya sıkıcı geldi; daha yaratıcı yön arayışı ayrı kaldı. Sonunda istenen sessiz sürümün teslimi, müzik revizyonunun tamamlandığı anlamına gelmedi. Video dosyasının gönderilmesi de sosyal ağda yayın sayılmadı. [Vaka C04](deneyimler.md#c04)

<a id="kurgu-senaryo-daha-yaratici-muzik-istegini-acmak"></a>

## Kurgu senaryo: daha yaratıcı müzik isteğini açmak

“Daha yaratıcı ol” yerine şu sınırlar seçenekleri karşılaştırılır yapar:

> Kitap geçişleri sakin kalsın, müzik klişe kurumsal fon gibi duyulmasın. Üç yön öner: minimal ritim, akustik doku ve deneysel ama dikkat dağıtmayan atmosfer. Her yönün geçişlerle ilişkisini açıkla. Lisans koşulu belirsiz dosyayı kullanılabilir diye sunma.

Burada beklenen ilk sonuç son müzik değil, seçilebilir yaratıcı yönlerdir. Tercihten sonra uygulama ve dinleyerek değerlendirme gelir.

<a id="kavram-anlatmak-icin-etkilesimli-gorsellestirme"></a>

## Kavram anlatmak için etkileşimli görselleştirme

Bir resmi izlemekle bir değişkeni oynatıp sonucunu görmek farklı öğrenme yollarıdır. Desteklenen masaüstü dağıtımında `@` menüsünde **Plugins → Visualize** görünüyorsa etkileşimli açıklama isteyebilirsin. Özellik kademeli önizlemede olduğundan menünde görünmesi erişimin en pratik göstergesidir. CLI ve IDE bu çıktıyı aynı şekilde göstermez. [Görselleştirmeler](https://learn.chatgpt.com/docs/visualizations)

**Kurgu senaryo:** Atölye'nin etkinlik bütçesini anlatıyorsun. “Katılımcı sayısı ve bilet fiyatını değiştiren iki denetimle gelir–gider grafiği hazırla. Sabit gideri ve kişi başı gideri ayrı göster. Veriler kurgu olsun ve bunu belirt” isteği, tek bir son sayıdan daha çok şey öğretir. Eğitimde denetimleri anlatıcı kullanabilir; dinleyiciye görev vermek gerekmez.

Etkileşim soruyu açıklamalı. Sırf hareket olsun diye ilgisiz düğmeler ekletme. Sayıların kısa metin açıklamasını ve mümkünse veri tablosunu da iste. Çıktı, üretildiği verinin bir görünümüdür; canlı veriye kendiliğinden bağlı gösterge paneli sayılmaz. Sonraki istek mevcut görsel yerine yeni bir çıktı oluşturabilir. Dışa aktarma seçenekleri yüzeye göre değişir. Herkesin kullanacağı, kalıcı veri ve yetki gerektiren ürün için Sites veya uygun bir uygulama geliştirme yolu daha uygundur.


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [12.5 Görsel değişikliği aynı koşullarda karşılaştır.](../codex-kontrol-listesi.md#m-12-5)
- [16.1 İlhamı iş ve bağlamla ilişkilendir.](../codex-kontrol-listesi.md#m-16-1)
- [16.2 Belirsiz yönleri temsili içerikle karşılaştır.](../codex-kontrol-listesi.md#m-16-2)
- [16.3 Reddedilen tasarımın nedenini sonraki deneye taşı.](../codex-kontrol-listesi.md#m-16-3)
- [16.4 Seçilen tasarım sözleşmesini tek yerde tut.](../codex-kontrol-listesi.md#m-16-4)

[İçindekiler](README.md) · [← Güvenilir sonuç elde etmek](12-dogrulama.md) · [Büyük işleri ve paralel çalışmayı yönetmek →](14-buyuk-isler.md)
