# Editoryal kontrol — 30 Ekim 2026

İncelenen metin: altı değişen bölüm ve iki ekin gövdesi. Rehberin tamamı yeniden yazılmadı. Mevcut ortak ilkeler bağlantıyla kullanıldı; yeni parçalar araç/cevap ayrımı, kabul kartı, amaç koruma, eski/yeni eşliği, tutarlılık ve görsel varlık seçimine odaklanır.

| Kontrol | Sonuç ve metindeki kanıt |
|---|---|
| 1. Açılışta gerilim | Evet; araç doğruyken son cevap yanlış olabilir (10), aynı puan farklı hataları gizler (18). |
| 2. Başarısızlık ve neden | Evet; kurgu CSV okumasının silinmesi gerçek girdiyi işlemeyi ortadan kaldırır (12). Gerçek olay iddiası değildir. |
| 3. Genellenebilir ders | Evet; kontrol ölçütünü düşürmeden işin amacını koruma (12). |
| 4. Yeniden kurulabilir model | Evet; girdi/beklenen/kaçınılacak hata/kontrol kartı (18). |
| 5. Sonuç rakamlarının kapsamı | Evet; 2/3 aynı üç kurgu örnek ve iki koşuma bağlıdır. Gerçek performans artışı iddiası yok. |
| 6. Güçlü iddiaların sınırı | Evet; araç testi son cevabı garanti etmez (10), eski hatalar körlemesine korunmaz (14). |
| 7. Birincil malzeme | Evet; resmî Cookbook metinleri doğrudan incelendi. Yeni senaryolar ayrıca kurgu olarak etiketlendi. |
| 8. Özgül adlar | Evet; Codex, GitLab, CSV, PLANS.md ve GOALS.md bağlamıyla açıklanır. |
| 9. Öğretici görselleştirme | Evet; araç/cevap, onarım, sürüm eşliği ve kabul kartı tabloları farklı kararları görünür kılar. |
| 10. Kapanışın işlevi | Evet; parçalar doğrulama veya sonraki bölüm bağlantısıyla biter. Ek moral özeti eklenmedi. |
| 11. Yazar boşluğu | Evet; [YAZAR] boşluğu yok. |
| D1. Somut örnek | Evet; Atölye takvimi, boş tahsilatlı CSV ve rehber üreticisi dönüşümü. |
| D2. Mekanizma | Evet; yanlış aşamayı belirleme, aynı girdiyi karşılaştırma ve değişebilir metni görselden ayırma. |
| D3. Sınır ve gözlem | Evet; koşum ile önbellek okuması, gerçek alfa ile boyalı dama zemini ayrılır. |
| D4. Yeni ayrım ve kaynak/kurgu | Evet; bölüm tablosu INCELEME.md içinde; her senaryo kaynaktan türetilen öğretim örneği olarak sunulur. |

## Dil ölçümü

`measure.mjs --lang=tr --json` önce ve sonra aynı sekiz gövde üzerinde çalıştırıldı. Girdi SHA-256 kayıtları [burada](editorial-input-hashes.json), ölçümler [önce](before-measure.json) / [sonra](after-measure.json).

| Ölçüm | Önce | Sonra |
|---|---:|---:|
| Kelime | 4.990 | 6.037 |
| Noktalı virgül / 1.000 kelime | 13,6 | 13,9 |
| Edilgen çatı / 1.000 kelime | 14,2 | 13,3 |
| Hazır ibare / 1.000 kelime | 0,2 | 0,2 |

Önce noktalı virgül, olasılık eki ve edilgen çatı; sonra noktalı virgül ve edilgen çatı bayraklı. Bu bir tam geçiş sonucu değildir. Teknik koşul ve karşılaştırma cümlelerinde bu yapılar korunmuştur; ölçümü düşürmek için anlam veya belirsizlik çıkarılmamıştır. Kapsam büyüdüğü için sayılar kontrollü bir üslup deneyi ya da öğretim başarısı karşılaştırması sayılamaz. Kurgu, ürün sınırı, kişisel deneyim ve doğrulanmış test sonucu ayrımı elle incelendi.
