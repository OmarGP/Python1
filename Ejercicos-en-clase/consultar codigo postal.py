import requests

url = 'https://www.zippopotam.us/es/'
Postal_Code = input("Digame su código postal: ")

response = requests.get(url + Postal_Code)

if (response.status_code == 200):
    data = response.json()
    for d in data['places']:
        print('Ciudad', d['place name'])
        print('Región', d['state'])
        print('Longitus', d['longitude'])
        print('Latitud', d['latitude'])
        print('')
else:
    print(f'Error')