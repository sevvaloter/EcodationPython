# region lab_1 
"""
print('Dünya\'nın',"En","Güzel","Şehri",sep="☙",end="→")
print('İSTANBUL \'', "dur." '')
print('"EGE\'nin', "İNCİSİ ", "İZMİR", sep=" ¤ ", end=" !! ")
print("\"EGE \'nin ", "İNCİSİ", 'İZMİR\"', sep=" ¤ ", end=" !! ")

"""
# endregion
# region lab_2

"""
delta örneği
a = 1
b = 4
c = 2
delta = b**2 - 4*a*c
print("delta değeri " , delta)

ortalama
s1 = 2
s2 = 4
ort = (s1 + s2) / 2
print("ortalama değeri ", ort)

saat bilgisini saniyeye dönüştürsün
saat = 2
saniye = 3600
print("Saat: ", saat)
print("Ekrandaki saat biriminin saniye karşılığı →", saat*saniye, " sn.")

# ipucu → formatter shift + alt + f
x=023
x = 023


sayi = 562
kalan = sayi % 10 #kalan=2
birler = kalan // 1 #birler=2
kalan = sayi % 100 #kalan=62
onlar = kalan // 10 #onlar=6
kalan = sayi % 1000 #kalan=562
yuzler = kalan //100 #kalan =5 
toplamDegeri = birler + onlar + yuzler
print(yuzler, onlar, birler)
print(sayi, " sayısının basamakları toplamı " , toplamDegeri)
"""

"""
print( " Leylek Uygulamasına Hoş Geldiniz,Sürüş Ücreti → 0.59/dk")
s = int(input("sürüş için geçen süre (saat)\t : "))
d = int(input("sürüş için geçen süre (dakika)\t : "))
toplamDakika = s*60
toplamDakika += d
toplamTutar = 0.59 * toplamDakika
print(f"Sürüş için geçen süre (saat)\t: {s}")
print(f"Sürüş için geçen süre (dakika)\t: {d}")
print(f"sürüşün toplam süresi {s}:{d} - {toplamDakika} dakika da bitmiştir")
print(f"kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")

# ödev →

km cinsinden girilen mesafe bilgisini mil'e çeviren programı yazınız.
mil =  km / 1.609344

"""




# ödev →
"""
Lütfen Üçgenin A Kenarı Açısını Giriniz: 30
Lütfen Üçgenin B Kenarı Açısını Giriniz: 60
C Kenarı 90 Derecedir
"""


# ödev →
"""
- Kullanıcıdan x1,x2,y1,y2 değerleri alınır
- uzaklik =[ (x1-x2)karesi + (y1-y2)karesi ] karekök
- format : (x1,x2) ve (y1,y2) noktaları arasındaki uzaklık .. birimdir.
- virgülden 2 basamak olacaktır.
"""


# ödev 
"""
- Kısaltmalar;
    - at    aylık tüketim giriniz
    - aeb   aktif enerji bedeli
    - db    dağıtım bedeli
    - teb   toplam enerji bedeli
    - tp    trt payı
    - ef    enerji fonu
    - etv   elektrik tüketim vergisi
    - vt    vergiler toplamı
- elektrik faturamızı hesaplayalım
    - aylık tüketim giriniz ? [kWh]  : 500
    - aktif enerji bedeli = aylık tüketim x 0.39736
    - dağıtım bedeli = aktif enerji bedeli x 0,2474
    - toplam enerji bedeli = aktif enerji bedeli + dağıtım bedeli
    - trt payı = 3.97
    - enerji fonu = 1.39
    - elektrik tüketim vergisi = 9.92
    - KDV = (toplam enerji bedeli + trt payı + enerji fonu + elektrik tüketim vergisi) x 0.18
    - vergiler toplamı = trt payı + eerji fonu + elektrik tüketim vergisi + kdv
    - toplam fatura = vergiler toplamı + toplam enerji bedeli
"""

# ödev 
"""
Güncel Benzin Endeksini Giriniz                 : 7.09
Yakıt Tüketimini Giriniz [100 km. başına] )     : 4.08
Kaç Kilometre Yol Aldınız?                      : 50
Toplam Yakıt Tüketimi → 14.4636  
"""


# ödev 
"""
Lütfen Ürün Adı Giriniz                         : A4 Fotokopi
A4 Fotokopi - Satın Alınacak Adet               : 2
Lütfen Ürün Fiyatı Giriniz [KDV-Dahil]          : 130.00
Lütfen İndirim Oranını Giriniz [%]              : 5
Ürünlerin Toplam Tutarı 247.0 TL.

"""