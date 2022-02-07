# i = 0
# while (i < 5):
#     print("I love coding")
#     i+=1

# i = 0
# while (i <= 20):
#     print(i)
#     i+=2
# print("The loop is over!")

# i = 1
# sonuc = 1
# faktoriyel = int(input("Bir sayi giriniz: "))
#
# while(i <= faktoriyel):
#     sonuc *= i
#     i+=1
# print(f"Sonuc: {sonuc}")

# sonuc = 0
# num = int(input("Bir sayi giriniz: "))
# while(num != 0):
#     sonuc += num
#     num -= 1
# print(sonuc)

# while True:
#     num = int(input("Bir sayi giriniz(0v/0>): "))
#     if (num == 0):
#         break
#     else:
#         continue
# print("You exited!")

# sayi = int(input("Bir sayi giriniz:"))
#
# for i in range(1,10):
#     if(sayi == 0):
#         break
#     else:
#         print(sayi - 1)
#         sayi -= 1

# for i in range(0,11,2):
#     print(i)

# import random
# while True:
#     n = random.randint(1, 20)
#
#     if(n % 2 == 0):
#         print(f"Cift sayi belirlendi!: {n}")
#         break;
#     else:
#         print(f"Rastgele sayi secildi: {n}")

# selam = print
# selam("Dunya")

# import math
# print(sin(30))

# def selamla(a = "Arkadasim"):
#     print(f"Merhaba {a}!")
#
# selamla("Robin")
# selamla("Baran")
# selamla()

# def mevsim_yaz(mevsim_dizisi):
#     for i in mevsim_dizisi:
#         print(i, end = " ")
#
# mevsimler = ["ilkbahar", "yaz", "sonbahar", "kis"]
# mevsim_yaz(mevsimler)

# def dortgen_alan(kenar1,kenar2):
#     print(f"Verilen dortgenin alani: {kenar1 * kenar2}")
#
# dortgen_alan(5,5)

# def tekmi_ciftmi(say1):
#     if say1 % 2 == 0:
#         print("Girdiginiz sayi cift!")
#     else:
#         print("Girdiginiz sayi tek!")
#
# num = int(input("Bir sayi giriniz: "))
# tekmi_ciftmi(num)

# def ortalama_hesapla(sinav1,sinav2,performans):
#     ortalama = (sinav1 + sinav2 + performans) / 3
#     print("Ortalamaniz", str(int(ortalama)))
#
# ortalama_hesapla(95,98,100)

# def tam_bolenlerini_bul(sayi):
#     tam_bolenleri = []
#     for i in range(1,sayi):
#         if(sayi % i == 0):
#             tam_bolenleri.append(i)
#         else:
#             continue
#     return tam_bolenleri
#
# sayi1 = int(input("Bir sayi giriniz: "))
# print(tam_bolenlerini_bul(sayi1))

# toplam = lambda a, b, c:a + b + c
# print(toplam(4,4,4))

# def carpan(n):
#     return lambda a:a*n
#
# print(carpan(5)(10))

# def tumevarim(sayi):
#     if sayi == 1:
#         return 1
#     else:
#         return sayi+tumevarim(sayi-1)
#
# sayi = int(input("Bir sayi giriniz; "))
# print(tumevarim(sayi))
# from datetime import datetime
# print(datetime.now())

# from datetime import datetime
# print(f"Bugunun tarihi: {datetime.today()}")
#
# yil, ay, gun = input("Lutfen dogum tarihinizi (Yil/Ay/Gun) olacak sekilde giriniz: ").split()
#
# yil, ay, gun = int(yil), int(ay), int(gun)
# dogum_tarihi = datetime(year = yil, month = ay, day = gun)
#
# print(dogum_tarihi)
# import datetime
# bugun = datetime.datetime.now()
# print(bugun.strftime("%Y %B %D %X"))
# foo = input("Enter a long foo name: ")
# sehir = "Sakarya"
# for i in sehir:
#     print(i)
# for i in range(1,10):
#     print(i)
#     i = 5
# list = list(range(1,10+1))
# print(list)

# users = {'Eleonore':'active', 'Hans':'inactive', 'Robin':'active'}
#
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#
# print(active_users)

# sum = sum(range(1,11))
# print(sum)

# print ("Hello World!")

# message = "Hello Python Crash Course reader!"
# print(mesage)

# name = input("Enter your name: ")
# print(name.title())

# first_name = "robin"
# last_name = "stardust"
# full_name = first_name + " " + last_name
#
# message = "Hello, " + full_name.title() + "!"
# print(message)

# print("Python")
# print("\tPython")
# print("Languages:\nPython\nC\nJavaScript")

# print("Languages:\n\tPython\n\tC\n\tJavascript")

# favorite_language = "Python "
# favorite_language = favorite_language.rstrip()
# print(favorite_language)

# print(5 + 3)
# print(11 - 3)
# print(4 * 2)
# print(16 / 2)

# favorite_number = 26
# message = "I love " + str(favorite_number) + " a lot"
# print(message)

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
