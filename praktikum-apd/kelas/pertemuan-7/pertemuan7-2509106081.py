def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas Persegi Panjang dengan panjang", panjang, "dan lebar", lebar, "adalah:", luas)

luas_persegi_panjang(4, 5)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

print ("Luas persegi :", luas_persegi(8))


def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
print ("Volume Persegi = ", volume)

luas_persegi(4)
volume_persegi(6)

Nama = "Hambali"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

def info():
    Nama = "Informatika"
    Mata_Kuliah = "Logika Informatika"

print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

info()


Nama = "Hambali"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"

def info():
    Nama = "Informatika"
    Mata_Kuliah = "Logika Informatika"

print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

print("Prodi:", Nama)
print("Mata Kuliah:", Mata_Kuliah)

info()

def menu():
    print("=== Menu Utama ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")
    return pilihan

def tambah_data():
    print("Menambahkan data")
    print("Data berhasil ditambahkan")
    
def hapus_data():
    print("Menghapus data")
    print("Data berhasil dihapus")

def tampilkan_data():
    print("Menampilkan data")
    print("Data ditampilkan")

while True:
    pilihan = menu()
    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        hapus_data()
    elif pilihan == '3':
        tampilkan_data()
    elif pilihan == '4':
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")


def derivative_at_point(f, a):
    h = 1e-5
    derivative = (f(a + h) - f(a)) / h
    return derivative

derivative_at_point(lambda x: x**2, 3) 

def integral_approximation(f, a, b, n):
    def rectangle_area(f, x, width):
        return f(x) * width
        def integral_approximation(f, a, b, n):
            width = (b - a) / n
            total_area = 0
            for i in range(n):
                x = a + i * width
                total_area += rectangle_area(f, x, width)
            return total_area
            def integral_approximation(f, a, b, n):
                width = (b - a) / n
                total_area = 0
                for i in range(n):
                    x = a + i * width
                    total_area += rectangle_area(f, x, width)
                return total_area
            
integral_approximation(lambda x: x**2, 0, 1, 1000)

try:
    angka = int(input("Masukkan sebuah angka: "))
    if angka < 0:
        raise ValueError("Angka tidak boleh negatif.")
except ValueError as ve:
    print("Terjadi kesalahan:", ve)
else:
    print("Anda memasukkan angka:", angka)

try:
    while True:
        print("Program berjalan... tekan Ctrl+C untuk berhenti")
except KeyboardInterrupt:
    print("\n✅ Program dihentikan oleh user")