frutas = ["naranja", "limón", "pomelo", "líma"]

frutas.append("manzana")
frutas.insert(2, "durazno")
#frutas.remove("naranja")
frutas.pop(3)
if("sandia" in frutas):
    frutas.remove("sandia")

print(frutas)
print(frutas[2])


frutas[2] = "fresa"

print(frutas)
print(len(frutas))

frutas.extend(["maracuya", "sandia", "kiwi", "banana"])
print(frutas)
print(len(frutas))


frutas.sort(reverse=True)
#frutas.reverse()
for f in frutas:
    print(f)
