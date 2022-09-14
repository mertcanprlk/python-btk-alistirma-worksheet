#Soru 1
#Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın
def belirt(kelime,adet):
    print(kelime * adet)

belirt("merhaba\n", 10) #Str ifadenin içindeki \n sonraki satıra geç demektir

#Soru 2
#Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çevirin

def parametreler(*params):
    liste = []
    for param in params:
        liste.append(param)

    return liste
result = parametreler(1,2,3,'slm')
print(result)

#Soru 3
#Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
def asalSayılariBul (sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi >1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break 
            else:
                print(sayi)

sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

asalSayılariBul(sayi1,sayi2)

#Soru 4
#Kendisine gönderilen bir sayının tam bölünenlerini bir liste haline getirin 

def tamBolenleribul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler 

print(tamBolenleribul(20))