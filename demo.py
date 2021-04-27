numeros = []
suma = 0
pares = 0
impares = 0

print(len(numeros))

try:
    while(len(numeros) < 11):
        num = input("Dime un número: ")
        if(num.isdigit()):
            numeros.append(int(num))

    for numero in numeros:
        print(f"Número: {numero}")
        suma += numero
        if(numero % 2 == 0):
            pares += 1
        else:
            impares += 1
    
    print(f"Suma Total: {suma}")
    print(f"Media: {suma / len(numeros)}")
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")
except Exception as ex:
    print(f"Error: {ex}")
    