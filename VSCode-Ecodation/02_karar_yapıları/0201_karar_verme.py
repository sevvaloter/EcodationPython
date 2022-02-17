# region karsilastirma_operatorleri_giris
"""
KARŞILAŞTIRMA OPERATÖRLERİ
1→  ==  eşittir
2→  !=  eşit değildir
3→  <   küçüktür
4→  >   büyüktür
5→  <=  küçük eşittir
6→  >=  büyük eşittir
"""
# endregion

# region ==
"""
print(10 == 10) #true
print(-5 == -5)
print(10 == 5)
print("istanbul" == "istanbul") #karşılaştırma operatörlerine str leri de karşılaştırırız.
print("istanbul" == "İstanbul") #case sensitive yapısı vardır.
print("meb" == "MEB")
print(" " == " ") #boşluk da bir karakterdir.
print(10=10) #expression cannot assignment,perhaps you meant "=="
"""
# endregion

# region !=
"""
print(10 != 10) #içindeki ifadenin not hali olarak düşünebilirsin.
print(10 != 5)
print("meb" != "MEB")
"""
# endregion

# region < operatoru
"""
print(10 < 20)
print(10 < 10)
print(20 < 10)
print(5 < 9)
"""
# endregion

# region > operatoru
"""
print(10 > 20)
print(10 > 10)
print(20 > 10)
"""
# endregion

# region <=
"""
print(10 <= 20)
print(10 <= 10)
print(20 <= 10)
"""
# endregion

# region >=
"""
print(10 >= 20)
print(10 >= 10)
print(20 >= 10)
"""
# endregion

# region ornek_1
"""
ogrenciYas = int(input("Lütfen Öğrencinin Yaşını Giriniz: "))
print(ogrenciYas >= 18) #true veya false döndürür.
"""
# endregion

# region ornek_2
"""
Kullanıcı Adını Giriniz : admin     → True 
Kullanıcı Adını Giriniz : user      → False 

uName = input("Lütfen K.A. Giriniz : ")
print(uName=="admin") 
"""
# endregion