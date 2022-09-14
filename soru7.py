
x,y,z =2,4,6

numbers =1,5,10,15,20

# 1)Kullanıcıdan aldığınız 2 sayısının çarpımı ile x,y,z toplamının farkı nedir
a= int(input("Lütfen sayı giriniz"))
b = int(input("Lütfen sayı giriniz"))
print((a * b)-(x+y+z))

# 2)y'nin x'e kalansız bölümünü hesaplayın
result = y // x
print(result)

# 3)(x,y,z) toplamının mod 3'ü nedir?
toplam = (x+y+z)
result = toplam % 3
print(result)

# 4)y'nin x. kuvvetini hesaplayınız
y ** x

# 5)x,*y, z = numbers işlemine göre z' küpü kaçtır
numbers =1,5,10,15,20
x,*y, z = numbers
print(result)