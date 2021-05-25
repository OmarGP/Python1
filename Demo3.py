import sqlite3
import sys

connection = sqlite3.connect('.\\Ficheros\\demo.db')
cursor = connection.cursor()

#En una base de datos nueva, necesitamos inicialmente crear las tablas.
#Estas sentencias se ejecutan una sola vez
command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Alumno'"
cursor.execute(command)
tablas = cursor.fetchone()[0]
if (tablas == 0):
    command = "CREATE TABLE Alumno (id, nombre, apellidos, curso, notas)"
    cursor.execute(command)

#Consultar datos
command = "SELECT id, nombre FROM Alumno LIMIT 2"

cursor.execute(command)
r = cursor.fetchone()
while (r):
    print(r)
    r = cursor.fetchone()

print("")

cursor.execute(command)
data  = cursor.fetchall()
print(data)
for r in data:
    print(r)

print("")

for r in cursor:
    print(r)

print("")


sys.exit()


#Insertar varios registros en la base de datos
listaAlumnos = [('H32', 'Ana', 'Trujillo', '2B', None), ('H33', 'Adrián', 'Sánchez', '2C', None), ('H34', 'Ana', 'Martínez', '2A', None)]
command = "INSERT INTO Alumno VALUES (?, ?, ?, ?, ?)"
cursor.executemany(command, listaAlumnos)
connection.commit()

#Insertar un registro en la base de datos
command = "INSERT INTO Alumno (id, nombre) VALUES ('A00', Borja)"
command = "INSERT INTO Alumno VALUES ('A00', 'Borja', 'Cabeza', '2B', Null)"
cursor.execute(command)
connection.commit()
