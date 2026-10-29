# İlk canlı dosya karşılaştırması

30 Ekim 2026: Pages içerik commit’i için built döndükten sonraki ilk paralel dosya indirmesi `urllib.error.HTTPError: HTTP Error 503: Service Unavailable` ile durdu. Tam dosya listesi bitmedi; başarısız isteğin dosya adı ilk traceback içinde yoktu. Bu koşum yayın eşliği kanıtı sayılmadı. HTTP 429/502/503/504 yanıtlarına en çok üç denemelik beklemeli yeniden deneme eklendi. Sonraki tamamlanmış karşılaştırma live-publication.json içinde; yeniden deneme kodları dosya bazında saklanır. Hatanın kök nedeni doğrulanmadı.
