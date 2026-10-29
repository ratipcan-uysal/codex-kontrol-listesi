# 12. Güvenilir sonuç elde etmek

İçerik güncellemesi: 2026-10-30. Kaynak kontrol tarihleri kaynak dizinindedir.

Güvenilir sonuç, yalnız doğru görünen cevap değildir. İddiaya uygun kanıtın bulunması gerekir. Aynı doğrulama yöntemi kod, çeviri ve tasarım için yeterli olmaz.

<a id="dort-tur-cumleyi-ayir"></a>

## Dört tür cümleyi ayır

**Kaynak bilgisi:** “Resmî belgede bu özellik macOS için belirtiliyor.” **Gözlem:** “Bu hesapta ilgili seçenek göründü.” **Çıkarım:** “Bu yüzden sorunun izin ayarından kaynaklanması olası.” **Öneri:** “Önce dar kapsamlı okuma denemesi yapalım.” Birinden diğerine geçerken kesinlik artıyorsa yeni kanıt gerekir.

> Bulguları kaynakta yazan, bizzat gözlenen ve yorumlanan olarak ayır. Açılmayan kaynağı doğrulanmış sayma. Sonuç çıkarmaya yetmeyen yerde neyin eksik olduğunu belirt.

<a id="i-se-gore-kalite-olcutu"></a>

## İşe göre kalite ölçütü

| İş | Asıl soru | Uygun kanıt |
|---|---|---|
| Kod düzeltmesi | Hata gerçekten ortadan kalktı mı? | Önceki hatayı yakalayan kontrol ve ilgili regresyon |
| Çeviri | Anlam, atıf ve kesinlik derecesi korundu mu? | Kaynakla cümle/iddia karşılaştırması |
| Araştırma | İddia gerçekten o kaynağa dayanıyor mu? | Kaynağın ilgili kısmı, tarih ve yöntem sınırı |
| Veri dönüşümü | Kayıt, birim ve hesaplar tutarlı mı? | Satır/anahtar kontrolleri, örnek hesap, eksik veri açıklaması |
| Tasarım | Kullanıcı işi anlayıp tamamlayabiliyor mu? | Gerçek içerikle açılmış görünüm ve uygun durumlar |
| Yayın | Doğru çıktı hedefte mi? | Hedefte tekrar okunan sürüm, dosya veya kayıt |

Örneğin İngilizce metinde “may reduce” ifadesini “azaltır” diye çevirmek, dilbilgisi düzgün olsa da iddianın gücünü değiştirir. Kaynak yeniden araştırılmadan yapılabilecek düzeltme, bu anlam farkını gidermektir.

<a id="yesil-testin-ne-soyledigini-oku"></a>

## Yeşil testin ne söylediğini oku

Test komutunun çıkış kodu sıfır olabilir ama hiç test seçilmemiş olabilir. Yanlış klasördeki eski derleme test edilmiş olabilir. Kontrol, yalnız dosyanın varlığını ölçüyor olabilir. Rapor bu ayrımları göstermeli: hangi kaynak, hangi komut, kaç test, hangi ortam ve hangi davranış.

Geçen testleri gerekçesiz tekrar etmek de güvenilirliği artırmaz. Kaynak, yapılandırma, ortam ve kapsam aynı kaldıysa kanıt yeniden kullanılabilir. İlgili değişiklik veya yeni hata varsa kontrol yenilenir.

<a id="onarim-isin-amacini-koruyor-mu"></a>

### Onarım işin amacını koruyor mu?

**Kurgu örnek:** CSV’yi okuyamayan rapor betiğinden dosya okuma adımı kaldırılıyor. Program artık hata vermiyor, fakat sabit örnek rakamları yazıyor. Çalıştırmanın geçmesi, raporun gerçek girdiyi işlediğini göstermez. Cookbook’ın onarım örneği de çalışabilirlik yanında özgün öğretim amacını korumayı denetler. [Onarım döngüleri](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex)

Anlatıcı şu küçük deneme kaydını gösterebilir:

| Deneme | Değişiklik | Kontrol | Kalan sorun |
|---|---|---|---|
| 1 — yanlış kestirme | CSV okuma kaldırıldı. | Program açılıyor; girdi değişince sonuç aynı. | Veri işleme amacı kayboldu. |
| 2 — hedefli düzeltme | Dosya yolu düzeltildi. | Aynı CSV doğru okunuyor; bir tutar değişince toplam değişiyor. | Eksik tutar hâlâ ayrı belirtilmeli. |

> Geçen kontrolün hangi davranışı kanıtladığını yaz. Hata veren işi silerek veya kabul ölçütünü gevşeterek başarı üretme. Kalan bulguyu sonraki denemeye taşı.

Bu son istek bizim uygulama önerimizdir. Kayıt, kapsamlı bir günlük olmak zorunda değil; değişiklik, gözlenen sonuç ve kalan sorun yeterli. Aynı sorun değişmeden sürüyorsa [Goals karar akışına](14-buyuk-isler.md#goals-ne-zaman-yararli) dön; açıklamasız yeni deneme ekleme.

<a id="gercek-deneyim-klavye-kontrolu-gecti-metin-ortuldu"></a>

## Gerçek deneyim: klavye kontrolü geçti, metin örtüldü

Bir yerel prototipte klavye ile giriş alanının çakışmadığını ölçen kontrol geçti. Ekran görüntüsünde ise ikinci metin satırı örtülüyordu. Sayısal konum kontrolü, okunabilirliğin bütününü ölçmüyordu. Görsel bulgudan sonra yerleşim düzeltildi ve son görünüm yeniden incelendi. Bu sonuç üretim ürününe aktarım veya fiziksel cihaz doğrulaması anlamına gelmedi. [Vaka C03](deneyimler.md#c03)

<a id="i-nceleme-ile-duzeltme-arasindaki-sinir"></a>

## İnceleme ile düzeltme arasındaki sınır

Git projesinde `/review`, seçilen değişiklikleri inceleyip bulgu üretmeye yarar; kendi başına bütün önerileri uygulama işi değildir. Review panelinde Unstaged, Staged, Commit, Branch ve Last turn gibi kapsamları doğru seç. Depodaki bütün değişiklikler yalnız son asistan turuna ait olmayabilir. [Kod inceleme](https://learn.chatgpt.com/docs/code-review)

Bağımsız ikinci bakış, özellikle aynı akıl yürütmenin hatasını tekrar etmesini azaltmak için değerlidir. İnceleyene “önceki yanıtı onayla” yerine hedef ve kanıtı ver. Hiç bulgu çıkmaması, bütün olası hataların yokluğunu kanıtlamaz.

![Değişen satıra bağlı inceleme bulgusu. İnceleme yorumu ilgili kod satırının yanında duruyor. Bulguyu öncelik etiketiyle birlikte gerekçesi ve etkilenen dosyası üzerinden değerlendir.](assets/review.png)

**Değişen satıra bağlı inceleme bulgusu.** İnceleme yorumu ilgili kod satırının yanında duruyor. Bulguyu öncelik etiketiyle birlikte gerekçesi ve etkilenen dosyası üzerinden değerlendir. [Tam boyut](assets/review.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/code-review) · 2026-10-29.

1. **Nereye bak:** Kod satırına bağlı bulgunun gerekçesine; yalnız P1 etiketine değil.
2. **Ne yap:** Bulgunun gerçek davranışı etkileyip etkilemediğini kontrol ettir.
3. **Ne gör:** Geçerli bulgu için dar kapsamlı fark ve ilgili doğrulama.

<a id="kurgu-senaryo-kayit-sayisi-dogru-anlam-yanlis"></a>

## Kurgu senaryo: kayıt sayısı doğru, anlam yanlış

Atölye'nin 80 katılımcı kaydı dönüşümden sonra yine 80 satır. Bu iyi bir ilk kontrol, ama iki kişinin e-postası yer değiştirmiş olabilir. Sabit kayıt anahtarıyla eşleştirme, alan bazlı karşılaştırma ve temsilî uç durumlar gerekir. Toplamın eşit olması kimliğin korunduğunu tek başına göstermez. Bu yüzden “80 satır korundu” ile “dönüşüm doğru” aynı rapor cümlesi olmamalı.

<a id="kaniti-sonucun-icinde-gor"></a>

## Kanıtı sonucun içinde gör

[Tablo örneği](is-veri.md) hesap ile iddia farkını; [sayfa örneği](is-sayfa.md) kaynak farkı ile görünüm kontrolünü somutlaştırıyor.


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [9.1 Önemli incelemeyi üreticiden ayrı bağlamda yap.](../codex-kontrol-listesi.md#m-9-1)
- [12.1 Çalışan test kümesini ve sayısını doğrula.](../codex-kontrol-listesi.md#m-12-1)
- [12.2 Yeni kontrolün hatayı yakaladığını sınayıp göster.](../codex-kontrol-listesi.md#m-12-2)
- [12.3 Alt ajanın tamamlanma raporunu asıl kanıtla eşleştir.](../codex-kontrol-listesi.md#m-12-3)
- [12.4 Kalan belirsizliği somut adlarla yaz.](../codex-kontrol-listesi.md#m-12-4)
- [12.6 Önemli diff’i bağımsız kod incelemesine ver.](../codex-kontrol-listesi.md#m-12-6)

[İçindekiler](README.md) · [← Talimatları ve kişisel çalışma düzenini kurmak](11-talimatlar.md) · [Tasarım ve yaratıcı üretim →](13-tasarim.md)
