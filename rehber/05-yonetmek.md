# 5. İş sürerken yönü yönetmek

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

İlk istek bütün kararları taşımaz. İyi bir çalışma, yeni bilgi geldiğinde yönünü değiştirebilir. Bunun için Codex'e yalnız memnuniyetsizliğini değil, hangi varsayımın değiştiğini söylemek gerekir.

<a id="ara-mesajin-etkisini-bil"></a>

## Ara mesajın etkisini bil

Settings → General → Follow-up behavior ayarı, iş sürerken gönderdiğin mesajın o işi yönlendirmesi veya sonraki tur için sıraya girmesi arasındaki tercihi belirler. Araç çağrısı çalışırken düzeltmenin etkisi bir sonraki uygun noktada görülebilir. Mesaj göndermek, başlamış bir dış işlemi geri almaz. [Mesaj davranışı](https://learn.chatgpt.com/docs/reference/settings)

Örneğin Codex Türkçe sayfayı düzeltirken “İngilizcesini de yap” dersen, bu kapsam genişlemesi olarak anlaşılabilir. Yalnız yanlış dosyayı açtığını fark ettiysen daha kesin bir düzeltme gerekir:

> Şu an yanlış dil dosyasındasın. Hedef Türkçe. İngilizce dosyada yaptığın değişiklikleri önce göster; bana ait önceki değişiklikleri koruyarak bu işe ait olanları geri al, sonra Türkçe dosyada devam et.

Bu istek önce hatanın etkisini belirletir. “Hepsini geri al” farklı bir yetki verir ve aynı klasördeki başka çalışmaları da riske atabilir.

<a id="tekrar-yerine-yeni-bilgi-ver"></a>

## Tekrar yerine yeni bilgi ver

| Tıkanan konuşma | İlerleten düzeltme |
|---|---|
| “Daha iyi yap.” | “Başlık bilgi vermiyor. Sonucu ilk cümlede söyle; girişteki üç genel cümleyi çıkar.” |
| “Hâlâ çalışmıyor.” | “Mobilde ikinci kart açılınca yatay taşma oluşuyor. Masaüstünde görülmüyor.” |
| “Uygulama var, bul.” | “Daha önce bu projede paket üretip açtık. Kaynak, derleme ürünü ve çalışan süreç durumlarını ayrı kontrol et.” |
| “Devam et.” | “Son başarılı kontrolden devam et. Yeni hata çıkmadıkça geçen testleri tekrarlama.” |
| “Bana tekrar sorma.” | “Yerel ve geri alınabilir düzeltmeleri yapabilirsin. Dışarıya gönderim kararı bende.” |

Örnekler genel çalışma önerisidir. Son satır, uygulamanın teknik izinlerini değiştirmez; görev içindeki karar yetkisini açıklar.

<a id="gercek-deneyim-bulunamayan-uygulama"></a>

## Gerçek deneyim: bulunamayan uygulama

İlk bakılan konumlarda paket bulunamayınca “uygulama yok” izlenimi doğdu. Sen daha önce uygulamayı test ettiğimizi hatırlattın. Kayıt sırasını yeniden okuyunca önemli bir ayrım ortaya çıkıyor: yeniden derleme zaten başlamıştı. Müdahalen, araştırmayı başlatmak yerine benim iddiamı daralttı. Son rapor paket, çalışan süreç ve doğrulanmamış pencere/işlev durumlarını ayırdı. [Vakanın tam zinciri](deneyimler.md#c01)

Başka işte kullanacağın soru: “Bu sonuç yalnız baktığın yerde mi geçerli, yoksa bütün ürün hakkında mı?” Daha çok araştırma istemeden önce yanlış kesinliği düzeltebilirsin.

<a id="durmak-yeniden-denemek-ve-kapsami-degistirmek"></a>

## Durmak, yeniden denemek ve kapsamı değiştirmek

Durdurma, o anda devam eden çalışmayı kesmek içindir. Değişmiş dosyaları veya yapılmış bir gönderimi kendiliğinden geri alacağını varsayma. Yeniden başlatırken “Nerede kaldık?” yerine eldeki durumu kullandır:

> Son yaptığın değişiklikleri ve açık işlemleri kontrol et. Geçerli kanıttan devam et; yarım kalan sunucu veya tarayıcı varsa aynı oturumu kullan. Hedef değişmedi.

Kapsam gerçekten değiştiyse bunu açıkça söyle: “Önceki web sitesi hedefini bırakıyoruz; yalnız içerik taslağı gerekiyor.” Böylece eski hedefi tamamlama çabası yeni isteğe karışmaz.

<a id="bir-degisiklik-nerelere-yayiliyor"></a>

## Bir değişiklik nerelere yayılıyor?

**Atölye'nin kurgu devamı:** Ücretsiz Tanışma Buluşması 14 Kasım'dan 21 Kasım'a taşınacak. Ücretli Uygulama Programı’nın kayıtları bu değişikliğe dahil değil. Yalnız sayfa başlığını düzeltmek yeterli olmayabilir. Bir bilgi başka dosyalara kopyalanmış veya bir zamanlamada kullanılmışsa onları birlikte gör.

> Tarihi değiştirmeden önce 14 Kasım bilgisinin kullanıldığı yerleri ve ona bağlı işlemleri bul. Güncellenecek yerel dosyaları, dış kayıtları ve yalnız geçmiş olarak korunacak kayıtları ayır. Saati ve diğer onaylı bilgileri değiştirme.

| Bulunan yer | Gerekli karar | Son kontrol |
|---|---|---|
| Onaylı program ve ondan üretilen site | Kaynağı 21 Kasım yap, siteyi aynı kaynaktan güncelle | Kaynak ile açılan sayfa aynı tarihi gösteriyor mu? |
| Güncel sunum ve gönderilmemiş duyuru | İlgili tarihleri güncelle | İki çıktı da aynı etkinliği anlatıyor mu? |
| Kayıt formu ve planlanmış hatırlatma | Hedef kayıt ve tarih/saat dilimi doğrulansın; görev yetkisi kapsamında değiştirilsin | Dış sistemde kayıtlı yeni değer geri okundu mu? |
| Daha önce gönderilmiş duyuru veya geçmiş kayıt | Sessizce geçmişi yeniden yazma; düzeltme duyurusu gereğini belirt | Yeni taslak ile gerçekten gönderilmiş mesaj ayrılıyor mu? |

Burada önce/sonra farkı “bir metin değişti” ile “etkinliğin güncel tarihini taşıyan yerler tutarlı” arasındadır. Aynı tarih başka bir etkinliğe de ait olabilir; her eşleşmeyi topluca değiştirme. Erişilemeyen dış kayıt varsa bunu açık bırak, tamamını güncelledim deme.

<a id="kurgu-senaryo-yanlis-cozumu-erken-yakalamak"></a>

## Kurgu senaryo: yanlış çözümü erken yakalamak

Atölye sayfasında “Başvur” düğmesinin çalışmadığı söyleniyor. Codex formu yeniden yazmaya girişiyor. Sen hatanın yalnız giriş yapmamış kişilerde olduğunu fark ediyorsun:

> Formu yeniden yazmayı durdur. Sorun anonim ziyaretçi akışında. Mevcut yönlendirme ve erişim kontrolünü incele; hatayı açıklayan en küçük değişikliği öner ve uygula.

Beklenen değer, daha uzun bir talimat değil, yanlış problem tanımının düzeltilmesidir. Son kontrol de giriş yapmamış ziyaretçiyle yapılır.

<a id="ana-isi-kesmeden-bir-seyi-anlamak-side"></a>

## Ana işi kesmeden bir şeyi anlamak: /side

Uzun bir dönüşüm sürerken “worktree ne demek?” diye sormak isteyebilirsin. `/side`, ana işi kesmeden geçici bir yan sohbet açar. Kavram açıklaması veya yaklaşımı anlamak için kullan. Örneğin komutu listeden seçip “Bu işte neden ayrı çalışma kopyası kullanıyoruz? Dosyaları değiştirmeden açıkla” yazabilirsin.

Ana işin kapsamını değiştireceksen bunu ana sohbette söyle. Yan sorudan çıkan kararı oraya taşı. Ana görevin yanlış yolda olduğunu görüyorsan yan sohbet yerine ana işi yönlendir veya durdur. [Yan sohbet ve komutlar](https://learn.chatgpt.com/docs/reference/slash-commands)

[İçindekiler](README.md) · Konu sırasıyla oku: [← İş vermenin incelikleri](04-is-vermek.md) · [Bağlam, bellek ve devamlılık →](06-baglam-bellek.md)
