from flask import request, send_file, jsonify
from app import app
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import logging
import threading
import asyncio
import aiohttp
from queue import Queue

UPLOAD_FOLDER = 'cargas'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

key = b'This_is_a16b_key'
NODOS = ["http://storage-node-1:5000", "http://storage-node-2:5000"]
queue = Queue()

logging.basicConfig(level=logging.DEBUG)
logging.debug(f"Longitud de la clave AES: {len(key)}")

def worker():
    while True:
        nodo, ruta_archivo = queue.get()
        if nodo is None:
            break
        replicar_archivo(nodo, ruta_archivo)
        queue.task_done()

num_worker_threads = 5
threads = []
for _ in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

@app.route('/cargar', methods=['POST'])
def cargar_archivo():
    archivo = request.files['archivo']
    ruta_archivo = os.path.join(UPLOAD_FOLDER, archivo.filename)

    try:
        cipher = AES.new(key, AES.MODE_EAX)
        data = archivo.read()
        ciphertext, tag = cipher.encrypt_and_digest(data)

        with open(ruta_archivo, 'wb') as file_enc:
            file_enc.write(cipher.nonce)
            file_enc.write(tag)
            file_enc.write(ciphertext)

        logging.info(f"Archivo {archivo.filename} cargado y cifrado exitosamente")

        for nodo in NODOS:
            queue.put((nodo, ruta_archivo))

        return 'Archivo cargado y cifrado exitosamente', 200
    except Exception as e:
        logging.error(f"Error al cargar y cifrar el archivo: {e}")
        return jsonify({'error': f'Error al cargar y cifrar el archivo: {e}'}), 500

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

for _ in range(num_worker_threads):
    queue.put((None, None))
for t in threads:
    t.join()


for rule in app.url_map.iter_rules():
    logging.debug(f"Ruta registrada: {rule}")

