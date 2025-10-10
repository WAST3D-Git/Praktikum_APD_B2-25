keranjang = ["Brokoli", "Apel", "Jamur", "Nanas", "Wortel", "Kiwi", "Kol", "Sawi", "Lobak"]
buah = ["Apel", "Nanas", "Kiwi"]
buah_saja = [item for item in keranjang if item in buah]
print(buah_saja)



data = ("Ajiva", "Membaca", 21, ["Matematika", "Pemrograman", "Fisika"])
data_terbalik = data[::-1]
print(data_terbalik)

matkul, umur, hobi, nama = data_terbalik
print(nama)
print(hobi)
print(umur)
print(matkul)
