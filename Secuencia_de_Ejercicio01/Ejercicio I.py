#I1. Pregunta al operador 5 colores
list_color = []
contador = 1

print(f"    >>>>>Ingrese CINCO colores de uno a uno<<<<<")
try:
    while(contador < 6):
        color = input("Dígame un color: \r\n")
        print("")
        list_color.append(color)
        contador += 1
finally:
    #I2. Muestra los colores ordenados
    print(" <<<-Ordenado en orden alfabético->>>")
    print(f"{sorted(list_color)}")


#I3. Muestra el color que más letras contenga

#I4. Muestra el color que más vocales contenga

#I5. Muestra la cantidad de colores que comienza y finaliza por vocal
