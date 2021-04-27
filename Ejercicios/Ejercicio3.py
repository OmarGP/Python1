texto = input("Dime una frase: ")
letra = ""

while (len(letra) != 1):                          #mientras número de caracteres de letra sea distinto de 1
    letra = input("Dime una letra: ")
    if (len(letra) != 1):
        print(f"{letra}, no es valido")
    elif (letra.isdigit() == True):
        print(f"{letra}, no es valido")
        letra = ""

###############################################

index = 0                                          #variable que funciona como índice de la colección
contador = 0                                       #variable que utilizamos para contar las coincidencias
while(index < len(texto)):                         #mientras valor de INDEX sea inferior al número de elementos de la colección
    if(texto[index].lower() == letra.lower()):
        contador += 1
    index +=1

###############################################

print(f"La letra {letra}, aparece en la frase {contador} vaces")