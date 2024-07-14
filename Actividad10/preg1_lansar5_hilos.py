import threading

def print_id(thread_id):
    for _ in range(10):
        print(f"Hilo {thread_id}")

threads = []
for i in range(5):
    thread = threading.Thread(target=print_id, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

'''
Ejercicio 2: Desarrolla un programa que cree tres hilos. Cada 
hilo debe incrementar un contador compartido 100 veces. Implementa una 
forma de esperar a
que todos los hilos terminen antes de imprimir el valor final del contador.'''

import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100):
        with lock:
            counter += 1

threads = []
for _ in range(3):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Valor final del contador:", counter)

'''
Implementa un programa que use
semáforos para controlar el acceso a un recurso
compartido por tres hilos.'''


import threading

semaphore = threading.Semaphore(1)
shared_resource = 0

def access_resource(thread_id):
    global shared_resource
    semaphore.acquire()
    try:
        print(f"Hilo {thread_id} accediendo al recurso compartido")
        shared_resource += 1
    finally:
        semaphore.release()

threads = []
for i in range(3):
    thread = threading.Thread(target=access_resource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Valor final del recurso compartido:", shared_resource)



''' 
Utiliza mutexes para proteger la escritura a una variable 
compartida en un entorno multihilo.
Asegúrate de que cada hilo pueda actualizar la variable de forma segura.'''

import threading

shared_variable = 0
mutex = threading.Lock()

def update_variable(thread_id):
    global shared_variable
    for _ in range(10):
        with mutex:
            shared_variable += 1
            print(f"Hilo {thread_id} actualizó la variable a {shared_variable}")

threads = []
for i in range(5):
    thread = threading.Thread(target=update_variable, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Valor final de la variable compartida:", shared_variable)


------------------------------
'''
Explica la diferencia entre un semáforo binario 
y un mutex. ¿En qué situaciones es preferible usar cada uno?
    Semáforo binario: Es un tipo de semáforo que puede tener solo dos valores: 0 y 1. Se usa para permitir o bloquear el acceso a un recurso compartido. A diferencia de un mutex, un semáforo binario no necesariamente está asociado a un solo hilo propietario y puede ser utilizado para sincronizar más de dos hilos.

    Mutex: Es un mecanismo de exclusión mutua que asegura que solo un hilo pueda acceder a un recurso compartido a la vez. Un mutex está asociado a un hilo propietario y solo ese hilo puede liberar el mutex.

Situaciones preferibles:

    Usar mutex cuando se necesita asegurar que solo un hilo puede acceder a un recurso compartido a la vez.
    Usar semáforo binario cuando se necesita controlar el acceso a un recurso de manera más general y posiblemente entre más de dos hilos.

'''

-------------------------------------------
'''Ejercicio 6: Describe un escenario en el que el uso de una barrera 
sería crítico en un sistema de procesamiento de datos distribuido.
¿Cómo asegurarías que todos los hilos alcancen la barrera de manera 
eficiente sin desperdiciar recursos del CPU?

Escenario: En un sistema de procesamiento de datos distribuido,
varios hilos realizan etapas de procesamiento de datos en paralelo.
Es crucial que todos los hilos completen una etapa antes de que cualquiera 
de ellos comience la siguiente.

Solución: Utilizar una barrera para sincronizar los hilos al final de 
cada etapa.
'''

import threading

def process_data(barrier, thread_id):
    print(f"Hilo {thread_id} procesando datos")
    barrier.wait()  # Espera a que todos los hilos alcancen la barrera
    print(f"Hilo {thread_id} ha alcanzado la barrera")

barrier = threading.Barrier(5)

threads = []
for i in range(5):
    thread = threading.Thread(target=process_data, args=(barrier, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


''' Ejercicio 7: Propón un algoritmo de detección de deadlock 
para un sistema con múltiples tipos de recursos. Considera cómo
podrías implementar este algoritmo en un sistema operativo real.

Algoritmo de detección de deadlock:

    Construir el grafo de asignación de recursos:
        Nodo por cada proceso y recurso.
        Arista desde un proceso a un recurso si el proceso ha
        solicitado el recurso.
        Arista desde un recurso a un proceso si el recurso está asignado a
        ese proceso.

    Detectar ciclos en el grafo:
        Utilizar un algoritmo de detección de ciclos (como DFS) para 
        identificar ciclos en el grafo de asignación de recursos.

    Implementación en un sistema operativo:
        Periodicamente, el sistema operativo debe construir el grafo de 
        asignación de recursos y ejecutar el algoritmo de detección de ciclos.
        Si se detecta un ciclo, el sistema operativo puede tomar acciones 
        correctivas como abortar uno de los procesos involucrados en el ciclo para romper el deadlock.
'''
------------------------------------------------------------
''' Ejercicio 8: Describe un escenario donde un sistema de intentos de 
recuperación automática podría llevar a un livelock. Propón una solución 
basada en el diseño del software.

Escenario: Dos procesos intentan acceder a dos recursos compartidos. 
Ambos procesos detectan que no pueden obtener todos los recursos necesarios, 
liberan los recursos y vuelven a intentar. Esto lleva a un ciclo sin progreso
(livelock).

Solución: Implementar un backoff aleatorio o un sistema de prioridad. 
Cada proceso espera un tiempo aleatorio antes de volver a intentar, o los
procesos tienen diferentes prioridades para acceder a los recursos.'''

--------------------------------------------------------------------------
''' 
Ejercicio 9: Crea un escenario de deadlock utilizando dos mutexes y
dos hilos. Cada hilo intenta adquirir los mutexes en orden diferente.'''

import threading

mutex1 = threading.Lock()
mutex2 = threading.Lock()

def thread1():
    with mutex1:
        print("Hilo 1 adquirió mutex1")
        with mutex2:
            print("Hilo 1 adquirió mutex2")

def thread2():
    with mutex2:
        print("Hilo 2 adquirió mutex2")
        with mutex1:
            print("Hilo 2 adquirió mutex1")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

'''
Ejercicio 10: Desarrolla un ejemplo de condición de carrera donde dos
hilos incrementan y decrementan, 
respectivamente, un contador compartido sin sincronización adecuada.'''


import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

def decrement():
    global counter
    for _ in range(100000):
        counter -= 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

t1.start()
t2.start()

t1.join()
t2.join()

print("Valor final del contador:", counter)

---------------------------------------------------------------
''' Ejercicio 11: Considera un sistema de votación online donde se esperan múltiples accesos concurrentes. Describe cómo podrías diseñar el sistema para evitar condiciones de carrera sin degradar el rendimiento.

Solución:

    Utilizar una base de datos transaccional que asegure la consistencia de las operaciones de voto.
    Implementar mecanismos de bloqueo a nivel de fila en la base de datos.
    Usar operaciones atómicas y sistemas de caché distribuido para manejar las lecturas concurrentes de resultados.

Ejercicio 12: Describe cómo el algoritmo de Lamport para la exclusión mutua 
puede ser aplicado en un sistema de reserva de entradas en línea.
¿Qué desafíos podrían surgir y cómo los resolverías?

Aplicación del Algoritmo de Lamport:

    Cada solicitud de reserva de entrada se envía con una marca de tiempo.
    Las solicitudes se ordenan por marca de tiempo y se procesan en orden.
    Cada servidor de reservas mantiene un reloj lógico para asegurar el orden de las solicitudes.

Desafíos:

    Retrasos en la red pueden causar diferencias en las marcas de tiempo.
    Solución: Usar un protocolo de sincronización de tiempo para ajustar las marcas de tiempo.

Ejercicio 13: Analiza el algoritmo de Ricart-Agrawala en el contexto de un sistema de control de tráfico aéreo. ¿Cómo se manejarían las prioridades de los mensajes?

Aplicación en Control de Tráfico Aéreo:

    Cada solicitud de acceso a una pista de aterrizaje se envía a otros controladores con una marca de tiempo.
    Las solicitudes se procesan en orden
'''

