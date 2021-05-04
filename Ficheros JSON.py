import json

#'CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax'

def PrintData(cliente):
    print(f"ID: {cliente['CustomerID']}")
    print(f"Empresa: {cliente['CompanyName']}")
    print(f"Contacto: {cliente['ContactName']} ({cliente['ContactTitle']})")
    print(f"Dirección: {cliente['Address']}")
    print(f"           {cliente['City']} {cliente['PostalCode']} {cliente['Country']}")
    print(f"Teléfono: {cliente['Phone']}, Fax: {cliente['Fax']}")


file = open(".\\Ficheros\\clientes.json", "rt", encoding='UTF-8')
dataJSON = file.read()
file.close()

clientes = json.loads(dataJSON)

#print(type(dataJSON))
#print(type(customers))
#print(len(customers))
#print(customers[0]['CompanyName'])
#print(customers[0].keys())

#Cód ANTR ANTON

Cliente = str.upper(input("ID: "))

#buscamos el cliente filter
busqueda = list(filter(lambda x : x['CustomerID'] == Cliente, clientes))
if (len(busqueda) == 0):
    print(f"El ID es incorrecto")
else:
    #llamamos Printdata
    PrintData(busqueda[0])

#llamamos Printdata

