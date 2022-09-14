# Soru1
# Kullanıcıdan isim, yaş ve eğitim bilgilerini siteyip ehliyet alabilme durumunut alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır kontrol ediniz. Ehliye

from cProfile import label
from itertools import zip_longest
from re import L


isim = input('isminizi giriniz: ')
yas= int(input('Yasinizi giriniz: '))
egitim = str(input('egitim durumunuzu giriniz: '))

if (yas >= 18):
    if (egitim == 'lise' or egitim=='universite'):
        print('Ehliyet alabilirsiniz')

else:
    print(f'sayin {isim} . Ehliyet alamazsiniz.')

#Soru2
# bir öğrencinin 2 yazılı bir sözlü notunu alıp not aralığına karşılık gelen not bilgisini yazdırın
yazili1 = int(input('İlk yazılınızı giriniz: '))
yazili2= int(input('İkinci yazılınızı giriniz: '))
sozlu = int(input('sözlünüzü giriniz: '))

ort = (yazili1 + yazili2 + sozlu) / 3

if (0<=ort<=24):
    print('0 aldınız')
elif (25<=ort<=44):
    print('1 aldınız')
elif (45<=ort<=54):
    print('2 aldınız')
elif (55<=ort<=69):
    print('3 aldınız')
elif (70<=ort<=84):
    print('4 aldınız')
elif (85<=ort<=100):
    print('5 aldınız')

#Soru3
#Trafiğe çıkış tarihi alınan bir aracın serbis zamanını aşağıdaki bilgere göre hesaplayınız
# 1. bakım => 1. yıl 
# 2. bakım => 2. yıl 
# 3. bakım => 3. yıl 


days = int(input('aracınız kaç gündür trafikte: '))

if days<=365:
    print('1. servis aralığı')
elif 365<days<=730:
    print('2. servis aralığı')
elif 730<=days<=1095:
    print('3. servis aralığı')
else:
    print('hatalı süre belirtildi hesaplanamıyor')

#3. soru için alternatif
#** süre hesabına alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayınız 
# **** bu soruda datetime modülünü kullanmamız gerekiyor