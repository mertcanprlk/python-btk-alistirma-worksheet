website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlaam Rehberiniz (40 saat)"

#1)Hello world karakter dizisinin baş ve son harfini silin
# result= 'Hello World'.strip('H,d') #Parantez içine silmek istediğimiz harfi yazıyoruz
# result= ' Hellor World '.lstrip() #soldan siler 
# result= ' Hello Worll '.rstrip() #sağdan siler
# print(result)

# 2)'www.sadikturan.com' içindeki sadikturan bilgisi haricinde her karakteri silin 
# result= website.strip('/:pth.wcom')
# print(result)

# 3)Course karakter dizisinin tüm karakterlerini küçük harf yapın
# result= course.lower()
# print(result)

# 4)'website' içinde kaç tane a karakteri vardır?
# result = website.count('a')
# print(result)

# 5)'website' 'www' ile başlayıp com ile bitiyor mu?
# result=website.startswith('www')
# result=website.endswith('com')
# print(result)

# 6)website içerisinde 'com' ifadesi var mı?
# result=website.find('.com') #ya da result=website.count('.com') dersek de bulabiliriz
# result=website.find('.com',0,10) #0 ile 10 arasında com var mı
# print(result)

# 7)course içindeki karakterlerin hepsi alfabetik mi?
# result=course.isalpha() #alfabe için .isalpha sayılar için .isdigit
# print(result)

# 8)'contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve solan * ekleyiniz
# result='contents'.center(50,'*') #.ljust'ta soldan .rjust'ta sağdan
# print(result)

# 9)'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
# result = course.replace(' ', '-') #bir virgül ekleyip bir sayı koyarsak o sayı kadar yapar bu işlemi
# print(result)

# 10)'hello world' karakter dizisinin 'world' ifadesini 'there' olarak değiştirin
# result = 'hello world'.replace('world','there')
# print(result)

# 11)course karakter dizisinin boşluklardan ayırın
# result = course.split(' ')
# #result = result[2] #2. ifadeyi göstermek adına
# print(result)