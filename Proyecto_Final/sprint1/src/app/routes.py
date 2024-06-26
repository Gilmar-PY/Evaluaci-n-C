from flask import request, send_from_directory, jsonify
from app import app
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import logging

UPLOAD_FOLDER = 'cargas'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Clave de cifrado (para producción,para gestionarse de manera segura)
key = get_random_bytes(16)

logging.basicConfig(level=logging.INFO)

@app.route('/cargar', methods=['POST'])
def cargar_archivo():
    archivo = request.files['archivo']
    ruta_archivo = os.path.join(UPLOAD_FOLDER, archivo.filename)
    
    try:
        # Cifrar el archivo
        cipher = AES.new(key, AES.MODE_EAX)
        data = archivo.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        # Guardar el archivo cifrado
        with open(ruta_archivo, 'wb') as file_enc:
            file_enc.write(cipher.nonce)
            file_enc.write(tag)
            file_enc.write(ciphertext)
        
        logging.info(f"Archivo {archivo.filename} cargado y cifrado exitosamente")
        return 'Archivo cargado y cifrado exitosamente', 200
    except Exception as e:
        logging.error(f"Error al cargar y cifrar el archivo: {e}")
        return jsonify({'error': 'Error al cargar y cifrar el archivo'}), 500

@app.route('/descargar/<nombre_archivo>', methods=['GET'])
def descargar_archivo(nombre_archivo):
    try:
        ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
        with open(ruta_archivo, 'rb') as file_enc:
            nonce = file_enc.read(16)
            tag = file_enc.read(16)
            ciphertext = file_enc.read()
        
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        
        return send_from_directory(UPLOAD_FOLDER, nombre_archivo)
    except Exception as e:
        logging.error(f"Error al descargar y descifrar el archivo: {e}")
        return jsonify({'error': 'Error al descargar y descifrar el archivo'}), 500

@app.route('/eliminar/<nombre_archivo>', methods=['DELETE'])
def eliminar_archivo(nombre_archivo):
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
    try:
        os.remove(ruta_archivo)
        logging.info(f"Archivo {nombre_archivo} eliminado exitosamente")
        return 'Archivo eliminado exitosamente', 200
    except Exception as e:
        logging.error(f"Error al eliminar el archivo: {e}")
        return jsonify({'error': 'Error al eliminar el archivo'}), 500
