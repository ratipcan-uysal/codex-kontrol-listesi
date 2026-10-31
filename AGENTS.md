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

- Arayüz görsellerinin kaydı GUIDE_FIGURES içindedir; kaynak, açıklama, alternatif metin ve dosya özeti birlikte tutulur. Resmî açıklayıcı gösterimi kullanıcı hesabında çekilmiş ekran diye sunma. Metin lisansının görselleri kapsadığını varsayma.
- Markdown ve HTML bölüm çapaları birlikte üretilir. Eski çapaları ve kullanıcı işareti biçimini koru; yeni bağlantıları iki çıktıda kontrol et.

- Öğretim yolları GUIDE_PATHS, şemalar GUIDE_FLOWS, indirilebilir örnekler GUIDE_EXAMPLES alanlarından üretilir. Kurgu çıktıyı çalıştırılmış oturum kanıtı gibi sunma; gerçek vakada kronolojiden desteklenmeyen neden-sonuç çıkarma.

- Eğitim rotası GUIDE_ROUTE; düzenlenebilir örnek sunumun karar verileri GUIDE_DECK ve dosya özetleri GUIDE_ARTIFACTS içindedir. Veri örneklerini example_data.py aynı canonical CSV’den hesaplar. Yeniden sunum üretimi kaynak/ORNEK-URETIMI.md içinde açıklanır. Kurgu ekran/çıktı ile gerçek uygulama oturumunu ayır.
