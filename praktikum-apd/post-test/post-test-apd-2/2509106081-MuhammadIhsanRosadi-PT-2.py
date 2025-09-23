nama = input("Masukkan Nama Lengkap: ")
nim = input("Masukkan NIM: ")

harga = int(input("Masukkan harga menu makanan (Rp): "))

pajak_lele = harga * (5 / 100)
total_lele = harga + pajak_lele

pajak_mie = harga * (8 / 100)
total_mie = harga + pajak_mie

pajak_padang = harga * (10 / 100)
total_padang = harga + pajak_padang

print("\n")
print(nama, "dengan NIM", nim, "ingin membeli makanan seharga Rp", int(harga))
print("========================================")
print("Menu           Pajak     Total Bayar")
print("----------------------------------------")
print("Pecel Lele     5%        Rp", int(total_lele))
print("Mie Ayam       8%        Rp", int(total_mie))
print("Nasi Padang    10%       Rp", int(total_padang))
print("========================================")
