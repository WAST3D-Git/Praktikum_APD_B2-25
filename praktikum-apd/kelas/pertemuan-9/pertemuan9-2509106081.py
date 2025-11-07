import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

plt.figure(figsize=(12, 6))
plt.xlabel('kasih nama Sumbu X')
plt.ylabel('kasih nama Sumbu Y')
plt.title("Ini judul loh")
plt.grid(True)

x = [1, 2, 3, 4, 5]
y = [10, 35, 20, 70, 60]

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("Contoh Grafik")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.grid(True)
plt.show()

x = [1, 2, 3, 4, 5]
y = [10, 35, 20, 70, 60]
y2 = [12, 43, 56, 23, 67]

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker="o", color="blue", label="Matematika")
plt.plot(x, y2, color="red", marker="h", linestyle="--", label="Fisika")
plt.title("Contoh Grafik")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.grid(True)
plt.legend()
plt.show()
plt.savefig("Real_Penggunaan.png")

kategori = ['Python', 'Assembly', 'Java', 'C++']
jumlah_pengguna = [100, 10, 50, 70]

plt.figure(figsize=(8, 5))
plt.bar(kategori, jumlah_pengguna)
plt.xlabel("Nama Bahasa Pemrograman")
plt.ylabel("Banyak Pengguna")
plt.title("Perbandingan Popularitas Bahasa Pemrograman")
plt.grid(axis="y", alpha=0.5, linestyle="--")
plt.show()

fisika_kelompok1 = [85, 88, 90, 92, 87]
matematika_kelompok1 = [60, 58, 55, 62, 59]
fisika_kelompok2 = [65, 68, 70, 72, 69]
matematika_kelompok2 = [80, 85, 82, 88, 84]

plt.figure(figsize=(8, 5))
plt.scatter(fisika_kelompok1, matematika_kelompok1, marker="o", label="Kelompok 1")
plt.scatter(fisika_kelompok2, matematika_kelompok2, marker="*", label="Kelompok 2")
plt.title("Perbandingan Nilai Fisika dan Matematika")
plt.xlabel("Nilai Fisika")
plt.ylabel("Nilai Matematika")
plt.legend(loc="lower left")
plt.grid(True, alpha=0.5)
plt.show()

views = [320, 450, 400, 390, 410, 470, 500, 490, 480, 510,
         530, 600, 620, 590, 550, 570, 610, 640, 700, 5000,
         1000, 2000, 800, 700, 750]

plt.figure(figsize=(7, 4))
plt.boxplot(views, vert=False)
plt.xlabel('Number of Views')
plt.ylabel('Instagram')
plt.grid(axis='y', alpha=0.5)
plt.show()

views_series = pd.Series(views)
views_clean = views_series[views_series < 1000]
print("Data tanpa outlier:", views_clean.values)

iris = sns.load_dataset("iris")

plt.figure(figsize=(8, 5))
plt.hist(iris["sepal_length"], bins=15, color="skyblue", edgecolor="black", alpha=0.7)
plt.title("Distribusi Panjang Sepal (sepal_length)")
plt.xlabel("Sepal Length")
plt.ylabel("Frekuensi")
plt.grid(axis='y', alpha=0.5)
plt.show()

nilai = [65, 70, 75, 80, 85, 90, 92, 95, 60, 78, 83, 88, 77, 69, 91, 85, 74, 72, 68, 66]

plt.figure(figsize=(8, 5))
plt.hist(nilai, bins=10, color="lightgreen", edgecolor="black", alpha=0.7)
plt.title("Distribusi Nilai Ujian Kelas")
plt.xlabel("Nilai")
plt.ylabel("Frekuensi")
plt.grid(axis='y', alpha=0.5)
plt.show()

tinggi_A = [165, 170, 172, 168, 166]
berat_A = [55, 58, 60, 57, 54]

tinggi_B = [175, 178, 180, 176, 177]
berat_B = [68, 70, 72, 69, 71]

plt.figure(figsize=(8, 5))
plt.scatter(tinggi_A, berat_A, marker="o", label="Kelompok A")
plt.scatter(tinggi_B, berat_B, marker="*", label="Kelompok B")
plt.title("Hubungan Tinggi dan Berat Badan Mahasiswa")
plt.xlabel("Tinggi Badan (cm)")
plt.ylabel("Berat Badan (kg)")
plt.legend()
plt.grid(True, alpha=0.5)
plt.show()
