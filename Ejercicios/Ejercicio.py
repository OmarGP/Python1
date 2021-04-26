from datetime import datetime

dt1 = datetime.now().date()

edad = 18
Fecha = input("Dime tu fecha de nacimiento: ")
dt2 = datetime.strptime(Fecha, "%d-%m-%Y").date()
años = dt1.year - dt2.year

print()
if (años>=edad):
        print(f"Tienes {años} años, eres mayor de edad.")
elif (años<edad):
        print(f"Te faltan {años} años para ser mayor de edad.")
