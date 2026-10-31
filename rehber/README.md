# Codex’i Derinlemesine Kullanma Rehberi

Codex ile iyi çalışmak, hangi komutun nerede olduğunu bilmenin ötesine geçiyor. Bir araştırmanın yanlış ölçütle sıralandığını, bir tablonun bilinmeyeni sıfıra çevirdiğini veya görsel sorunun yanlış katmanda çözüldüğünü fark edebilmek sonucu değiştiriyor. Bu eğitim, o kararları görünür kılıyor.

<a id="uc-isi-bastan-sona-izle"></a>

## Üç işi baştan sona izle

Bu üç örnek eğitim anlatısının ana yolu. Her birinde girdi, istek, ara çıktı, düzeltme ve teslim var. Kurgu verileri ve örnek dosyaları anlatıcı açıp gösterebilir; dinleyicinin kurulum yapması, alıştırma çözmesi veya komut ezberlemesi gerekmez.

1. [Araştırmadan karar ve sunuma](is-arastirma.md): seçenekleri doğru ölçütle ele, kararı gerekçelendir, doğrulanmış bilgiden yeni çıktılar üret.
2. [Dağınık tablodan güvenilir rapora](is-veri.md): kimliği koru, eksik veriyi görünür tut, bir sayının neyi anlattığını doğru adlandır.
3. [Görsel sorundan doğrulanmış yayına](is-sayfa.md): bölgeyi işaretle, yalnız gereken boyutu düzelt, aynı koşulda kontrol et ve gerçek hedefte bitir.

Uygulamayı ilk kez açıyorsan önce [ilk dosyayı üretme yolunu](02-uygulama.md#i-lk-dosyani-uret-ac-duzelt) gör. Sonra bu üç işe dön. Her örneğin içindeki bağlantılar, ihtiyaç duyulduğu anda ilgili özelliği açıyor.

<a id="once-hangi-bes-karari-ogrenmelisin"></a>

## Önce hangi beş kararı öğrenmelisin?

| Karar | Çalışırken söyleyebileceğin şey | Neden değerli? |
|---|---|---|
| Hangi sonuç gerekiyor? | “Karar notu ve düzenlenebilir sunum gerekiyor.” | İş, yalnız sohbet cevabında kalmaz |
| Hangi bilgi esas? | “Bu onaylı not ana kaynak; yeni iddia ekleme.” | Biçim değişirken anlam korunur |
| Ne değişecek, ne kalacak? | “Yalnız kart genişliği değişsin; metin ve renk aynı kalsın.” | İyi çalışan parçalar yeniden açılmaz |
| Nerede belirsizlik var? | “Boş tahsilatı sıfır sayma; ayrı göster.” | Güzel görünen sonuç yanlış kesinlik üretmez |
| Ne zaman tamamlandı? | “Son dosyayı aç; yayın istediysem canlı hedefi de kontrol et.” | Ara adım son teslimle karışmaz |

<a id="bizim-deneyimlerimiz-bu-anlatida-nerede"></a>

## Bizim deneyimlerimiz bu anlatıda nerede?

[Dokuz gerçek vaka](deneyimler.md), gözlenen sorun ile müdahalenin neyi değiştirdiğini ayırıyor. Kullanıcının düzeltmesi kayıtlıysa anlatılıyor. Yalnız inceleme bulgusu varsa ona sonradan konuşma uydurulmuyor. Örneğin uygulama bulma vakasında müdahale, yeniden derlemeyi başlatmadı; “uygulama yok” iddiasının kapsamını düzeltti. Bu küçük ayrım, eğitimde doğru neden–sonuç kurmanın bir parçası.

<a id="egitim-yolu-ve-basvuru-rehberi-birlikte-nasil-kullanilir"></a>

## Eğitim yolu ve başvuru rehberi birlikte nasıl kullanılır?

Eğitimde aşağıdaki rotayı izle; 18 bölüm, ihtiyaç duyduğun anda açacağın başvuru kaynağıdır. Üç örnekten sonra bölüm 1’den yeniden başlaman gerekmez. Başlangıçta talimat dosyası, MCP, hook veya otomasyon kurman gerekmiyor. Tekrarlanan bir ihtiyaç ortaya çıktığında ilgili bölüm değer kazanır. [Komutlar](komutlar.md), [sorun giderme](sorun-giderme.md) ve 107 maddelik kontrol listesi iş sırasında hızlı başvuru için duruyor.

**İçerik güncellemesi: 31 Ekim 2026.** Kaynakların kendi kontrol tarihleri kaynak dizininde yer alır. Ürün bilgisi resmî kaynaklara, gerçek vakalar seçili kayıtlara dayanır. Üç örneğin verileri kurgu; mini web sayfaları bu rehber için üretildi. Resmî uygulama görselleri ile örnek HTML'nin gerçek tarayıcı görüntüleri ayrı etiketlidir. Görsellerin altındaki “Nereye bak / Ne yap / Ne gör” açıklamaları öğretim yorumumuzdur. Erişim koşulları ve doğrulama sınırları [kaynaklarda](kaynaklar.md).


<a id="anlaticinin-tek-rotasi"></a>

## Anlatıcının tek rotası

İlk dosya → araştırma ve sunum → veri ve grafik → sayfa düzeltmesi → skill → devir → worktree → paralel iş → otomasyon → yöntemi iyileştirme. Her sayfanın sonundaki **Eğitimde sıradaki** bağlantısı bu yolu izler. Numaralı konu rehberi ayrı başvuru sırasını korur.

Anlatıcı örnek dosyaları açar, bir kararın çıktıyı nasıl değiştirdiğini gösterir ve devam eder. Dinleyiciden kurulum veya alıştırma beklenmez. Platform ayrıntıları, komut envanteri ve teknik ekler soru geldiğinde açılabilir.

<a id="tam-icindekiler"></a>

## Tam içindekiler

1. [Codex ile neler yapabilirsin?](01-olanaklar.md)
2. [Uygulamanın tamamını tanımak](02-uygulama.md)
3. [Codex gerçekte nasıl çalışıyor?](03-calisma-mantigi.md)
4. [İş vermenin incelikleri](04-is-vermek.md)
5. [İş sürerken yönü yönetmek](05-yonetmek.md)
6. [Bağlam, bellek ve devamlılık](06-baglam-bellek.md)
7. [Model, düşünme seviyesi, hız ve kullanım](07-model-hiz-kullanim.md)
8. [Dosyalar ve çalışma ortamları](08-ortamlar.md)
9. [İnternet, tarayıcı ve bilgisayar kullanımı](09-web-tarayici-bilgisayar.md)
10. [Bağlantılar, MCP, plugin ve skill](10-baglantilar-skills.md)
11. [Talimatları ve kişisel çalışma düzenini kurmak](11-talimatlar.md)
12. [Güvenilir sonuç elde etmek](12-dogrulama.md)
13. [Tasarım ve yaratıcı üretim](13-tasarim.md)
14. [Büyük işleri ve paralel çalışmayı yönetmek](14-buyuk-isler.md)
15. [Otomasyon ve tekrar eden işler](15-otomasyon.md)
16. [İzinler, gizlilik ve güvenlik](16-izinler-guvenlik.md)
17. [Teslim, yayın ve geri dönüş](17-teslim-yayin.md)
18. [Kendi kullanımını sürekli iyileştirmek](18-iyilestirmek.md)

<a id="ekler-ve-hizli-erisim"></a>

## Ekler ve hızlı erişim

- [Komutlar ve kısayollar](komutlar.md)
- [Gerçek deneyimlerden dokuz ders](deneyimler.md)
- [On iki kurgu kullanım senaryosu](senaryolar.md)
- [Sade terimler sözlüğü](sozluk.md)
- [Sorun giderme tablosu](sorun-giderme.md)
- [İleri teknik ayrıntılar](ileri-teknik.md)
- [84 özellik ailesinin kapsam envanteri](kapsam.md)
- [107 maddenin rehberle eşlemesi](esleme.md)
- [Kaynaklar, kanıt türleri ve güncellik](kaynaklar.md)

[107 maddelik hızlı kontrol listesine dön](../codex-kontrol-listesi.md) · [Tek dosyada rehberi indir](tam-rehber.md)