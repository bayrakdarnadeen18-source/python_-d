count = 0
toplam = 0
min_s = None
max_s = None

while True:
    n = int(input("Sayı gir (-1 çıkış): "))

    if n == -1:
        break

    count += 1
    toplam += n

    if min_s is None or n < min_s:
        min_s = n

    if max_s is None or n > max_s:
        max_s = n

    print("Count:", count)
    print("Sum:", toplam)
    print("Min:", min_s)
    print("Max:", max_s)