# Conexión con MongoDb
from pymongo import MongoClient

#Cliente
client = MongoClient('mongodb://localhost:27017/')
#Base de datos
db = client.Northwind

#Buscar cuantos productos tenemos
products = db.products
NumProductos = products.count_documents({})

print(f"Numero de productos: {NumProductos}")

#Buscar y mostrar todos los productos
listProductos = products.find()
for pn in listProductos:
    print(f"{pn['ProductName']}")

print("________________________")
#cursor = products.find()
#while(cursor.alive):
#   print(cursor.next()['ProductName])

#Buscar todos los productos. Con un filter buscamos los productos con UnitsInStock = 0
listProductos = products.find()
prod = list(filter(lambda p: p['UnitsInStock'] == '0', listProductos))
for pd in prod:
    print(f"{pd['ProductName']}")
print("________________________")

#Buscar los productos con UnitsInStock = 0
listProductos = products.find({'UnitsInStock': '0'})
while(listProductos.alive):
    print(listProductos.next()['ProductName'])
print("________________________")

#Importe total de nuestro stock - Producto -> unidades, UnitPrice
listProductos = products.find()
totalStock = 0
for n in listProductos:
    totalStock = totalStock + (float(n['UnitPrice']) * float(n['UnitsInStock']))
print(f"\nValor del Stock: {totalStock:1.2f}")