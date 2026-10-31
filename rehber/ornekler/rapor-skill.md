---
name: atolye-raporu
description: Atölye katılım CSV dosyalarından kimliği ve eksik tahsilatı koruyarak haftalık rapor hazırla. Yalnız yazım düzeltmesi veya serbest etkinlik fikri için kullanma.
---

# Atölye raporu

1. Kaynak CSV'yi değiştirme; kayit_id ile kayıtları ayır.
2. Sayı biçimini düzelt; boş tahsilatı sıfıra veya bilet bedeline çevirme.
3. katıldı, iptal, bekliyor dışındaki durumları yeni durum olarak raporla; sessizce eşleme.
4. Bilinen tahsilat, eksik tahsilat kimlikleri ve durum dağılımını ayrı yaz.
5. Son raporu kaynakla kimlik ve değer bazında karşılaştır. Hedef hafta dosyası varsa yenile; ikinci kopya üretme.

Bu kurgu eğitim örneğidir. Kurulacak skill paketinde dosyanın adı SKILL.md olur. İndirmek otomatik kurulum veya hesap erişimi sağlamaz.
