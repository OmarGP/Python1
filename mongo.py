from pymongo import MongoClient
from pprint import pprint

## Establecer conexión con MongoDB (motor de base de datos)
client = MongoClient("localhost", 27017)
client = MongoClient('mongodb://localhost:27017/')
## Mostrar el estado del servidor (motor de base de datos)

#Asignmamos a la variable db el objeto que representa la base de datos admin
db = client.admin
#Ejecutamos comandos en la base de datos utilizando la función command
#El comando serverStatus nos retorna el estado del servidor en JSON
status = db.command("serverStatus")
#print(db.command("status"))

##Trabajando con datos
#Seleccionar la base de datos con la que vamos a trabajar
northwindDB = client['Northwind']
northwindDB = client.Northwind

#Listar las colecciones de la base de datos
print(northwindDB.list_collection_names())

#Seleccionar una coleccion de la base de datos
#collection = client.Northwind.customers
#collection = client['Northwind']['customers']
#collection = northwindDB['customers']
collection = northwindDB.customers

#Utilizamos estimated_document_count() para saber el número de documentos en la colección.
result = collection.estimated_document_count()

#Buscar documentos dentro de una colección.
result = collection.find({'Country': 'USA'})
result = collection.find({'Country': 'USA'}).limit(3)
result = collection.find({'Country': 'USA'}).skip(5)
result = collection.find({'Country': 'USA'}).sort('City')
result = collection.find({'Country': 'USA'})
result = collection.find({'Country': 'USA', 'City': 'Portland'}).sort('City')
result = collection.find({'Country': {'$in' : ['USA', 'Mexico']}}).sort('City')

print("Número de documentos: ", result.count())
#print("Número de documentos: ", collection.count_documents({'Country': 'Mexico'}))

print("Datos por leer: ", result.alive)

while (result.alive):
    cliente = result.next()
    pprint(cliente)

result.close()

print("Datos por leer: ", result.alive)

print("==============================")
#Buscar documentos dentro de una colección y retornamos el primer documento encontrado.
#result = collection.find_one({'CustomerID': 'ANATR'})
#pprint(result)


customer = {
    "CustomerID": "DEMO1",
    "CompanyName": "Catering Rapidash, SL",
    "ContactName": "Omar García",
    "ContactTitle": "Propietario",
    "Address": "Calle de Ponferrada, 39",
    "City": "Madrid",
    "Region": "Madrid",
    "PostalCode": "28029",
    "Country": "Spain",
    "Phone": "(91) 782 57 29",
    "Fax": "(91) 782 57 30"
}

#idNewDocument = collection.insert_one(customer).inserted_id
#print('ID Nuevo Documento: ', idNewDocument)

query = ("CustomerID": "DEMO1")
newValues = (
    "$set" : {
        "CompanyName": "Catering Amanda, SL",
        "Address": "Calle Monforte de Lemos, 39",
        "Phone": "(91) 732 69 10"
        }
    )

result = collection.update_one(query, newValues)
print(result.matched_count, ' elementos encontrados.')
print(result.modified_count, ' elementos modificados.')
print(result)