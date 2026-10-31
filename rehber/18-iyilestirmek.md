# 18. Kendi kullanımını sürekli iyileştirmek

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Kullanımını geliştirmek için bütün ayarları açmak veya her yeni modeli denemek gerekmez. En çok tekrarlanan sürtüşmenin nedenini bulmak daha fazla değer üretebilir.

<a id="bir-basarisizligi-siniflandir"></a>

## Bir başarısızlığı sınıflandır

| Belirti | Önce sınanacak neden |
|---|---|
| Sürekli yanlış dosya değişiyor | Hedef klasör, birincil proje veya worktree yanlış mı? |
| İstenen içerik sürekli yeniden araştırılıyor | Geçerli kaynak ve önceki karar erişilebilir mi? |
| Sonuç bitmiş deniyor ama kullanılamıyor | Bitiş ölçütü gerçek hedefte mi tanımlı? |
| Aynı konuda onay soruluyor | Görev yetkisi belirsiz mi, teknik engel mi var? |
| Görsel sonuç sıradanlaşıyor | Referans, içerik veya tasarım kararı eksik mi? |
| Uzun iş ilerlemiyor | Araç beklemesi, gereksiz tekrar veya bağımlılık mı var? |

Bu tablo modelin hiç hata yapmadığını söylemez. Yalnız çözümü seçmeden önce hatanın yerini bulur.

<a id="temsil-islerle-karsilastir"></a>

## Temsilî işlerle karşılaştır

Bir model veya talimat değişikliğini değerlendirirken aynı başlangıç dosyası, aynı hedef ve aynı bitiş ölçütünü kullan. Kolay bir yazım düzeltmesindeki başarıyı karmaşık hata ayıklamaya genelleme. Senin işlerinden birkaç temsilî tür seç: kaynaklı metin, kod hatası, görsel karar, veri dönüşümü gibi.

Karşılaştırmada sonucu, müdahale ihtiyacını ve örnek bazında tutarlılığı birlikte gözle. Gerçek süre veya kullanım ölçülmediyse sayısal hız iddiası ekleme. Tek başarılı deneme evrensel sıralama oluşturmaz.

**Kurgu karşılaştırma:** Aşağıdaki iki koşumun toplamı aynı; geçen işler farklı.

| Örnek | İlk koşum | İkinci koşum |
|---|---|---|
| Eksik ödemeyi koruma | Geçti | Kaldı |
| Belirsiz takvim kaydını ayırma | Kaldı | Geçti |
| Kaynaktaki tarihi doğru aktarma | Geçti | Geçti |
| Toplam | 2/3 | 2/3 |

Bu tablo gerçek model ölçümü değildir. Öğrettiği ayrım şu: aynı başarı oranı, aynı güvenilir davranış demek olmayabilir. Model içeren değerlendirmede birkaç temsilî örneği aynı koşullarda tekrar çalıştır; hangi örneklerin değişken olduğunu ve kaç müdahale istediğini kaydet. Önbellekten eski cevabı yeniden okumak yeni deneme sayılmaz. [Tutarlılık değerlendirmesi](https://developers.openai.com/cookbook/examples/partners/harness_aware_plugin_evals/harness_aware_plugin_evals)

Bu tekrarlar değişken model davranışını araştırır. Değişmeyen deterministik testleri, yani aynı girdide aynı sonucu veren kontrolleri gerekçesiz yeniden çalıştırma önerisi değildir.

<a id="i-yi-yontemi-sakla-gecici-ayrintiyi-birak"></a>

## İyi yöntemi sakla, geçici ayrıntıyı bırak

Tekrarlanan sürtüşmenin türünü seç: yöntem için [skill örneği](10-baglantilar-skills.md#yontem-ikinci-haftada-neyi-koruyor), proje kuralı için [talimat bölümü](11-talimatlar.md), açık iş için [devir notu](06-baglam-bellek.md#devir-notunu-ve-yeni-baslangici-yan-yana-gor). Buradaki yeni karar, kaydettiğin yöntemin sonraki girdide işe yarayıp yaramadığını sınamaktır.

<a id="duzeltmeni-kucuk-bir-kabul-ornegine-donustur"></a>

### Düzeltmeni küçük bir kabul örneğine dönüştür

Girdi, beklenen sonuç ve yanlış sayılacak davranışı birlikte sakla. Modelin önerdiği ölçütü de gözden geçir. [Geri bildirimden değerlendirmeye](https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop)

| Alan | Veri örneğindeki karşılığı |
|---|---|
| Girdi | K04’ün tahsilatı boş olan altı satır |
| Beklenen | K04 boş kalır; 1.800 TL bilinen tahsilat diye adlandırılır |
| Hata | Boşluğu 0/600 yapmak veya kesin toplam demek |
| Kontrol | Kimlik/değer betikle; raporun iddiası kaynakla karşılaştırılarak |

[İkinci hafta raporu](ornekler/hafta-2-raporu.md) aynı yöntemi yeni durumla karşılaştırmak için hazır. Her küçük iş için test sistemi kurmak gerekmez; tekrar eden veya etkisi önemli düzeltmeyle başla.

<a id="guncellemede-neye-bakmali"></a>

## Güncellemede neye bakmalı?

Yeni özellik mevcut sürtüşmeni çözüyor mu? Hesabında ve platformunda var mı? Kullanacağın yüzeyde mi? Eski yöntemin yerini mi alıyor, yoksa ek kurulum mu istiyor? Bu sorular bir sürüm duyurusunu kullanım kararına çevirir.

Resmî uygulama ve komut belgelerini kontrol et; menü görünmüyorsa sürüm, platform, kurum politikası ve erişim dağıtımını ayır. Güncel belgeyle kurulu davranış çelişirse ikisini tarihleriyle kaydet. Özelliği görememek, herkesten kaldırıldığı sonucunu vermez. [Uygulama](https://learn.chatgpt.com/docs/app) · [Sorun giderme](https://learn.chatgpt.com/docs/reference/troubleshooting)

<a id="gercek-deneyim-yanlis-hata-teshisi"></a>

## Gerçek deneyim: yanlış hata teşhisi

Kontrol listesinin önceki çalışmasında kısıtlı ağ ortamındaki kimlik kontrolü başarısız olmuştu. Bu çıktı doğrudan hesap anahtarının geçersizliğini kanıtlamıyordu. Uygun erişimle yapılan salt okuma kontrolü farklı sonuç verdi. Benzer biçimde PATH üzerinden çağrılan CLI ile uygulamanın beraberinde gelen CLI farklı sürümlerdi. Bir komutun varlığına ilişkin çelişkiyi çözmek için hangi ikilinin çalıştığını bilmek gerekti. Bunlar tarihli gözlemler; bugün her kurulumda aynı farkın bulunduğu iddiası değil. [Vaka C07 ve C08](deneyimler.md)

<a id="kurgu-senaryo-yeni-ozellik-icin-karar"></a>

## Kurgu senaryo: yeni özellik için karar

Yeni özelliği mevcut bir sürtüşmeye bağla. Atölye raporunda zamanlama kararını [otomasyon tablosuyla](15-otomasyon.md#ne-zaman-zamanlamaya-hazir) zaten verdik; burada yeni karar, güncelleme sonrasında eski kabul örneğinin hâlâ geçip geçmediğidir.

Örneğin yeni model K04’ü korurken `yedek` durumunu yanlış değiştiriyorsa genel puan yerine bu farkı kaydet. Yöntemi buna göre daralt. Ürün adı veya komut değiştiğinde de ilgili bölümü ve envanteri birlikte güncelle; eski örneği sessizce geçerli bırakma.


**Eğitim rotası tamamlandı.** Konu ayrıntıları için [içindekilere dön](README.md).


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [5.6 Model değişikliğini aynı görevle karşılaştır.](../codex-kontrol-listesi.md#m-5-6)
- [18.3 Tekrarlanan hatadan dar ve sınanabilir kural çıkar.](../codex-kontrol-listesi.md#m-18-3)
- [19.1 Düzenli aralıkla kullanım ve bekleyen işleri karşılaştır.](../codex-kontrol-listesi.md#m-19-1)
- [19.5 Geçmiş kullanımını ölçülü ve mahremiyeti koruyarak değerlendir.](../codex-kontrol-listesi.md#m-19-5)

[İçindekiler](README.md) · Konu sırasıyla oku: [← Teslim, yayın ve geri dönüş](17-teslim-yayin.md)
