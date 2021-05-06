# B1. Pregunta un número al operador y muestra el resultado de multiplicarlo por PI. 
# Utiliza la constante "math.pi" y recuerda incluir "import math"

import math

numero = float(input("Dime un número: "))
pi = math.pi
resultado = pi * numero
result = "{:0.4f}".format(resultado)
#if (numero == ):    
print(f"{pi:0.4f} x {numero} es igual a: " + result)
#else:
#print(f"{numero}, no es un número.")
print("===============================================================================")
# B2. Muestra la raíz cuadrada del mismo número.
if (numero>0):
    print(f"La raiz cuadrada de {numero} es igual a: {(math.sqrt(numero)):0.3f}")
else:
    print(f"No se puede obtener la Raiz Cuadrada de números negativos o iguales a 0.")

print("===============================================================================")

#B3. Muestra el arco coseno del mismo número.
if (numero<=1 or numero>=-1):
    print(f"EL arco coseno de {numero} es igual a: {math.acos(numero):0.4f}")
else:
    print("El número está fuera del dominio para calcular el arco coseno.")