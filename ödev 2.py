notu = int(input("Notunuzu girin (0-100): "))

if notu < 0 or notu > 100:
    print("Geçersiz not")
elif notu >= 90:
    print("Harf notu: A")
elif notu >= 80:
    print("Harf notu: B")
elif notu >= 70:
    print("Harf notu: C")
elif notu >= 60:
    print("Harf notu: D")
elif notu >= 50:
    print("Harf notu: E")
else:
    print("Harf notu: F")