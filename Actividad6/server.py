
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/square', methods=['GET'])
def square():
    # Obtener el parámetro 'number' de la URL
    number = request.args.get('number', default=1, type=int)
    
    # Calcular el cuadrado del número
    result = number ** 2
    
    # Devolver el resultado en formato JSON
    return jsonify({'number': number, 'square': result})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
