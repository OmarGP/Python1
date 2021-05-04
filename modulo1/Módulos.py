from datetime import datetime

#Buscar Género con función def:
def buscarMale(Item):
        if (Item.Genero == "Male"):
            return True
        else:
            return False

def buscarFemale(Item):
        if (Item.Genero == "Female"):
            return True
        else:
            return False

#def buscar

#Fin 
class Cliente:
    Identificador = None
    Nombre = None
    Apellidos = None
    Genero = None
    Pais = None
    Edad = None
    FechaAlta = None

    def __init__(self, id, nombre, apellidos) -> None:
        self.Identificador = id
        self.Nombre = nombre
        self.Apellidos = apellidos

    def ClienteId(Item):
        if (Item.Id == "1562"):
            return True
        else:
            return False
    
    
          
clientes = []
path = "modulo1\\fichero.txt"
file = open(path)

#Inicio del For
for linea in (file.readlines()):
    data = linea.split(",")
    if (data[0].isdigit() == True):
        #clientes.append(Cliente(data[7], data[1], data[2]))
        cliente = Cliente(data[7].strip(), data[1].strip(), data[2].strip())
        cliente.Genero = data[3].strip()
        cliente.Edad = int(data[5].strip())
        cliente.Pais = data[4].strip()
        cliente.FechaAlta = datetime.strptime(data[6].strip(), "%d/%m/%Y").date()
        clientes.append(cliente)
#Fin del For

file.close()
print(f"{len(clientes)} clientes importados.")

resultado = list(filter(lambda x : x.Identificador == "1562", clientes))
print(len(resultado))

print("===============================")

#print(f"{len(list(filter(buscarMale, clientes)))} clientes hombre")
#print(f"{len(list(filter(buscarFemale, clientes)))} clientes mujer")

print("===============================")

#Buscar Género con función lambda:
print(f"{len(list(filter(lambda x: x.Genero == 'Female', clientes)))} clientes mujer")
print(f"{len(list(filter(lambda x: x.Genero == 'Male', clientes)))} clientes hombre")
#FIN
print("===============================")
#Buscamos clientes menores de 26 años de Francia
print(f"{len(list(filter(lambda x: x.Edad < 26 and x.Pais == 'France', clientes)))}, clientes menores de 26 años de Francia")
#Buscamos clientes hombres de Estados Unidos
print(f"{len(list(filter(lambda x: (x.Genero == 'Male' and x.Pais == 'United States'), clientes)))}, clientes hombres de EEUU")
#Buscamos Mujeres Inglaterra mayores de 26 años
print(f"{len(list(filter(lambda x: (x.Genero == 'Female' and x.Pais == 'Great Britain' and x.Edad > 26), clientes)))}, clientes mujeres mayores de 26 años de Inglaterra")

print("===============================")


print("===============================")

#24 años / United States / Male
e = int(input("Edad: "))
p = input("Pais (France, United States, Great Britain): ")
g = input("Genero (Female o Male): ")
resultado = list(filter(lambda x: x.Edad == e and x.Pais == p and x.Genero == g, clientes))
print(f"{len(resultado)} clientes coincidentes.")

contador = 0
file2 = open("resultado.txt", "wt")
file2.write("Row,First Name,Last Name,Gender,Country,Age,Date,Id\n")

for item in resultado:
    contador += 1
    file2.write(f"{contador},{item.Nombre},{item.Apellidos}, {item.Genero}, {item.Pais}, {item.Edad}, {item.FechaAlta.strftime('%d/%m/%Y')}\n")

file2.close()