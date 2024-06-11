import threading

mutex = threading.Lock()

def critical_section():
    mutex.acquire()
    try:
        # Código de la sección crítica
        pass
    finally:
        mutex.release()
