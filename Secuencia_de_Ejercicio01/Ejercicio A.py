cadena = "Hola mundo !!"
numero = 100
lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

#A1. Pregunta el nombre de Operador y muestra un saludo incluyendo el contenido de la variable.cadena.
TuNombre = str(input("¿Cómo te llamas?: "))
print(cadena + ". ¡Es un placer conocerte, " + TuNombre + "!.")
print("==================================================")

#A2. Muestra el saludo, en mayúsculas, minúsculas y con la letra de cada palabra en mayúsculas.
print((cadena + ". ¡Es un placer conocerte, " + TuNombre + "!.").upper())
print("==================================================")
print((cadena + ". ¡Es un placer conocerte, " + TuNombre + "!.").lower())
print("==================================================")
print((cadena + ". ¡Es un placer conocerte, " + TuNombre + "!.").title())
