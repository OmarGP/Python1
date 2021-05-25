import requests, json, random

url = 'http://school.labs.com.es/api/students/'

nombre = input("Dígame su nombre: \r\n")
apellido = input("Dígame sus apellidos: \r\n")
fecha_Nac = input("Dígame su fecha de nacimiento: \r\n")
clase = random.randint(1, 3)

headers = { 'content-type':'application/json' }
data = { 'firstName' : nombre, 'lastName' : apellido, 'dateOfBirth' : fecha_Nac, 'classId' : clase }

response = requests.post(url, headers=headers, data=json.dumps(data))

if (response.status_code == 201):
    print(f"Alumno: ", response.json()['id'])
else:
    print("Error: ", response.reason)