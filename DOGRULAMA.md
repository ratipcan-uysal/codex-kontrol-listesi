# Doğrulama kaydı

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
| Yeni rehberin uzak/canlı durumu | NOT_PUBLISHED | Yerel değişiklikler hazır; eski canlı yayın yeni rehberin kanıtı değildir. |

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
