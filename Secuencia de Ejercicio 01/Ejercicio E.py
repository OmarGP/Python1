import random

numero = random.randint(1, 100)
intentos = 0
#E1. Pregunta un número al operador y muestra el mensaje los siguientes mensajes:
while True:
    num = int(input(f"Dime un número entre el 1 y el 100:\r\n"))
    intentos += 1

#Correcto si el valor coincide con el contenido en la variable numero
    if (num == numero):
        print(f"Correcto, has acertado.")
        break
        print("=============================================")

#Bajo si el valor es inferior al contenido en la variable numero
    elif (num < numero):
        print(f"Bajo, prueba con un número mas alto.")
        print("=============================================")

#Alto si el valor es superior al contenido en la variable numero
    elif (num > numero):
        print(f"Alto, prueba con un número mas bajo.")
        print("=============================================")
#Añade la palabra Demasiado si la diferencia entre el valor y contenido de la variable numero es de 25 o más.




print("Lo has hecho en: " + str(intentos) + " intentos.")
