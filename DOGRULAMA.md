# Doğrulama kaydı

## 29 Ekim 2026 — Eğitim anlatısı: yerel doğrulama

24 Python testi ve 21 rehber tarayıcı kontrolü geçti. [Tarayıcı sonuçları](dogrulama/egitim-20261029/guide/results.json), [107 maddeyi koruma](dogrulama/egitim-20261029/legacy-preservation.json), [önce/sonra davranışı](dogrulama/egitim-20261029/demo-results.json) ve [inceleme](dogrulama/egitim-20261029/INCELEME.md). Masaüstü giriş, dar ekran akış ve açıklamalı örnek görüntüsü açılarak incelendi. Yerel tarayıcı koşumunun 16 süreci kapandı; yakalama koşumunun 10 süreci de kapandı. Mevcut kontrol listesi davranışı değişmedi. Canlı hedef doğrulaması ayrı kaydedilir.

## 29 Ekim 2026 — Görselli revizyon GitHub Pages üzerinde doğrulandı

**PASS:** [Güncel çevrimiçi rehber](https://ratipcan-uysal.github.io/codex-kontrol-listesi/rehber/) yeni içerik, altı arayüz gösterimi ve nötr paletle yayında.

- İçerik commit’i: `2fee67c517b058e3e5703d47dfb4959772f76c13`. GitHub `main` dalına gönderildi ve Pages aynı commit için `built` döndü.
- Canlı 29 HTML dosyası ve 6 PNG, yerel dosyalarla SHA-256 düzeyinde birebir aynı. [35 dosyanın yayın kanıtı](dogrulama/rehber-revizyon-20261029/live-publication.json).
- Boş Chrome profilinde **18 canlı tarayıcı kontrolü** geçti. Altı görselin yüklenmesi/atıfları, klavyeyle tam boyut açılması, mobil taşma, açık/koyu renkler, bölüm geçişleri ve eski işaretin korunması dahil. [Sonuçlar](dogrulama/rehber-revizyon-20261029/live/results.json).
- İlk canlı masaüstü çekimi görsel yüklenmeden alınmıştı; [erken çekim](dogrulama/rehber-revizyon-20261029/live-first-capture/README.md) korundu. Çekim öncesinde görselin decode edilmesini bekleyen kontrol eklendi. Canlı masaüstü/mobil görsel sayfası ve koyu tema görüntüleri açılıp incelendi. 14 görev süreci kapandı; [temizlik kaydı](dogrulama/rehber-revizyon-20261029/live/cleanup.json). Görevce oluşturulan Python önbelleği de kaldırıldı ve yokluğu doğrulandı.
- Bu yayın kaydı ve kanıtları sonraki belgeleme commit’inde eklenir; rehberin doğrulanan HTML ve görsellerini değiştirmez.

## 29 Ekim 2026 — Başlangıç ve görsel revizyonu: yerel kontroller

18 bölüm ve altı yazılmış ek yeniden okundu. [Bölüm bazında inceleme](dogrulama/rehber-revizyon-20261029/INCELEME.md), [metin ölçümü ve sınırları](dogrulama/rehber-revizyon-20261029/EDITORIAL.md).

- 21 Python testi (6 eski içerik + 15 rehber) ve JavaScript sözdizimi geçti. [Son üretim](dogrulama/rehber-revizyon-20261029/build-tests.json).
- 107 madde, bütün özgün alanlar ve eşlemeler aynı. [Karşılaştırma](dogrulama/rehber-revizyon-20261029/legacy-preservation.json).
- 28 kontrol listesi ve 18 rehber tarayıcı kontrolü geçti. Görsel yükleme, kaynak, tam boyut açma, klavye, mobil taşma ve nötr tema dahil. [Kontrol listesi](dogrulama/rehber-revizyon-20261029/checklist/browser-results.json) · [Rehber](dogrulama/rehber-revizyon-20261029/guide/results.json).
- Altı resmî arayüz gösterimi ve sitenin masaüstü/mobil açık/koyu görüntüleri açılıp incelendi. Sonrasında yalnız dört terimin kısa açıklaması netleştirildi; layout, asset, link ve davranış kodu aynı. Son metin yeniden üretildi, Python/link kontrolleri tekrar geçti.
- İlk kontrolün dizin/çapa hataları düzeltildi ve [başarısızlık kaydı](dogrulama/rehber-revizyon-20261029/first-attempt.md) korundu.
- Görsel yakalamanın 12 ve yerel tarayıcı koşumunun 29 görev süreci kapandı. [Yakalama](dogrulama/rehber-revizyon-20261029/capture-cleanup.json) · [Yerel test](dogrulama/rehber-revizyon-20261029/process-cleanup.json).
- Ürün envanteri 84 aile / 70 resmî kaynak. Bu, bütün Codex özelliklerinin canlı çalıştırılması veya tüm hesaplarda erişim garantisi değildir. Safari, Firefox, fiziksel cihaz ve VoiceOver testleri yapılmadı.

Bu kayıt yerel revizyonu doğrular. Push ve canlı hedef sonucu üstteki ayrı yayın kaydındadır; aşağıdaki ilk rehber yayını tarihsel kayıttır.

## 29 Ekim 2026 — GitHub ve çevrimiçi rehber yayında

**PASS:** [Çevrimiçi ana rehber](https://ratipcan-uysal.github.io/codex-kontrol-listesi/rehber/) GitHub Pages üzerinden giriş gerektirmeden açılıyor. [GitHub deposunun](https://github.com/ratipcan-uysal/codex-kontrol-listesi) girişine doğrudan çevrimiçi okuma bağlantısı eklendi.

- İçerik commit'i: `8e6ffa6d3da49460a1ab38056d439454972c9945`. `main` dalına gönderildi; Pages bu commit için `built` döndü.
- 28 rehber sayfası ve kontrol listesi dahil 29 HTML dosyasının canlı SHA-256 özeti yerel dosyayla birebir aynı. [Yayın kanıtı](dogrulama/rehber-20261029/live-publication.json).
- Boş Chrome profilinde 6 canlı kontrol geçti: giriş bağlantısı, bölüm geçişleri, maddeye geri dönüş ve odak, işaret koruma, 320 px komut görünümü ve JavaScript hatası kontrolü. [Sonuçlar](dogrulama/rehber-20261029/live/results.json).
- Canlı masaüstü ve mobil ekran görüntüleri açılıp incelendi. Teste ait süreçler kapandı; [temizlik kaydı](dogrulama/rehber-20261029/live/cleanup.json).
- Bu yayın kaydı ve kanıtları içerik commit'inden sonraki belgeleme commit'inde eklenir. Rehber HTML'sini değiştirmez.

## 29 Ekim 2026 — Yeni rehberin yerel doğrulaması

**Yerel kontrolün başlangıç durumu:** Aynı GitHub deposunun yerel kopyasında yayıma hazır değişiklikler. Bu kontroller alındığında commit, push ve canlı yayın yapılmamıştı. 29 Ekim gönderimi kullanıcı tarafından ayrıca yetkilendirildi; dış yayın sonucu ayrı kaydedilir. Aşağıdaki 21 Ekim yayın kaydı önceki kontrol listesine aittir.

| Kontrol | Sonuç | Kanıt ve sınır |
|---|---|---|
| Üretim | PASS | `python3 kaynak/build.py`; Markdown/HTML aynı canonical içerikten oluşuyor. |
| Eski içerik testleri | PASS | 6 Python testi. |
| Rehber testleri | PASS | 12 Python testi; iç bağlantı/çapa, 107 eşleme, 28 komut, kaynak alanları, deterministik üretim ve renderer olumsuz girdileri. |
| 107 maddeyi koruma | PASS | Bütün özgün madde alanları, kaynaklar ve ilk on sırası başlangıç commit'i ile aynı: [kanıt](dogrulama/rehber-20261029/legacy-preservation.json). |
| JavaScript | PASS | Mevcut ve yeni tarayıcı betiklerinin sözdizimi kontrol edildi. |
| Kontrol listesi tarayıcı regresyonu | PASS | [28 kontrol](dogrulama/rehber-20261029/checklist/browser-results.json). Eski işaret biçimi, içe/dışa aktarma ve filtreler dahil. |
| Yeni rehber gezinmesi | PASS | [14 kontrol](dogrulama/rehber-20261029/guide/results.json). 28 sayfa, sıralı okuma, geri bağlantı, işaret koruma, 320/390 px ve JavaScript kapalı kullanım. |
| Görsel inceleme | PASS | Açık masaüstü giriş ve komutlar, koyu bölüm, 320 px komut sayfası ve kontrol listesi giriş görüntüleri açıldı. Mobil komut bölünmesi düzeltildi. |
| Kaynak denetimi | BELGE | [64 resmî sayfanın manifesti](rehber/kaynak-manifest.json); gerekli bölümler okundu. [75 özellik ailesi](rehber/kapsam.md) ve erişim sınırları eşlendi. |
| Metin incelemesi | KOŞULLU ÖLÇÜM | [Önce/sonra ve pasaj değerlendirmesi](dogrulama/rehber-20261029/EDITORIAL.md). Üç regex eşiği korunmuş teknik anlatım nedeniyle açık; otomatik PASSED iddiası yok. |
| Görev kaynakları | PASS | Test tarayıcıları ve localhost sunucuları kapandı; [son koşum temizliği](dogrulama/rehber-20261029/process-cleanup.json). |
| Ürün özelliklerini uçtan uca çalıştırma | NOT_RUN | Rehber oluşturmak için hesap izinleri, otomasyonlar, gönderimler veya Goals senaryoları etkinleştirilmedi. |
| Diğer tarayıcı/platform | NOT_RUN | Otomasyon Chrome ile sınırlı. Safari/Firefox, fiziksel cihaz ve gerçek VoiceOver testi yapılmadı. |
| Yeni rehberin uzak/canlı durumu | PASS | Üstteki 29 Ekim yayın kaydı yeni rehberin commit, dağıtım ve canlı doğrulamasını gösterir. |

### Bulunan sorunlar ve korunmuş başarısızlık

Yeni rehberden kontrol maddesine tam sayfa dönüşünde ayrıntı açıldı, klavye odağı kayboldu. [İlk başarısız kontrol](dogrulama/rehber-20261029/first-attempt/results.json) saklandı. Başlangıç hash işleme `pageshow` ile sayfanın yerel odak davranışından sonra yürütüldü; aynı kontrol ve mevcut regresyon geçti. Bu değişiklik same-document `hashchange` davranışını korur.

Mobil görsel incelemede uzun komut adı satır ortasında bölünüyordu. Tablo içi kodu bölmeden gösterecek stil ve yatay kaydırma açıklaması eklendi. Rehberin 14 tarayıcı kontrolü yeni stil üzerinde yeniden geçti. Kontrol listesi aynı kaynakla daha önce geçtiği için bu son CSS değişikliğinde gereksiz yere yeniden çalıştırılmadı.

### Yeniden üretme

```sh
python3 kaynak/build.py
python3 kaynak/test_build.py
python3 kaynak/test_guide.py
node --check kaynak/app.js
node --check kaynak/test_guide_browser.cjs
python3 -m http.server 8769 --bind 127.0.0.1
```

Ayrı terminalde Playwright ve Chrome/Chromium varsa `node kaynak/test_browser.cjs` ve `node kaynak/test_guide_browser.cjs` çalıştırılır. Gerekirse `PLAYWRIGHT_MODULE`, `CHROME_PATH`, `BASE_URL`, `EVIDENCE_DIR` belirtilir. Derleme için üçüncü taraf paket kurulumu gerekmez. Tarayıcılar görev için geçici profil açıp kapatır; sunucu da işlem sonunda kapatılmalıdır.

## 21 Ekim 2026 — Önceki kontrol listesinin tarihsel kaydı

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

## Herkese açık yayın

PASS — [GitHub deposu](https://github.com/ratipcan-uysal/codex-kontrol-listesi) PUBLIC;
[GitHub Pages sitesi](https://ratipcan-uysal.github.io/codex-kontrol-listesi/) giriş gerektirmeden HTTP 200 döndü.
İlk içerik commit’i `938f363cfcfc04e3922a343bb0b891182943b989` için Pages durumu `built` olarak gözlendi.
Canlı HTML SHA-256 değeri yerel adayla birebir eşleşti.
Ayrıca boş tarayıcı profilinde 6 canlı kontrol geçti: HTTP, 107 madde, temel filtre,
arama, aynı belge içinde madde bağlantısı ve depo alt yolundan Markdown erişimi.
[Makine okunur yayın kanıtı](dogrulama/yayin.json).

Yerel kapsamlı kontroller, hash’i aynı kalan bu içerik için geçerlidir.
Sonraki bu rapor güncellemesi içerik HTML’sini değiştirmez.
