# 3. Codex gerçekte nasıl çalışıyor?

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Bir konuşma turunda Codex metin üretebilir, araç çağırabilir, aracın sonucunu değerlendirebilir ve sonraki adımı seçebilir. Aynı cümle farklı ortamda farklı sonuç verir: belgeyi düzenlemek için dosyaya erişim gerekir. Dosyanın adını mesajda anmak içeriğini sağlamaz.

<a id="dort-parcayi-ayir"></a>

## Dört parçayı ayır

| Parça | Rolü | Yaygın yanlış beklenti |
|---|---|---|
| Model | İsteği yorumlar, çözüm ve araç kullanımına karar verir | Her bilgiye zaten sahip olduğu |
| Bağlam | Mesajlar, okunan kaynaklar ve ilgili talimatlar | Klasördeki her dosyanın tamamen okunmuş olduğu |
| Araç | Dosya okuma, komut, arama veya servis işlemi | Aracın kurulu olmasının doğru hesaba erişim sağladığı |
| Ortam | İşin yürüdüğü dosyalar, yazılımlar ve izinler | Bilgisayardaki her şeyin bulutta da bulunduğu |

Araç bir sonuç döndürdüğünde o sonuç da değerlendirme ister. “İşlem kabul edildi”, “işlem tamamlandı” ve “istenen kayıt değişti” farklı durumlardır. Dosya yüklenmiş olsa da onu ilgili sayfaya ayrıca bağlamak gerekebilir.

<a id="hangi-kaynak-hangi-karari-yonetiyor"></a>

## Hangi kaynak hangi kararı yönetiyor?

**Kurgu kaynak paketi:** `onayli-program.md` son tarihleri, `eski-taslak.md` önceki önerileri, görsel referans yalnız düzeni gösteriyor. Hepsini aynı ağırlıkta kullanmak eski tarihi geri getirebilir.

> İçerikte onaylı programı esas al. Eski taslağı yalnız değişiklik geçmişi için, görseli yalnız düzen için kullan. Çelişkiyi bu öncelikle çöz; onaylı belgenin kendi içinde tutarsızlık varsa belirt.

Dinleyiciye iki tarih göster: eski taslakta 12 Kasım, onaylı belgede 14 Kasım. Beklenen çıktı 14 Kasım’dır. Daha çok dosya eklemekten önce dosyanın hangi kararda söz sahibi olduğunu belirledik.

<a id="okumak-hatirlamak-ve-tahmin-etmek"></a>

## Okumak, hatırlamak ve tahmin etmek

Codex'in dosya adını söylemesi dosyanın içeriğini okuduğunu göstermez. Geçmişten hatırlanan yol doğru olabilir ama dosya değişmiş olabilir. Bir ürün iddiası için asıl kayıt, araştırma iddiası için ilgili kaynak, görsel değerlendirme için güncel görüntü gerekir.

Bu ayrımı görünür kılmak için uzun düşünce dökümü istemene gerek yok. Kararı değerlendirmeye yarayan kanıtı iste:

```text
Önerini dayandırdığın mevcut davranışı göster.
Hangi dosyayı veya kaydı okuduğunu belirt.
Doğrudan gördüğün bilgi ile çıkardığın sonucu ayır.
```

Bu, bütün ara işlemleri raporlamasını istemekten farklı bir ihtiyaçtır. İlgili kontrolü tekrar bulabileceğin bir kayıt yeterlidir.

<a id="bir-islem-zincirini-dogru-okumak"></a>

## Bir işlem zincirini doğru okumak

Atölye sayfasındaki tarih için kaynak dosya → üretilen sayfa → açılan görünüm zincirini takip et. Kaynak 14 Kasım iken önizleme 12 Kasım gösteriyorsa hemen metni tekrar yazdırma; hangi dosyanın üretildiğini ve açıldığını buldur. Commit, push ve canlı hedef aşamalarının tam karşılaştırması [teslim bölümünde](17-teslim-yayin.md#durumlari-birbirine-karistirma).

<a id="kurgu-senaryo-listede-gorunen-ama-erismeyen-baglanti"></a>

## Kurgu senaryo: listede görünen ama erişmeyen bağlantı

Atölye'nin kayıtları bağlı bir belge servisinde. Plugin kurulu görünüyor ama istenen tablo dönmüyor. Muhtemel açıklamalar farklı: yanlış hesap, dosya paylaşım sınırı, eksik araç yeteneği, ağ sorunu veya yanlış kayıt kimliği. Modeli değiştirerek başlamanın bu ayrımlar için doğrudan bir yararı yok.

```text
Önce bağlantının hangi hesaba ve hangi dosyaya erişebildiğini zararsız bir
okumayla doğrula. Tabloyu bulamazsan aradığın kapsamı belirt.
Eksik erişimi eksik veri gibi raporlama.
```

Plugin, MCP ve işletim sistemi izinleri farklı erişim katmanlarıdır. Birinin çalışması diğerlerini doğrulamaz. [Bağlantılar](https://learn.chatgpt.com/docs/extend/mcp) · [İzin katmanları](https://learn.chatgpt.com/docs/permission-modes)

<a id="bir-isi-anlatmakla-dosyayi-degistirmek-arasindaki-fark"></a>

## Bir işi anlatmakla dosyayı değiştirmek arasındaki fark

“Şöyle yapabilirsin” yanıtı bir açıklamadır. “Bu klasördeki dosyaya uygula” isteği ise araçla işlem gerektirir. Yalnız öneri geldiğinde istek şöyle netleşebilir: “Bu yaklaşımı mevcut dosyaya uygula, kaydet ve sonucu aç.” Araç erişimi yoksa Codex sınırı söylemeli; yapılmış işlem uydurmamalı.

Bir komutun başarılı bitmesiyle istediğin sonucun doğrulanması arasındaki farkı [güvenilir sonuç bölümünde](12-dogrulama.md) ayrıntılı ele alıyoruz. Burada temel alışkanlık, yanıtın hangi kaynağa dayandığını ve dosyada neyin değiştiğini takip etmek.

[İçindekiler](README.md) · [← Uygulamanın tamamını tanımak](02-uygulama.md) · [İş vermenin incelikleri →](04-is-vermek.md)
