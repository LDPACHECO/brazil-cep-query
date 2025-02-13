from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Habilitando CORS para permitir requisições de diferentes origens

@app.route('/cep/<cep>', methods=['GET'])
def get_cep_info(cep):
    # URL da API de consulta de CEP
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    # Fazendo a requisição para a API
    response = requests.get(url)
    
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'CEP not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)