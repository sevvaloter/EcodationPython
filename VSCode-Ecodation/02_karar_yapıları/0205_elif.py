# elif bloğu koşul sağlanmadığında diğer koşullara da bakılmasını sağlar.
# region ornek
"""
havaDurumu= "serin"
if havaDurumu== "yağmurlu":
    print("Şemsiye almalısın.")
elif havaDurumu== "sıcak":
    print("Hava sıcak Güneş kremi al.")
else:
    print("Hava normal.")
print("?")
"""
# endregion

# nested if
# region ornek_1
"""
havaYagisliMi = False
havaSogukMu = True
i = 1
print("a")
if havaYagisliMi == True:
    if havaSogukMu == True:
        print("b")
    else:
        print("c")
else:
    if i == 0:
        print("d")
    else:
        print("e")
print("f")
"""
# endregion
# region ornek_2
"""
+   kullanıcı değer girecek
+   int dönüşümü yapılacak
+   kullanıcı 0 yada negatif değer girmemeli
+   0-100 arası yada 100+ olup/olmadığını bulan prog.
+   ekrana kullanıcı dostu çıktı verecek

sayı = int(input("Lütfen sayı griniz:\t "))
if sayı > 0:
    if sayı > 100:
        print(f" {sayı} sayısı 100 den büyüktür.")
    else:
        print(f" {sayı} sayısı 100 den küçüktür.")
else:
    print("Lütfen negatif veya sıfır değer girmeyiniz.")
"""
# endregion
