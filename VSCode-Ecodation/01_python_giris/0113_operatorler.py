#region atama_operatoru
"""
name = "Jhon"
print(name)
"""
#endregion

#region round
"""
s = 1.838983121212
print(round(s, 3)) #round fonksiyonu sayının uzayan ondalık kısmını yuvarlar.
#Burada 3 denilince evirgülden sonraki üç basamağı yuvarlar.
kg = 80
mt = 1.60
vki = kg/mt**2
print(round(vki, 2))
"""
#endregion

#region sonucu_yine_kendi_degerine_atama
"""
i = 1
print(i)
i = i + 1
print(i)
sayi = 10
sayi = sayi - 1
sayi = sayi * 2
x=10
x = x + 1
print(sayi)
print(x)
"""
#endregion

#region az_sayida_degisken_kullanma
"""
sayi = 5
toplam = 0
toplam = toplam + sayi
sayi = 10
sayi = sayi + 1
toplam = toplam + sayi
"""
#endregion
#region kisa_yol_operatorleri
"""
Kısayol operatörleri
+=  -=  *=   /=
sayi = 10
sayi -= 5     #sayi = sayi - 5
sayi *=2
print(sayi)
"""
#endregion

#region ornek
"""
skor = 0
can = 3
#engeli geçtiğinde skor 1 artar
skor += 1
#engele çarptığında can 1 azalır
can -= 1
print("anlık skorunuz", skor)
print("kalan canınız", can)
"""
#endregion
#region string_operatorleri
"""
+ = concatenation
* = replication
a = "A"
b = "B"
c = "C"
yazdir = a + b + c
print(yazdir)
"""

"""
print(3*3)
print("istanbul"*3)
print("+"*50)
print("+"*50)
print("+")"""
#endregion

#region ornek
"""

okulTuru = "Anadolu"
seviye = 12
print(okulTuru + " " + str(seviye)) #str ve int concat edilemez casting yapıp str(seviye ) de.
"""

#endregion