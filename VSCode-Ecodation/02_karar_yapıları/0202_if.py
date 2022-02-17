#region if_aciklama
#if kullanımı
"""
1- önce if yazılır.          if i==2 :
2- sonra koşul yazılır          print("doğru bildiniz.")
3- sonra da : iki nokta ile blok başlatılır
"""
#endregion

#region ornek_1
"""
havaDurumu = "güneşli"
print("HAVA GÜNEŞLİ TADINI ÇIKARIN.")
if havaDurumu == "yağmurlu":
    print("şemsiye alın lütfen")
print("c")
"""
#endregion

#region ornek_2
"""
a =-10
if a<0:
    print(f"{a} sayısı negatiftir")
"""
#endregion

#region ornek_3
"""
s = int(input("Lütfen sayı giriniz \t : "))
if s == 0:
    print("lütfen 0 değeri girmeyin")
"""
#endregion

#region ornek_4
"""
uName = input("lütfen kullanıcı adınızı giriniz : ")
if uName != "admin":
    print(f"{uName} admin paneline giriş yapamaz")
"""
#endregion

#region pass
#if bloğu boş geçilemez
"""
kAdi = input('Kullanici Adi Giriniz: ')
if kAdi!= "admin":
    pass  
"""
#pass koşul yazmdan önce yer tutar,koşul sonrası işletilecek kodu yazmdan önce yazarız çünkü if bloğu boş geçilemez.

#endregion
#region break-point
"""
kAdi = input("Kullanici Adi Giriniz: ")
print("a")
if kAdi!= "admin":
    print(f"{kAdi} yetkisi ile admin paneline giremezsiniz...")
    print("b")
print("c")
#run-->start debugging-->python file [break point ekleme]
"""
#endregion