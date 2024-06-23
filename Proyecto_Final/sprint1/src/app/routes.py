from flask import request, send_from_directory
from app import app
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

UPLOAD_FOLDER = 'cargas'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/cargar', methods=['POST'])
def cargar_archivo():
    archivo = request.files['archivo']
    ruta_archivo = os.path.join(UPLOAD_FOLDER, archivo.filename)
    archivo.save(ruta_archivo)
    return 'Archivo cargado exitosamente', 200

@app.route('/descargar/<nombre_archivo>', methods=['GET'])
def descargar_archivo(nombre_archivo):
    return send_from_directory(UPLOAD_FOLDER, nombre_archivo)

@app.route('/eliminar/<nombre_archivo>', methods=['DELETE'])
def eliminar_archivo(nombre_archivo):
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
    os.remove(ruta_archivo)
    return 'Archivo eliminado exitosamente', 200
