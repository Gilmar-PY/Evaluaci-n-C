from flask import request, send_from_directory, jsonify
from app import app
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import requests

UPLOAD_FOLDER = 'cargas'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Generación de una clave de cifrado
key = get_random_bytes(16)

@app.route('/cargar', methods=['POST'])
def cargar_archivo():
    archivo = request.files['archivo']
    ruta_archivo = os.path.join(UPLOAD_FOLDER, archivo.filename)

    # Cifrar el archivo
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(archivo.read())

    with open(ruta_archivo, 'wb') as file:
        file.write(cipher.nonce)
        file.write(tag)
        file.write(ciphertext)

    return 'Archivo cargado y cifrado exitosamente', 200

@app.route('/descargar/<nombre_archivo>', methods=['GET'])
def descargar_archivo(nombre_archivo):
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)

    with open(ruta_archivo, 'rb') as file:
        nonce = file.read(16)
        tag = file.read(16)
        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    return data, 200

@app.route('/eliminar/<nombre_archivo>', methods=['DELETE'])
def eliminar_archivo(nombre_archivo):
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
    os.remove(ruta_archivo)
    return 'Archivo eliminado exitosamente', 200

@app.route('/sync', methods=['POST'])
def sync_file():
    data = request.get_json()
    nombre_archivo = data['nombre_archivo']
    contenido_archivo = data['contenido_archivo']
    with open(os.path.join(UPLOAD_FOLDER, nombre_archivo), 'wb') as file:
        file.write(contenido_archivo.encode())
    return 'Archivo sincronizado exitosamente', 200

# Función para sincronizar con otros nodos
def sincronizar_con_nodo(nombre_archivo, nodo_url):
    with open(os.path.join(UPLOAD_FOLDER, nombre_archivo), 'rb') as file:
        contenido_archivo = file.read()
    data = {'nombre_archivo': nombre_archivo, 'contenido_archivo': contenido_archivo.decode()}
    response = requests.post(f'http://{nodo_url}/sync', json=data)
    return response.status_code
