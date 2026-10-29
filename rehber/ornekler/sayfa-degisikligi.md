# Kurgu HTML örneği / kaynak farkı

İki dosya arasındaki tek metinsel fark `.event-card` genişliğidir:

```diff
-.event-card{width:440px;
+.event-card{width:100%;
```

Ana alan max-width:520px, iç boşluk 20px ve genel box-sizing:border-box kullanıyor. Bu koşullarda kart kapsayıcısına sığar. Metin, renk, tarih ve #program bağlantısı aynıdır. Evrensel taşma onarımı değildir.
