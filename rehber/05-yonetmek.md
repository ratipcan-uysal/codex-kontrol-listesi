# 5. İş sürerken yönü yönetmek

Belge kontrolü: 2026-10-29.

İlk istek bütün kararları taşımaz. İyi bir çalışma, yeni bilgi geldiğinde yönünü değiştirebilir. Bunun için Codex'e yalnız memnuniyetsizliğini değil, hangi varsayımın değiştiğini söylemek gerekir.

## Ara mesajın etkisini bil

Settings → General → Follow-up behavior ayarı, iş sürerken gönderdiğin mesajın o işi yönlendirmesi veya sonraki tur için sıraya girmesi arasındaki tercihi belirler. Araç çağrısı çalışırken düzeltmenin etkisi bir sonraki uygun noktada görülebilir. Mesaj göndermek, başlamış bir dış işlemi geri almaz. [Mesaj davranışı](https://learn.chatgpt.com/docs/reference/settings)

Örneğin Codex Türkçe sayfayı düzeltirken “İngilizcesini de yap” dersen, bu kapsam genişlemesi olarak anlaşılabilir. Yalnız yanlış dosyayı açtığını fark ettiysen daha kesin bir düzeltme gerekir:

> Şu an yanlış dil dosyasındasın. Hedef Türkçe. İngilizce dosyada yaptığın değişiklikleri önce göster; bana ait önceki değişiklikleri koruyarak bu işe ait olanları geri al, sonra Türkçe dosyada devam et.

Bu istek önce hatanın etkisini belirletir. “Hepsini geri al” farklı bir yetki verir ve aynı klasördeki başka çalışmaları da riske atabilir.

## Tekrar yerine yeni bilgi ver

| Tıkanan konuşma | İlerleten düzeltme |
|---|---|
| “Daha iyi yap.” | “Başlık bilgi vermiyor. Sonucu ilk cümlede söyle; girişteki üç genel cümleyi çıkar.” |
| “Hâlâ çalışmıyor.” | “Mobilde ikinci kart açılınca yatay taşma oluşuyor. Masaüstünde görülmüyor.” |
| “Uygulama var, bul.” | “Daha önce bu projede paket üretip açtık. Kaynak, derleme ürünü ve çalışan süreç durumlarını ayrı kontrol et.” |
| “Devam et.” | “Son başarılı kontrolden devam et. Yeni hata çıkmadıkça geçen testleri tekrarlama.” |
| “Bana tekrar sorma.” | “Yerel ve geri alınabilir düzeltmeleri yapabilirsin. Dışarıya gönderim kararı bende.” |

Örnekler genel çalışma önerisidir. Son satır, uygulamanın teknik izinlerini değiştirmez; görev içindeki karar yetkisini açıklar.

## Gerçek deneyim: bulunamayan uygulama

Bir masaüstü projesinde ilk bakılan konumlarda uygulama paketi bulunamayınca, daha önce çalıştırılmış uygulamanın yokluğu izlenimi doğdu. Kullanıcının itirazı araştırmanın yönünü değiştirdi. Kaynak proje bulundu, Release derlemesi alındı ve uygulama süreci gözlendi. Pencerenin görünürlüğü ve yeni ses işlevlerinin testi ayrıca doğrulanmamıştı. Ders, bulunamayan dosyayla hiç üretilmemiş ürünü aynı sonuca bağlamamak. [Vaka C01](deneyimler.md#c01)

## Durmak, yeniden denemek ve kapsamı değiştirmek

Durdurma, o anda devam eden çalışmayı kesmek içindir. Değişmiş dosyaları veya yapılmış bir gönderimi kendiliğinden geri alacağını varsayma. Yeniden başlatırken “Nerede kaldık?” yerine eldeki durumu kullandır:

> Son yaptığın değişiklikleri ve açık işlemleri kontrol et. Geçerli kanıttan devam et; yarım kalan sunucu veya tarayıcı varsa aynı oturumu kullan. Hedef değişmedi.

Kapsam gerçekten değiştiyse bunu açıkça söyle: “Önceki web sitesi hedefini bırakıyoruz; yalnız içerik taslağı gerekiyor.” Böylece eski hedefi tamamlama çabası yeni isteğe karışmaz.

## Kurgu senaryo: yanlış çözümü erken yakalamak

Atölye sayfasında “Başvur” düğmesinin çalışmadığı söyleniyor. Codex formu yeniden yazmaya girişiyor. Sen hatanın yalnız giriş yapmamış kişilerde olduğunu fark ediyorsun:

> Formu yeniden yazmayı durdur. Sorun anonim ziyaretçi akışında. Mevcut yönlendirme ve erişim kontrolünü incele; hatayı açıklayan en küçük değişikliği öner ve uygula.

Beklenen değer, daha uzun bir talimat değil, yanlış problem tanımının düzeltilmesidir. Son kontrol de giriş yapmamış ziyaretçiyle yapılır.

[İçindekiler](README.md) · [← İş vermenin incelikleri](04-is-vermek.md) · [Bağlam, bellek ve devamlılık →](06-baglam-bellek.md)
