# # def inputNama():
# #     while True:
# #         try:
# #             nama = input("Masukkan nama anda:").strip()
# #             if not nama:
# #                 raise ValueError("Nama tidak boleh kosong")
# #             if nama.isspace():
# #                 raise ValueError("Nama tidak boleh hanya berisi spasi")
# #             return nama
# #         except ValueError as e:
# #             print(f"error: {e}")

# # inputNama()

# # def inputPassword():
# #     while True:
# #         try:
# #             password = input("Masukkan Password: ")

# #             if len(password) < 8:
# #                 raise ValueError("Password minimal 8 karakter")

# #             hasNumber = any(char.isdigit() for char in password)
# #             if not hasNumber:
# #                 raise ValueError("Password harus mengandung setidaknya satu angka")
            
# #             return password
        
# #         except ValueError as e:
# #             print(f"error: {e}")
# #             print("Kriteria Password:")
# #             print("- Minimal 8 karakter")
# #             print("- Mengandung setidaknya satu angka")

# # inputPassword()

# # def cariBarang():
# #     barang = {
# #         "A001": "Laptop",
# #         "A002": "Mouse",    
# #         "A003": "Keyboard",
# #         "A004": "Monitor",
# #     }

# #     while True:
# #         try: 
# #             kode = input("Masukkan kode barang: ")
# #             if kode not in barang:
# #                 raise KeyError("Kode barang tidak ditemukan")
            
# #             print(f"Barang dengan kode {kode}: {barang[kode]}")
# #             return barang[kode]
# #         except KeyError as e:
# #             print(f"error: {e}")

# # cariBarang()


# daftar_lomba = ["Programming Competition", "UI/UX Design", "Data Science", "Cyber Security"]
# peserta_lomba = {
#     "Programming Competition": [],
#     "UI/UX Design": [],
#     "Data Science": [],
#     "Cyber Security": []
# }

# def tampilkan_lomba():
#     print("\n--- DAFTAR LOMBA GEBYAR INFORMATIKA ---")
#     for i, lomba in enumerate(daftar_lomba, 1):
#         print(f"{i}. {lomba}")
#         print(f"   Jumlah peserta: {len(peserta_lomba[lomba])}")

# def tambah_peserta():
#     tampilkan_lomba()
    
#     try:
#         pilihan = int(input("\nPilih nomor lomba: ")) - 1
        
#         if pilihan < 0 or pilihan >= len(daftar_lomba):
#             print("Pilihan tidak valid!")
#             return
        
#         lomba_terpilih = daftar_lomba[pilihan]
#         nama_peserta = input("Masukkan nama peserta: ")
        
#         peserta_lomba[lomba_terpilih].append(nama_peserta)
#         print(f"Peserta {nama_peserta} berhasil ditambahkan ke lomba {lomba_terpilih}!")
        
#     except ValueError:
#         print("Input harus berupa angka!")

# def tampilkan_menu():
#     print("\n=== SISTEM MANAJEMEN LOMBA ===")
#     print("1. Tampilkan Daftar Lomba")
#     print("2. Tambah Peserta")
#     print("3. Tampilkan Peserta per Lomba")
#     print("4. Keluar")

# def tampilkan_peserta():
#     tampilkan_lomba()
    
#     try:
#         pilihan = int(input("\nPilih nomor lomba untuk melihat peserta: ")) - 1
        
#         if pilihan < 0 or pilihan >= len(daftar_lomba):
#             print("Pilihan tidak valid!")
#             return
        
#         lomba_terpilih = daftar_lomba[pilihan]
#         peserta = peserta_lomba[lomba_terpilih]
        
#         print(f"\n--- PESERTA LOMBA {lomba_terpilih} ---")
#         if peserta:
#             for i, nama in enumerate(peserta, 1):
#                 print(f"{i}. {nama}")
#         else:
#             print("Belum ada peserta yang terdaftar.")
            
#     except ValueError:
#         print("Input harus berupa angka!")

# def main_gebyar_informatika():
#     while True:
#         tampilkan_menu()
#         pilihan = input("Pilih menu (1-4): ")
        
#         if pilihan == "1":
#             tampilkan_lomba()
#         elif pilihan == "2":
#             tambah_peserta()
#         elif pilihan == "3":
#             tampilkan_peserta()
#         elif pilihan == "4":
#             print("Terima kasih telah menggunakan sistem!")
#             break

# main_gebyar_informatika()

def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def program_konversi_suhu():
    print("=== KONVERSI SUHU CELCIUS KE FAHRENHEIT ===")
    
    try:
        suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))
        suhu_fahrenheit = celcius_ke_fahrenheit(suhu_celcius)
        print(f"{suhu_celcius}°C = {suhu_fahrenheit:.2f}°F")
    except ValueError:
        print("Error: Input harus berupa angka!")

program_konversi_suhu()