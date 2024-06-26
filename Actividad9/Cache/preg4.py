<<<<<<< HEAD
=======
'''
4 . Analiza el código que implementa una forma sencilla de prefetching 
de datos, cargando datos en la caché antes de que sean necesarios.'''

>>>>>>> f47a74695eb7a0eefc6abf9022444b7255c0ec51
import numpy as np
import random
import time

def prefetch_data(array, indices, prefetch_distance):
    for i in range(len(indices) - prefetch_distance):
        _ = array[indices[i + prefetch_distance]]  # Prefetch
        array[indices[i]] += 1  # Access

size = 10**6
array = np.zeros(size)
indices = list(range(size))
random.shuffle(indices)
prefetch_distance = 10

start_time = time.perf_counter()#guarda el tiempo actual
prefetch_data(array, indices, prefetch_distance)
end_time = time.perf_counter()

total_time = end_time - start_time
print(f"Tiempo con prefetching: {total_time:.6f} segundos")

