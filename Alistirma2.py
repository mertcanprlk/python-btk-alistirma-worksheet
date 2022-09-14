# 66
# 66
# 66
# 66
# 66 karşılık gelen kodu yaz

for k in range(5):
    f=""
    for m in range(2):
        f=f+"6"
    print(f)

# 878
# 878
# 878
# 878 karşılık gelen kodu yaz
for k in range(4):
    f="878"
    for m in range(1,3):
        f=f+""
    print(f)

#5 6 7 8 9
#5 6 7 8 9
#5 6 7 8 9
#rakam, birleştirme oparatörü ve iç içe döngü kullanarak yapınız
for k in range(3):
    f="5 6 7 8 9"
    for m in range(1):
        f=f+""
    print(f)

#9'dan 12'ye kadar olan sayılarda 10 hariç hepsini toplayın
x=9
toplam = 0
while x<12:
    if x == 10:
        x += 1
        continue
    toplam += x
    x += 1
print(toplam)

#15'den 50'ye kadar olan sayılardan çiftler hariç hepsini toplayın
x=15
toplam=0
while x<50:
    if x % 2 == 0:
        x=x +1
        continue
    toplam = toplam + x
    x += 1
print(toplam)

#10'dan 86'ya kadar olan sayılardan 10 ile bölünenler hariç çarpın
x=10
carp=1
while x<86:
    if x % 10 == 0:
        x += 1
        continue
    carp=carp*x
    x += 1
print(carp)

#15'ten 67'ye kadar olan sayılardan 50 42 ve 16 olan sayılar hariç hepsini toplayın
k=15
toplam=0
while k<64:
    if k == 50 and k == 42 and k == 16:
        k += 1
        continue
    toplam = toplam + k
    k += 1
print(toplam)

#100'den 200'e kadar olan sayıların 180 ve 111 olmadan toplayıp yazdırın
e = 100
toplam = 0
while e<200:
    if e == 180 and e==111:
        x += 1
        continue
    toplam += e
    e += 1
print(toplam)

a = "+"
print(a)
for m in range(3):
    a = a + "+"
    print(a)

#Provided to YouTube by Sony Music Entertainment cümlesini yazıdırın
say = 0
for x in "Provided to YouTube by Sony Music Entertainment":
    print(x)
    say += 1

##Provided to YouTube by Sony Music Entertainment cümlesinde ne kadar p varsa yazdırın
say = 0
a = "Provided to YouTube by Sony Music Entertainment cümlesini yazıdırın"
a=a.lower()
for x in a:
    if x =='p':
        say += 1
print(say)

#Korin and I playing a cover of "in the shadow of the valley" by lost weekend western swing band cümlensinde ne kadar a varsaya gösterin
say = 0
e = 'Korin and I playing a cover of in the shadow of the valley by lost weekend western swing band'
for x in e:
    if x == 'a':
        say += 1
print(say)

##Kullanıcı tarafından 1 girilene kadar girilen tüm sayıları toplatınız. carpım sonucu ekranda yazdırın
carp = 1
while True:
    a = int(input("sayi giriniz: "))
    if a == 1:
        break
    carp *= a 
print(carp)


#Kullanıcı tarafından 10 girilene kadar girilen tüm sayıları çıkartınız. çıkartmanın sonucu ekranda yazdırın
çıkar=0
while True:
    l =int(input("Sayi giriniz"))
    if l == 10:
        break
    çıkar -= l
print(çıkar)

