# 31 Ekim 2026 — Dinleyici revizyonu

## Uygulanan değişiklikler

1. Atölye'nin ücretsiz Tanışma Buluşması ile ücretli Uygulama Programı ayrıldı. Altı tahsilat kaydı ücretli programa ait; 60 kişilik ücretsiz buluşmanın örneklemi değil. Tarih ve kapasite denemeleri kurgu devam olarak işaretlendi.
2. İlk kullanım, kaynak notu → istek → dosyayı açma → aynı dosyayı düzeltme akışına dönüştü. Üç indirilebilir Markdown dosyası kaynak ve önce/sonra karşılaştırmasını somutlaştırıyor.
3. Eğitim rotası ilgili öğretim sahnesine açılıyor. Numaralı konu sırası ayrı, varsayılan kapalı bir başvuru alanında; iki farklı sonraki adım yarışmıyor.
4. Sohbet seçimi, bilinmeyen ödeme ve otomasyona geçiş tekrarları kısa bağlantılarla birleştirildi. Platform bilgisi, eski başlık bağlantıları ve kontrol listesi korundu.
5. Araştırma işine, belirsiz isteği üç soruyla karara dönüştüren kurgu konuşma eklendi. Kaynakta cevabı olan soruyu tekrar sormama ve teknik karar yükünü kullanıcıya taşımama ilkeleri örnekte gösteriliyor.
6. Sayfa işine, yanlış tarih için iki açıklamayı ayıran küçük kontrol eklendi. Kaynak değişmemiş mi, başka kopya mı açık? Sonuç görülmeden yeni düzeltmeye geçilmiyor.

## Görsel kapsamı ve açık sınırlama

**BLOCKED — Yeni Atölye uygulama ekranları:** Bilgisayar kontrolü, Codex uygulamasına erişimi güvenlik gerekçesiyle reddetti. Başka ekran yakalama yöntemiyle bu sınır aşılmadı. Yeni Atölye oturumu kaydı üretilmedi.

Mevcut gerçek resmî proje ve önizleme görselleri ilk kullanımın ilgili adımlarına taşındı. Bunların farklı resmî örnekler olduğu, Atölye'nin dört adımlık oturumu olmadığı açıkça yazıyor. Üç Markdown dosyası hazırlanmış öğretim çıktılarıdır, çalıştırılmış oturum kanıtı değildir. Kendi Atölye oturumunun gerçek ekranları sonraki tamamlayıcı iş olarak kalıyor.

## Doğrulama

27 Python testi ve JavaScript sözdizimi kontrolü geçti. Yerel rehberin 26 tarayıcı kontrolü geçti: eğitim rotası, konu sırası, indirilebilir dosyalar, önce/sonra sırası ve dar ekran davranışı dahil. Son iki metin düzeltmesinden sonra Python kontrolleri tekrar geçti; canlı tarayıcı koşumu yayınlanan son içeriği kontrol eder.

Yerel masaüstü proje adımı, dar ekran düzeltme adımı, masaüstü soru-cevap tablosu ve dar ekran ayırıcı kontrol tablosu açılıp incelendi. Tablolar dar ekranda kendi içinde yatay kayıyor. Eski HTML kimlikleri sayfa bazında karşılaştırıldı; kayıp yok. Değişmeyen kontrol listesi, eşlemeler, CSV'ler, görseller ve sunum dosyaları korundu.

## İlk başarısızlıklar ve temizlik

İlk görüntü alma koşumunda 26 davranış kontrolü geçtikten sonra yardımcı seçici, rakamla başlayan kimlik için geçersiz CSS üretti. Seçici düzeltildi; ikinci koşum ve görüntüler başarılı. İlk koşumun kaydı özel çalışma dizininde korundu; izlenen 15 sürecin tamamı kapandı. Son yerel koşumun izlenen 14 süreci kapandı, kalan yok.

İlk içerik hazırlama denemesinde dört kaynak takma adı doğrulamadan geçmedi; yazımdan önce düzeltildi. Bir üretim komutu yanlış klasörden çağrıldığı için çalışmadı; doğru klasörde başarılı oldu. Süreç envanteri ilk izinli ortamda okunamadı, yetkili salt-okunur kontrolle alındı.

Uygulama erişimi reddedildikten sonra CUA oturumu sıfırlandı; bu işlem ortak Node sunucusunun kapandığı iddiası değildir. Kesin görev sahipliği kurulamayan ortak MCP altyapısına dokunulmadı. Tarayıcı koşumlarının kendi süreçleri ayrı izlendi ve kapatıldı. Yeni bağımlılık veya simülatör kurulmadı; yayımlanacak dosyalar ve kanıtlar korundu.
