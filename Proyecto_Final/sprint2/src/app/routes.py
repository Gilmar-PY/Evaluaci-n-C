from flask import request, send_file, jsonify
from app import app
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import aiohttp
import asyncio
import threading
import logging

UPLOAD_FOLDER = 'cargas'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Clave de cifrado de 16 bytes (para producción, gestionar de manera segura)
key = b'This_is_a16b_key'
assert len(key) == 16, f"Longitud de la clave AES incorrecta: {len(key)}"

logging.basicConfig(level=logging.DEBUG)
logging.debug(f"Longitud de la clave AES: {len(key)}")

NODOS = ["http://storage-node-1:5000", "http://storage-node-2:5000"]

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
        # Cifrar el archivo
        cipher = AES.new(key, AES.MODE_EAX)
        data = archivo.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)
        
        # Guardar el archivo cifrado
        with open(ruta_archivo, 'wb') as file_enc:
            file_enc.write(cipher.nonce)
            file_enc.write(tag)
            file_enc.write(ciphertext)
        
        # Replicar el archivo en otros nodos
        threads = [threading.Thread(target=replicar_archivo, args=(nodo, ruta_archivo)) for nodo in NODOS]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        logging.info(f"Archivo {archivo.filename} cargado y cifrado exitosamente")
        return 'Archivo cargado y cifrado exitosamente', 200
    except Exception as e:
        logging.error(f"Error al cargar y cifrar el archivo: {e}")
        return jsonify({'error': f'Error al cargar y cifrar el archivo: {e}'}), 500

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
        
        temp_file_path = os.path.join(UPLOAD_FOLDER, f"temp_{nombre_archivo}")
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(data)
        
        return send_file(temp_file_path, as_attachment=True, download_name=nombre_archivo)
    except Exception as e:
        logging.error(f"Error al descargar y descifrar el archivo: {e}")
        return jsonify({'error': f'Error al descargar y descifrar el archivo: {e}'}), 500

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

