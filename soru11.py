from cgi import print_form


sayilar = [1,3,5,7,9,12,19,21]
# örn1
#sayılar listesindeki hangi sayılar 3ün katıdır

for uc in sayilar:
    print(uc % 3 == 0)

#Örn2
#sayılar listesine sayıların toplamı kaçtır

for toplam in sayilar:
    toplam = 1+3+5+7+9+12+19+21
    print(toplam)

# örn3
#sayılar listesindeki tek sayıların karesini alınız

for karesi in sayilar:
    if(karesi % 2 == 1):
        print(karesi ** 2)

sehirler = ['trabzon','afyon','bolu','van','muş']
#Örn 4
#sehirlerden hangileri en fazla 5 karakterlidir?

for sehir in sehirler:
    if len(sehir) <=5:
        print(sehir)

urunler = [
{'name':'samsung S6', 'price':'3000'},
{'name':'samsung S7', 'price': '4000'},
{'name':'samsung S8', 'price':'5000'},
{'name':'samsung S9', 'price': '6000'}
]

#Örn 5
#Ürünlerin fiyatları toplamı nedir?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(toplam)


#Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz
for urun in urunler:
    if(int(urun['price']) <= 5000):
        print(urun['name'])