import random

numero = random.randint(1, 15)
intentos=0
while True:
     numero1 = int(input("Dime un numero entre 1 y 15: "))
     intentos += 1
     print("Tu número de intentos es: " + str(intentos))
     if numero1 == numero:
         print("Felicidades, has acertado.")
         break
     elif numero1 > numero:
         print("Prueba con un número menor")
         
     elif numero1 < numero:
         print("Prueba con un número mayor")

     elif numero1 != numero:
        print("No es correcto, vuelve a intentarlo.")

intentos += 1
print("Lo hiciste en" + str(intentos) "intentos")        

print("Fin del WHILE")


