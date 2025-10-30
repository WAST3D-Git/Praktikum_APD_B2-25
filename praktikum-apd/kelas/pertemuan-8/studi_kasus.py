import random

def buat_kata_sandi():
    karakter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    kata_sandi = ''.join(random.choice(karakter) for _ in range(12))
    return kata_sandi

print("Kata sandi baru:", buat_kata_sandi())

from datetime import datetime

waktu_sekarang = datetime.now()
waktu_format_id = waktu_sekarang.strftime("%d/%m/%Y, %H:%M:%S")

print("Waktu sekarang:", waktu_format_id)
