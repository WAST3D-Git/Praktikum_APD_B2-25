total_belanja = int(input("Masukkan total belanja: "))
if total_belanja > 100000:
    print("Selamat, Anda mendapatkan diskon 20%!")
elif total_belanja > 50000:
    print("Selamat, Anda mendapatkan diskon 10%!")
else:
    print("Maaf, Anda tidak mendapatkan diskon.")
