ulangi = 10
for i in range (ulangi):
    print(f"Perulangan ke {i}")


simpan = [1, "Dapupu", 4.00, False]
for i in simpan:
    print(i)

# Contoh NESTED FOR
for i in range(1, 4):
    for j in range(1, 5):
        print(f"{i} x {j} = {i * j}")
    print(" ")

# Contoh WHILE
jawab = 'ya'
hitung = 0
while jawab == 'ya':
    hitung += 1
    jawab = input("Ulangi lagi? (ya/tidak) ")
print(f"Perulangan ke {hitung}")

# Contoh BREAK
angka = [2, 13, 43, 23, 45, 67, 89, 90]
print('Mencari angka yang lebih besar dari 50')
for n in angka:
    print(f'Sekarang memeriksa angka: {n}')
    if n > 50:
        print(f'Angka {n} lebih besar dari 50')
        break
print('Program selesai')

# Contoh CONTINUE
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(f'Angka genap telah ditemukan {i}')
print('Program selesai')