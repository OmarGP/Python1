import pickle
import os

if (os.name == "nt"):
    os.system("cls")
else:
    os.system("clear")


file = open(".\\Ficheros\\clientes.json", "rt", encoding='UTF-8')
contenido = file.read()
file.close()

file2 = open(".\\Ficheros\\clientes.bin", "wb")
pickle.dump(contenido, file2)
file2.close()

t1 = "Texto de prueba"
file3 = open(".\\Ficheros\\demo.txt", "wt")
file3.write(t1)
file3.close()

print("========================================")

texto = "En un lugar de la mancha de cuyo ..."

textoBytes1 = texto.encode()
textoBytes2 = bytes(texto, "utf-8")
textoBytes3 = "En un lugar de la mancha de cuyo ..."

print(type(textoBytes1))
print(type(textoBytes2))
print(type(textoBytes3))

print(textoBytes1)
print(textoBytes2)
print(textoBytes3)

print(textoBytes1.hex())
print(textoBytes2.hex())
print(textoBytes3.hex())

for c in textoBytes1:
    print(c, end=" ")

file4 = open(".\\Ficheros\\demoBytes.txt", "wb")
file4.write(textoBytes1.hex())
file2.close()

os.remove(".\\Ficheros\\demoBytes.txt")