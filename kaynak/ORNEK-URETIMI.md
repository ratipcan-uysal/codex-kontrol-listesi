# İndirilebilir örneklerin kaynağı

Metin/CSV/HTML örnekleri `content.py` içindeki GUIDE_EXAMPLES'tan normal build ile üretilir. Grafik sayıları ve ikinci hafta raporu `example_data.py` ile aynı ham veriden hesaplanır. Girdi dosyası değişmez; boş tutar ve yeni durum korunur.

Sunumun karar verileri GUIDE_DECK içindedir. Üç düzenlenebilir slayt, önce/sonra görüntüleri ve grafik `render_examples.mjs` ile Artifact Tool kullanılarak oluşturuldu. Normal build sunumu yeniden render etmez; yayımlanan dosyaların hash'ini doğrular. Gereksinimler: Artifact Tool içeren Node çalışma ortamı, Presentations becerisinin doğrulayıcıları, Python ve Arial. Bu araçlar genel rehber okurunun kurulumu için gerekli değildir.

Yeniden üretim için boş bir çalışma dizinine `python3 kaynak/export_example_inputs.py <dizin>` ile girdileri yaz. `RUNTIME_NODE_MODULES`, `PRESENTATIONS_SKILL_DIR`, `RUNTIME_PYTHON` ortam değişkenleri gerçek kurulum yollarını göstermelidir. `node kaynak/render_examples.mjs <dizin>` aday sunumu doğrular, ayrı final dosyasını yazar ve final dosyayı içe alıp üç slaytı render eder. Aynı dizindeki final dosyanın üzerine yazmaz; yeni çalışma dizini kullan.

Görselleri tek tek açıp incele. Doğrulanan PPTX ve 1/3. slaytları rehber/ornekler'e, 2. slayt/önce görüntüsü/grafiği rehber/assets'e al. GUIDE_ARTIFACTS ve GUIDE_FIGURES özetlerini ve tarihlerini güncelle. Ardından normal build ve rehber kontrollerini çalıştır. Dosyaların kaynak/kurgu etiketi korunur. Başarılı dosya kontrolü PowerPoint veya Google Slides uygulamasında test edildiği anlamına gelmez.
