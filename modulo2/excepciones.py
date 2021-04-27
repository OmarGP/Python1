num1 = 20
num2 = 100

try:
    num3 = num2 / num1
    print(f"Número 3: {num3}")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except:
    print("Upsss Error!!!!")
finally:
    print("Finalizado try/except")
print("=======================================")
print("Fin del PROGRAMA")