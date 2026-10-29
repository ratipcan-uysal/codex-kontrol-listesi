# Cookbook derslerinin rehbere yerleştirilmesi — 30 Ekim 2026

Goals dışındaki sekiz Codex konu yazısı mevcut rehberle karşılaştırıldı. Altı eksik ders mevcut bölümlere işlendi; yeni bir ana bölüm veya alıştırma dizisi açılmadı.

| Ders | Yer ve somut örnek | Kaynak anahtarı |
|---|---|---|
| Araç çıktısı, araç seçimi ve son cevap ayrı doğrulanır | Bölüm 10; kurgu takvim saatinin cevapta yanlış aktarılması | cb-plugin-evals |
| Kullanıcı düzeltmesi tekrar sınanabilir kabul örneğine dönüşür | Bölüm 18; mevcut kurgu CSV'deki boş tahsilatı koruyan kontrol kartı | cb-improvement |
| Onarım, işin asıl amacını korumalı | Bölüm 12; CSV okumasını kaldırarak geçen çalışmanın neden yeterli olmadığı | cb-repair |
| Yeniden yazımda davranış karşılaştırılır | Bölüm 14; aynı 107 maddeyle eski/yeni üretici karşılaştırması, kurgu dönüşüm | cb-modernization |
| Toplam başarı puanı değişen hataları gizleyebilir | Bölüm 18; aynı 2/3 puana ulaşan farklı hata kümeleri, kurgu ölçüm | cb-plugin-evals |
| Görselin yeniden kullanımı ile sayısal doğruluğu farklı ihtiyaçlardır | Bölüm 13; katmanlı kampanya varlıkları ve veriden üretilen grafik | cb-transparent |

Bölüm 11'de PLANS.md / GOALS.md gibi dosya adlarının komut olmadığı açıklandı (cb-workflows). İleri teknik ekte eski GitLab örneğinin güncellik ve hata durumları sınırı belirtildi (cb-gitlab). Eski modele/API'ye özgü prompting ayarları genel masaüstü kuralına dönüştürülmedi. Kaynak URL'leri ve kontrol tarihleri [kaynak dizininde](../../rehber/kaynaklar.md).

## Kanıt ve sınırlar

- 24 Python testi, JavaScript sözdizimi ve diff boşluk kontrolü geçti. [Koruma karşılaştırması](preservation.json): 107 maddenin bütün alanları, eşlemeler, 229 eski HTML çapası, görseller, akışlar ve indirilebilir örnekler aynı.
- [Yerel tarayıcı](guide/results.json): 21 mevcut rehber kontrolü + 12 yeni bölüm/ekran genişliği kontrolü = 33 PASS. Masaüstünde bölüm 14/18, 320 px ekranda bölüm 10/13 görüntüleri açılıp incelendi. Tablolar dar ekranda kendi alanlarında kaydırılır; sayfa yatay taşmaz.
- Son yerel tarayıcı koşumundan sonra yalnız kaynak dizinindeki tarih açıklaması ve manifest tarih alanları düzeltildi; 24 Python testi yeniden geçti. Değişmeyen ekran kanıtları bu metin düzeltmesi için tekrar üretilmedi. Canlı kontrol nihai çıktıyı kapsar.
- 15 görev süreci kapandı; yerel test sunucusu kapalı. [Temizlik](process-cleanup.json).
- 7 yeni kaynakla toplam 77 kaynak. Eski 70 kaynağın tarihleri değiştirilmedi. İçerik güncelleme tarihi kaynak inceleme tarihinden ayrıldı.
- Cookbook notebook/API/benchmark örnekleri çalıştırılmadı. Kurgu senaryolar gerçek kullanıcı oturumu veya başarı ölçümü değildir. Öğrenme etkisi ölçülmedi. Safari, Firefox, fiziksel cihaz ve VoiceOver bu revizyonda sınanmadı. Değişmeyen kontrol listesinin 28 ayrı etkileşim kontrolü yeniden koşulmadı.

Canlı yayın kanıtı, yayın tamamlandıktan sonra ayrı kaydedilir.
