# Gerçek deneyimlerden sekiz ders

Belge kontrolü: 2026-10-29.

Bu bölüm, bu rehber hazırlanırken seçili proje raporları ve ilgili konuşma parçaları üzerinden doğrulanan gerçek deneyimleri anonimleştirir. Tüm sohbet geçmişinin eksiksiz tarandığı iddiası yoktur. Özel kayıtlar, hesaplar, yerel yollar ve ham konuşmalar kamuya taşınmaz. Bölümlerdeki “Kurgu senaryo” metinleri bu vakaların kaydı değildir.

## C01

### Bulunamayan uygulama, hiç var olmamış uygulama değildir

**Gözlenen:** Daha önce çalıştırılmış bir masaüstü uygulamasının paketi ilk kontrol edilen konumlarda bulunamadı. Kullanıcı bu yoruma itiraz etti. Kaynak proje üzerinden Release derlemesi alındı ve uygulama süreci gözlendi.

**Ders:** “Bu yolda bulunamadı” sonucunu “uygulama yok” iddiasına dönüştürme. Kaynak, paket, çalışan süreç ve görünür pencere ayrı kanıtlardır.

**Sınır:** Pencere görünürlüğü ve yeni işlevlerin davranış testi bu kayıtla doğrulanmadı. Derleme başarısı ses kalitesini kanıtlamaz. Kontrol tarihi: 28 Ekim 2026.

## C02

### Eski not, güncel ürünün gerçeği olmayabilir

**Gözlenen:** Ürün incelemesinde eski “ilk kullanım akışı yok” notu mevcut kaynakla çelişti. Akış vardı; derleme koşulları farklı davranıyordu. Aynı incelemede bazı çevrilmiş içeriklerin uygulama paketine aktarılmadığı görüldü.

**Ders:** Belleği araştırma başlangıcı yap. İçerik, paketleme ve çalışma zamanı sorunlarını ayır. Mevcut çeviriyi yeniden üretmeden önce hangi katmanda eksik olduğunu bul.

**Sınır:** Kaynak ve paket incelemesi kullanıcı etkisi, mağaza sürümü veya fiziksel cihaz davranışı ölçümü değildi. Kontrol tarihi: 27 Ekim 2026.

## C03

### Geçen konum kontrolü, okunabilirliğin tamamını ölçmez

**Gözlenen:** A/B yerel prototipte klavye ve giriş alanına ilişkin konum kontrolü geçti; görüntüde ikinci metin satırının örtüldüğü görüldü. Yerleşim düzeltildi, ilgili kontrol ve son görsel inceleme yapıldı.

**Ders:** Testi hangi iddiayı ölçtüğüyle oku. Gerçek içerikli ekran görüntüsünü açmak, geometrik kontrolün kaçırdığı kusuru gösterebilir.

**Sınır:** Kullanıcının tasarım seçimi ve ana ürüne aktarım ayrı kaldı. Fiziksel cihaz ve gerçek VoiceOver doğrulaması bu prototip kanıtından çıkarılamaz. Kontrol tarihi: 20 Ekim 2026.

## C04

### Video doğrulaması, müzik beğenisini veya sosyal yayını kanıtlamaz

**Gözlenen:** Kitap kapaklarından oluşan videoda kapak sayısı, benzersizlik ve tam çözümleme kontrol edildi. Müzik yönü kullanıcıyı tatmin etmedi. Sonraki istek sessiz sürümün e-postayla teslimiydi.

**Ders:** Teknik bütünlük, yaratıcı tercih ve teslim aşamasını ayrı değerlendir. “Daha yaratıcı” geri bildirimini somut yönlere dönüştür.

**Sınır:** Sessiz sürümün teslim kaydı, müzik revizyonunun bittiğini veya sosyal platformda yayın yapıldığını göstermiyor. Kontrol tarihi: 19 Ekim 2026.

## C05

### Arama, “detayları aç” düğmesinin durumunu değiştirdi

**Gözlenen:** Kontrol listesinde arama ayrıntıları açabiliyordu; genel aç/kapat düğmesi önceki duruma göre davrandığında tutarsızlık oluştu. Düğmenin görünür ayrıntıların gerçek durumundan türetilmesiyle sorun giderildi ve regresyon kontrolü eklendi.

**Ders:** Etkileşim durumunu tek bir önceki tıklamadan çıkarma. Arama, filtre ve toplu işlem aynı durumu etkiliyorsa birlikte sınanmalı.

**Sınır:** Bu belirli sayfa davranışı için kanıttır; her arama uygulaması aynı yapıyı kullanmaz. [Önceki doğrulama raporu](../DOGRULAMA.md), 21 Ekim 2026.

## C06

### Aynı sayfada bağlantı değişimi, ilk yüklemeyle aynı olay değildir

**Gözlenen:** Maddeye derin bağlantı, sayfa ilk açıldığında çalışırken aynı sayfadaki başka hash bağlantısına geçişte beklenen açılmayı sağlamıyordu. `hashchange` davranışı ele alındı ve kontrol edildi.

**Ders:** Bir bağlantının doğrudan açılması ile gezinme sırasında kullanılması ayrı senaryolardır. Kullanıcının gerçek yolunu test et.

**Sınır:** Sayfa içi bağlantı davranışıdır; uzak yayın veya bütün tarayıcı uyumluluğu kanıtı değildir. [Önceki doğrulama raporu](../DOGRULAMA.md), 21 Ekim 2026.

## C07

### Ağ engeli, yanlış kimlik bilgisi demek değildir

**Gözlenen:** Kısıtlı ortamda başarısız kimlik kontrolü, uygun erişimle yapılan salt okuma kontrolüyle aynı sonucu vermedi.

**Ders:** Hata metnini nedenin tamamı sayma. DNS/ağ, sandbox, oturum ve hizmet iznini ayrı sınayarak ilerle; kanıt olmadan anahtar değiştirme.

**Sınır:** Bu vaka, bütün kimlik hatalarının ağdan kaynaklandığını söylemez. 21 Ekim 2026 tarihli çalışma kaydı. Özel erişim günlüğü bu kamuya açık rehbere eklenmez.

## C08

### Aynı isimli CLI, farklı ikili olabilir

**Gözlenen:** PATH üzerinden çağrılan CLI ile masaüstü uygulamasının beraberinde gelen CLI farklı sürümlerdeydi. Seçili komut desteği güncel ikilinin yardım çıktısıyla kontrol edildi.

**Ders:** Sürüm karşılaştırırken çağrılan dosyayı ve yüzeyi belirt. Eski CLI'da komut bulunmaması, uygulamanın tamamında yeteneğin bulunmadığını kanıtlamaz.

**Sınır:** Sürüm numaraları tarihli gözlemdir. Güncel kurulumun `--version` ve `--help` çıktısı yeniden kontrol edilmelidir. [Önceki kaynak denetimi](../KAYNAKLAR.md), 21 Ekim 2026.

[İçindekiler](README.md)
