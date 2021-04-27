valor = 0
while (valor < 5):
    if (valor == 3):
        continue
    print(f"Valor: {valor}")
    valor = valor + 1
    #valor += 1


print("Fin del While")


citricos = ["naranja", "limón", "pomelo", "líma"]


for fruta in citricos:
    print(fruta)
print("======================================================================")

for index in range (len(citricos)):
    print(citricos[index])