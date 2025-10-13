import os

users = [["mihsanr81", "2509106081", "admin"]] 
projects = [] 

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== SISTEM MANAJEMEN PROYEK DESAIN GRAFIS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    # LOGIN
    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ")
        password = input("Password: ")
        user_ditemukan = None

        for u in users:
            if u[0] == username and u[1] == password:
                user_ditemukan = u
                break

        if user_ditemukan == None:
            print("Login gagal! Username atau password salah.")
            input("Tekan Enter Untuk Melanjutkan...")
            continue

        # ADMIN
        if user_ditemukan[2] == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=== MENU ADMIN ===")
                print("1. Tambah Proyek")
                print("2. Lihat Proyek")
                print("3. Update Proyek")
                print("4. Hapus Proyek")
                print("5. Logout")
                pilih = input("Pilih: ")

                # CREATE
                if pilih == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH PROYEK ===")
                    judul = input("Judul: ")
                    deskripsi = input("Deskripsi: ")
                    software = input("Software: ")
                    deadline = input("Deadline: ")
                    klien = input("Klien: ")
                    status = input("Status: ")
                    if judul != "" and klien != "":
                        projects.append([judul, deskripsi, software, deadline, klien, status])
                        print("Proyek berhasil ditambah!")
                    else:
                        print("Wajib diisi!")
                    input("Tekan Enter Untuk Melanjutkan...")

                # READ
                elif pilih == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR PROYEK ===")
                    if len(projects) == 0:
                        print("Belum ada proyek.")
                    else:
                        for i, p in enumerate(projects):
                            print(f"\n[{i+1}] {p[0]}")
                            print(f"Deskripsi: {p[1]}")
                            print(f"Software : {p[2]}")
                            print(f"Deadline : {p[3]}")
                            print(f"Klien    : {p[4]}")
                            print(f"Status   : {p[5]}")
                    input("\nTekan Enter Untuk Melanjutkan...")

                # UPDATE
                elif pilih == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UBAH PROYEK ===")
                    if len(projects) == 0:
                        print("Belum ada proyek.")
                        input("Tekan Enter Untuk Melanjutkan...")
                        continue

                    for i, p in enumerate(projects):
                        print(f"[{i+1}] {p[0]}")

                    nomor = input("\nPilih nomor proyek: ")
                    if nomor.isdigit():
                        nomor = int(nomor) - 1
                        if 0 <= nomor < len(projects):
                            while True:
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"=== UBAH PROYEK: {projects[nomor][0]} ===")
                                print("1. Judul")
                                print("2. Deskripsi")
                                print("3. Software")
                                print("4. Deadline")
                                print("5. Klien")
                                print("6. Status")
                                print("7. Selesai Update")
                                pilih_update = input("Pilih data yang ingin diubah: ")

                                if pilih_update == "1":
                                    projects[nomor][0] = input("Masukkan judul baru: ")
                                elif pilih_update == "2":
                                    projects[nomor][1] = input("Masukkan deskripsi baru: ")
                                elif pilih_update == "3":
                                    projects[nomor][2] = input("Masukkan software baru: ")
                                elif pilih_update == "4":
                                    projects[nomor][3] = input("Masukkan deadline baru: ")
                                elif pilih_update == "5":
                                    projects[nomor][4] = input("Masukkan nama klien baru: ")
                                elif pilih_update == "6":
                                    projects[nomor][5] = input("Masukkan status baru: ")
                                elif pilih_update == "7":
                                    break
                                else:
                                    print("Pilihan tidak valid!")
                                    input("Tekan Enter Untuk Melanjutkan...")

                            print("Data proyek berhasil diperbarui!")
                        else:
                            print("Nomor proyek tidak valid!")
                    else:
                        print("Input harus angka!")
                    input("Tekan Enter Untuk Melanjutkan...")

                # DELETE
                elif pilih == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS PROYEK ===")
                    if len(projects) == 0:
                        print("Belum ada proyek.")
                        input("Tekan Enter Untuk Melanjutkan...")
                        continue
                    for i, p in enumerate(projects):
                        print(f"[{i+1}] {p[0]}")
                    nomor = input("Pilih nomor proyek: ")
                    if nomor.isdigit():
                        nomor = int(nomor) - 1
                        if 0 <= nomor < len(projects):
                            hapus = input(f"Hapus proyek '{projects[nomor][0]}'? (y/n): ").lower()
                            if hapus == "y":
                                del projects[nomor]
                                print("Proyek dihapus!")
                            else:
                                print("Dibatalkan.")
                        else:
                            print("Nomor tidak valid.")
                    else:
                        print("Input harus angka.")
                    input("Tekan Enter Untuk Melanjutkan...")

                elif pilih == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter Untuk Melanjutkan...")

        # USER BIASA
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"=== MENU PENGGUNA ({user_ditemukan[0]}) ===")
                print("1. Lihat Proyek")
                print("2. Logout")
                pilih_user = input("Pilih: ")

                if pilih_user == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR PROYEK ===")
                    if len(projects) == 0:
                        print("Belum ada proyek.")
                    else:
                        for i, p in enumerate(projects):
                            print(f"\n[{i+1}] {p[0]}")
                            print(f"Deskripsi: {p[1]}")
                            print(f"Software : {p[2]}")
                            print(f"Deadline : {p[3]}")
                            print(f"Klien    : {p[4]}")
                            print(f"Status   : {p[5]}")
                    input("\nTekan Enter Untuk Melanjutkan...")
                elif pilih_user == "2":
                    break
                else:
                    print("Pilihan tidak valid!")
                    input("Tekan Enter Untuk Melanjutkan...")

    # REGISTER
    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER ===")
        username = input("Username baru: ")
        password = input("Password: ")
        sudah_ada = False
        for u in users:
            if u[0] == username:
                sudah_ada = True
                break
        if username == "" or password == "":
            print("Username dan password wajib diisi!")
        elif sudah_ada:
            print("Username sudah digunakan!")
        else:
            users.append([username, password, "user"])
            print("Akun berhasil dibuat!")
        input("Tekan Enter Untuk Melanjutkan...")

    # KELUAR
    elif menu == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter Untuk Melanjutkan...")
