from datetime import datetime

edad = 21

dt1 = datetime.now().date()

print(dt1)

Fecha = input("Dime tu fecha de nacimiento: ")
dt2 = datetime.strptime(Fecha, "%d-%m-%Y").date()
años = dt1.year - dt2.year

print()
if (años>edad):
        #Inicio del bloque de sentencias cuando es TRUE
        print(f"Tienes {años} años, eres mayor de edad.")
        #Fin del bloque de sentencias
elif (años<edad):
        #Inicio del bloque de sentencias cuando es FALSE
        print(f"Te faltan {años} años para ser mayor de edad.")
        #Fin del bloque de sentencias