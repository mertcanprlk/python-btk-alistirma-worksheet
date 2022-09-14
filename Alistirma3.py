#Örn 1
#4den büyük ve 6 ve 6'dan küçük sayıların doğru değerlerinin false ve true olduğu kodu yazın
from re import X


a=6 
print(a>4 and a<6)

#Örn2
#-3den küçük ve 2den büyük sayıların doğru değerlerinin false ve true olduğu kodu yazın
a=5
print(a>2 or a<-3)
print(not(a<2 and a>-3))

#Örn 3
#-3 ve -1 ayrıca 1 ve 4 arasında değerleri false yazan kod yazınız
a=-2
print((a>-3 and a<-1)or(a>1 and a<4))

#Örn4
#3'ten 10'a kadar olan sayılarda 5 hariç diğer sayıları gösterin
x=3
while x<=10:
    if x != 5:
        print(x)
    x +=1

#Örn 5
#2'den 30'a kadar olan sayılardan 10 ve 15 dışındakileri toplayarak ekrana toplam sonucu yazdırın

x=2
toplam = 0
while x<30:
    if x == 10 or x ==15:
        x += 1
        continue
    toplam += x
    x += 1
print(toplam)

#Örn2
# 1
# 1
# 1
# 2
# 2
# 2
# 3
# 3
# 3
# 4
# 4
# 4
# 5
# 5
# 5 tranpozunu yazdırın
for k in range(1,6):
    for m in range(3):
        print(k)

