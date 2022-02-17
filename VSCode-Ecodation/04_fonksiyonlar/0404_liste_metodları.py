
"""
ogrenciListesi=["doganay","dilara","sevval"]
ogrenciListesi.insert(3,"hatıce")
print(ogrenciListesi)

numbers = [2, 6, 3, 7, 5, 8]
eb=0 
for i in numbers:
    if i>eb:
        eb=i
print(f"listesinin maksimum elemanı {eb}")
"""
"""
Eklenecek Öğrenci Giriniz, Çıkmak İçin -1   : Doğanay
Eklenecek Öğrenci Giriniz, Çıkmak İçin -1   : Elif
Eklenecek Öğrenci Giriniz, Çıkmak İçin -1   : Şevval
Eklenecek Öğrenci Giriniz, Çıkmak İçin -1   : -1
Öğrenci Listesi:
============
Doğanay
Elif
Şevval,

ogrencıListesi=[]
while True:
    mesaj=input("Eklenecek Öğrenci Giriniz, Çıkmak İçin -1   :")
    if mesaj=="-1":
        break
    ogrencıListesi.append(mesaj)
sayac=1
for i in ogrencıListesi:
    print(f"{sayac}. öğrencinin adı {i}")
    sayac+=1

  
Ad-Soyad Giriniz, Çıkmak İçin -1   : Doğanay Bil
Doğanay Bil 1.snv Notu : 60
Doğanay Bil 2.snv Notu : 90
Ad-Soyad Giriniz, Çıkmak İçin -1   : Elif Aslan
Doğanay Bil 1.snv Notu : 60
Doğanay Bil 2.snv Notu : 80
Ad-Soyad Giriniz, Çıkmak İçin -1   : Dilara Özmen
Doğanay Bil 1.snv Notu : 80
Doğanay Bil 2.snv Notu : 80
Öğrenci Ortlama Listesi:
============
75.0
70.0
80.0
Min → 70
Mak → 80

lısteOrt=[]
while True: 
    ad=input("Ad-Soyad Giriniz, Çıkmak İçin -1   :")
    if ad=="-1":
     break
    s1=int(input(f"{ad} 1.sınav notunuz : "))
    s2=int(input(f"{ad} 2.sınav notunuz : "))
    ortalama=(s1+s2)/2
    lısteOrt.append(ortalama)
for i in lısteOrt:
    print(i)
print(f" maksimum not--> {max(lısteOrt)}")
print(f" minimum not--> {min(lısteOrt)}")

# ödev →

Lütfen Bir Sayı Giriniz: 83
Yüz Seksen Üç

liste=[]
sayı=int(input("Lütfen Bir Sayı Giriniz:"))
birlerBasamagı=sayı%10
onlarBasamagı=sayı//10
yuzlerBasamagı=sayı
birler=["","Bir", "iki"," üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar=["","On", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
print(f"{sayı} sayısının yazıyla {onlar[onlarBasamagı]} {birler[birlerBasamagı]} ")
#birler[3]

['Bora', 'Elif', 'Ekin', 'Dilara', 'Doğanay', 'Sevval']
Lütfen Aradığınız Öğrenci Adını Giriniz:    Ekin

ogrenciListesi= ['Bora', 'Elif', 'Ekin', 'Dilara', 'Doğanay', 'Sevval']
arananOgrenci=input("Lütfen Aradığınız Öğrenci Adını Giriniz:  ")
if arananOgrenci in ogrenciListesi:
    print(f"{arananOgrenci} listemizde mevcut ")
else:
    print(f"{arananOgrenci} öğrencilerimiz arasında mevcut değil")
   
   
Örn. kurum içi bilgisayarların özelliklerini tutacağınız bir tablo
Bil.No  Cihaz Adı       CPU     PID
1       Desktop_Test    %56     chrome.exe
2       Guest101        %60     excel.exe
3       Kat-1_Laptop    %90     camtasia.exe, chrome.exe

ogrenci1 = ["Alp", "Besi", 90,	90]
ogrenci2 = ["Batu", "Koçhan", 10, 90]
ogrenci3 = ["Emir", "Besi", 100,90]
ogrenci4 = ["Umut", "Ahmet", 95, 80]
ogrenci5 = ["Aziz", "Bektaş", 15, 10]
ogrenciler = [ogrenci1, ogrenci2, ogrenci3, ogrenci4, ogrenci5]

for i in ogrenciler : 
    print(i[0],i[1],end="  ")
    ortalama=(i[2]+i[3])/2
    if ortalama>50:
        print(f"geçtiniz.ortalamanız:{ortalama}")databasede kişilerin notları var user interfacede ortalama basılıyor.
        yani user interface genelde hesaplama sonuçlarını alırız.
        native dataları hocaların girdiği notlaar ,notlara göre ders geçip geçemediğimizi user interface da
    e okuldaki hocaların vize finak notları  dtaabase de buna göre dersi geçip kaldığımızı hesaplamamız user interfacedadir
    
    
    else:
        print(f"kaldınız.ortalamanız:{ortalama}") databasede nsanların doğum tarihi var user interfacede sadece doğum traihini gördük.
  """  