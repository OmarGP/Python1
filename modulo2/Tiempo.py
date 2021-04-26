import time

print("Time : ", time.time())
print(time.localtime(time.time()))
print("Año: ", time.localtime(time.time()).tm_year)
print("Minutos: ", time.localtime(time.time()).tm_min)
print("Milliseconds: ", int(time.time() * 10))