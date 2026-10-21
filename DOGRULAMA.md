# Doğrulama kaydı

Tarih: 21 Ekim 2026. Kapsam: 19 bölüm, 107 madde, 25 temel / 82 ileri.

| Kontrol | Sonuç | Kanıt / sınır |
|---|---|---|
| İçerik ve derleme bütünlüğü | PASS | 6 Python testi; eksik doğrulama, bilinmeyen kaynak ve yinelenen kimlik olumsuz örnekleri reddedildi. |
| Eski madde kimlikleri | PASS | İlk sürümün 97 kimliği korundu. |
| JavaScript sözdizimi | PASS | `node --check kaynak/app.js`. |
| Tarayıcı davranışı | PASS | 28 kontrol; [ham sonuç](dogrulama/browser-results.json). |
| Kaynak bağlantıları | PASS | 21 bağlantı HTTP 200; [adres ve durumlar](dogrulama/source-links.json). Erişim, tüm içerik iddialarının kanıtı değildir. |
| Görsel inceleme | PASS | 1440 px açık/koyu, 390 px ana ekran ve açılmış hook maddesi görüntüleri açılarak incelendi. |
| Dar ekran | PASS | 320 ve 390 px görünümde yatay sayfa taşması yok; mobil bölüm seçimi çalışıyor. |
| Seçili CLI bayrakları | PASS | 0.163.0-alpha.10.2 yardım çıktıları [kanıt dizininde](dogrulama/). Canlı iş koşumu değildir. |
| Rehberdeki tüm Codex senaryoları | NOT_RUN | Modeller, hook’lar, izin profilleri, zamanlayıcı ve cihaz örnekleri uçtan uca çalıştırılmadı. |
| Safari, Firefox, fiziksel mobil cihaz | NOT_RUN | Otomatik tarayıcı koşumu Chrome 155.0.8059.85 ile sınırlı. |

Arama, temel/ileri filtre, yapılmamış filtresi, yeniden yüklemede işaret koruma,
kopyalama, JSON dışa/içe alma, eski yedek, iptal, geçersiz/büyük yedeği reddetme,
derin bağlantı, depolama engeli ve JavaScript kapalıyken Markdown erişimi sınandı.

## Bulunan ve düzeltilen hatalar

- Arama detayları açtığı hâlde düğme ayrı bir durum tutuyordu. [Önceki koşumda](dogrulama/toggle-before.json) 10 açık detay düğmeye basınca açık kaldı. Durum artık görünür detaylardan türetiliyor; aynı kontrol geçti.
- Aynı belgede madde hash’i değişince detay açılmıyordu. [Önceki koşum](dogrulama/before-deeplink-fix.json) başarısızlığı korur. `hashchange` işleme eklendi; ilgili kontrol geçti.

## Kontrolleri yeniden çalıştırma

```sh
python3 kaynak/build.py
python3 kaynak/test_build.py
node --check kaynak/app.js
python3 -m http.server 8769 --bind 127.0.0.1
```

Başka terminalde, Playwright kuruluysa:

```sh
node kaynak/test_browser.cjs
```

Gerekirse `PLAYWRIGHT_MODULE` ile paket yolunu, `CHROME_PATH` ile tarayıcı
çalıştırılabilir dosyasını belirt. `BASE_URL` başka bir test adresi,
`EVIDENCE_DIR` çıktı dizini seçer. Test boş bir tarayıcı profili açar ve sonunda
kapatır. Sonuçlar ve görüntüler varsayılan olarak `work/browser-evidence/` altına yazılır.

Bu rapor yayından önceki yerel adayın kontrolüdür. GitHub Pages dağıtım durumu
ve canlı HTTP/içerik kimliği yayından sonra ayrıca doğrulanır.
