##Girilen bir sayının asal sayı olup olmadığını bulun
#asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir

a = int(input('sayi giriniz: '))

if a % 2 !=0 and a % 3 !=0 and a % 4 !=0 and a % 5 !=0 and a % 6 !=0 and a % 7 !=0 and a % 8 !=0 and a % 9 !=0 and a!= 1 :
    print(f'{a} bir asal sayıdır')
elif a == 2:
    print(f'{a} bir asal sayıdır')
else:
    print(f'{a} bir asal sayı değildir')