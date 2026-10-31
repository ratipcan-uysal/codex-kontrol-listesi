# 31 Ekim 2026 — Altı ek kullanım dersi

## İçerik yerleşimi ve tekrar denetimi

| Ders | Ana açıklama | Bağlandığı mevcut örnek |
|---|---|---|
| Girdi biçimi seçimi | 2. bölüm: aynı bilgi, farklı girdi | Katılım CSV'si, ekran görüntüsü ve formüllü çalışma kitabının farklı soruları cevaplaması |
| Gerçekten düzenlenebilir çıktı | 17. bölüm: kullanacağın biçimde teslim | Mevcut Atölye PPTX ve PNG karşılaştırması; tahsilat için değişken girdi kontrolü |
| Değişikliğin etkileri | 5. bölüm | Atölye tarihinin 14 Kasım'dan 21 Kasım'a taşınmasının dosya ve dış kayıtlardaki etkisi |
| Toplu işlem önizlemesi | 8. bölüm | Taslak/onaylı programın aynı hedef ada çakışması |
| Bağımsız dayanak | 9. bölüm | B seçeneğinin aynı CSV iddiasını aktaran üç sayfa |
| İncelenen kapsam | 3. bölüm | Tam okunan not, yalnız örneklenen CSV ve kısmen okunabilen PDF |

12 ve 14. bölümler ayrıntıyı tekrarlamak yerine ilgili ana açıklamaya bağlanır. Araştırma ve veri yolculuklarına ihtiyaç noktasında bağlantı eklendi. Genel teslim biçimi açıklaması yeni ölçütlerle birleştirildi; ayrı bir ikinci anlatım yapılmadı. Yeni ana bölüm veya katılımcı alıştırması yok. Mevcut Atölye örnek dosyaları değiştirilmedi.

Prompting ve Work with files resmî kaynaklarının ilgili bölümleri yeniden açıldı; yalnız bu iki kaynağın tarih ve içerik özeti yenilendi. Örneklerin iş akışı yorumları ürünün garantisi olarak sunulmadı.

## Doğrulama

- 6 kontrol listesi + 21 rehber Python kontrolü PASS. Üretim ve JavaScript sözdizimi kontrolü PASS.
- 25 mevcut rehber tarayıcı kontrolüne ek olarak altı yeni tablonun 1440/320 px görünümü ve örnek işlerden gelen iki bağlantı tek odaklı denetimde kontrol edildi; yerelde toplam 26 PASS.
- Altı tablonun seçili masaüstü/mobil görüntüleri açılarak incelendi. Mobilde mevcut yatay kaydırmalı tablo davranışı korunur.
- 107 madde, eşleme, 84 özellik ailesi, mevcut görseller/örnekler/akışlar/eğitim rotası aynı. 256 eski HTML kimliği korundu.
- 1.800 → 1.900 TL örneği gerçek örnek CSV'deki değerlerden hesaplandı; kaynak dosya değiştirilmedi. K04 boş kalıyor. Bu doğrulama bir XLSX uygulaması testi değildir.

## Sınırlar ve çalışma kaynakları

Kurgu tarih değişikliği, PDF okuma kaydı, dosya yeniden adlandırma ve dışa aktarma denemesi gerçek kullanıcı sistemlerinde çalıştırılmadı. Yeni bir XLSX veya PowerPoint uygulama testi yapılmadı; mevcut PPTX'in düzenlenebilir tablo yapısı mevcut rehber testiyle doğrulandı. Öğrenme başarısı ölçülmedi.

İlk yardımcı Python sözdizimi kontrolü sistem önbelleğine yazmaya çalıştığı için izin hatası verdi. Sistem önbelleği izni genişletilmedi; aynı kaynak bellek içinde AST ile kontrol edildi ve tarayıcı koşumu tamamlandı. İçerik üretimi ve testlerde hata yoktu. Son yerel koşumda 15 görev süreci ve geçici sunucu kapandı; kalan yok. Paylaşılan araç kurulumu kullanıldı, bağımlılık kurulmadı. Kaynaklar ve kanıtlar korundu.

Yayın ve canlı kontrollerin sonucu DOGRULAMA.md içinde ayrı kaydedilir.
