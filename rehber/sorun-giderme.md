# Sorun giderme tablosu

Belge kontrolü: 2026-10-29.

Bir hata mesajı nedeni daraltır; her zaman tek nedeni belirlemez. Aşağıdaki tablo ilk ayırıcı kontrolü gösterir. İşe yaramayan yolu aynı biçimde tekrarlamak yerine yeni kanıt topla. [Resmî sorun giderme](https://learn.chatgpt.com/docs/reference/troubleshooting)

| Belirti | İlk ayırıcı kontrol | Kullanılabilir istek |
|---|---|---|
| Özellik menüde yok | Yüzey, hesap, platform, sürüm, kurum politikası | “Bu özelliğin hangi koşulda desteklendiğini resmî belgeyle karşılaştır.” |
| Komut bulunamadı | CLI mı mesaj alanı mı; doğru ikili mi? | “Çalıştırılan ikilinin yolunu, sürümünü ve yardım çıktısını kontrol et.” |
| Değişiklik önizlemede yok | Sunucu hangi klasör/porttan çalışıyor? | “Önizleme kaynağıyla düzenlenen dosyanın aynı olduğunu göster.” |
| Test geçti ama hata sürüyor | Test seçimi, sayı, kaynak sürümü ve tekrar koşulu | “Bu kontrolün eski hatayı gerçekten yakaladığını doğrula.” |
| İçerik kaynakta var, uygulamada yok | Üretim/paketleme adımı | “Yeni içerik son pakete girmiş mi; yeniden yazmadan önce kontrol et.” |
| Kimlik hatası | Ağ/DNS, sandbox, hizmet oturumu ayrımı | “Giriş bilgisini değiştirmeden salt okuma ile erişim nedenini ayır.” |
| Plugin kurulu ama araç görünmüyor | Hesap bağlantısı, sohbet keşfi, yüzey desteği | “Kurulum, yetkilendirme ve araç kullanılabilirliğini ayrı raporla.” |
| Araç var ama veri gelmiyor | Doğru hesap, dosya izni, sorgu kapsamı | “Küçük bir okuma denemesiyle hangi erişimin eksik olduğunu bul.” |
| Yerleşik tarayıcıda giriş yok | Ayrı tarayıcı profili | “Doğru profil ve hesapta olduğumuzu doğrula.” |
| Dosya yükleme çalışmıyor | Bu tarayıcı yolunun yükleme desteği | “Yerleşik tarayıcının sınırını kontrol et; desteklenen yolu belirt.” |
| Bilgisayar kullanımı çalışmıyor | OS ekran/erişilebilirlik izinleri, aktif oturum | “Hangi izin eksik, hangi işlem denenmiş, ayır.” |
| Bellek eski bilgi veriyor | Mevcut kaynakla tarihli notu karşılaştır | “Güncel durum değiştiyse eski kararın yerine geçtiğini kaydet.” |
| Ara mesaj dikkate alınmadı | Steer/queue tercihi, çalışan araç | “Yeni mesaj mevcut hedefi düzeltiyor; sonraki tur işi değil.” |
| Sürekli onay soruluyor | Gerçek teknik engel mi yetki belirsizliği mi? | “Zaten yetkili yerel işleri tamamla; kalan engelin adını ve gerekçesini ver.” |
| Otomasyon çalışmadı | Zamanlama, host, uygulama, proje erişimi | “Zamanlandı, başladı ve çıktı oluştu aşamalarını ayrı kontrol et.” |
| İkinci koşum çift kayıt üretti | Sabit anahtar / önce hedefi okuma | “Tekrar güvenliği ekle; mevcut kayıtları rastgele silme.” |
| Görsel hâlâ kötü | İçerik, hiyerarşi, etkileşim veya stil katmanı | “Hangi tasarım kararı soruna yol açıyor, aynı içerikle alternatif göster.” |
| İş bitmiş ama süreçler açık | Kaynak sahipliği ve etkin tüketici | “Yalnız bu görevin açtığı, işi bitmiş süreçleri kapat ve çıkışı doğrula.” |
| Yerel PDF eski görünüyor | Son derleme hatası ve son başarılı çıktı | “Kaynak kaydedildi mi, son derleme başarılı mı; ayrı kontrol et.” |
| Paylaşılan link yanlış sürüm | Uzak commit, deployment ve önbellek | “Hedef URL'deki sürümü kaynak kimliğiyle karşılaştır.” |

<a id="yardim-isterken-kucuk-ama-ayirici-kanit"></a>

## Yardım isterken küçük ama ayırıcı kanıt

“Çalışmıyor” yerine son başarılı adımı, beklenen davranışı, gözlenen sonucu ve tekrar koşulunu ver. Gerekirse ekran görüntüsü veya kısa log ekle. Tam log büyükse dosyada tutup ilgili hata bölümünü okut; binlerce satırı sohbetin içine kopyalamak asıl sinyali gizleyebilir.

```text
Beklenen: yeni başlık mobil görünümde iki satıra sığsın.
Gözlenen: yalnız açık menüde sayfa yatay taşıyor.
Tekrar: 320 piksel görünüm, uzun Türkçe başlık, menü açık.
Son değişiklik: başlık boyutu ve üst boşluk.
İstek: mevcut yönü koruyan en küçük düzeltme ve aynı koşulda doğrulama.
```

Bu şablon bir zorunlu form değildir. Sorunu ayıran bilgi zaten belliyse kısa cümle yeterlidir.

[İçindekiler](README.md)
