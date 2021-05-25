import requests, json

#Buscar estudiantes por ID
url = 'http://school.labs.com.es/api/students/'
#Ingresar el ID con input
id_ = input("Digame el ID: ")

headers = { 'Content-Type' : 'application/json' }

response = requests.delete(url + str(id_))
if (response.status_code == 200):
    print(f"El alumno con el ID: {id_} ha sido eliminado con éxito.")
else:
    print("Error: ", response.reason)
