# Erken ekran görüntüsü

Canlı 18 işlev kontrolü geçti; altı görselin decode ve yüklenme kontrolleri de bu koşumda geçti. Ancak daha sonra yeniden açılan uygulama bölümünün masaüstü ekran görüntüsü alınırken decode beklenmiyordu. Açılan görüntüde görsel alanı boştu; mobil görüntü ve tam boyut kontrolleri doluydu. Yakalama öncesine açık decode bekleme eklendi. Bu kayıt ilk kusurlu kanıtı korur; bütün kullanıcıların görsel göremediği iddiası değildir.
