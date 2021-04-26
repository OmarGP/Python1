from datetime import datetime

dt1 = datetime.now().date()
dt2 = datetime.now()

print("Fecha1: ", dt1.strftime("%A %d-%m-%Y"))
print("Fecha2: ", dt2)
print("Año: ", dt2.year)
print("Month: ", dt2.month)
print("Día: ", dt2.day)
print(f"Hora: {dt2.hour}:{dt2.minute}")

print("===============================================")
fecha32 ="10-11-2018"
obj = datetime.strptime(fecha32, "%d-%m-%Y").date()
print(obj)
print(f"{obj.day}-{obj.month}-{obj.year}")


print("===============================================")

print(dt2.strftime("%A, %d %b %Y"))






print("===============================================")

fecha = input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()
años = dt1.year - dt3.year

print("Fecha3: ", dt3)
print(f"Tienes {años} años.")


