import inquirer
from utils.helpers import clear_screen
from auth.login import login
from auth.register import register

def tampilkan_menu_awal():
    clear_screen()
    print("=== SISTEM MANAJEMEN PROYEK DESAIN GRAFIS ===")
    pertanyaan = [
        inquirer.List("menu", message="Pilih menu:", choices=["Login", "Register", "Keluar"])
    ]
    jawaban = inquirer.prompt(pertanyaan)
    return jawaban["menu"]

def main():
    while True:
        pilihan = tampilkan_menu_awal()
        if pilihan == "Login":
            login()
        elif pilihan == "Register":
            register()
        elif pilihan == "Keluar":
            clear_screen()
            print("Terima kasih telah menggunakan program ini.")
            break

if __name__ == "__main__":
    main()
