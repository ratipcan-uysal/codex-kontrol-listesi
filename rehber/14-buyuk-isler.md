# 14. Büyük işleri ve paralel çalışmayı yönetmek

İçerik güncellemesi: 2026-10-31. Kaynak kontrol tarihleri kaynak dizinindedir.

Büyük işi parçalamak, bütün dosyaları eşit gruplara ayırmak değildir. Parçalar ayrı sonuç üretebilmeli ve bir araya geldiklerinde aynı hedefe hizmet etmelidir.

<a id="bagimsizligi-sonuc-uzerinden-olc"></a>

## Bağımsızlığı sonuç üzerinden ölç

Atölye sitesi için kaynak araştırması ile mevcut arayüzün erişilebilirlik incelemesi bağımsız ilerleyebilir. Aynı sayfanın başlığını, düzenini ve CSS'ini üç ayrı çalışmanın eşzamanlı değiştirmesi ise yoğun koordinasyon ister.

Her parçaya bir çıktı ve sınır ver: “Kaynak iddialarını kontrol et, kodu değiştirme” veya “Yalnız arama davranışını düzelt, içerik metnini değiştirme.” Entegrasyonu kimin yapacağı da belli olsun. Farklı çalışmaların çıktılarını birleştirmek ayrı iştir; son doğrulamanın sahibi gerekir.

İşi bölmeden önce [Atölye'nin tarih değişikliğindeki etki tablosunu](05-yonetmek.md#bir-degisiklik-nerelere-yayiliyor) kullan: aynı kaynağa bağlı dosyalar ve dış kayıtlar görünür olsun. Böylece iki çalışmanın aynı tarihi farklı yerlerde değiştirmesinden doğacak tutarsızlığı erken fark edersin.

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

<a id="buyuk-donusumde-ayni-girdiyi-iki-surumde-calistir"></a>

## Büyük dönüşümde aynı girdiyi iki sürümde çalıştır

Bir sistemi yeniden yazarken önce sınırlı bir kullanıcı akışı seç. Eski ve yeni sürüme aynı girdiyi ver; hangi çıktıların eşleşmesi, hangi farkların kabul edilmesi gerektiğini belirle. Bu, davranış eşliğini sınamaktır. [Modernizasyon örneği](https://developers.openai.com/cookbook/examples/codex/code_modernization)

**Bu rehbere uyarlanmış kurgu:** İçeriği HTML’ye dönüştüren üreticiyi değiştireceğiz. “Yeni sayfa açılıyor” tek başına kabul ölçütü olamaz.

| Ortak girdi | Korunacak sonuç | Ayrı kararla değişebilecek yön |
|---|---|---|
| Aynı 107 kontrol maddesi | Madde kimlikleri ve bağlantı hedefleri | Yazı tipi ve boşluklar |
| Eski işaret yedeği | İşaretlerin aynı maddelere yüklenmesi | İşaret sayacının görünümü |
| Aynı rehber metni | Bölüm sırası ve eski çapalar | Sayfa düzeni |

> Önce tek bir bölümle eski ve yeni üreticiyi aynı girdide karşılaştır. Farkları içerik, kimlik/bağlantı ve görünüm olarak ayır. Kabul edilmeyen farkları düzeltmeden tüm rehbere yayma.

Bu örnekte gerçek bir üretici geçişi yapılmıyor. Eski sürümün hatalı davranışını da körlemesine korumak gerekmez: düzeltilecek hata ayrı karar olsun, bilinçli değişiklik ile kazara kayıp birbirine karışmasın. Bu son ayrım bizim uygulama önerimizdir.

<a id="goals-ne-zaman-yararli"></a>

## Goals ne zaman yararlı?

**Bitiş noktası belli, fakat sonraki adım denemeden öğrenilecekse** Goals yararlıdır. Tek satır düzeltme için normal istek yeterlidir. Hata araştırması veya ölçüme göre ilerleyen iyileştirmede hedef birkaç tur boyunca korunur. [Hedef yazma kılavuzu](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)

<a id="hedefi-hazirlamak-ile-baslatmak"></a>

### Hedefi hazırlamak ile başlatmak

Önce `/plan` ile hedefi netleştir; ardından desteklenen masaüstü istemcisinde `/goal` ile başlat. Şu doğal dil isteği yalnız taslak içindir:

> Bu işi bir hedef taslağına dönüştür; henüz Goals başlatma. Başarı kanıtını, korunacak koşulları ve ilerlemeyi engelleyecek eksikleri belirle.

Hedefi çalıştırmadan önce sonucu ve kapsamını oku. Menüde görünen seçenekler hesap ve ortama göre değişebilir. [Masaüstü Goals](https://learn.chatgpt.com/docs/reference/slash-commands)

<a id="alti-parcayi-tek-ornekte-gor"></a>

### Altı parçayı tek örnekte gör

**Kurgu eğitim örneği:** Bu rehberin iç bağlantılarında hatalar bulunduğunu varsayalım. Aşağıdaki tablo, Cookbook’taki hedef yazma yaklaşımının bu işe uyarlamasıdır; yapılmış bir hata araştırmasının kaydı değildir.

| Parça | Bu işte ne yazılır? |
|---|---|
| Sonuç | Bozuk iç bağlantılar giderilsin. |
| Kanıt | Bağlantı denetimi geçsin; HTML ve Markdown hedefleri bulunsun. |
| Korunacak koşul | 107 madde, mevcut çapalar ve kullanıcı işaretleri korunsun. |
| Çalışma sınırı | Bu depo içinde çalış; dış siteleri değiştirme, yayın yapma. |
| Denemeler arasında seçim | Hata çıktısını oku; sonraki düzeltmeyi kalan hatanın nedenine göre seç. |
| Engel halinde teslim | İlerleyemediğin noktayı, denediğin yolları ve gereken bilgi veya erişimi bildir. |

**Zayıf istek:** “Bağlantıları düzelt, bitene kadar devam et.”

**Daha güçlü hedef metni:**

> Bu rehberdeki bozuk iç bağlantıları gider. Bağlantı denetimini çalıştır; HTML ve Markdown hedeflerini doğrula. 107 maddeyi, mevcut çapaları ve kullanıcı işaretlerini koru. Yalnız bu depoda çalış, yayın yapma. Her başarısız kontrolde hata çıktısına göre sonraki düzeltmeyi seç. Erişemediğin dış bağlantıyı bozuk sayma; ayrı raporla. Mevcut sınırlar içinde ilerleme yolu kalmazsa denediklerini ve işi açacak bilgi ya da erişimi bildir.

Burada “devam et” sözüne **bir seçim kuralı** eklendi. Örneğin bağlantı dosyası varsa ama başlık çapası yoksa dosyayı yeniden üretmek tek başına çözüm değildir. Yeni deneme, önceki kontrolün gösterdiği eksikliği hedeflemeli. Aynı başarısız işlemi açıklamasız tekrarlamak ilerleme sayılmaz.

**Goal karar akışı: çalış → kontrol et → sonuca göre ilerle**

1. **Çalış:** Kanıta dayanan bir sonraki adımı uygula.
2. **Kontrol et:** Hedef sağlandı ve koruma koşulları geçti mi?
3. **Karar ver:** Evet → tamamla. Hayır, geçerli yol var → yeni denemeye dön.
4. **Engeli bildir:** Geçerli yol kalmadıysa eksik bilgi veya erişimi yaz. Bütçe bittiyse ilerlemeyi özetle; başarı ilan etme.

<a id="hedef-neden-durmus-olabilir"></a>

### Hedef neden durmuş olabilir?

Goal, ilgili sohbetin kalıcı durumudur; global bellek veya proje talimatı değildir. Otomatik devam için hedef etkin, sohbet boşta ve bütçe uygun olmalıdır. Bekleyen kullanıcı mesajı veya başka iş varken aynı anda yeni devam turu başlamaz. Bütçe tükenmesi başarı anlamına gelmez. [Goals çalışma koşulları](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)

![Mesaj alanının üstünde hedef denetimleri. Paused goal satırı duraklamış hedefi gösteriyor. Sağdaki denetimlerle hedefi düzenleme, sürdürme veya temizleme işlemlerine ulaşılır; bunlar yeni slash komutları değildir.](assets/goal.png)

**Mesaj alanının üstünde hedef denetimleri.** Paused goal satırı duraklamış hedefi gösteriyor. Sağdaki denetimlerle hedefi düzenleme, sürdürme veya temizleme işlemlerine ulaşılır; bunlar yeni slash komutları değildir. [Tam boyut](assets/goal.png) · OpenAI’nin resmî arayüz gösterimi · [Kaynak](https://learn.chatgpt.com/docs/reference/slash-commands) · 2026-10-29.

1. **Nereye bak:** Mesaj alanının üstündeki Paused goal satırına.
2. **Ne yap:** Hedef aynıysa sürdür; değiştiyse önce hedef metnini düzelt.
3. **Ne gör:** Etkin hedef ile yapmak istediğin iş aynı kapsamı taşır.

**Paused goal** duraklamayı gösterir. Masaüstündeki ilerleme satırından duraklat, sürdür, düzenle veya temizle; Cookbook’taki CLI alt komutlarını masaüstüne aynen taşıma. Çalışırken ek mesajlarla yön verebilir, kavram sorusunu `/side` ile ayırabilirsin. [Masaüstü denetimleri](https://learn.chatgpt.com/docs/reference/slash-commands)

Hedef oluşturmak erişim izinlerini genişletmez. Belirli saatte yeniden çalışma ise [otomasyon](15-otomasyon.md) konusudur. [Uzun işler](https://learn.chatgpt.com/docs/long-running-work)

<a id="arastirmada-bitis-iddia-basina-kanit"></a>

### Araştırmada bitiş: iddia başına kanıt

Araştırma hedefinde tek bir başarı etiketi yerine doğrulanan, yaklaşık desteklenen, eksik veriyle engellenen ve belirsiz kalan iddiaları ayır. Benzer bir sonuç elde etmek, özgün deneyi aynen tekrarlamak anlamına gelmez. [Araştırma örneği](https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex)

Bizim [araştırmadan karara](is-arastirma.md) örneğimizde şu teslim isteği kullanılabilir: “Her seçenek için iddiayı, dayandığı kaydı, kanıt durumunu ve açık soruyu göster. Kaynakta bulunmayan ücreti tahminle doldurma.” Bu, eksik bilgi yüzünden bütün araştırmayı çöpe atmadan hangi karara güvenilebildiğini gösterir. Genel kaynak ve kanıt ayrımı [doğrulama bölümünde](12-dogrulama.md) açıklanır.

<a id="kurgu-senaryo-paralelligin-faydasiz-oldugu-is"></a>

## Kurgu senaryo: paralelliğin faydasız olduğu iş

Tek paragrafı üç ajana bölmek gereksiz koordinasyon yaratabilir.

<a id="i-ki-bulgudan-tek-karara"></a>

## İki bulgudan tek karara

Aynı Atölye kararında bir alt iş zorunlu koşulları, diğeri listelenen maliyetleri incelesin.

| Ayrı bulgu | Tek başına çıkarılabilecek yanlış karar | Birleştirilmiş karar |
|---|---|---|
| Koşul incelemesi: yalnız B hem hesapsız kayıt hem CSV sunuyor | Maliyeti hiç sorgulamamak | B koşulları karşılıyor; ek ücret henüz bilinmiyor |
| Maliyet incelemesi: C, B’den 800 TL ucuz | C’yi doğrudan seçmek | C zorunlu hesap koşuluna takılıyor |

İki alt iş aynı kaynak paketini kullanır, ana sorumlu eleme ölçütünü koruyarak tek öneri yazar. Bu tablo kurgu çıktıları birleştirmeyi öğretir; ölçülmüş süre kazancı veya gerçekten çalıştırılmış alt ajan kaydı değildir. [Başlangıç kaynakları](is-arastirma.md#2-kaynak-yiginini-karsilastirilabilir-kanita-donustur)

<a id="bu-is-gercekten-paralellik-gerektiriyor-mu"></a>

## Bu iş gerçekten paralellik gerektiriyor mu?

Yukarıdaki küçük örnek tek sohbetle de çözülebilir. Daha büyük bir işte bağımsız kanıt veya ayrı çıktı gerekiyorsa aynı paylaşımı kullan. Ajan sayısı yerine hangi alt sonucun tek başına incelenebileceğine bak; birleşmiş sonucun kontrolü ana sorumluda kalsın.


**Eğitimde sıradaki:** [Yöntemi tekrar eden işe dönüştür](15-otomasyon.md)


<a id="kontrol-listesinde-karsiligi"></a>

## Kontrol listesinde karşılığı

- [11.4 Ağır iş sayısını makinenin durumuna göre sınırla.](../codex-kontrol-listesi.md#m-11-4)
- [11.6 Ajan sayısını bağımsız iş miktarıyla sınırla.](../codex-kontrol-listesi.md#m-11-6)
- [13.1 Sen yokken hangi kararın verilebileceğini yaz.](../codex-kontrol-listesi.md#m-13-1)

[İçindekiler](README.md) · [← Tasarım ve yaratıcı üretim](13-tasarim.md) · [Otomasyon ve tekrar eden işler →](15-otomasyon.md)
