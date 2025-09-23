nama = "Rosadi"
umur = int(input("Masukkan Umur Anda: "))
listNama = ["Ahmad", "Ihsan", "Rosadi", 19, 3.14, True, False, [1, 2, 3]]
namaAuto = input("Masukkan Nama Anda: ")
pemakaian = int(input("Masukkan Jumlah Pemakaian listrik (dalam kwh): "))
tarif = 1200
total_biaya = pemakaian * tarif
angka = 10
angka += 90

print(angka)
print(f"""Halo, nama saya adalah {nama}
umur saya {umur}""")
print(listNama[0:5])
print(f"Nama anda adalah {namaAuto}")
print(f"total biaya pemakaian listrik anda adalah Rp{total_biaya}")