### uso de mutex

import threading

# Crear un mutex
mutex = threading.Lock()

def critical_section():
    mutex.acquire()
    try:
        # Código de la sección crítica
        print("Thread", threading.current_thread().name, "está en la sección crítica")
    finally:
        mutex.release()

# Función que cada hilo ejecutará
def thread_function():
    for _ in range(3):
        critical_section()

# Crear varios hilos
threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, name=f'Thread-{i+1}')
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()
#######################
uso de semaforros binarios 
import threading

# Crear un semáforo binario
binary_semaphore = threading.Semaphore(1)

def critical_section():
    binary_semaphore.acquire()
    try:
        # Código de la sección crítica
        print("Thread", threading.current_thread().name, "está en la sección crítica")
    finally:
        binary_semaphore.release()

# Función que cada hilo ejecutará
def thread_function():
    for _ in range(3):
        critical_section()

# Crear varios hilos
threads = []
for i in range(5):
    thread = threading.Thread(target=thread_function, name=f'Thread-{i+1}')
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

