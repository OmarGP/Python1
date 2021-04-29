def Func2(lista, numItems)



def Func1(lista):
    num1 = int(input("Dime tus números: "))
            if (type(num1) is int):
                lista.append(num1)
                contador += 1

    numeros = []

    try:
        while (contador < 11):
            Func1(numeros)
    except ValueError:
        print("Solo puede ingresar números enteros.")

print(Func1)