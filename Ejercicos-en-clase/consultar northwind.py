import requests

url = 'http://api.labs.com.es/v1.0/clientes.ashx'

i = input("Introduzca el ID: ")
params_Cliente = {'id' : i}
response = requests.get(url, params=params_Cliente)

if (response.status_code == 200):
    data = response.json()
    for d in data:
        print(f"{'ID: ':>15} {d['CustomerID']}")
        print(f"{'CompanyName: ':>15} {d['CompanyName']}")
        print(f"{'ContactName: ':>15} {d['ContactName']}")
        print(f"{'ContactTitle: ':>15} {d['ContactTitle']}")
        print(f"{'Address: ':>15} {d['Address']}")
        print(f"{'City: ':>15} {d['City']}")
        print(f"{'Region: ':>15} {d['Region']}")
        print(f"{'PostalCode: ':>15} {d['PostalCode']}")
        print(f"{'Country: ':>15} {d['Country']}")
        print(f"{'Phone: ':>15} {d['Phone']}")
        print(f"{'Fax: ':>15} {d['Fax']}")
        print("__________________________________________")
else:
    print('Error')