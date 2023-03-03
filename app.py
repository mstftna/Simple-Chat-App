from data import *

a = input("Bir şey yazın: ")
if a in database:
    print(database[a])
else:
    verilecek_cevap = input(f"Birisi {a} dediğinde ne demeliyim: ")
    database[a] = verilecek_cevap
    ekle()
print(database)
