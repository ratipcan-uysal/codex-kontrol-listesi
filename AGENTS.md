# Codex kontrol listesi

- İçeriği kaynak/content.py içinde düzenle; üretilen rehber/ çıktıları, index.html, README.md ve codex-kontrol-listesi.md dosyalarını doğrudan değiştirme.
- Yeni maddeleri bölüm sonuna ekle. Mevcut id ve anchor değerleri kullanıcı işaretlerinin anahtarıdır.
- Ürün iddiaları için ilgili güncel resmî belgeyi oku; iş akışı önerisini ürün zorunluluğu olarak sunma.
- Kontroller: python3 kaynak/build.py; python3 kaynak/test_build.py; node --check kaynak/app.js. Etkileşim değişirse kaynak/test_browser.cjs kapsamını çalıştır; görüntüyü açıp incele.
- Yayın: main kökünden GitHub Pages. Yerel test, push, Pages build ve herkese açık canlı yanıt ayrı durumlardır.
- docs/memory, kişisel dosyalar, kimlik bilgileri ve test tarayıcı profilleri public yayına dahil edilmez.
- Test sunucusunu ve görevce oluşturulan geçici tarayıcı süreçlerini iş bitince kapat; kanıtı ve yayımlanan dosyaları koru.

- Rehberin tek içerik kaynağı content.py içindeki GUIDE_* alanlarıdır. Özellik/komut değişince kaynak tarihi, envanter ve ilgili bölüm birlikte güncellenir. Gerçek deneyim ve kurgu senaryo etiketini koru.
- Rehber kontrolü: python3 kaynak/test_guide.py. Yeni rehber gezinmesi için kaynak/test_guide_browser.cjs; tarihli yayın durumunu DOGRULAMA.md içinde ayrı tut.
