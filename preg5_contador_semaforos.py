import threading

# Crear un semáforo contador con un valor inicial de 3
counting_semaphore = threading.Semaphore(3)

def limited_resource_access():
    counting_semaphore.acquire()
    try:
        # Código que accede al recurso limitado
        pass
    finally:
        counting_semaphore.release()
