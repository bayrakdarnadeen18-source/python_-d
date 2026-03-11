print("1- Çarpma")
print("2- Bölme")

secim = input("Seçiminiz: ")

sayi1 = float(input("Birinci sayı: "))
sayi2 = float(input("İkinci sayı: "))

if secim == "1":
    print("Sonuç:", sayi1 * sayi2)

elif secim == "2":
    if sayi2 == 0:
        print("0'a bölme hatası!")
    else:
        print("Sonuç:", sayi1 / sayi2)

else:
    print("Geçersiz seçim")