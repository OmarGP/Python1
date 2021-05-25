import requests, json

url = {
    'Base' : 'https://openapi.emtmadrid.es/v1/',
    'Login' : 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'Places' : 'https://openapi.emtmadrid.es/<version>/citymad/places/parkings/availability/'
}
header = { 'X-ClientId' : '5a16a9f7-53f8-4256-a4df-43808d569e6a', 'passKey' : 'E7880237284AA4E694936FD41EF5299CF43D9AAADBE6B1927C488217A047A9E40677C955D12AFBA182FBA01A51711D7BD3D437AD2E97D50CEB7812703F8993BA' }
response = requests.get(url['Login'], headers=header )
token = None

if (response.status_code == 200):
    token = response.json()['data'][0]['accessToken']
    accessToken = {'accessToken' : token}
    responsePlaces = requests.get(url['Places'], headers=accessToken)
    data = responsePlaces.json()

    for datos in data['data']:
        if (datos['freeParking'] != None):
            print("============================================================")
            print(f"{' Lugar: ' :>18}", datos['name'])
            print(f"{' Dirección: ':>18}", datos['address'])
            print(f"{' Código Postal: ':>18}", datos['postalCode'])
            print(f"{' Número de plaza: ':>18}", datos['freeParking'])
            print("")
        elif (datos['freeParking'] == None or datos['postalCode'] == None):
            print("============================================================")
            print(f"{' Lugar: ' :>18}", datos['name'])
            print(f"{' Dirección: ':>18}", datos['address'])
            print(f"{' Código Postal: ':>18}", "")
            print(f"{' Número de plaza: ':>18}", "No hay plazas disponibles.")

else:
    print('Error', response.reason)