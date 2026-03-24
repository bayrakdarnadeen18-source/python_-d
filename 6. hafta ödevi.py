students = []

while True:
    name = input("İsim (çıkış: q): ").strip()
    if name.lower() == "q":
        break
    if not name:
        continue

    raw = input("Not (0-100): ").strip()
    if not raw.isdigit():
        continue

    grade = int(raw)
    if not (0 <= grade <= 100):
        continue

    students.append((name, grade))

if not students:
    print("Hiç veri girilmedi.")
else:
    sorted_students = sorted(students, key=lambda x: x[0])
    print("\nİsme göre sıralı liste:")
    for s in sorted_students:
        print(s)

    max_student = max(students, key=lambda x: x[1])
    print("\nEn yüksek not alan:", max_student)

    min_student = min(students, key=lambda x: x[1])
    print("En düşük not alan:", min_student)

    total = sum(s[1] for s in students)
    avg = total / len(students)
    print("Ortalama:", avg)