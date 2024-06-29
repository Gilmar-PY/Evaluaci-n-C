
import requests
from flask import request, send_file, jsonify
from app import app
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import logging
import threading
import asyncio
import aiohttp

UPLOAD_FOLDER = '/app/cargas'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Clave de cifrado válida de 16 bytes
key = b'This_is_a_16byte'

# Configurar logging
logging.basicConfig(level=logging.DEBUG)

# Lista de nodos para replicar archivos
NODOS = ["http://storage-node-2:5000", "http://storage-node-3:5000"]

def cifrar_archivo(data):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, tag, ciphertext

def descifrar_archivo(nonce, tag, ciphertext):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

async def replicar_archivo_async(nodo, ruta_archivo):
    try:
        form = aiohttp.FormData()
        form.add_field('archivo', open(ruta_archivo, 'rb'), filename=os.path.basename(ruta_archivo))
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{nodo}/cargar", data=form) as response:
                logging.debug(f"Replicación en {nodo} completada con estado {response.status}")
    except Exception as e:
        logging.error(f"Error replicando en {nodo}: {e}")

def replicar_archivo(nodo, ruta_archivo):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(replicar_archivo_async(nodo, ruta_archivo))
    loop.close()

@app.route('/cargar', methods=['POST'])
def cargar_archivo():
    archivo = request.files['archivo']
    ruta_archivo = os.path.join(UPLOAD_FOLDER, archivo.filename)
    
    try:
        data = archivo.read()
        nonce, tag, ciphertext = cifrar_archivo(data)
        
        with open(ruta_archivo, 'wb') as file_enc:
            file_enc.write(nonce)
            file_enc.write(tag)
            file_enc.write(ciphertext)
        
        # Replicar el archivo en otros nodos utilizando threading
        threads = [threading.Thread(target=replicar_archivo, args=(nodo, ruta_archivo)) for nodo in NODOS]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        logging.debug(f"Archivo {archivo.filename} cargado y cifrado exitosamente en {ruta_archivo}.")
        return 'Archivo cargado y cifrado exitosamente', 200
    except Exception as e:
        logging.error(f"Error al cargar y cifrar el archivo: {e}")
        return jsonify({'error': f'Error al cargar y cifrar el archivo: {e}'}), 500

@app.route('/descargar/<nombre_archivo>', methods=['GET'])
def descargar_archivo(nombre_archivo):
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
    temp_file_path = os.path.join(UPLOAD_FOLDER, f"temp_{nombre_archivo}")

    try:
        logging.debug(f"Intentando descargar y descifrar el archivo desde {ruta_archivo}.")
        
        with open(ruta_archivo, 'rb') as file_enc:
            nonce = file_enc.read(16)
            tag = file_enc.read(16)
            ciphertext = file_enc.read()
        
        data = descifrar_archivo(nonce, tag, ciphertext)
        
        # Crear un archivo temporal descifrado
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(data)
        
        logging.debug(f"Archivo {nombre_archivo} descifrado exitosamente y guardado en {temp_file_path}.")
        
        if not os.path.exists(temp_file_path):
            logging.error(f"El archivo temporal {temp_file_path} no existe.")
            raise FileNotFoundError(f"No such file or directory: '{temp_file_path}'")
        
        response = send_file(
            temp_file_path,
            as_attachment=True,
            download_name=nombre_archivo
        )
        response.call_on_close(lambda: os.remove(temp_file_path))
        return response
    except Exception as e:
        logging.error(f"Error al descargar y descifrar el archivo: {e}")
        return jsonify({'error': f'Error al descargar y descifrar el archivo: {e}'}), 500

@app.route('/eliminar/<nombre_archivo>', methods=['DELETE'])
def eliminar_archivo(nombre_archivo):
    ruta_archivo = os.path.join(UPLOAD_FOLDER, nombre_archivo)
    try:
        os.remove(ruta_archivo)
        logging.debug(f"Archivo {nombre_archivo} eliminado exitosamente de {ruta_archivo}.")
        return 'Archivo eliminado exitosamente', 200
    except Exception as e:
        logging.error(f"Error al eliminar el archivo: {e}")
        return jsonify({'error': f'Error al eliminar el archivo: {e}'}), 500
        
