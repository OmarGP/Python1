
# G1. Pregunta al operador cualquier cosa.
infor = input("Díme lo que quieras: \r\n")
end = "fin" 
 
while (infor != end):      
# G2. Muestra por Simón dice xxxxxxxxx incluyendo la respuesta del operador
    print(f"Simón dice {infor}.")
# G3. Esta secuencia de pregunta / mostrar en pantalla se repite hasta que el operado responde fin.    
    if (infor == end):
        print("Simón dice Adiós")
    break