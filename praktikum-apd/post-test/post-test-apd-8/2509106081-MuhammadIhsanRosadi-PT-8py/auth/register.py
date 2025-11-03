from tinydb import Query
from database.db_config import users_table
from utils.helpers import clear_screen, pause

def register():
    clear_screen()
    print("=== REGISTER ===")
    username = input("Username baru: ")
    password = input("Password: ")

    if not username or not password:
        print("Username dan password wajib diisi.")
    elif users_table.get(Query().username == username):
        print("Username sudah digunakan.")
    else:
        users_table.insert({"username": username, "password": password, "role": "user"})
        print("Akun berhasil dibuat.")
    pause()
