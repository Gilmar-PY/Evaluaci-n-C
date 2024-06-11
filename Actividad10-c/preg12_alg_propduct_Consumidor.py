## Algoritmo de productores y consumidores
import threading  # Importa el módulo threading para manejar hilos
import time  
import random  

buffer = []  # Inicializa el buffer como una lista vacía
buffer_size = 10  # Tamaño máximo del buffer

# Semáforo que cuenta las posiciones vacías en el buffer
empty = threading.Semaphore(buffer_size)
# Semáforo que cuenta los elementos llenos en el buffer
full = threading.Semaphore(0)
# Semáforo para asegurar el acceso exclusivo al buffer
mutex = threading.Semaphore(1)

# Función del productor
def producer():
    while True:
        item = random.randint(1, 100)  # Genera un elemento aleatorio
        empty.acquire()  # Decrementa el semáforo empty (espera si el buffer está lleno)
        mutex.acquire()  # Entra en la sección crítica
        buffer.append(item)  # Añade el elemento al buffer
        print(f'Producer produced {item}')
        mutex.release()  # Sale de la sección crítica
        full.release()  # Incrementa el semáforo full (indica que hay un nuevo elemento en el buffer)
        time.sleep(random.random())  # Espera un tiempo aleatorio antes de producir el siguiente elemento

# Función del consumidor
def consumer():
    while True:
        full.acquire()  # Decrementa el semáforo full (espera si el buffer está vacío)
        mutex.acquire()  # Entra en la sección crítica
        item = buffer.pop(0)  # Remueve el primer elemento del buffer
        print(f'Consumer consumed {item}')
        mutex.release()  # Sale de la sección crítica
        empty.release()  # Incrementa el semáforo empty (indica que hay una posición vacía en el buffer)
        time.sleep(random.random())  # Espera un tiempo aleatorio antes de consumir el siguiente elemento

# Crea e inicia el hilo del productor
producer_thread = threading.Thread(target=producer)
# Crea e inicia el hilo del consumidor
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
# Espera a que los hilos terminen (en este caso, nunca terminan)
producer_thread.join()
consumer_thread.join()
'''


    Productor:
        Genera un elemento aleatorio y lo añade al buffer.
        Utiliza el semáforo empty para esperar si el buffer está lleno.
        Usa mutex para acceder de forma exclusiva al buffer.
        Incrementa full para indicar que hay un nuevo elemento disponible.

    Consumidor:
        Retira un elemento del buffer.
        Utiliza el semáforo full para esperar si el buffer está vacío.
        Usa mutex para acceder de forma exclusiva al buffer.
        Incrementa empty para indicar que hay una nueva posición vacía en el buffer.

Resumen de la Lógica

    Sincronización con Semáforos:
        Los semáforos empty y full aseguran que el productor no añada elementos a un buffer lleno y que el consumidor no retire elementos de un buffer vacío.
        El semáforo mutex asegura que solo un hilo acceda al buffer a la vez, previniendo condiciones de carrera.

    Sección Crítica:
        Las operaciones de añadir y retirar elementos del buffer están protegidas por el semáforo mutex para evitar inconsistencias.
        '''
