#output anıdna casting - dönüşüm ile ilgili efor harcamamak için format yöntemleri kullanırız

#region format
#ekrana output formatlarken ilk yöntem → format
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girdiğiniz rakamın bir fazlası {}".format(rakam+1)) #{içine değerler yazılır.}
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam+1)))
a = int(input("lütfen  a. değeri giriniz: "))
b = int(input("lütfen b. değeri  giriniz: "))
print("{} değeri ile {} değerinin toplamı {}". format(a, b, (a+b)))
"""
#endregion

#region fstring
#ekrana output formatlarken ilk yöntem → fstring
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print(f"girdiğiniz {rakam} rakamının bir fazlası {rakam+1}")
a = int(input("lürfen a. değerini giriniz: "))
b = int(input("lütfen b. değerini giriniz: "))
print(f"{a} değeri ile {b} değerinin toplamı {a+b}")
"""
#endregion

#region ornek
"""
s1 = int(input("lütfen sayı giriniz:\t"))
s2 = int(input("lütfen sayı giriniz:\t"))
print(f"girdiğiniz sayıların toplamı {s1+s2}")
print(f"{s1} + {s2} = {s1+s2}")


"""
#endregion