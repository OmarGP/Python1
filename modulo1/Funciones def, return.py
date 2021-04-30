from datetime import datetime

#Ejemplo de una función que NO tiene parámetros (no recibe datos) y no retorna datos
def Func1():
    print("Hola a todos!!!")


#Ejemplo de una función que SI tiene parámetros (SI recibe datos) y no retorna datos
def Func2(nombre, numero):
    print(f"Me llamo {nombre} y mi número de la suerte es {numero}")


#Ejemplo de una función que SI tiene parámetros (SI recibe datos) y SI retorna datos
def Func3(frase):
    #print(f"La frase es: {frase}")
    cant = 0
    cant = len(frase)
    return cant

#Ejemplo de una función que NO tiene parámetros (no recibe datos) y SI retorna datos
def Func4():
    return datetime.now().date().strftime("%A")

Func1()
Func2("Omar", 7)
dato = Func3("Hola a todos")
print(f"Dato: {dato}")
print(Func3("Adios!!!"))

dato2 = Func4()
print(f"")