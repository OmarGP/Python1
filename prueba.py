from datetime import datetime

dt1 = datetime.now().date()
dt2 = datetime.now()


def calcular_edad(fecNac, edad):
 
    edad = dt1.year - dt3.year





fecha = input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()
#años = dt1.year - dt3.year

print("Tu naciste el: ", dt3)
print(f"Tienes {edad} años.")
