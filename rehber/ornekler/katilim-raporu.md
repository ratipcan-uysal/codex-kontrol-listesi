# Kurgu katılım raporu

Kaynak: katilim-ham.csv. Sonuç: katilim-temiz.csv. Gerçek kişi veya tahsilat kaydı değildir.

- 6 kayıt ve 6 benzersiz kayit_id korunuyor.
- Durum: 3 katıldı, 2 iptal, 1 bekliyor.
- Bilinen tahsilat: 1.800 TL. Tam toplam henüz bilinmiyor.
- Eksik tahsilat: K04. Boş değer 0 veya 600 olarak doldurulmadı.
- K02 ve K03 aynı adla ayrı kayıtlar olarak korundu.
- K05 bekliyor durumunda olmasına rağmen 600 TL kayıtlı tahsilata sahip.

Bu örnek beklenen çıktı olarak hazırlanmıştır; gerçek otomasyon koşum kaydı değildir.
