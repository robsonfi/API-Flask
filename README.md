# API-Flask
Visual Studio Code, codigo de python

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/matricula", methods=['POST'])
def envio():
    data = request.get_json()
    nome = data.get('nome')
    ra = data.get('ra')
    idade = data.get('idade')
#KNN, Regressão. Arvore

    return jsonify ({'message': f'Recebido: {nome},RA: {ra} e Idade: {idade}'}), 200
#retorno de algo.

if(__name__=='__main__'):
    app.run(debug=True)



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
