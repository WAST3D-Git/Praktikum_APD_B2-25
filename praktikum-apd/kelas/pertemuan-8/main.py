from autentikasi import login
from create import tambah_data_siswa
print("Selamat datang di aplikasi!")

if login("admin", "123"):
    print("Login berhasil!")
    tambah_data_siswa({"nama": "Budi", "nilai": 90})
else:
    print("Login gagal!")