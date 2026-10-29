# 18. Kendi kullanımını sürekli iyileştirmek

Belge kontrolü: 2026-10-29.

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

Karşılaştırmada yalnız sonucu değil, senin müdahale ihtiyacını da gözle. Kaç kez yanlış varsayımı düzelttin? Hangi adım tekrarlandı? Gerçek süre veya kullanım ölçülmediyse sayısal hız iddiası ekleme. Bir kez iyi çıkan örnek eğilim gösterebilir; evrensel sıralama oluşturmaz.

<a id="i-yi-yontemi-sakla-gecici-ayrintiyi-birak"></a>

## İyi yöntemi sakla, geçici ayrıntıyı bırak

Tekrarlanan düzeltmeyi uygun yere taşı: genel tercih global talimata, proje kuralı `AGENTS.md` dosyasına, tekrar eden yöntem skill'e, mekanik dönüşüm betiğe. Her olay için yeni bir katman ekleme. Aynı işi iki talimat farklı biçimde tarif ediyorsa birleştir.

> Son çalışmadaki tekrarları incele. Hangisi eksik bilgi, hangisi araç sınırı, hangisi kalıcı yöntem sorunu? Yalnız tekrar etmesi muhtemel ve somut karşılığı olan dersleri proje notlarına yaz.

<a id="guncellemede-neye-bakmali"></a>

## Güncellemede neye bakmalı?

Yeni özellik mevcut sürtüşmeni çözüyor mu? Hesabında ve platformunda var mı? Kullanacağın yüzeyde mi? Eski yöntemin yerini mi alıyor, yoksa ek kurulum mu istiyor? Bu sorular bir sürüm duyurusunu kullanım kararına çevirir.

Resmî uygulama ve komut belgelerini kontrol et; menü görünmüyorsa sürüm, platform, kurum politikası ve erişim dağıtımını ayır. Güncel belgeyle kurulu davranış çelişirse ikisini tarihleriyle kaydet. Özelliği görememek, herkesten kaldırıldığı sonucunu vermez. [Uygulama](https://learn.chatgpt.com/docs/app) · [Sorun giderme](https://learn.chatgpt.com/docs/reference/troubleshooting)

<a id="gercek-deneyim-yanlis-hata-teshisi"></a>

## Gerçek deneyim: yanlış hata teşhisi

Kontrol listesinin önceki çalışmasında kısıtlı ağ ortamındaki kimlik kontrolü başarısız olmuştu. Bu çıktı doğrudan hesap anahtarının geçersizliğini kanıtlamıyordu. Uygun erişimle yapılan salt okuma kontrolü farklı sonuç verdi. Benzer biçimde PATH üzerinden çağrılan CLI ile uygulamanın beraberinde gelen CLI farklı sürümlerdi. Bir komutun varlığına ilişkin çelişkiyi çözmek için hangi ikilinin çalıştığını bilmek gerekti. Bunlar tarihli gözlemler; bugün her kurulumda aynı farkın bulunduğu iddiası değil. [Vaka C07 ve C08](deneyimler.md)

<a id="kurgu-senaryo-yeni-ozellik-icin-karar"></a>

## Kurgu senaryo: yeni özellik için karar

Atölye'nin haftalık raporu her seferinde elle başlatılıyor, içerik yöntemi artık tutarlı. Yeni otomasyon özelliği bu sürtüşmeyi çözebilir. Buna karşılık rapor her hafta yanlış kaynakları seçiyorsa önce kaynak seçme yöntemi düzeltilir. Zamanlamayı otomatikleştirmek yanlış seçimi iyileştirmez.

Bu rehberi de aynı biçimde güncelle: kaynak tarihi değiştiğinde ilgili bölümü ve envanter satırını birlikte kontrol et. Bir özelliğin adı değişirse eski komut örneklerini sessizce geçerli bırakma; hangi yüzeyde neyin yerini aldığını belirt.

<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [5.6 Model değişikliğini aynı görevle karşılaştır.](../codex-kontrol-listesi.md#m-5-6)
- [18.3 Tekrarlanan hatadan dar ve sınanabilir kural çıkar.](../codex-kontrol-listesi.md#m-18-3)
- [19.1 Düzenli aralıkla kullanım ve bekleyen işleri karşılaştır.](../codex-kontrol-listesi.md#m-19-1)
- [19.5 Geçmiş kullanımını ölçülü ve mahremiyeti koruyarak değerlendir.](../codex-kontrol-listesi.md#m-19-5)

[İçindekiler](README.md) · [← Teslim, yayın ve geri dönüş](17-teslim-yayin.md)
