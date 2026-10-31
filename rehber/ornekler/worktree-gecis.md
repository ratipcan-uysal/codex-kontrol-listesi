# Kurgu worktree geçiş kaydı

| Alan | Ana çalışma | Ayrı deneme |
|---|---|---|
| Dosya alanı | atolye/ | atolye-deneme/ |
| İş | Kullanıcı program metnini düzenliyor | Kart genişliği düzeltmesi |
| Fark | program.md tarih değişikliği | sayfa.css: 440px → 100% |
| Önizleme | Ana klasörden çalışan sunucu | Deneme klasöründen çalışan sunucu |

Bunlar gerçek makine yolu veya çalıştırılmış geçiş kaydı değildir. Desteklenen Hand off akışında önce yerel değişiklikler incelenir. Çatışma varsa iki taraf açıklanır; program.md sessizce geri alınmaz. Geçişten sonra ana klasördeki sayfa açılır, kart ve tarih birlikte kontrol edilir. Ayrı çalışma kopyasını arşivlemek, başka sistemdeki gönderimi geri almaz.
