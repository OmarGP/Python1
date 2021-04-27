# 1 Preguntar 10 números al operador (nos aseguramos que sean números)
    #Añadir los números a la lista
# 2 Mostramos los númneros
# 3 Mostramos por pantalla la suma total de todos, la media, la cantidad de numeros pares e impares

numeros = []
suma = 0
pares = 0
impares = 0

contador = 1

try:
    while (contador < 11):
        num1 = int(input("Dime tus números: "))
        if (type(num1) is int):
            numeros.append(num1)
            contador += 1
    for num in numeros:
        suma = suma + num
        if (num % 2 == 0):
            pares += 1
        else:
            impares += 1
finally:

    print("==========================================================================")
    print(f"Tus números elegidos son: {numeros}")
    print("==========================================================================")
    print(f"La suma total es: {suma}")
    print("==========================================================================")
    print(f"La media es: {suma / len(numeros)}")
    print("==========================================================================")
    print(f"Los números pares son: {pares}")
    print("==========================================================================")
    print(f"Los números impares son: {impares}")
    print("==========================================================================")
    print("FIN")
    

