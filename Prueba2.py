#file2 = open("resultado.txt", "wt")
#file2.write("Demo escritura en un fichero\n")
#file2.write("Demo escritura en un fichero\n")


#lineas = []
#lineas.append("Linea 1: Demo escritura en un fichero\n")
#lineas.append("Linea 2: Demo escritura en un fichero\n")
#lineas.append("Linea 3: Demo escritura en un fichero\n")
#lineas.append("Linea 4: Demo escritura en un fichero\n")


#file2.writelines(lineas)
#for item in lista:


#file2.close()

numero = input("Dime un número: ")

if(numero.isdigit() == True):
    print(f"TABLA DE MULTIPLICAR DEL {numero}")
    print("========================================")
    
    for n in range(1, 11, 1):
        print(f"{n:2.0f} x {numero} = {(n * int(numero)):6.2f}")
else:
    print(f"{numero}, no es un número.")