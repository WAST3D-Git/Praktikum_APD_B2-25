buah = {"apel", "jeruk", "mangga", "apel"}
buah = (["apel", "jeruk", "mangga", "apel"])
print(buah)

angka_ganjil = {1, 3, 5, 7, 9}
for angka in angka_ganjil:
    print(angka, end="")

Daftar_buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}

print(Daftar_buku["Buku1"])
print(Daftar_buku)

List_game = dict(GTA5 = "Action", PUBG = "Battle Royale", DOTA2 = "MOBA")

Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {
"Instagram" : "daffahrhap"
}
}

print(f"nama saya adalah {Biodata["Nama"]}")
print(f"Instagram : {Biodata['Social Media']['Instagram']}")
print(f"nama saya adalah {Biodata.get["Nama"]}")
print(Biodata.get("Nama"))

Nilai = {
"Matematika": 80,
"B. Indonesia": 90,
"B. Inggris": 81,
"Kimia": 78,
"Fisika": 80
}
for i in Nilai:
    print(i)
print("") 

for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
print(Film)

Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})
print(Film)

Film["Sherlock Holmes"] = "Action"
Film.update({"The Conjuring" : "Tragedy"})
print(Film)

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
print(data)

del data["Nama"]
print(data)
print(data.get("Nama"))

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
print(data)

cache = data.pop("Nama")
print(data)

print(data.get("Nama"))
print(cache)

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
print(data)

data.clear()
print(data)

print("Jumlah Data = ", len(data))

buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}
pinjam = buku.copy()
print("Dictionary yang telah disalin : ", pinjam)

key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value)
print(buah)
{'apel': 1, 'jeruk': 1, 'mangga': 1}

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}

for i in Nilai.keys():
    print(i)
print("")
for i in Nilai.values():
    print(i)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
print(Nilai)
print("")
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
print("")

student = {
    "name": "Alice",
    "age": 21,
    "grades": {
        "math": 90,
        "science": 85,
        "history": 88
    }
}


print(student["name"])        
print(student["grades"]["math"]) 

outer_set = set()

inner_set1 = frozenset({1, 2, 3})
inner_set2 = frozenset({4, 5, 6})

outer_set.add(inner_set1)
outer_set.add(inner_set2)

print(outer_set)
