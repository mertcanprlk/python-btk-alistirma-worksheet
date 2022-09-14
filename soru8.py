#Kullanıcıdan girilen 2 sayıdan hangisi büyüktür?
from unittest import result


a=input("İlk Sayıyı giriniz")
b=input("İkinci Sayı giriniz")
if (a<b):
    print("ikinci sayı büyük")
if (b<a):
    print("ilk sayı büyük")

#kullanıcıdan 2 bize (%60) ve final (%40) notunu alıp ortalama yapınız
a=input("Vizeyi giriniz")
b=input("Finali giriniz")
a=int(a)
b=int(b)
a=a*60/100
b=b*40/100
if (a+b<50):
    print("Kaldınız")
if(a+b>=50):
    print("Geçtiniz")

#Girilen bir sayının tek mi çift mi olduğunu yazdırın
a=input("Bir sayı giriniz")
a=int(a)
tekcift = (a % 2 == 0)
print(f'girilen sayı çift olma durumu: {tekcift}')

#Girilen bir sayının negatif mi pozitif mi olduğunu yazdırın
a=input("Bir sayı giriniz")
a=int(a)
isaret = (a>0)
print(f'girilen sayının pozitif olma durumu: {isaret}')

#Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
a=input("E-mail giriniz")
a=="mert.166169@gmail.com"

if(a=="mert.166169@gmail.com"):
    print("parolanızı giriniz")
    b=input("Parola giriniz")
    if(b=="abc123"):
        print("Ujgeldin")
else:
    print("tekrar deneyiniz")