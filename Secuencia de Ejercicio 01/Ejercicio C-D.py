lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

#C1. Muestra el número de elementos de lista.
print(f"Existe un total de: " + str(len(lista)) + " elementos")
#C2. Muestra el primer y el último elemento de lista.
print("El primer elemento es: "+lista[0]+" y el último elemento es: "+lista[22])

print("============================================================================")

#D1. Pregunta al operador su DNI sin letra.
dni = []
def IngresoDNI (datos):
    for d in datos:
        dni.append(d)
    #print(f"Su DNI es: " + str(dni))   

documento = input("Introduzca unicamente los números de su DNI:\r\n")
IngresoDNI(documento)

print("============================================================================")
        
#D2. Calcula el resto de dividir el número del DNI entre 23.
nif = int(documento)
resto = nif%23
#print(resto)
#D3. Muestra el DNI con la letra. El resto de la división representa la posición de la letra del DNI en lista.
letra = lista[resto]
print(f"La letra de su DNI es, {letra}.\r\nY su número completo sería: {documento}{letra}")

print("============================================================================")
