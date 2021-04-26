num1 = input("Escoge un número: ")

if (num1.isdigit() == True):
    print(f"Tabla del {num1}")

    for n in range(1, 11):
        print(f"{n:2.0f} * {num1} = {(n * int(num1)):5.0f}")

else:
    print(f"{num1}, no es un número.")