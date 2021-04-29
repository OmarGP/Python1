class Cliente:
    Identificador = None
    Nombre = None
    Apellidos = None
    Genero = None
    Pais = None
    FechaNacimiento = None

    def __init__(self, id, nombre, apellidos) -> None:
        self.Identificador = id
        self.Nombre = nombre
        self.Apellidos = apellidos
    
    
clientes = []
path = "modulo2\\fichero.txt"
file = open(path)

for linea in (file.readlines()):
    data = linea.split(",")
    if (data[0].isdigit() == True):
        #clientes.append(Cliente(data[7], data[1], data[2]))
        cliente = Cliente(data[7], data[1], data[2])
        clientes.append(cliente)


file.close
print(f"{len(clientes)} clientes importados.")

#for c in clientes:
    #print(c.Nombre)

while (True):
    posicion = int(input("Dime una posición: "))
    print(f"{clientes[posicion].Nombre} {clientes[posicion].Apellidos}")

    break

print(type(clientes))

print("FIN")