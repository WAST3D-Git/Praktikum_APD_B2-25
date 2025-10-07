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

while True:
    print("1. Menu 1")
    print("2. Menu 2")
    print("3. Menu 3")
    opsi = int(input("Pilih menu (1/2/3): "))
    if opsi == 1:
        print("Anda memilih menu 1")
    elif opsi == 2:
        print("Anda memilih menu 2")
    elif opsi == 3:
        print("Anda memilih menu 3")
    else:
        print("Opsi tidak valid, silakan coba lagi.")
        continue
