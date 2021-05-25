import math
#H1. Muestra las siguientes secuencias de número utilizando un WHILE:

#H1.1 Secuencia del 1 al 100
a = 1
print(f"  >>>> Secuencia del 1 al 100 <<<<")
while (a <= 10):
    print (f"# {a}")
    a += 1
print("=============================")

#H1.2 Los números impares del 51 al 91.
print(f"    >>>> Secuencia de números impares del 51 al 91 <<<<")
b = 51
while(b <= 91):
    print(f"# {b}")
    b += 2
print("=============================")

#H1.3 Tabla de multiplicar de PI.
print(f"    >>>> Secuencia de Tabla de multiplicar de PI <<<<")
pi = math.pi
c = 1
while (c <= 10):
    print(f"{pi:1.5} x {c} = {pi * c:1.5}")
    c += 1
print("=============================")

#H1.4 Del 20 al 10 multimplicado del 5 a 8, utilizando un FOR
print(f"    >>>> Secuencia Del 20 al 10 multimplicado del 5 a 8, utilizando un FOR <<<<")
d = 20

while (d >= 10):
    print("")
    for d1 in range(5, 9):
        print(f"{d} x {d1} = {d * d1}")
        d -= 1
print("=============================")

