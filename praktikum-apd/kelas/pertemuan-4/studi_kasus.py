#KPK dan FPB
x = int(input("Masukkan berapa hari fatin masuk: "))
y = int(input("Masukkan berapa hari fani masuk: "))

a = x
b = y
while b != 0:
    sisa = a % b
    a = b   
    b = sisa
fpb = a
print(fpb)
kpk = (x * y) // fpb
print("Fatin dan Fani akan masuk bersama setiap", kpk, "hari")

#Segitiga Sama Kaki
n = int(input("Masukkan tinggi segitiga sama kaki: "))
print("\nSegitiga sama kaki:")
for i in range(1, n + 1):
    for j in range (n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

#Segitiga Sama Kaki Terbalik
m = int(input("Masukkan tinggi segitiga samas kaki terbalik: "))
print("\nSegitiga sama kaki terbalik: ")
for i in range (m, 0, -1):
    for j in range(m-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()
