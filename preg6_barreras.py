import threading
import time
import random

# Crear una barrera para 3 hilos
barrier = threading.Barrier(3)

def worker(barrier, id):
    print(f'Thread {id} is starting.')
    time.sleep(random.uniform(0.1, 1.0))
    print(f'Thread {id} is waiting at the barrier.')
    barrier.wait()
    print(f'Thread {id} has passed the barrier.')

# Crear y lanzar hilos
threads = [threading.Thread(target=worker, args=(barrier, i)) for i in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
