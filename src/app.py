from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "API is running"})

@app.route('/cep/<cep>', methods=['GET'])
def get_cep_info(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'CEP not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)