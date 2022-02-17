""" 
compilaton=derleme // interpretation=yorumlama(kaynak kodu yorumlamak zorunda olduğum her an çalışır.)

Compilation
:Avantaj
1- Compile edilmiş kodların execute işlemini hızlıdır.Compile edilen dillerde tüm kodların
runtimeda (test aşamasında değil.) hatasız olduğunu bilirse output olarak basılır.(Interpreter da 
hata olana kadar hatasız kısım output olarak basılır.)
2-Compiler sadece kod yazılan pc de olmalı,son kullanıcıda olmasına gerek yok.
3- Compile edilen kodlar makine diline çevrileceği için son kullanıcının bu kodları anlaması zor.
Kodların manipülasyonları zor ama imkansız değil reverse-engine yaparak .exe i .cs ye çevirenler var =)

:Dezavantaj
1-Compile işlemi,derleme işleme anı yavaş.
2-Compiler,donanım platformlarına göre farklılık gösterir.Platform bağımlıdır.
###

Interpretation
:Avantaj
1-Kodu yazar ve çalıştırır.Ek derleme süresi istemez.
2-Platform bağımlı değildir.Her donanımda her işletim sisteminde çalışır,ayrı ayrı derleyici istemez.
Runtime da iken(çalışma anında)interpreter olması yeterli.Bu da Python Kütüphanelerinde mevcut.
:Dezavantaj
1-Tüm kaynağı runtime da iken bitirir,çalışma anı yavaştır.
2-Hem kodu yazan kişinin hem de son kullanıcının bilgisayarında interpreter olmalı.
"""