#####################################################################
# Trabajando con fechas                                             #
#####################################################################
#                                                                   #
#   Sintaxis: datetime.now()                                        #
#             datetime.now().date()                                 #
#             datetime.now().today()                                #
#                                                                   #
#             datetime.strptime("11-03-1998", "%d-%m-%Y").date()    #
#             print(datetime.now().strftime("%A, %d %m, %Y")        #
#                                                                   #
#####################################################################

from datetime import datetime

#Almacenamos en la variable dt1 la fecha actual del sistema
dt1 = datetime.now().date()
print("Fecha1: ", dt1)

#Almacenamos en la variable dt2 la fecha y hora actual del sistema
dt2 = datetime.now()
print("Fecha2: ", dt2)

print("Fecha1: ", dt1.strftime("%A %d-%m-%Y"))
print("Año: ", dt2.year)
print("Month: ", dt2.month)
print("Día: ", dt2.day)
print(f"Hora: {dt2.hour}:{dt2.minute}")

print("===============================================")
fecha3 ="10-11-2018"
obj = datetime.strptime(fecha3, "%d-%m-%Y").date()
print(obj)
print(f"{obj.day}-{obj.month}-{obj.year}")


print("===============================================")

#Dar formato a una fecha antes de ser mostrada en pantalla utilizando "STRFTIME"
print(dt2.strftime("%A, %d %b %Y"))

print("===============================================")

#Convertimos un valor alfanúmerico en fecha utilizando "STRPTIME"
fecha = input("Escribe tu fecha de nacimiento: ")
dt3 = datetime.strptime(fecha, "%d-%m-%Y").date()

print("===============================================")

#Calculos entre fechas
años = dt1.year - dt3.year
print(f"Tienes {años} años.")