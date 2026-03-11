try:
    sayi = int(input("Bir sayı gir: "))
    sonuc = 10 / sayi
    print("Sonuç:", sonuc)

except ValueError:
    print("Lütfen sayı gir!")

except ZeroDivisionError:
    print("0'a bölme hatası!")