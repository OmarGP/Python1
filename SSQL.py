import pymssql
import sys

conexion = pymssql.connect(server='localHost', user='Test', password='123456', database='NORTHWIND')

cursor = conexion.cursor(as_dict=True)
cursor.execute('SELECT * FROM Customers')

lista = cursor.fetchall()

#row = cursor.fetchone()

for row in lista:
    print(f" ID: {row['CustomerID']} Empresa: {row['CompanyName']}")

    cursor.execute('SELECT * FROM Orders WHERE CustomerID = %d', row['CustomerID'])
    listaPedidos = cursor.fetchall()
    for rowPedido in listaPedidos:
        print("  ->", rowPedido['OrderID'])

sys.exit()
while (row):
    print(f" ID: {row['CustomerID']} Empresa: {row['CompanyName']}")
    cursor2 = conexion.cursor(as_dict=True)
    cursor.execute('SELECT * FROM Orders WHERE CustomerID = %d', row['CustomerID'])

    row2 = cursor2.fetchone()
    while (row2):
        print(row2)
        row2 = cursor2.fetchone()
    
    row = cursor.fetchone()

cursor.close()
conexion.close()