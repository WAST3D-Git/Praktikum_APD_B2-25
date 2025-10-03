angka = 2
if angka > 5:
    print("Angka lebih besar dari 5.")
elif angka == 5:
    print("Angka sama dengan 5.")   
else:
    print("Angka tidak lebih besar dari 5.")


nilai = float(input("Masukkan nilai: "))  
if nilai >= 90:
    print("A")
elif nilai >= 80:
    print("B")
elif nilai >= 70:
    print("C")  
elif nilai >= 60:
    print("D")  
else:
    print("E")

harga = float(input("Masukkan harga Pecel Lele: "))

pajak = harga * 0.1
total = harga + pajak

print(f"Harga Pecel Lele: {total}")

ternary = "Genap" if angka % 2 == 0 else "Ganjil"
print(ternary)

lambda_genap = lambda x: "Genap" if x % 2 == 0 else "Ganjil"
print(lambda_genap(angka))

class Nilai:
    def __init__(self, nilai):
        self.nilai = nilai 
    def cek_nilai(self):
        if self.nilai >= 90:
            return "A"
        elif self.nilai >= 80:
            return "B"
        elif self.nilai >= 70:
            return "C"  
        elif self.nilai >= 60:
            return "D"  
        else:
            return "E"
        
nilai_akhir = Nilai(85)
print(nilai_akhir.cek_nilai())

