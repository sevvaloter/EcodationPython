# region giris
# loop
# loop ne zaman kullanılır?
# loop → sürekli tekrarlayan işlemlerin yapılmasını sağlayan komutlardır
"""
print("24 saatte kargoda")
print("24 saatte kargoda")
print("24 saatte kargoda")
i = 0
while i<1000:
    i +=1
    print("12 saatte kargoda")
"""
# endregion

# region aman_dikkat
"""
while True:
    print("şu an while döngüsü içindeyim") #infinite loop
"""
# endregion

# region while_yazim_kurallari
"""
1 → BAŞLANGIÇ
2 → BİTİŞ
3 → ARTIŞ MİKTARI
 
i = 0
print("a")
while i<=3:
    i +=1
    print("b")
print("c")
"""
# endregion

# region dikkat_edilmesi_gereken_kurallar
"""
i = 1
while i <3:   # i büyük 3 olduğu sürece DÖN   
    print("sponsorlu ürün")
  #ctrl+c ile sonsuz döngüden çıkılır.
 """
# endregion

# region ornek_1
"""
i = 1
print("a")
while i<=3:
    print("b")
    i += 1
print("c")

i=1
print("a")
while i<=3:
    print("b")
    if i==2:
        print("elif")
    i+=1
print("c")
"""

# endregion

# region ornek_2
"""
sayac = 1
while sayac<=5:
    print(sayac)
    sayac += 1
"""
# endregion

# region ornek_3
"""
sayac = 5
while sayac:       #yada sayac != 0:
    print(sayac)
    sayac -= 1
# def. da siz koşulu  koşulu int bir tam sayıya bağlı olarak yazarsanız sıfır olduğunda döngü kırılır.
#boolean tipinde true veya false olmak üzere iki değer vardır.
#defaultta tam sayı 0 olduğunda döngü kırılır
#boolean tipe değer atamadığımızda true olarak atanır.



sayac = 5
devamMi = True
while devamMi:
    print(sayac)
    if sayac == 2:
        devamMi = False
    sayac -= 1

"""
# endregion
#region infinite _loop-> sonsuz döngü
tekSayılarınAdedi,ciftSayılarınAdedi=0,0
sayi=int(input("Lütfen bir sayı giriniz,çıkmak için -1 e basınız \t :"))
while sayi != 0:
    if sayi %2 == 0:
         ciftSayılarınAdedi += 1
    else:
        tekSayılarınAdedi += 1
    sayi=int(input("Lütfen bir sayı giriniz,çıkmak için -1 e basınız \t:"))
print(f" girdiğiniz sayılar içinde {tekSayılarınAdedi} adet tek sayı var.")
print(f" girdiğiniz sayılar içinde {ciftSayılarınAdedi} adet çift sayı var.")
#endregion
