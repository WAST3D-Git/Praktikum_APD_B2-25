import math
import random
from datetime import datetime
import inquirer

num = int("42") 
name = str(123) 
data = list("abc") 
data = dict(a=1, b=2) 

print(type(num))

abs(-9) 
max([1, 3, 7]) 
min([1, 3, 7]) 
round(3.14159,2) 
sum([1, 2, 3]) 

for i, v in enumerate(['a','b']):
    print(i, v) 
len([10, 20, 30]) 
list(map(str, [1,2,3])) 
sorted([3, 1, 2]) 
list(zip([1,2],['a','b'])) 

x = 42
def fungsi():
    x = 10
    y = 20
    z = 30
    print(globals()['x']) 
    print(locals()['x']) 
    print(locals()) 
fungsi()

print(math.sqrt(16))
print(math.factorial(4))

print(random.randint(1, 5)) 
pilih_acak = ["pisang", "rambutan", "manggis"]
acak = "apcb"
print(random.choice(pilih_acak)) 
print(random.choice(acak)) 
kumpulan_angka = "1234567890"
hasil = ""
for i in range(4):
    hasil += random.choice(kumpulan_angka)
print(hasil)

acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
random.shuffle(acak_kartu)
print(acak_kartu)

print(datetime.now())


pertanyaan = [
inquirer.List(
'size',
message="What size do you need?",
choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
),
]
answer = inquirer.prompt(pertanyaan)
print(answer) 
print(answer['size'])


data = {
'nama': [],
'nim': [],
'no_hp': []
}
def tambahData():
    questions = [
inquirer.Text('nama', message="Input nama mu"),
inquirer.Text('nim', message="Input NIM kamu"),
inquirer.Text('no_hp', message="Input nomor hp kamu",)
]
    answers = inquirer.prompt(questions) 

    data['nama'].append(answers['nama'])
    data['nim'].append(answers['nim'])
    data['no_hp'].append(answers['no_hp'])
tambahData()

print(f"List nama:")
for i, nama in enumerate(data['nama']):
    print(f"{i+1}. {nama}")
print(f"List NIM:")
for i, nim in enumerate(data['nim']):
    print(f"{i+1}. {nim}")  
print(f"List No HP:")
for i, no_hp in enumerate(data['no_hp']):
    print(f"{i+1}. {no_hp}")