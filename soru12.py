from cgi import print_exception


sayilar = [1,3,5,7,9,12,19,21]

#Örn1
#sayilar listesinin while ile ekrana yazıdırın

x=0
while (x < len(sayilar)):
    print(sayilar[x])
    x = x+1

#Örn2
# Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
a=int(input('ilk sayiyi giriniz'))
b=int(input('son değeri giriniz'))
x=a

if (a==1< b==21):
        while (x < a):
            x = x+1
            if(x % 2 == 1):
                print(x)

#Örn3
# 1-100'e kadar olan sayıları azalan şekilde yazıdırın
x = 100

while x >= 1:
    print(x)
    x = x-1

# Örn4
# Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
a= int(input('Sayı giriniz:  '))
b= int(input('Sayı giriniz:  '))
c= int(input('Sayı giriniz:  '))
d= int(input('Sayı giriniz:  '))
e= int(input('Sayı giriniz:  '))
girilen = [a, b,c,d,e]
x=0
while (x < len(girilen)):
    print(girilen[x])
    x = x+1

#Örn 5
#Kullanıcıdan alacağınız sınırsız ürün bilhisini ürünleri listesi içinde saklayınız
#Bu örneği yapmak için şu sırayı takip etmeliyiz:
#1)Ürün sayısını kullanıcıya sorunuz
#2)Dictionary listesi yapsı (name, price) şeklinde olsun
#3)Ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler = []

adet = int(input('kaç ürün eklemek istiyorsunuz: '))
i=0

while (1<adet):
    name = input('ürün ismi: ')
    price = input ('ürün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1
