# 3. Codex gerçekte nasıl çalışıyor?

Belge kontrolü: 2026-10-29.

Bir konuşma turunda Codex metin üretebilir, araç çağırabilir, aracın sonucunu değerlendirebilir ve sonraki adımı seçebilir. Aynı cümle farklı ortamda farklı sonuç verir: belgeyi düzenlemek için dosyaya erişim gerekir. Dosyanın adını mesajda anmak içeriğini sağlamaz.

## Dört parçayı ayır

| Parça | Rolü | Yaygın yanlış beklenti |
|---|---|---|
| Model | İsteği yorumlar, çözüm ve araç kullanımına karar verir | Her bilgiye zaten sahip olduğu |
| Bağlam | Mesajlar, okunan kaynaklar ve ilgili talimatlar | Klasördeki her dosyanın tamamen okunmuş olduğu |
| Araç | Dosya okuma, komut, arama veya servis işlemi | Aracın kurulu olmasının doğru hesaba erişim sağladığı |
| Ortam | İşin yürüdüğü dosyalar, yazılımlar ve izinler | Bilgisayardaki her şeyin bulutta da bulunduğu |

Araç bir sonuç döndürdüğünde o sonuç da değerlendirme ister. “İşlem kabul edildi”, “işlem tamamlandı” ve “istenen kayıt değişti” farklı durumlardır. Dosya yüklenmiş olsa da onu ilgili sayfaya ayrıca bağlamak gerekebilir.

## Okumak, hatırlamak ve tahmin etmek

Codex'in dosya adını söylemesi dosyanın içeriğini okuduğunu göstermez. Geçmişten hatırlanan yol doğru olabilir ama dosya değişmiş olabilir. Bir ürün iddiası için asıl kayıt, araştırma iddiası için ilgili kaynak, görsel değerlendirme için güncel görüntü gerekir.

Bu ayrımı görünür kılmak için uzun düşünce dökümü istemene gerek yok. Kararı değerlendirmeye yarayan kanıtı iste:

```text
Önerini dayandırdığın mevcut davranışı göster.
Hangi dosyayı veya kaydı okuduğunu belirt.
Doğrudan gördüğün bilgi ile çıkardığın sonucu ayır.
```

Bu, bütün ara işlemleri raporlamasını istemekten farklı bir ihtiyaçtır. İlgili kontrolü tekrar bulabileceğin bir kayıt yeterlidir.

## Bir işlem zincirini doğru okumak

Kurgu örnekte Atölye'nin internet sitesindeki etkinlik tarihini değiştirmek istiyorsun. Zincir şöyle olabilir:

1. Codex tarihin kaynak dosyasını bulur.
2. Kaynağı düzenler.
3. Siteyi yeniden üretir.
4. Yerel sayfada doğru tarihi kontrol eder.
5. Yetkiliyse değişikliği uzak depoya gönderir.
6. Yayın tamamlanınca canlı adresi yeniden okur.

İkinci adımın başarısı altıncıyı kanıtlamaz. Dördüncü adım yanlış sunucuya bakıyorsa yerel doğrulama da yanlış olur. Bu nedenle “hangi çıktı, nerede?” sorusu her teslimde işe yarar.

## Kurgu senaryo: listede görünen ama erişmeyen bağlantı

Atölye'nin kayıtları bağlı bir belge servisinde. Plugin kurulu görünüyor ama istenen tablo dönmüyor. Muhtemel açıklamalar farklı: yanlış hesap, dosya paylaşım sınırı, eksik araç yeteneği, ağ sorunu veya yanlış kayıt kimliği. Modeli değiştirerek başlamanın bu ayrımlar için doğrudan bir yararı yok.

```text
Önce bağlantının hangi hesaba ve hangi dosyaya erişebildiğini zararsız bir
okumayla doğrula. Tabloyu bulamazsan aradığın kapsamı belirt.
Eksik erişimi eksik veri gibi raporlama.
```

Plugin, MCP ve işletim sistemi izinleri farklı erişim katmanlarıdır. Birinin çalışması diğerlerini doğrulamaz. [Bağlantılar](https://learn.chatgpt.com/docs/extend/mcp) · [İzin katmanları](https://learn.chatgpt.com/docs/permission-modes)

## Başarı mesajının kapsadığı alan

Bir komutun sıfır çıkış kodu, o komutun sözleşmesi içinde başarı demektir. Yanlış test filtresi hiç test çalıştırmadan başarılı bitebilir. Bir dosyanın üretilmesi içeriğinin doğru olduğunu, sayfanın açılması kaydın kalıcı olduğunu göstermez.

“Nasıl emin oldun?” sorusunun iyi cevabı bir sıfat değildir. Beklenen davranış, yapılan kontrol ve gözlenen sonuç birlikte görünmelidir. Bir başlık düzeltmesinde dosyayı yeniden açmak yeterli olabilir. Veri dönüşümünde ise satır sayısı ve kayıt kimlikleri gibi daha güçlü kontroller gerekir.

[İçindekiler](README.md) · [← Uygulamanın tamamını tanımak](02-uygulama.md) · [İş vermenin incelikleri →](04-is-vermek.md)
