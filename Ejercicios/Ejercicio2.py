disMe = input("Metros recorridos: ")
timMi = input("Minutos empleados: ")

disKm = float(disMe)/1000
TimHo = float(timMi)/60

velocidad50= disKm / timHo

if (velocidad > 75):
    print(f"La velocidad de {velocidad:1.2f} Km/h es Alta.")
elif (velocidad < 30):
    print(f"La velocidad de {velocidad:1.2f} Km/h es Baja")
else:
    print(f"La velocidad de {velocidad:1.2f} Km/h es Moderada")