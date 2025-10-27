import os

users = [
    {"username": "mihsanr81", "password": "2509106081", "role": "admin"}
]
projects = []
user_ditemukan = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Tekan Enter Untuk Melanjutkan...")

def tampilkan_menu_awal():
    clear_screen()
    print("=== SISTEM MANAJEMEN PROYEK DESAIN GRAFIS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    return input("Pilih menu: ")

def lihat_proyek():
    clear_screen()
    print("=== DAFTAR PROYEK ===")
    if len(projects) == 0:
        print("Belum ada proyek.")
    else:
        for i, p in enumerate(projects):
            print(f"\n[{i+1}] {p['judul']}")
            print(f"Deskripsi: {p['deskripsi']}")
            print(f"Software : {p['software']}")
            print(f"Deadline : {p['deadline']}")
            print(f"Klien    : {p['klien']}")
            print(f"Status   : {p['status']}")
    pause()

def tambah_proyek(username):
    global projects
    clear_screen()
    print("=== TAMBAH PROYEK ===")
    try:
        judul = input("Judul: ")
        deskripsi = input("Deskripsi: ")
        software = input("Software: ")
        deadline = input("Deadline: ")
        klien = input("Klien: ")
        status = input("Status: ")

        if judul == "" or klien == "":
            raise ValueError("Judul dan Klien wajib diisi!")

        project_baru = {
            "judul": judul,
            "deskripsi": deskripsi,
            "software": software,
            "deadline": deadline,
            "klien": klien,
            "status": status
        }
        projects.append(project_baru)
        print("Proyek berhasil ditambah!")
    except ValueError as e:
        print(e)
    finally:
        pause()

def update_proyek(index):
    global projects
    try:
        if len(projects) == 0:
            raise Exception("Belum ada proyek untuk diubah.")
        if not (0 <= index < len(projects)):
            raise IndexError("Nomor proyek tidak valid!")

        while True:
            clear_screen()
            print(f"=== UBAH PROYEK: {projects[index]['judul']} ===")
            print("1. Judul")
            print("2. Deskripsi")
            print("3. Software")
            print("4. Deadline")
            print("5. Klien")
            print("6. Status")
            print("7. Selesai Update")
            pilih = input("Pilih data yang ingin diubah: ")

            if pilih == "1":
                projects[index]["judul"] = input("Masukkan judul baru: ")
            elif pilih == "2":
                projects[index]["deskripsi"] = input("Masukkan deskripsi baru: ")
            elif pilih == "3":
                projects[index]["software"] = input("Masukkan software baru: ")
            elif pilih == "4":
                projects[index]["deadline"] = input("Masukkan deadline baru: ")
            elif pilih == "5":
                projects[index]["klien"] = input("Masukkan nama klien baru: ")
            elif pilih == "6":
                projects[index]["status"] = input("Masukkan status baru: ")
            elif pilih == "7":
                break
            else:
                print("Pilihan tidak valid!")
                pause()
        print("Data proyek berhasil diperbarui!")
    except Exception as e:
        print(e)
    finally:
        pause()

def hapus_proyek():
    global projects
    clear_screen()
    print("=== HAPUS PROYEK ===")
    try:
        if len(projects) == 0:
            raise Exception("Belum ada proyek.")
        for i, p in enumerate(projects):
            print(f"[{i+1}] {p['judul']}")
        nomor = input("Pilih nomor proyek: ")
        if not nomor.isdigit():
            raise ValueError("Input harus angka.")

        nomor = int(nomor) - 1
        if not (0 <= nomor < len(projects)):
            raise IndexError("Nomor tidak valid.")

        hapus = input(f"Hapus proyek '{projects[nomor]['judul']}'? (y/n): ").lower()
        if hapus == "y":
            del projects[nomor]
            print("Proyek dihapus!")
        else:
            print("Dibatalkan.")
    except (ValueError, IndexError, Exception) as e:
        print(e)
    finally:
        pause()

def pilih_dan_update_proyek():
    clear_screen()
    print("=== UBAH PROYEK ===")
    if len(projects) == 0:
        print("Belum ada proyek.")
        pause()
        return
    for i, p in enumerate(projects):
        print(f"[{i+1}] {p['judul']}")
    nomor = input("\nPilih nomor proyek: ")
    if nomor.isdigit():
        update_proyek(int(nomor) - 1)
    else:
        print("Input harus angka!")
        pause()

def menu_admin():
    clear_screen()
    print("=== MENU ADMIN ===")
    print("1. Tambah Proyek")
    print("2. Lihat Proyek")
    print("3. Update Proyek")
    print("4. Hapus Proyek")
    print("5. Logout")

    pilih = input("Pilih: ")

    if pilih == "1":
        tambah_proyek(user_ditemukan["username"])
    elif pilih == "2":
        lihat_proyek()
    elif pilih == "3":
        pilih_dan_update_proyek()
    elif pilih == "4":
        hapus_proyek()
    elif pilih == "5":
        return
    else:
        print("Pilihan tidak valid!")
        pause()

    menu_admin()

def login():
    global user_ditemukan
    clear_screen()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    user_ditemukan = None
    for u in users:
        if u["username"] == username and u["password"] == password:
            user_ditemukan = u
            break

    if user_ditemukan is None:
        print("Login gagal! Username atau password salah.")
        pause()
        return

    if user_ditemukan["role"] == "admin":
        menu_admin()
    else:
        menu_pengguna()

def register():
    clear_screen()
    print("=== REGISTER ===")
    username = input("Username baru: ")
    password = input("Password: ")
    sudah_ada = any(u["username"] == username for u in users)

    if username == "" or password == "":
        print("Username dan password wajib diisi!")
    elif sudah_ada:
        print("Username sudah digunakan!")
    else:
        users.append({"username": username, "password": password, "role": "user"})
        print("Akun berhasil dibuat!")
    pause()

def menu_pengguna():
    while True:
        clear_screen()
        print(f"=== MENU PENGGUNA ({user_ditemukan['username']}) ===")
        print("1. Lihat Proyek")
        print("2. Logout")
        pilih_user = input("Pilih: ")

        if pilih_user == "1":
            lihat_proyek()
        elif pilih_user == "2":
            break
        else:
            print("Pilihan tidak valid!")
            pause()

def main():
    while True:
        menu = tampilkan_menu_awal()
        if menu == "1":
            login()
        elif menu == "2":
            register()
        elif menu == "3":
            clear_screen()
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid!")
            pause()

main()
