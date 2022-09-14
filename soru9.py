#Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
a=int(input("bir sayı giriniz"))
result = a>=0 and a<=100
print(result)

#Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
a=int(input("bir sayı giriniz"))
result = a>0 and a %2 == 0
print(result)

#Email ve parola bilgileri ile giriş kontrolü yapınız
a=input("e-mailinizi giriniz")
emailkontrol = a== "mert.166169@gmail.com"
b=int(input("parolanızı giriniz"))
parolakontrol = b== 123456
result = a== "mert.166169@gmail.com" and b== 123456
print(result)

#Kullanıcıdan kullanıcıdan vize (%60) ve final (%40) notunu alıp ortalama yapınız
a=input("Vizeyi giriniz")
b=input("Finali giriniz")
a=int(a)
b=int(b)
result = a*60/100 + b*40/100
sonuc = result>=50 and b>=50 or b>70
print(f'Geçme kalma durumunuz: {sonuc}')

#Girilen 3 sayının büyüklük olarak karşılaştırınız
a=int(input("İlk sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))
c=int(input("Üçüncü sayıyı giriniz: "))

result = (a > b) and (a > c)
print(f'a en büyük sayıdır: {result}')

result= (c > b) and (c > a)
print(f'c en büyük sayıdır: {result}')

result =(b > c) and (b > a)
print(f'b en büyük sayıdır: {result}')


#Kişinin ad kilo ve boy bilgilerini alıp kilo indekslerini hesaplayın
a=input("İsim giriniz: ")
b=float(input("boy giriniz: "))
c=float(input("kilo giriniz: "))

zayif = (result >=0) and (result<=18.4)
normal =(result >18.4) and (result<=24.9)
kilolu = (result >24.9) and (result<=29.9)
obez = (result>= 29.9) and (result<=34.9)
result = c/(b**2)

print(f'{a} kilo indeksin: {result} ve kilo değerlendirmen: {zayif}')
print(f'{a} kilo indeksin: {result} ve kilo değerlendirmen: {normal}')
print(f'{a} kilo indeksin: {result} ve kilo değerlendirmen: {kilolu}')
print(f'{a} kilo indeksin: {result} ve kilo değerlendirmen: {obez}')
