import pymssql
import sys

conexion = pymssql.connect(server='localHost', user='Test', password='123456', database='NORTHWIND')

cursor = conexion.cursor()
#cursor.execute("INSERT INTO Customers (CustomerID, CompanyName, City, Country) VALUES ('DEMO4' , 'Empresa Demo Cuatro, SL', 'Madrid', 'Spain')")


command0 = "INSERT INTO Customers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"
command1 = "INSERT INTO Customers (CustomerID, CompanyName, City, Country) VALUES (%d, %d, %d, %d)"
lista = []
lista.append(('DEXX1', 'Empresa 1, SL', 'Madrid', 'Spain'))
lista.append(('DEXX2', 'Empresa 2, SL', 'Madrid', 'Spain'))
lista.append(('DEXX3', 'Empresa 3, SL', 'Madrid', 'Spain'))
lista.append(('DEXX4', 'Empresa 4, SL', 'Madrid', 'Spain'))

cursor.executemany(command1, lista)
conexion.commit()
#conexion.rollback()

sys.exit()


cursor = conexion.cursor(as_dict=True)
cursor.execute('SELECT * FROM Customers')

row = cursor.fetchone()
print(type(row))
print(row)

"""while (row):
    print(f"     ID: {row[0]}")
    print(f"Empresa: {row[1]}")
    print(f"")
    row = cursor.fetchone()"""

cursor.close()
conexion.close()