from tinydb import Query
from database.db_config import users_table
from utils.helpers import clear_screen, pause
from projects.project_menu import menu_admin, menu_pengguna

def login():
    clear_screen()
    print("=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    user = users_table.get((Query().username == username) & (Query().password == password))

    if not user:
        print("Login gagal! Username atau password salah.")
        pause()
        return

    if user["role"] == "admin":
        menu_admin()
    else:
        menu_pengguna(user["username"])
