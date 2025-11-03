import inquirer
from utils.helpers import clear_screen
from .project_crud import tambah_proyek, lihat_proyek, hapus_proyek, pilih_dan_update_proyek

def menu_admin():
    while True:
        clear_screen()
        print("=== MENU ADMIN ===")
        pertanyaan = [
            inquirer.List("menu", message="Pilih tindakan:", choices=[
                "Tambah Proyek", "Lihat Proyek", "Update Proyek", "Hapus Proyek", "Logout"
            ])
        ]
        jawaban = inquirer.prompt(pertanyaan)
        pilihan = jawaban["menu"]

        if pilihan == "Tambah Proyek":
            tambah_proyek()
        elif pilihan == "Lihat Proyek":
            lihat_proyek()
        elif pilihan == "Update Proyek":
            pilih_dan_update_proyek()
        elif pilihan == "Hapus Proyek":
            hapus_proyek()
        elif pilihan == "Logout":
            break


def menu_pengguna(username):
    while True:
        clear_screen()
        print(f"=== MENU PENGGUNA ===")
        pertanyaan = [
            inquirer.List("menu", message="Pilih tindakan", choices=["Lihat Proyek", "Logout"])
        ]
        jawaban = inquirer.prompt(pertanyaan)
        pilihan = jawaban["menu"]

        if pilihan == "Lihat Proyek":
            lihat_proyek()
        elif pilihan == "Logout":
            break
