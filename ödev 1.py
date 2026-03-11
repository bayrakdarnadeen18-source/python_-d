import random

sayi = random.randint(1,100)

while True:
    tahmin = int(input("1 ile 100 arasında tahmin gir: "))

    if tahmin > sayi:
        print("Daha küçük bir sayı gir")
    elif tahmin < sayi:
        print("Daha büyük bir sayı gir")
    else:
        print("Tebrikler doğru tahmin!")
        break