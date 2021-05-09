import pymssql
import sys
#Cliente
conexion = pymssql.connect(server='localHost', user='Test', password='123456', database='NORTHWIND')

cursor = conexion.cursor(as_dict=True)

#Introducir número de pedido.
idPedido = input("Identificador del pedido: ")
cursor.execute("SELECT * FROM Orders WHERE OrderID = %d", idPedido)

if (cursor.rowcount == 0):
    print(f"El pedido {idPedido} no existe")
else:
    pedido = cursor.fetchone()
    print("==========================================================================")
    print(f"DATOS DEL PEDIDO: {idPedido}.")
    print("==========================================================================")
    print(f"Entregar: {pedido['ShipName']}")
    print(f"        : {pedido['ShipAddress']}")
    print(f"        : {pedido['ShipCity']}({pedido['ShipCountry']})")
    print("")

    print("==========================================================================")
    print(f"  {'Nombre del Producto':<32} {'Cantidad':>10} {'Precio':>11} {'Total':>11}")
    print("==========================================================================")

#Buscamos el detalle del pedido.
    cursor.execute("SELECT * FROM [Order Details] WHERE OrderID = %d", idPedido)
    totalPedido = 0
    lineas = cursor.fetchall()
    for linea in lineas:
        #Buscamos y mostramos la descripción del producto, utilizando ProductoID.
        cursor.execute("SELECT ProductName FROM Products WHERE ProductID = %d", linea['ProductID'])
        producto = cursor.fetchone()
        #producto - cantidad - precio - precio*cantidad.
        totalLinea = linea['Quantity'] * linea['UnitPrice']
        totalPedido += totalLinea
        totalFormat = "{:0.2f}".format(totalLinea)
        print(f"  {producto['ProductName']:<32} = {linea['Quantity']:>8} {linea['UnitPrice']:>10}€ {totalFormat:>10}€")
#Mostramos el importe total del pedido
print("==========================================================================")
totalPedidoFormat = "{:0.2f}".format(totalPedido)
print(f"  {'TOTAL':>55} {totalPedidoFormat:>10}€")


sys.exit()

"""lista = cursor.fetchall()

for row in lista:
    print(f"  ID: {row['CustomerID']} Empresa: {row['CompanyName']}")

    cursor.execute('SELECT * FROM Orders WHERE CustomerID = %d', row['CustomerID'])
    listaPedidos = cursor.fetchall()
    for rowPedido in listaPedidos:
        print(" -> ", rowPedido['OrderID'])"""


"""while row:
    print(f"  ID: {row['CustomerID']} Empresa: {row['CompanyName']}")
    cursor2 = conexion.cursor(as_dict=True)
    cursor2.execute('SELECT * FROM Orders WHERE CustomerID = %d', row['CustomerID'])
    
    row2 = cursor2.fetchone()
    while (row2):
        print(" -> ", row2['OrderID'])
        row2 = cursor2.fetchone()


    row = cursor.fetchall()


cursor.close()
conexion.close()

sys.exit()"""