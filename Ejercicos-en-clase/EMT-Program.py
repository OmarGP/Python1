import requests, json
from datetime import date, datetime

url = {
    'Base' : 'https://openapi.emtmadrid.es/v1/',
    'Login' : 'https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/',
    'StopInfo' : 'https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/<stopsId>/arrives/'
}

headers = { 'X-ClientId' : '5a16a9f7-53f8-4256-a4df-43808d569e6a', 'passKey' : 'E7880237284AA4E694936FD41EF5299CF43D9AAADBE6B1927C488217A047A9E40677C955D12AFBA182FBA01A51711D7BD3D437AD2E97D50CEB7812703F8993BA' }
token = None
response = requests.get(url['Login'], headers=headers )

if (response.status_code == 200):
    #print(response.text)
    #print('token:', response.json()['data'][0]['accessToken'])
    token = response.json()['data'][0]['accessToken']
else:
    print(f'Error: ', response.reason)

print("=====================================================")

stop = input(f"Introduzca la parada que desea: \r\n")
body = {
    'cultureInfo' : 'ES',
    'Text_StopRequired_YN' : 'Y',
    'Text_EstimationsRequired_YN' : 'Y',
    'Text_IncidencesRequired_YN' : 'N',
    'DateTime_Referenced_Incidencies_YYYYMMDD' : datetime.now().date().strftime('%Y%m%d')
 }

header = {'accessToken' : token, 'Content-Type' : 'application/json'}
response2 = requests.post(url['StopInfo'].replace('<stopId>', stop), headers=header, data=json.dumps(body))
if (response2.status_code == 200):
    data = response2.json()
    arrive = data['data'][0]['Arrive']
    print(f"Informacíon de la parada: {stop}")
    
    for a in arrive:
        print(f"{'Línea: ':>6}", a['line'])
else:
    print(f'Error: ', response2.reason)
