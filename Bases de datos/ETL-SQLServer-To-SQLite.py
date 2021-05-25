import sqlite3
import pymssql
import sys

#Creamos una base de datos de SQLite llamada Nortwind.db
conn = sqlite3.connect('.\\Ficheros\\Northwind.db')
cursor = conn.cursor()
#Creamos una tabla llamada Customers
command = "SELECT count() FROM sqlite_master WHERE type = 'table' AND name = 'Customers'"
cursor.execute(command)
tablas = cursor.fetchone()[0]
if (tablas == 0):
    command = "CREATE TABLE Customers (CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax)"
    cursor.execute(command)
#Trasladamos la informacion de SQL Server -> Customers ha SQLite -> Customers
conexion = pymssql.connect(server='localHost', user='Test', password='123456', database='NORTHWIND')

cursor2 = conexion.cursor()
command = "SELECT * FROM Customers"
cursor2.execute(command)
data  = cursor2.fetchall()
#print(data)

command = "INSERT INTO Customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(command, data)
conn.commit()

cursor.close()
conexion.close()

sys.exit()