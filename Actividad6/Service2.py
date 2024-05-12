from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/square', methods=['GET'])
def square():
    """Obtiene un número aleatorio del servicio 1 y devuelve su cuadrado."""
    response = requests.get('http://localhost:5000/random')
    number = response.json()['number']
    squared_number = number ** 2
    return jsonify(squared_number=squared_number)

if __name__ == '__main__':
    app.run(port=5001)
