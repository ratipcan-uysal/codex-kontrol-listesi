# Yapılandırılmış çıktı örneği

Madde 14.6 için `schema.json`, Codex’e verilebilecek küçük bir çıktı sözleşmesidir.
Dosyayı inceleyeceğin projenin köküne kopyaladıktan sonra o dizinde çalıştır:

```sh
codex exec --sandbox read-only --output-schema schema.json -o sonuc.json "Proje adını, belgelenmiş test komutunu ve dayandığın dosyaları çıkar. Test komutu bulunmuyorsa null yaz. Komut çalıştırma."
python3 -m json.tool sonuc.json
```

`json.tool` yalnız JSON sözdizimini denetler; şema ve içerik doğruluğunu kanıtlamaz.
Alan türlerini şema doğrulayıcında, test komutunu ve dosya adlarını gerçek kaynakta
ayrıca kontrol et. Örnek canlı model koşumu bu yayında çalıştırılmadı (`NOT_RUN`).
