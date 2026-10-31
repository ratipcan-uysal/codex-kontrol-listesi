# 4. İş vermenin incelikleri

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

İyi bir istek, Codex'in yanlış seçmesi pahalı olacak kararları açık eder. Her adımı önceden yazmak zorunda değilsin. İşin amacı belli olduğu hâlde uygulamanın bütün ayrıntılarını dayatmak, daha iyi bir çözüm bulma alanını daraltabilir.

<a id="alti-bilgiden-hangileri-gerekiyor"></a>

## Altı bilgiden hangileri gerekiyor?

Amaç, girdi, çıktı, korunacaklar, karar sınırı ve bitiş ölçütü bir isteği kurmak için yararlı altı başlıktır. Basit işte bunların çoğu bağlamdan bellidir. “Bu paragraftaki yazım hatalarını düzelt” için yeni bir brief gerekmeyebilir. Veri taşıma işinde ise hangi kayıtların korunacağı ve hedefin ne olduğu belirleyicidir.

```text
Etkinlik kayıtlarını tarih sırasına koy ve düzenlenebilir bir tablo üret.
Kaynak dosyayı değiştirme. Aynı adlı kişileri kendiliğinden birleştirme.
Geçersiz tarihleri ayrı listede göster.
Kaynak ve sonuç kayıt sayısını karşılaştır; fark varsa nedenini açıkla.
```

Örneğin gücü uzunluğundan gelmiyor. “Aynı ad aynı kişi değildir” kararını baştan koruyor. Aksi durumda temiz görünen bir tablo yanlış birleştirme içerebilir.

<a id="i-s-turunu-acikca-sec"></a>

## İş türünü açıkça seç

| İhtiyaç | Kullanılabilir istek |
|---|---|
| Anlamak | “Bu akış nasıl çalışıyor? Mevcut dosyalardan açıkla.” |
| Araştırmak | “Bu üç seçeneği belirtilen ölçütlerle karşılaştır; kaynakları aç.” |
| Karar vermek | “Seçenekleri, önerini ve önerini değiştirecek kanıtı yaz.” |
| Planlamak | “Önce uygulanabilir plan çıkar; bu aşamada dosya değiştirme.” |
| Üretmek | “Bu kapsamı uygula, sonucu kontrol et ve hataları düzelt.” |
| İncelemek | “Somut kusurları ve etkilerini raporla; dosya değiştirme.” |

Plan modu arayüzde mevcutsa onu kullanabilirsin. Normal mesajla “önce planla” diyerek de niyetini aktarabilirsin. Bu durumda arayüzdeki modun ayrıca değiştiğini varsayma. İsteğin sonunda “uygulama” ve “yalnız inceleme” yönlerinin çelişmemesine dikkat et. [İstek yazımı](https://learn.chatgpt.com/docs/prompting)

<a id="tekrarli-ciktinin-alanlarini-sec"></a>

## Tekrarlı çıktının alanlarını seç

Haftalık raporları karşılaştıracaksan aynı dört alanı iste: **karar, dayanak, açık soru, sonraki adım**. Bir hafta uzun deneme, diğer hafta dağınık maddeler üretmek karşılaştırmayı zorlaştırır.

> Bu haftaki bulguları bu dört alanla yaz. Kaynakta sorumlu veya tarih yoksa uydurma. İkinci haftada aynı alan sırasını kullan.

**Kurgu karşılaştırma:** Araştırma işindeki kararın iki haftasını aynı alanlarla oku. İkinci hafta hesap açma koşulunun kabul edildiğini varsayıyoruz.

| Alan | İlk hafta | İkinci hafta |
|---|---|---|
| Karar | B koşullu öneri | C yeniden aday |
| Dayanak | Hesapsız kayıt ve CSV şartlarını B karşılıyor | Hesap açma artık kabul ediliyor; C’nin 1.700 TL fiyatı yeniden değerlendirilebilir |
| Açık soru | Ek ücretler bilinmiyor | C’nin ek ücretleri bilinmiyor |
| Sonraki adım | B’nin ek ücretlerini doğrula | C’nin ek ücretlerini doğrula; toplam maliyeti karşılaştır |

Bilgi değişir, nerede aranacağı değişmez. Bu, teknik bir veri biçimi öğrenmeden çıktı sözleşmesi kurmaktır. Makinenin okuyacağı JSON gibi biçimler [ileri ekte](ileri-teknik.md#makineye-aktarilacak-cikti).

Plan için de küçük bir karar yeterlidir: “Sunumda fiyat mı, katılım kolaylığı mı önce gelsin?” sorusunu `/plan` ile netleştir; tercihini verdikten sonra “Bu kararı uygula, üç slaytı üret” de. Planı tekrar tekrar genişletmek yerine incelenebilir ilk çıktıya geç.

<a id="ornek-karsi-ornek-ve-korunacak-davranis"></a>

## Örnek, karşı örnek ve korunacak davranış

“Profesyonel yaz” birçok farklı tona karşılık gelebilir. “Aşağıdaki örneğin bilgi yoğunluğunda, satış baskısı kurmadan yaz” isteği daha belirgin bir hedef verir. Verdiğin örnekte hangi niteliğin önemli olduğunu söyle. Örneğin uzunluğunu veya tek bir kelimesini neden korumak istediğin belli değilse bunları zorunlu kurala çevirme.

Kurgu senaryoda Atölye'nin iptal mesajı şöyle iyileştirilebilir:

```text
Katılımcıya etkinliğin ertelendiğini anlatan kısa mesaj yaz.
Örnek ton: “Yeni tarihi cuma günü paylaşacağız. Kaydın korunuyor.”
Kaçın: “Kaçırılmayacak bu deneyim için heyecanla bekleyin!”
Henüz kesinleşmemiş yeni bir tarih ekleme.
```

Bir karşı örnek, beğenmediğin sonucu eleştirmekten daha erken işe yarar. Yaratıcı işlerde ilk taslağı gördüğünde yeni tercihler fark edebilirsin. Her ayrıntıyı ilk mesajda bilmen gerekmez.

<a id="yetkiyi-karar-turune-gore-ver"></a>

## Yetkiyi karar türüne göre ver

“Bana sormadan her şeyi yap” belirsiz kapsam bırakır. Daha iyi bir sınır, geri alınabilir uygulama ayrıntıları ile senin kararını gerektiren değişiklikleri ayırır:

```text
Mevcut tasarım içinde düzeni ve metni düzeltebilirsin.
Yeni ücretli servis, veri kaybı veya farklı görsel yön gerektiren kararda
seçenekleri ve önerini getir. Diğer yetkili işleri tamamla.
```

Bu yaklaşım, ajanın her satırda onay istemesine de bütün ürünü yeniden kurmasına da kapı açmaz. Yetki sınırını işin etkisine göre seç. Basit düzeltmeyi ilgisiz yasaklarla ağırlaştırma.

<a id="bir-ust-duzey-soru-dogru-isi-mi-istiyorsun"></a>

## Bir üst düzey soru: doğru işi mi istiyorsun?

“Bana bir dashboard yap” talebinin arkasında haftalık toplantıda karar verebilmek olabilir. Dashboard için gerekli veri yoksa ilk iş veri sahiplerini belirlemek veya küçük bir rapor hazırlamak olabilir. Codex'ten çözüm önerisini problemle birlikte sorgulamasını isteyebilirsin:

```text
İstediğim çözümün hangi problemi çözdüğünü çıkar.
Daha küçük bir çözüm aynı sonucu sağlıyorsa karşılaştır.
Önerini mevcut malzemeye dayandır; yeni ihtiyaç uydurma.
```

Bir fikir eleştirisi uygulama yetkisi vermez. Karar netleşince üretim isteğine dönmek, analizin sonsuza kadar sürmesini önler.

<a id="kucuk-ornekle-yontemi-netlestir-sonra-genislet"></a>

## Küçük örnekle yöntemi netleştir, sonra genişlet

200 kayda uygulanacak bir dönüşümde önce zor örnekleri seç: aynı isimli farklı kayıt, boş tutar veya sıra dışı sayı biçimi. Kural bu örneklerde doğruysa bütün tabloya yay. Tek bir yazım hatası için böyle bir ara aşama gerekmeyebilir.

[Altı kayıtlık rapor örneğinde](is-veri.md) bu kararın sonucunu görebilirsin: kayıt kimliği korunuyor, boş tutar sıfıra dönüşmüyor, “bilinen tahsilat” ile “tam toplam” ayrılıyor. Yöntem sabitlenince tekrarlı dönüşümü bir betiğe taşımak daha tutarlı olabilir.

<a id="i-yi-bir-revizyon-korunacak-kismi-da-soyler"></a>

## İyi bir revizyon, korunacak kısmı da söyler

“Daha iyi yap” yerine değişecek boyutu belirt: “İlk paragrafı yarıya indir; iddiaları, bağlantıları ve belirsizlik ifadelerini koru.” Görselde “üst boşluğu azalt; yazı tipi, renk ve içerik sırası aynı kalsın” de. Bu, memnun olduğun parçaların her turda yeniden tasarlanmasını azaltır.

Beklentiyi yanlış anlamışsa kelimeleri çoğaltmak yerine amaç farkını düzelt: “Ben dosya oluşturmanı değil, mevcut dosyadaki iki çelişkiyi bulmanı istiyorum.” Bu tür yön düzeltmeleri [iş sürerken yönetim bölümünde](05-yonetmek.md) devam ediyor.


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [3.1 İşe başlamadan bitişi tanımla.](../codex-kontrol-listesi.md#m-3-1)
- [3.2 Kabul koşulunu gözlenebilir davranış olarak yaz.](../codex-kontrol-listesi.md#m-3-2)
- [3.3 Belirsiz büyük işte plan, küçük düzeltmede uygulama iste.](../codex-kontrol-listesi.md#m-3-3)
- [3.4 Sınırları ve korunacak davranışı belirt.](../codex-kontrol-listesi.md#m-3-4)
- [3.5 İstenen sonuca bir örnek ve karşı örnek ver.](../codex-kontrol-listesi.md#m-3-5)
- [3.6 Gerekli soruda öneri ve gerekçe iste.](../codex-kontrol-listesi.md#m-3-6)
- [3.7 Uzun brief’te boşluk ve çelişkiyi erken buldur.](../codex-kontrol-listesi.md#m-3-7)
- [4.1 “İyi” kelimesini somut özelliklerle aç.](../codex-kontrol-listesi.md#m-4-1)
- [4.2 Okuru, yüzeyi ve verilecek kararı söyle.](../codex-kontrol-listesi.md#m-4-2)
- [4.3 Ayrıntıyı değerle ilişkilendir.](../codex-kontrol-listesi.md#m-4-3)
- [4.4 Tekrarlanan çıktıya alan şablonu ver.](../codex-kontrol-listesi.md#m-4-4)

[İçindekiler](README.md) · [← Codex gerçekte nasıl çalışıyor?](03-calisma-mantigi.md) · [İş sürerken yönü yönetmek →](05-yonetmek.md)
