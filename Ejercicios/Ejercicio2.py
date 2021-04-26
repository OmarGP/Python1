disKm = float(input("Metros recorridos: "))/1000
timHo = float(input("Minutos empleados: "))/60

velocidad = disKm/timHo

if (velocidad > 75):
    print(f"La velocidad de {velocidad:1.2f} Km/h es Alta.")
elif (velocidad < 30):
    print(f"La velocidad de {velocidad:1.2f} Km/h es Baja")
else:
    print(f"La velocidad de {velocidad:1.2f} Km/h es Moderada")