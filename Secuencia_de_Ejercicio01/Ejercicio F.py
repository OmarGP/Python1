import math

# F1. Muestra las siguientes secuencias de número utilizando un FOR:
# F1.1 Del 1 al 100.
print(f"    >>>> Secuencia del 1 al 100 <<<<")
for a in range(1, 101):    
    print(f"# {a}")
print("=============================")

# F1.2 Del 200 al 190.
print(f"    >>>> Secuencia del 200 al 190 <<<<")
for b in reversed(range(190, 201)):    
    print(f"# {b}")  
print("=============================")

# F1.3 Del 10 al 10000 de 100 en 100.
print(f"    >>>> Secuencia del 10 al 10000 de 100 en 100 <<<<")
for c in range(10, 10011, 100):    
    print(f"# {c}")
print("=============================")

# F1.4 Los números impares del 51 al 91.
print(f"    >>>> Secuencia de números impares del 51 al 91 <<<<")
for d in range(51, 92):    
    if (d % 2 == 0):
        continue
    else:
        print(f"# {d}")
print("=============================")

# F1.5 Los multiplos de 5 del 40 al 30.
print(f"    >>>> Secuencia de multiplos de 5 del 40 al 30 <<<<")
for e in reversed(range(30, 41, 5)):    
    print(f"# {e}")
print("=============================")
# F1.6 Tabla de multiplicar de PI.
pi = math.pi
rango = range(1, 11)
print(f"    >>>> Secuencia de Tabla de multiplicar de PI <<<<")
for f in range(1, 11):    
    print(f"{pi:>1.4} x {f} = {pi * f:>1.4}")
print("=============================")

# F1.7 Del 10 al 20 sumado con el anterior.
print(f"    >>>> Secuencia del 10 al 20 sumado con el anterior <<<<")
for g in range(10, 22):
    suma = g + (g - 1)    
    print(f"{g} + {g - 1} = {suma}")
print("=============================")

# F1.8 Del 20 al 10 multimplicado del 5 a 8, utilizando dos FOR.
print(f"    >>>> Secuencia Del 20 al 10 multimplicado del 5 a 8, utilizando dos FOR <<<<")
for h in reversed(range(10, 21)):    
    print("")
    for h1 in range(5, 9):
        print(f"{h} x {h1} = {h * h1}")
print("=============================")