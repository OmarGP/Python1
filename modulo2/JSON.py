import json

citricos = ["naranja", "limón", "pomelo", "líma"]
listaJSON = json.dumps(citricos)

print(citricos)
print(citricos[2])
print(type(citricos))
print(listaJSON)
print(listaJSON[2])
print(type(listaJSON))

dias = json.loads('["]')