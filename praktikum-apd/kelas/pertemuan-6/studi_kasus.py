
mahasiswa = {
    "2509106081": {"nama": "Rosadi", "kelas": "25-A", "IPK": 3.7},
    "2509106888": {"nama": "Ihsan", "kelas": "25-B", "IPK": 3.6}
}

for nim in mahasiswa:
    print("NIM:", nim)
    for key in mahasiswa[nim]:
        print(key, ":", mahasiswa[nim][key])
    print("-----------")
