# Eğitim anlatısı incelemesi — 29 Ekim 2026

Ana okuma yolu üç tamamlanmış örnek işe taşındı: araştırmadan karar ve sunum taslağına, ham CSV’den açıklanabilir rapora, taşan sayfadan doğrulanmış düzeltmeye. 18 konu bölümü başvuru olarak korundu. Dinleyiciye alıştırma, kurulum veya ödev yüklenmiyor.

Her örnekte başlangıç malzemesi, istek, hatalı yaklaşım, müdahale, çıktı ve bitiş ölçütü var. Dokuz örnek dosya aynı içerik kaynağından üretiliyor. Araştırma ve veri dosyaları kurgu örneklerdir; gerçek bir Codex çalıştırmasının kaydı olarak sunulmaz. Sunum dosyası Markdown taslağıdır, PPTX değildir. Sayfa örneğinin önce/sonra HTML’si gerçekten tarayıcıda çalıştırıldı.

## Gerçek deneyimler

Dokuz anonim vaka içinde ilk dört vaka müdahale ve sonuç ayrımlarıyla derinleştirildi. İlk uygulama vakasında kronoloji düzeltildi: kullanıcının itirazı yeniden derlemeyi başlatmadı; daha önce yapılan derleme sonrasında fazla geniş “uygulama yok” iddiasını daralttı. Kaynak bulunması, yerel çalıştırma ve teslim birbirinden ayrıldı. Görsel prototip vakasında otomatik çerçeve testi ile ekrandaki okunabilirliğin farklılığı korundu. Müzik vakasına kanıtlanmamış yaratıcı başarı eklenmedi. Dokuzuncu vaka bu rehberin görsel ve öğretim revizyonudur. Öğrenme etkisi ölçülmedi.

## Öğretici görseller

Altı resmî açıklayıcı arayüz gösterimine “Nereye bak / Ne yap / Ne gör” notları eklendi. İki yeni görüntü kurgu HTML’nin gerçek tarayıcı ekranıdır; Codex uygulaması ekranı diye sunulmaz. Üç anlamsal akış şeması aynı veriden HTML ve Markdown’a çıkar. Beyaz/nötr gri görünüm korundu.

Masaüstü giriş, 320 px akış ve 390 px açıklamalı örnek görseli açılıp incelendi. Önce/sonra ham görüntüleri de incelendi. Tarayıcı kontrolleri görsel kalite değerlendirmesinin yerine geçirilmedi.

## Doğrulama ve sınırlar

- 24 Python testi: 6 kontrol listesi + 18 rehber. Bağlantılar, çapalar, üretim, akışlar, veri kimliği, eksik değerler ve örneklerin eşliği dahil.
- 21 yerel rehber tarayıcı kontrolü geçti. Üç işin sırası, 320/390/1440 px görünüm, sekiz görsel ve açıklamaları, eski madde işaretleri ve önce/sonra davranışı dahil.
- 107 özgün madde, kaynak alanları, ilk on sırası ve eşlemeler önceki commit ile aynı. Kontrol listesinin değişmeyen etkileşim koduna ait önceki 28 test kanıtı geçerliliğini korur; bu tur yeniden koşulmuş sayılmaz.
- Dört ilgili resmî belge yeniden okundu: komutlar, tarayıcı, dosya önizleme ve projeler. 84 özellik ailesi ve 70 kaynak korundu. Bütün ürün özellikleri çalıştırılmadı.
- İlk çapa hatası düzeltildi; başarısızlık kaydı korundu.
- Yerel yakalama ve tarayıcı süreçleri kapandı. Canlı yayın ayrı doğrulama kaydına bağlıdır.
- Safari, Firefox, fiziksel cihaz ve VoiceOver çalıştırılmadı. Gerçek dinleyici değerlendirmesi yapılmadı.
