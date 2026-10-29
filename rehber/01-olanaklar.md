# 1. Codex ile neler yapabilirsin?

Belge kontrolü: 2026-10-29.

Codex ile çalışırken kazanacağın beceri, bir isteği güzel cümlelerle anlatmaktan daha geniş. Dosyayı bulmak, doğru ortamda çalışmak, bir fikri görünür çıktıya çevirmek ve sonucun gerçekten istediğin şey olup olmadığını anlamak aynı işin parçaları. Bu rehber bunları birlikte öğretiyor.

<a id="yapabileceklerini-cikti-uzerinden-dusun"></a>

## Yapabileceklerini çıktı üzerinden düşün

Codex araştırma yapabilir, kaynakları karşılaştırabilir, kod ve metin düzenleyebilir, dosya üretebilir ve mevcut araçları kullanarak sonucu kontrol edebilir. Hangi işin mümkün olduğu seçtiğin ortamın dosyalarına, araçlarına ve izinlerine bağlıdır. Uygulamada Codex'i seçmiş olmak her servise bağlandığın anlamına gelmez. [Ürün yüzeyleri](https://learn.chatgpt.com/docs/use-chatgpt)

| Elindeki malzeme | İsteyebileceğin sonuç | Sonuçta bakılacak şey |
|---|---|---|
| Dağınık toplantı notları | Kararlar ve açık sorular içeren kısa belge | Karar ile öneri karışmış mı? |
| Bir veri tablosu | Temizlenmiş kopya ve açıklamalı grafik | Satır kaybı, birim ve eksik değer davranışı |
| Çalışan bir uygulama | Tek hatanın onarımı | Aynı hata yeniden üretildi mi, düzeldi mi? |
| Kaynak makaleler | Atıflı karşılaştırma | Kaynak gerçekten ilgili iddiayı destekliyor mu? |
| Görsel referanslar | Karşılaştırılabilir tasarım adayları | Aynı içerikte ne değişiyor? |
| Tekrarlanan kontrol işi | Sonuç veren, sınırlı bir rutin | Çalıştı mı, ne zaman duracak? |

Tablo, her iş için hangi doğruluk ölçütünü belirlemen gerektiğini gösterir. Örneğin bir grafiğin açılması, verinin doğru işlendiğini kanıtlamaz.

<a id="i-lk-isi-nasil-secersin"></a>

## İlk işi nasıl seçersin?

İyi başlangıç işinde girdi erişilebilir, çıktı tanımlı ve düzeltme maliyeti düşüktür. Bir belgenin tutarsızlıklarını bulmak, mevcut sayfadaki taşmayı düzeltmek veya on kayıtlık örnekte veri temizleme yöntemi kurmak bu yüzden öğreticidir. Bir şirketin bütün operasyonunu otomatikleştirmek ise çok sayıda yetki, belirsizlik ve bağımlılığı aynı anda getirir.

İşi küçültmek değerini azaltmak zorunda değil. Bir müşteri kaydının baştan sona doğru aktarılması, yalnız güzel görünen on ekranın hazırlanmasından daha fazla şey doğrulayabilir. Sonraki genişleme için çalışan bir temel elde edersin.

<a id="kurgu-senaryo-atolye-adli-bir-ogrenme-toplulugu"></a>

## Kurgu senaryo: Atölye adlı bir öğrenme topluluğu

Bu rehberin bazı örneklerinde Atölye adlı hayalî bir topluluk kullanılıyor. Elinde etkinlik notları, katılımcı tablosu ve basit bir internet sitesi var. Bu örneklerde geçen dosyalar ve beklenen sonuçlar öğretim amacıyla kurgulandı. Gerçek müşteri veya ölçülmüş kazanç anlatılmıyor.

```text
Bu klasördeki etkinlik notlarından gelecek ayın program taslağını çıkar.
Yalnız notlarda kesinleşmiş oturumları programa al.
Tarih veya konuşmacı eksikse ayrı açık sorular listesine koy.
Sonucu düzenlenebilir bir belge olarak hazırla ve kullandığın kaynakları belirt.
```

Bu istek üç kararı birlikte veriyor: kaynak belli, taslağa girecek bilginin eşiği belli, eksik bilgiye davranış belli. Codex'in programı dolu göstermek için tarih uydurmasına gerek kalmıyor. İlk taslağı gördükten sonra yoğunluğu, sıralamayı veya dili değiştirebilirsin.

<a id="tek-ciktiyi-birkac-ise-donustur"></a>

## Tek çıktıyı birkaç işe dönüştür

Bir kaynak paketinden önce karar notu, sonra onaylı nottan sunum ve kısa duyuru ürettirebilirsin. Böylece her biçimde konuyu yeniden araştırmak yerine doğrulanmış bilgiyi kullanırsın. Yeni biçim yeni iddia gerektiriyorsa o boşluğu ayrıca araştırırsın.

> Önce kaynaklardan bir sayfalık karar notu çıkar. Ben bu notu onayladıktan sonra aynı bilgiyle beş slaytlık sunum ve 150 kelimelik duyuru hazırla. Her çıktıda tarih ve sayıları ana notla karşılaştır.

Bu, rehberin iş akışı önerisi. Kazanç yalnız yazma hızından gelmez: aynı kararın üç belgede farklı anlatılması da önlenir. Hangi dosyayı üreteceğini ve nerede açacağını [ilk iş akışında](02-uygulama.md#i-lk-dosyani-uret-ac-duzelt) görebilirsin.

<a id="i-yi-sonuc-icin-iki-ayri-karar-ver"></a>

## İyi sonuç için iki ayrı karar ver

Önce yapılacak işi seçersin. Sonucu bu seçime göre değerlendirirsin. Codex ilk kararı düşünmene de yardım eder. “Önce bu fikrin varsayımlarını eleştir” isteği, uygulamaya başlamadan yararlı olabilir. Fakat her küçük işte kapsamlı araştırma ve plan istemek de yük yaratır. İhtiyacın yalnız bir başlığın düzeltilmesiyse bunu doğrudan söyle.

Okurken her özelliği açmaya çalışma. Bir özelliğin hangi sorunu çözdüğünü öğrenmek, onu sürekli kullanmaktan daha değerlidir.

<a id="i-lk-calismada-akisi-gormek"></a>

## İlk çalışmada akışı görmek

Araştırmadan karar ve sunuma giden [tam örnek işte](is-arastirma.md), aynı doğrulanmış bilginin üç farklı çıktıda nasıl korunduğunu izle.

[İçindekiler](README.md) · [Uygulamanın tamamını tanımak →](02-uygulama.md)
