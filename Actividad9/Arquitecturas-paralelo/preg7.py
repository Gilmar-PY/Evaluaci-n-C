
from multiprocessing import Process, Queue #creación de procesos concurrentes
import time
import random
#Proporciona una cola que permite la comunicación segura entre procesos.
def producer(queue):
    for _ in range(10):
        item = random.randint(1, 100)
        queue.put(item) #Cada valor generado se coloca en la cola compartida
        print(f"Produced {item}")
        time.sleep(random.random())

def consumer(queue):
    while True:
        item = queue.get()
        if item is None: 
            break
        print(f"Consumed {item}")
        time.sleep(random.random())

if __name__ == "__main__":
    queue = Queue()   #cola compartida
# Crea dos procesos
    producers = [Process(target=producer, args=(queue,)) for _ in range(2)]
    consumers = [Process(target=consumer, args=(queue,)) for _ in range(2)]

    for p in producers:
        p.start()

    for c in consumers:
        c.start()

    for p in producers:
        p.join()

    ## Añade valores de terminación (None) a la cola para señalizar a los consumidores que deben terminar
    for _ in consumers:
        queue.put(None)

    for c in consumers:
        c.join()
