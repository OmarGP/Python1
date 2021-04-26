a =10
b = 100

print(a>b)
if (a>b):
        #Inicio del bloque de sentencias cuando es TRUE
        print("A es mayor de 100")
        #Fin del bloque de sentencias
elif (a>b):
        #Inicio del bloque de sentencias cuando es TRUE
        print("A es mayor de 100")
        #Fin del bloque de sentencias
else:
        #Inicio del bloque de sentencias cuando es FALSE
        print("A es mayor de 50")
        #Fin del bloque de sentencias

print("Fin")

if (a>b):
        print(f"El número mayor es {a}")
elif (b>a):
        print(f"El número mayor es {b}")
else:
        print(f"Los dos números son iguales")
