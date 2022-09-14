#https://www.algoritmaornekleri.com/python/python-calisma-sorulari-ve-cevaplari/ 
#Soru1
# Ekranda “Merhaba Dünya” yazdıran Python Örneği
print('merhaba dünya')

#Soru2
#Kullanıcının İsmini Alarak Merhaba (kullanıcı ismi) Yazdıran Python Örneği
a=input('İsminizi giriniz: ')
print(f'Merhaba {a}')

#Soru3
#Girilen 2 Sayıyı Toplayan Python Örneği
b=int(input('1. sayıyı giriniz: '))
c=int(input('2. sayıyı giriniz: '))
resul = b+c
print(resul)

#Soru4
#Girilen 2 Sayının Ortalamasını Bulan Python Örneği
b=int(input('1. sayıyı giriniz: '))
c=int(input('2. sayıyı giriniz: '))
resul = (b+c)/2
print(resul)

#Soru5
#Girilen Vize ve Final Notu Ortalaması Hesaplayan Python Örneği
b=int(input('Vizenizi giriniz: '))
c=int(input('Finalinizi giriniz: '))
resul = b * 0.15 + c * 0.85 
print(resul)

#Soru6
#Girilen 3 Yazılı Notunun Ortalamasını Bulan Python Örneği
b=int(input('1. notunuz giriniz: '))
c=int(input('2. notunuz giriniz: '))
d=int(input('3. notunuz giriniz: '))
resul = (b+c+d)/3
print(resul)

#Soru 7
# Yazılı Ortalaması Girilen Öğrencinin Sınıf Geçme Durumunu (GEÇTİ – KALDI) Gösteren Python Örneği
b=int(input('Vizenizi giriniz: '))
c=int(input('Finalinizi giriniz: '))
resul = b * 0.15 + c * 0.85 
if resul >= 50:
    print(f'{resul} ortalama ile geçtiniz')

else:
    print(f'{resul} ortalama ile kaldınız')

#Soru 8
#Girilen Sayının Tek mi Çift mi Olduğunu Bulan Python Örneği.
b=int(input('Sayı giriniz: '))
if b % 2 == 0:
    print('sayı çiftir')

elif b % 2 == 1:
    print('sayı tektir')

else:
    print('sayı 0')

#Soru 9
#Girilen Sayının Pozitif, Negatif, ya da 0 Olduğunu Bulan Python Örneği
b=int(input('Sayı giriniz: '))
if b> 0:
    print('sayı pozitif')

elif b <0 :
    print('sayı negatif')

else:
    print('sayı 0')

#Soru10
#Yaşı Girilen Kişinin Ehliyet Alıp Alamayacağını Gösteren Python Örneği
b=int(input('Yaşınızı giriniz: '))
if b>= 18:
    print('Ehliyet alabilirsiniz')

elif b < 18:
    print('Ehliyet alamazsınız')

else:
    print('lütfen geçerli bir yaş giriniz')

#Soru11
#1-100 Arası Sayıları Ekranda Listeleyen Python Örneği.

x=0

for x in range(1,101):
    print(x)

#Soru12
#1-100 arası Çift Sayıları Listeleyen Python Örneği.
x=0

for x in range(1,101):
    if x % 2 == 0:  
        print(x)

#Soru 13
# 1-100 Arası Tek Sayıları Listeleyen Python Örneği
x=0

for x in range(1,101):
    if x % 2 == 1:  
        print(x)

#Soru 14
#1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python Örneği

x= 0
for x in range(1,101):
    if x % 3 == 0 and x % 5 ==0:
        print(x)


#Soru15
# 1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen Python
a = int(input('sayı giriniz: '))

x=1
while x <= a:
    print(x)
    x = x +1

#Soru16
# Kenarları Girilen Dikdörtgenin Alanı ve Çevresini Bulan Python Örneği
uzunkenar = int(input('uzun kenarı giriniz: '))
kısakenar = int(input('kısa kenarı giriniz: '))

alan = kısakenar * uzunkenar
cevre = 2 * (kısakenar + uzunkenar) 

if uzunkenar > kısakenar:
    print(f'dikdörtgenin alanı: {alan}')
    print(f'dikdörtgenin çevresi: {cevre}')

else: 
    print('Kısa kenar ve uzun kenar uzunluklarına dikkat ediniz')

#Soru17
#Girilen metnin harflerini alt alta yazdıran Python Örneği
k=input("metin giriniz")
for m in k:
    print(m)

#Soru 18
#Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python Örneği.
b=int(input('1. sayıyı giriniz: '))
c=int(input('2. sayıyı giriniz: '))

toplam =0

while c<=b:
    print(toplam)
    c = c+1
while b<=c:
    print(toplam)
    b = b+1
print(toplam)

#Soru 19
##Girilen bir sayının asal sayı olup olmadığını bulun
#asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir

a = int(input('sayi giriniz: '))

if a % 2 !=0 and a % 3 !=0 and a % 4 !=0 and a % 5 !=0 and a % 6 !=0 and a % 7 !=0 and a % 8 !=0 and a % 9 !=0 and a!= 1 :
    print(f'{a} bir asal sayıdır')
elif a == 2:
    print(f'{a} bir asal sayıdır')
else:
    print(f'{a} bir asal sayı değildir')


#Soru 20
#1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda gösteren Python Örneği
a = int(input('sayi giriniz: '))

toplam=0
for x in range(1,a):
    if x % 2 == 0:
        toplam = toplam +x
print(toplam)

toplam=0
for x in range(1,a):
    if x % 2 != 0:
        toplam = toplam +x
print(toplam)

#Soru 21
# Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren Python örneği:
a = int(input('eski maaşiniz giriniz: '))
b = float(input('zam oranını giriniz: '))

resul = (a * b)
print(f'yeni maaşınız {resul + a}')

#Soru 22-25 arasını geçtim

#Soru 26
#Python ile bir liste içinde 5’in katları olan sayıları listeleme.
sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]

for x in sayilar:
    if x % 5 == 0:
        print(x)




