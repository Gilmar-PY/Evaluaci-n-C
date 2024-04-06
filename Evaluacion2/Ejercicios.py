## Ejercicio 1 (son solo sugerencias)

import threading
import time

# Tarea 1: Imprimir números del 1 al 10 con retardo
def imprimir_numeros():
    for numero in range(1, 11):
        time.sleep(0.5)
        print(numero)

# Tarea 2: Imprimir letras de la 'a' a la 'j' con retardo
def imprimir_letras():
    for letra in 'abcdefghij':
        time.sleep(0.75)
        print(letra)

# Tarea 3: Imprimir "¡Listo!" al finalizar las otras tareas
# Esta tarea espera a que las tareas 1 y 2 se completen
def imprimir_listo():
    tarea1.join()
    tarea2.join()
    print("¡Listo!")

# Creación y lanzamiento de threads
tarea1 = threading.Thread(target=imprimir_numeros)
tarea2 = threading.Thread(target=imprimir_letras)
tarea3 = threading.Thread(target=imprimir_listo)

tarea1.start()
tarea2.start()
tarea3.start()



## Ejercicio 2

from multiprocessing import Pool
import math

# Función para determinar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Función para calcular los números primos dentro de un rango
def calcular_primos(rango):
    # Usando Pool para paralelizar el cálculo de números primos
    with Pool(processes=4) as pool:
        resultados = pool.map(es_primo, range(rango[0], rango[1]))
        # Filtrar los números primos basados en los resultados
        primos = [i + rango[0] for i, es_primo in enumerate(resultados) if es_primo]
    return primos

# Ejemplo de uso
if __name__ == '__main__':
    rango = (1, 100)
    primos = calcular_primos(rango)
    print(f"Números primos entre {rango[0]} y {rango[1]}: {primos}")




## Ejercicio 3


import asyncio
import aiohttp

async def fetch(url, session):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        responses = await asyncio.gather(*tasks)
        # Procesar las respuestas
        for response in responses:
            if response is not None:
                print(response[:100])  # Imprime los primeros 100 caracteres de cada respuesta

# Lista de URLs para hacer solicitudes de ejemplo
urls = [
    'http://example.com',
    'http://example.org',
    'http://example.net',
]

# Ejecutar el recolector de datos asincrónico
asyncio.run(main(urls))



## Ejercicio 4


from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import os

def redimensionar_imagen(path_origen, path_destino, size):
    """Redimensiona una imagen al tamaño especificado."""
    try:
        img = Image.open(path_origen)
        img = img.resize(size, Image.ANTIALIAS)
        img.save(path_destino)
        print(f"Imagen redimensionada y guardada en: {path_destino}")
    except Exception as e:
        print(f"Error al procesar {path_origen}: {e}")

def procesar_imagenes_concurrentemente(paths_origen, path_destino, size):
    """Procesa múltiples imágenes en paralelo."""
    with ThreadPoolExecutor() as executor:
        for path_origen in paths_origen:
            destino = os.path.join(path_destino, os.path.basename(path_origen))
            executor.submit(redimensionar_imagen, path_origen, destino, size)

# Ejemplo de uso
if __name__ == "__main__":
    paths_origen = ['./img1.jpg', './img2.jpg', './img3.jpg']  # Ejemplo de paths de origen
    path_destino = './destino/'
    size = (800, 600)  # Nuevo tamaño de las imágenes

    procesar_imagenes_concurrentemente(paths_origen, path_destino, size)


## Ejercicio 5


import dask.dataframe as dd

def calcular_suma_columna(df, columna):
    """Calcula la suma de una columna en un DataFrame de Dask."""
    suma = df[columna].sum().compute()
    return suma

if __name__ == "__main__":
    # Suponiendo que 'datos.csv' es un archivo grande dividido en partes
    df = dd.read_csv('datos.csv', assume_missing=True)
    
    # Calcular la suma de la columna 'valor'
    suma_valor = calcular_suma_columna(df, 'valor')
    print(f"La suma de la columna 'valor' es: {suma_valor}")




## Ejercicio 6

import dask.dataframe as dd

def cargar_datos(path):
    """Carga un conjunto de datos distribuido desde varios archivos CSV."""
    return dd.read_csv(path)

def agrupar_y_sumar(df, columna_grupo, columna_suma):
    """Agrupa el DataFrame por una columna y calcula la suma de otra columna."""
    resultado = df.groupby(columna_grupo)[columna_suma].sum().compute()
    return resultado

if __name__ == "__main__":
    # Carga de un conjunto de datos grande distribuido en varios archivos CSV
    df = cargar_datos('datos-*.csv')  # Suponiendo que los archivos se llaman datos-01.csv, datos-02.csv, etc.
    
    # Ejemplo de operación de agrupación y suma
    suma_por_grupo = agrupar_y_sumar(df, 'columna_grupo', 'columna_suma')
    print(suma_por_grupo)



### Ejercicio 7


## Servidor

import socket

def iniciar_servidor(host, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, puerto))
        s.listen()
        print(f"Servidor escuchando en {host}:{puerto}")
        conn, addr = s.accept()
        with conn:
            print(f"Conectado por {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

if __name__ == "__main__":
    HOST = '127.0.0.1'  # Dirección del servidor
    PUERTO = 65432      # Puerto para escuchar (puertos no privilegiados son > 1023)
    iniciar_servidor(HOST, PUERTO)


## Cliente

import socket

def iniciar_cliente(host, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, puerto))
        s.sendall(b'Hola, mundo')
        data = s.recv(1024)
    print(f"Recibido {data!r}")

if __name__ == "__main__":
    HOST = '127.0.0.1'  # La dirección del servidor
    PUERTO = 65432      # El mismo puerto que el servidor
    iniciar_cliente(HOST, PUERTO)



## Ejercicio 8


import asyncio

class ServidorChat:
    def __init__(self):
        self.clientes = []

    async def manejar_cliente(self, reader, writer):
        while True:
            data = await reader.read(100)
            mensaje = data.decode().strip()

            # Registro del cliente para enviar mensajes futuros
            if writer not in self.clientes:
                self.clientes.append(writer)
                print("Nuevo cliente conectado")

            # Envío del mensaje recibido a todos los clientes conectados
            if mensaje:
                print(f"Enviando: {mensaje}")
                for cliente in self.clientes:
                    cliente.write(data)
                    await cliente.drain()

            else: # Cliente desconectado
                print("Cliente desconectado")
                self.clientes.remove(writer)
                writer.close()
                break

    async def iniciar_servidor(self):
        server = await asyncio.start_server(
            self.manejar_cliente, '127.0.0.1', 8888)
        addr = server.sockets[0].getsockname()
        print(f'Servidor de chat en {addr}')

        async with server:
            await server.serve_forever()

if __name__ == '__main__':
    servidor = ServidorChat()
    asyncio.run(servidor.iniciar_servidor())



## Ejercicio 9


import queue
import threading
import time

class SistemaColasMensajes:
    def __init__(self):
        self.cola = queue.Queue()

    def productor(self, mensaje):
        print(f"Produciendo mensaje: {mensaje}")
        self.cola.put(mensaje)

    def consumidor(self):
        while True:
            mensaje = self.cola.get()
            print(f"Consumiendo mensaje: {mensaje}")
            self.cola.task_done()
            time.sleep(1)  # Simular trabajo

def iniciar_sistema():
    sistema = SistemaColasMensajes()

    # Crear productores
    for i in range(5):
        mensaje = f"mensaje {i}"
        threading.Thread(target=sistema.productor, args=(mensaje,)).start()

    # Crear consumidor
    threading.Thread(target=sistema.consumidor, daemon=True).start()

    # Esperar a que todos los mensajes sean procesados
    sistema.cola.join()
    print("Todos los mensajes han sido consumidos.")

if __name__ == "__main__":
    iniciar_sistema()


## Ejercicio 10


pip install celery

from celery import Celery

app = Celery('nombre_proyecto', broker='URL_DEL_BROKER_DE_MENSAJES')


@app.task
def sumar(x, y):
    return x + y


celery -A nombre_proyecto worker --loglevel=info


# celery.py
from celery import Celery

app = Celery('mi_proyecto', broker='pyamqp://guest@localhost//')

# tareas.py
from celery import shared_task

@shared_task
def sumar(x, y):
    return x + y


from mi_proyecto.tareas import sumar

resultado = sumar.delay(4, 4)
print('El resultado es:', resultado.get())





