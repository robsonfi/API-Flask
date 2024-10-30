import requests
import json

url = "http://127.0.0.1:5000"

data = {
    'ra': '93298984'
    'nome': 'João',
    'idade': '16'
}

response = requests.post(url,json=data)

print('StatusCode:', response.status_code)
print('Responde Json', response.json())
