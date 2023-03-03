database = {}

with open("database.txt", "r") as file:
    icerik = file.readlines()
    

for i in range(len(icerik)): #\n kaldırma
    if "\n" in icerik[i]:
        index = icerik[i].find("\n")
        icerik[i] = icerik[i][0:index]

for i in icerik: #sözlüğü değiştirme
    j = i.split(" : ")
    database.update({j[0]:j[1]})

def ekle():
    with open("database.txt", "w") as file:
        file.write("")
    with open("database.txt", "a") as file:
        for key in database.keys():
            value = database[key]
            file.write(key + " : " + value)
