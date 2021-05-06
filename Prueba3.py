while(products.alive):
    Prod = products.next()
    totalProd = int(Prod['UnitsInStock']) * float(Prod['UnitPrice'])
    totalPedido += totalLinea
    total1 = "{:0.2f}".format(totalProd)
    print(f"  {Prod['UnitsInStock']:>6} {Prod['UnitPrice']:>8}€ {total1:>8}€")
