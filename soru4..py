# 1)"Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz



arabalar = ['Bmw','Mercedes','Opel','Mazda']

# # 1.1)Liste kaç elemanlı
print(len(arabalar)) 

# # 1.2)Listenin ilk ve son elemanı nedir?
print(arabalar[0])
print(arabalar[3])

# 1.3)Mazda değerini toyota ile değiştirin
arabalar[-1]='Toyota'
print(arabalar)

# 1.4)Mercedes listenin bir elemanı mıdır?
print('Mercedes' in arabalar)

# 1.5)Listenin -2 indeksindeki değer nedir?
print(arabalar[-2])

# 1.6) Listenin ilk 3 elemanını alın
print(arabalar[:3])

# 1.7) Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerini ekleyin
arabalar[-2:] = ['Toyota','Renault']
print(arabalar)

# 1.8) listenin üzerine audi ve nissan değerlerini ekleyin
print(arabalar + ['Audi', 'Nissan'])

# 1.9) Listenin son elemanını silin
del arabalar[-1]
print(arabalar)

# 1.10) Listenin elemanlarını testen yazdırınız
print(arabalar[::-1])

# 2)Aşağıdaki verileri bir liste içinde saklayınız
# studentA : Yiğit Bilgi 2010, (70,60,70)
# studentB : Sena Turan 1999, (80,80,70)
# studentC : Ahmet turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999, [80,80,70]]
studentC = ['Ahmet','Turan',1998, [80,70,90]]

# 2.1)Liste elemanlarını ekrana yazdırınız
print(studentA[0])