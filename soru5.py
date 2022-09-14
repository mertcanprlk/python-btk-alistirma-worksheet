names = ['Ali','Ela','Lale','Ozan']
years = [1998, 2002,1999,2010]

# 1)Cenk ismini listenin sonuna ekleyiniz
names.append('Cenk')
print(names)

# 2)Sena Listenin başına ekleyiniz
names.insert(0, 'Sena')
print(names)

# 3)Ozan ismini silin
names.remove('Ozan')
print(names)

# 4)Ela isminin indeki nedir?
index = names.index('Ela')
print(index)

# 5)Peyker listenin bir elemanı mıdır?
count = names.count('Peyker')
print(count)

# 6)Listenin elemanlarını ters çevirin
names.reverse()
print(names)

# 7)Listeyi alfabetik olarak sıralayınız
names.sort()
print(names)

# 8)years listesini rakamsal büyüklüğe göre srıralayınız
years.sort()
print(years)

# 9)str = "Ford, Tofas" karakter dizisini listeye çeviriniz
str = "Ford, Tofas"
result = str.split(',')
print(result)

# 10)years dizisinin en büyük ve en küçük elemanı nedir
val = min(years)
print(val)
val = max(years)
print(val)

# 11)Years dizisinin içerisinde kaç tane 1998 değeri vardır?
count = years.count(1998)
print(count)

# 12)Years dizisinin bütün elemanlarını siliniz
years.clear()
print(years)

# 13)Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayın
markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)