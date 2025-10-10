praktikum = ["Mahasiswa", 20, True, 45.10, 
             [[True, False], "APD", 25], ['list', 100, False]]
praktikum2 = ["Mahasiswa", 20, True, 45.10, 
             [[True, False], "APD", 25], ['list', 100, False]]
praktikum3 = [
    [True, False],
    [86, 90, 100],
    ['Data', 'Science', 'Kelas'],
]

praktikum.append("86")
praktikum[4][0].append("Kelas")
praktikum.insert(2, "Data")
praktikum.append(["Sains", 50])
praktikum.insert(3, "Hello")
praktikum[2] = "Data Science"
del praktikum[2]
praktikum.remove("Hello")
praktikum.pop()
last = praktikum.pop(5)
print(praktikum)
print(praktikum[0])
print(praktikum[5])
print(praktikum[5][1])
print(praktikum[::-1])
print(praktikum[1:2:2])
print(praktikum + praktikum2)
print(praktikum * 3)
for i in praktikum3[1]:
    for j in praktikum3[2]:
        print(i, j, end=", ")

anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
liststudy=list(studyclub)
liststudy.append("Web")
liststudy.insert(2,"Web")
studyclub=tuple(liststudy)
print(studyclub)
print(studyclub)
print(anggota)
print(anggota[1])
print(anggota[-1])


