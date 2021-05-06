from pymongo import MongoClient

#Cliente
client = MongoClient('mongodb://localhost:27017/')

#Base de datos
db = client.Northwind

#Colecciones
orders = db.orders
details = db.order_details
products = db.products

idPedido = input("Identificador del pedido: ")

pedido = orders.find_one({ 'OrderID' : idPedido })
if(pedido != None):
    print("==================================")
    print(f"DATOS DEL PEDIDO: {idPedido}.")
    print("==================================")
    print(f"Entregar: {pedido['ShipName']}")
    print(f"        : {pedido['ShipAddress']}")
    print(f"        : {pedido['ShipCity']}({pedido['ShipCountry']})")
    print("==================================")
#Buscamos el detalle del pedido.
    detalle = details.find({'OrderID' : idPedido})
    print("==========================================================================")
    print(f"  {'Nombre del Producto':<30} {'Cantidad':>6} {'Precio':>9} {'Total':>8}")
    print("==========================================================================")

    totalPedido = 0
#Recorremos con Whilw el curso del detalle del pedido.
    while(detalle.alive):
        linea = detalle.next()
#Buscamos y mostramos la descripción del producto, utilizando ProductoID.
        producto = products.find_one({'ProductID' : linea['ProductID']})
#Descripción - cantidad - precio - precio*cantidad.
        totalLinea = int(linea['Quantity']) * float(linea['UnitPrice'])
        totalPedido += totalLinea
        total1 = "{:0.2f}".format(totalLinea)
#Mostramos cada línea del pedido.
        print(f"  {producto['ProductName']:<30} = {linea['Quantity']:>6} {linea['UnitPrice']:>8}€ {total1:>8}€")
#Mostramos el importe total del pedido
    print("==========================================================================")
    totalPedidoFormat = "{:0.2f}".format(totalPedido)
    print(f"  {'TOTAL':>49} {totalPedidoFormat:>8}€")
    print("==========================================================================")
else:
    print("El pedido #" + idPedido + " no existe.")

