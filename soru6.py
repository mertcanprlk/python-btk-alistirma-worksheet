ogrenciler = {
'120': {
    'ad':'Ali',
    'soyad': 'Arı',
    'telefon': '546 356 8978'
},
'125': {
    'ad':'Veli',
    'soyad': 'Ata',
    'telefon': '536 887 4595'
},
'128': {
    'ad':'Ayse',
    'soyad': 'Abdal',
    'telefon': '578 952 3565'
},
}

# 1)Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerlerle dictionary içinde saklayınız

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# ogrenciler[number] = { #ister böyle yap ister .update şekilnde yap
#      'ad': name,
#      'soyad': surname,
#      'telefon':phone
# }

ogrenciler.update(
{
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
}
)

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update(
{
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
}
)

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler.update(
{
    number:{
        'ad': name,
        'soyad': surname,
        'telefon':phone
    }
}
)

#art arda 3 tane öğrencinin bilgisini de aldı
print(ogrenciler)

# 2)Öğrenci numarasının kullanıcıdan alıp bilgileri öyle gösterin
print('*'*50)
ogrNo = input('Öğrenci no: ')
ogrenci = ogrenciler(ogrNo)

print(f"aradığınız {ogrNo} nolu öğrencinin adı {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}") 
