import threading

# Crear un semáforo binario
binary_semaphore = threading.Semaphore(1)

def critical_section():
    binary_semaphore.acquire()
    try:
        # Código de la sección crítica
        pass
    finally:
        binary_semaphore.release()
