def login(username, password):
    print(f"Memverifikasi {username}...")
    if username == "admin" and password == "123":
        return True
    return False