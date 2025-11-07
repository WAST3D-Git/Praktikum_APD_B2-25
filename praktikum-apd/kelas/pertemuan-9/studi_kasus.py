import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

nilai = [65, 70, 75, 80, 85, 90, 92, 95, 60, 78, 83, 88, 77, 69, 91, 85, 74, 72, 68, 66]

df_nilai = pd.DataFrame({'Nilai': nilai})

plt.figure(figsize=(8, 5))
plt.hist(df_nilai['Nilai'], bins=np.arange(60, 101, 5), edgecolor='black', alpha=0.7)
plt.title("Histogram Nilai Ujian Kelas", fontsize=14)
plt.xlabel("Nilai Ujian", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

tinggi_A = [165, 170, 172, 168, 166]
berat_A = [55, 58, 60, 57, 54]
tinggi_B = [175, 178, 180, 176, 177]
berat_B = [68, 70, 72, 69, 71]

df_A = pd.DataFrame({'Kelompok': 'A', 'Tinggi': tinggi_A, 'Berat': berat_A})
df_B = pd.DataFrame({'Kelompok': 'B', 'Tinggi': tinggi_B, 'Berat': berat_B})

df_all = pd.concat([df_A, df_B])

plt.figure(figsize=(8, 5))
plt.scatter(df_A['Tinggi'], df_A['Berat'], marker='o', label='Kelompok A')
plt.scatter(df_B['Tinggi'], df_B['Berat'], marker='s', label='Kelompok B')
plt.title("Hubungan Tinggi dan Berat Badan Mahasiswa", fontsize=14)
plt.xlabel("Tinggi Badan (cm)", fontsize=12)
plt.ylabel("Berat Badan (kg)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
