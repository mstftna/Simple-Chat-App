import json
database = {}
if __name__ == '__main__':
    print(dir(json))

elif __name__ != '__main__':
    with open("database.json", "r") as file:
        database = json.loads(file.read())

def ekle():
    with open ("database.json", "w", encoding="utf8") as file:
        file.write(json.dumps(database, indent=4, sort_keys=True, ensure_ascii=False))