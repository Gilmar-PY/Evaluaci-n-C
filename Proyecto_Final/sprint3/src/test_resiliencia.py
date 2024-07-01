
# test_resiliencia.py

import requests
import docker
import time
from Crypto.Cipher import AES
import os

# Configuración
client = docker.from_env()
url_cargar = 'http://localhost:5000/cargar'
url_descargar = 'http://localhost:5000/descargar/Actividad.txt'
key = b'This_is_a16b_key'
UPLOAD_FOLDER = 'cargas'

# Cargar archivo
files = {'archivo': open('Actividad.txt', 'rb')}
response = requests.post(url_cargar, files=files)
print("Archivo cargado exitosamente. Ejecutando prueba de fallo de nodo...")

# Simular fallo de nodo
try:
    container = client.containers.get('storage-node-1')
    container.stop()
    print("Nodo storage-node-1 detenido.")
    
    # Esperar un momento
    time.sleep(5)
    
    # Intentar descargar el archivo
    response = requests.get(url_descargar)
    with open('descargado_resiliencia.txt', 'wb') as f:
        f.write(response.content)
    
    print("Archivo descargado exitosamente después del fallo del nodo.")
    
    # Descifrar el archivo descargado
    ruta_archivo = 'descargado_resiliencia.txt'
    with open(ruta_archivo, 'rb') as file_enc:
        nonce = file_enc.read(16)
        tag = file_enc.read(16)
        ciphertext = file_enc.read()
    
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    
    with open('descifrado_resiliencia.txt', 'wb') as f:
        f.write(data)
    
    print("Archivo descifrado exitosamente.")
    
    # Reiniciar el nodo
    container.start()
    print("Nodo storage-node-1 reiniciado.")
except Exception as e:
    print(f"Error durante la prueba de fallo de nodo: {e}")

