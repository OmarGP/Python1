#####################################################################
# Sentencias de Control - If / Elif / Else                          #
#####################################################################
#                                                                   #
#   Las sentencias de decisión determinar el flujo del programa     #
#   tras evaluar una expresión de comparación.                      #
#                                                                   #
#                                                                   #
#   Sintaxis:          Es igual: a == b                             #
#                   No es igual: a != b                             #
#                     Menor que: a <  b                             #
#                 Menor o igual: a <= b                             #
#                     Mayor que: a >  b                             #
#                 Mayor o igual: a >= b                             #
#                                                                   #
#####################################################################

a = 100
b = 10

#Inicio del IF
if (b>a):
        #Inicio del bloque de sentencias cuando es TRUE
        print("B es mayor que A")
        #Fin del bloque de sentencias
elif (a==b):
        #Inicio del bloque de sentencias cuando es TRUE
        print("A y B son iguales")
        #Fin del bloque de sentencias
else:
        #Inicio del bloque de sentencias cuando es FALSE
        print("A es mayor que B")
        #Fin del bloque de sentencias
#Fin del IF
print("Fin")
print("============================================")
if (a>b):
        print(f"El número mayor es {a}")
elif (b>a):
        print(f"El número mayor es {b}")
else:
        print(f"Los dos números son iguales")
