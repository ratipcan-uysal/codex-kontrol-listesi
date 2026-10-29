# 14. Büyük işleri ve paralel çalışmayı yönetmek

Belge kontrolü: 2026-10-29.

Büyük işi parçalamak, bütün dosyaları eşit gruplara ayırmak değildir. Parçalar ayrı sonuç üretebilmeli ve bir araya geldiklerinde aynı hedefe hizmet etmelidir.

<a id="bagimsizligi-sonuc-uzerinden-olc"></a>

## Bağımsızlığı sonuç üzerinden ölç

Atölye sitesi için kaynak araştırması ile mevcut arayüzün erişilebilirlik incelemesi bağımsız ilerleyebilir. Aynı sayfanın başlığını, düzenini ve CSS'ini üç ayrı çalışmanın eşzamanlı değiştirmesi ise yoğun koordinasyon ister.

Her parçaya bir çıktı ve sınır ver: “Kaynak iddialarını kontrol et, kodu değiştirme” veya “Yalnız arama davranışını düzelt, içerik metnini değiştirme.” Entegrasyonu kimin yapacağı da belli olsun. Farklı çalışmaların çıktılarını birleştirmek ayrı iştir; son doğrulamanın sahibi gerekir.

<a id="alt-ajan-ayri-sohbet-ve-worktree"></a>

## Alt ajan, ayrı sohbet ve worktree

**Alt ajan**, desteklenen istemcide ana görevin bir parçasını çalışan yardımcı ajandır. **Ayrı sohbet**, kullanıcı tarafından bağımsız takip edilen bir iş alanıdır. **Worktree**, dosya kopyasını yalıtır. Bunlar birbirinin yerine geçmez. Ayrı sohbet aynı klasöre yazabilir; alt ajan ortak dosyalarda çakışabilir. [Alt ajanlar](https://learn.chatgpt.com/docs/agent-configuration/subagents)

Alt ajan erişimi, mevcut çalışma politikasına ve kullanıcı yetkisine bağlıdır. Kullanılabilen model ve düşünme seviyeleri de istemciye bağlıdır. Yardımcıyı sırf ana model güçlü diye aynı ayara zorlamak yerine alt işin zorluğunu değerlendir. Sırf daha fazla ajan mümkün diye kullanmak gerekmez. Şu istek paralel çalışmayı açıkça tanımlar:

> Yetki veriyorum: kaynak doğrulaması ve erişilebilirlik incelemesini iki bağımsız alt işe ayır. İkisi de salt okuma yapsın. Bulguları sen birleştir; aynı sorunu iki kez raporlama.

Bu, yeni kullanıcı sohbetleri oluşturma talimatı değildir. Yeni sohbet gerekiyorsa ayrıca o sonuç için oluşturulmalıdır.

<a id="entegrasyon-neden-zorlasir"></a>

## Entegrasyon neden zorlaşır?

İki çalışma aynı kavrama farklı ad verir, biri eski dosyayı okur, diğeri farklı sürümde test yapar. “Her parça geçti” sonucu birleşmiş ürünün çalıştığını göstermez. Başlangıç sürümü, ortak veri sözleşmesi ve dokunulacak alanlar belirlenirse bu risk azalır.

Son aşamada değişikliklerin aynı kaynak üzerinde buluştuğunu kontrol et. Çelişen önerileri sessizce birleştirmek yerine hangisinin neden seçildiğini kaydet. Bağımsız incelemede kaynak değişiyorsa eski bulgunun hâlâ geçerli olup olmadığını yeniden değerlendir.

<a id="goals-ne-zaman-yararli"></a>

## Goals ne zaman yararlı?

Masaüstünde `/goal` ile başlatılan Goals, desteklenen Codex istemcisinde bir hedefin birkaç tur boyunca sürdürülmesi ve ilerleme durumunun takip edilmesi içindir. Normal istekten daha uzun devamlılık gerektiren işlerde anlamlıdır. Hedef, bitiş ölçütü ve varsa bütçe açık olmalı. Her masaüstü sürümünde aynı komut görünümünü varsayma; güncel istemci desteğini kontrol et. [Masaüstü Goals](https://learn.chatgpt.com/docs/reference/slash-commands) · [Hedef yazma kılavuzu](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)

> Hedef: bu deponun bozuk iç bağlantılarını gider ve üretim kontrolünü çalışır hâle getir. Başarı: bağlantı denetimi geçiyor ve ilgili içerik kaybolmuyor. Yayın yapma. Gerekli bir dış karar olmadan ilerleyemiyorsan bunu açıkça bildir.

Masaüstünde etkin hedefin üstündeki ilerleme denetimleriyle duraklatma, sürdürme, düzenleme ve temizleme yapılır. CLI kılavuzundaki alt komutları masaüstüne aynen taşımamak gerekir.

“Sınırsız devam et” iyi bir bitiş ölçütü değildir. Bütçenin bitmesi, hedefin tamamlanması ve kullanıcının durdurması ayrı durumlardır. Goals zamanlanmış otomasyon da değildir; belirli gün/saatte uyanma ihtiyacı 15. bölümün konusudur.

![Mesaj alanının üstünde hedef denetimleri. Paused goal satırı duraklamış hedefi gösteriyor. Sağdaki denetimlerle hedefi düzenleme, sürdürme veya temizleme işlemlerine ulaşılır; bunlar yeni slash komutları değildir.](assets/goal.png)

**Mesaj alanının üstünde hedef denetimleri.** Paused goal satırı duraklamış hedefi gösteriyor. Sağdaki denetimlerle hedefi düzenleme, sürdürme veya temizleme işlemlerine ulaşılır; bunlar yeni slash komutları değildir. [Tam boyut](assets/goal.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/reference/slash-commands) · 2026-10-29.

İlerleme satırında **Paused goal** yazıyorsa hedef duraklatılmıştır. Satırdaki sürdürme, düzenleme ve temizleme denetimleri hedefin yönetimi içindir. Hedef açıkken kavram sormak için `/side` kullanabilirsin. Bağlantının kesileceğini biliyorsan önceden duraklatmak ve devamda mevcut çıktıyı kontrol etmek yararlı olur. Hedef oluşturmak erişim izinlerini genişletmez. [Uzun işler](https://learn.chatgpt.com/docs/long-running-work)

<a id="kurgu-senaryo-paralelligin-faydasiz-oldugu-is"></a>

## Kurgu senaryo: paralelliğin faydasız olduğu iş

Tek paragrafın üslubunu düzeltmek için üç ajan kurmak, görev dağıtımı ve uzlaştırmayı asıl işten uzun hâle getirebilir. Aynı yazının kaynak doğrulaması, anlam kontrolü ve görsel yerleşimi ise yeterince büyükse ayrılabilir. Karar verirken ajan sayısına değil, bağımsız kanıt ve bağımsız çıktı ihtiyacına bak.

Teslimde yalnız yardımcıların özetlerini aktarma. Ana sorumlu, birleşmiş sonucun istenen hedefi karşıladığını ve hangi kontrollerin hâlâ yapılmadığını söylemeli.

<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [11.4 Ağır iş sayısını makinenin durumuna göre sınırla.](../codex-kontrol-listesi.md#m-11-4)
- [11.6 Ajan sayısını bağımsız iş miktarıyla sınırla.](../codex-kontrol-listesi.md#m-11-6)
- [13.1 Sen yokken hangi kararın verilebileceğini yaz.](../codex-kontrol-listesi.md#m-13-1)

[İçindekiler](README.md) · [← Tasarım ve yaratıcı üretim](13-tasarim.md) · [Otomasyon ve tekrar eden işler →](15-otomasyon.md)
