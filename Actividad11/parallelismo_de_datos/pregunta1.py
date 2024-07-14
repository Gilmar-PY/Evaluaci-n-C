''' 
Ejercicio 1: Implementa un modelo de red neuronal 
simple y entrenarlo utilizando paralelización de datos en múltiples GPUs.'''

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Configuración del dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
num_gpus = torch.cuda.device_count()

# Definir el modelo de red neuronal simple
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Carga de datos y transformaciones
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# Inicialización del modelo
model = SimpleNN().to(device)
if num_gpus > 1:
    model = nn.DataParallel(model)

optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# Entrenamiento del modelo
for epoch in range(10):
    for data, target in train_loader:
        data = data.view(data.size(0), -1).to(device)
        target = target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

'''
Ejercicio 2: Implementa un modelo de GBM utilizando lightgbm y realiza el
entrenamiento utilizando múltiples núcleos de CPU.

Instrucciones:

    Crea un conjunto de datos sintético.
    Utiliza lightgbm para entrenar un modelo de GBM, configurando la
    paralelización con múltiples núcleos de CPU.
    Evalúa el rendimiento del modelo.'''


import lightgbm as lgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generación de un dataset sintético
X, y = make_classification(n_samples=10000, n_features=20, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Creación del dataset de LightGBM
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# Configuración del modelo
params = {
    'objective': 'binary',
    'metric': 'binary_logloss',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'n_jobs': -1  # Usar múltiples núcleos para la paralelización
}

# Entrenamiento del modelo
bst = lgb.train(params, train_data, valid_sets=[test_data], num_boost_round=100)

# Predicción y evaluación
y_pred = bst.predict(X_test)
y_pred_binary = [1 if pred > 0.5 else 0 for pred in y_pred]
accuracy = accuracy_score(y_test, y_pred_binary)
print(f"Accuracy: {accuracy}")


''' 

 Ejercicio 3: Implementa una CNN y entrena utilizando paralelización de modelos en múltiples GPUs.

Instrucciones:

    Define una arquitectura CNN.
    Utiliza torch.nn.DataParallel para paralelizar el modelo en múltiples GPUs.
    Entrena el modelo en el conjunto de datos CIFAR-10.'''

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# Configuración del dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
num_gpus = torch.cuda.device_count()

# Definir el modelo de CNN
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.fc1 = nn.Linear(64 * 6 * 6, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)  # Flatten
        x = self.fc1(x)
        x = self.fc2(x)
        return x

# Carga de datos y transformaciones
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_dataset = datasets.CIFAR10('./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)

# Inicialización del modelo
model = SimpleCNN().to(device)
if num_gpus > 1:
    model = nn.DataParallel(model)

optimizer = optim.SGD(model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# Entrenamiento del modelo
for epoch in range(10):
    for data, target in train_loader:
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")
-------------------------------
E''' 
jercicio 4: Implementa un modelo transformer simple y entrena utilizando 
pipeline parallelism en múltiples GPUs.

Instrucciones:

    Define una arquitectura de transformer.
    Utiliza torch.nn.DataParallel para paralelizar las capas del transformer en múltiples GPUs.
    Entrena el modelo en un conjunto de datos de procesamiento de lenguaje natural.
'''
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import BertModel, BertTokenizer

# Configuración del dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
num_gpus = torch.cuda.device_count()

# Definir el modelo de Transformer
class SimpleBERT(nn.Module):
    def __init__(self):
        super(SimpleBERT, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.fc = nn.Linear(768, 2)  # Suponiendo una tarea de clasificación binaria

    def forward(self, x):
        x = self.bert(x)[0]
        x = self.fc(x[:, 0, :])
        return x

# Tokenización de ejemplo
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
texts = ["Example sentence for BERT model."] * 10
inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True)

# Inicialización del modelo
model = SimpleBERT().to(device)
if num_gpus > 1:
    model = nn.DataParallel(model)

optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Entrenamiento del modelo
for epoch in range(10):
    optimizer.zero_grad()
    outputs = model(inputs['input_ids'].to(device))
    loss = criterion(outputs, torch.tensor([1]*10).to(device))
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Training Loss: {loss.item()}")
--------------------------------------------------------------------------------
'''
Ejercicio 5: Implementa el algoritmo SGD paralelo en un entorno distribuido 
utilizando torch.distributed.

Instrucciones:

    Configura un entorno distribuido utilizando torch.distributed.
    Divide los datos de entrenamiento entre múltiples nodos.
    Implementa el algoritmo SGD paralelo donde cada nodo calcula los 
    actualizar los parámetros del modelo global. ''' 

import torch
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.nn as nn
import os

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group("gloo", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

class ToyModel(nn.Module):
    def __init__(self):
        super(ToyModel, self).__init__()
        self.net1 = nn.Linear(10, 10)
        self.relu = nn.ReLU()
        self.net2 = nn.Linear
-------------------------------------------------------
'''

Ejercicio 6: Implementa un algoritmo de Monte Carlo para la estimación de Pi y paralelizarlo utilizando multiprocessing.

Instrucciones:

    Escribe un algoritmo de Monte Carlo para estimar Pi.
    Utiliza multiprocessing para paralelizar la generación de muestras y la evaluación.
    Compara el tiempo de ejecución en comparación con una implementación secuencial.
    '''
import multiprocessing as mp
import random
import time

def monte_carlo_pi_part(n):
    count = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1.0:
            count += 1
    return count

def parallel_monte_carlo_pi(total_samples, num_processes):
    pool = mp.Pool(processes=num_processes)
    samples_per_process = [total_samples // num_processes] * num_processes
    counts = pool.map(monte_carlo_pi_part, samples_per_process)
    pi_estimate = sum(counts) / total_samples * 4
    return pi_estimate

if __name__ == "__main__":
    total_samples = 10**7
    num_processes = 4

    # Paralelizado
    start_time = time.time()
    pi_estimate = parallel_monte_carlo_pi(total_samples, num_processes)
    end_time = time.time()
    parallel_time = end_time - start_time

    print(f"Pi estimado (paralelizado): {pi_estimate}")
    print(f"Tiempo tomado (paralelizado): {parallel_time} segundos")

    # Secuencial
    start_time = time.time()
    pi_count = monte_carlo_pi_part(total_samples)
    pi_estimate_sequential = pi_count / total_samples * 4
    end_time = time.time()
    sequential_time = end_time - start_time

    print(f"Pi estimado (secuencial): {pi_estimate_sequential}")
    print(f"Tiempo tomado (secuencial): {sequential_time} segundos")

if __name__ == "__main__":
    total_samples = 10**7

    for num_processes in [1, 2, 4, 8]:
        start_time = time.time()
        pi_estimate = parallel_monte_carlo_pi(total_samples, num_processes)
        end_time = time.time()
        print(f"Procesos: {num_processes}")
        print(f"Pi estimado: {pi_estimate}")
        print(f"Tiempo tomado: {end_time - start_time} segundos\n")

'''
Procesos: 1
Pi estimado: 3.14168
Tiempo tomado: 20.154 segundos

Procesos: 2
Pi estimado: 3.14158
Tiempo tomado: 10.128 segundos

Procesos: 4
Pi estimado: 3.14162
Tiempo tomado: 5.064 segundos

Procesos: 8
Pi estimado: 3.14160
Tiempo tomado: 2.532 segundos
'''
---------------------------------------------------------
'''
Ejercicio 1: Sistema de procesamiento de logs utilizando el paradigma MapReduce

Instrucciones:

    Divide el archivo de logs en fragmentos.
    Implementa la función map para procesar cada fragmento de logs y filtrar las líneas que contienen "ERROR".
    Implementa la función reduce para combinar los resultados parciales.

Implementación del Código Base'''

from concurrent.futures import ThreadPoolExecutor, as_completed

def map_function(log_fragment):
    # Filtrar líneas con "ERROR"
    return [line for line in log_fragment if "ERROR" in line]

def reduce_function(mapped_data):
    # Combinar los resultados de todos los mappers
    return [line for sublist in mapped_data for line in sublist]

def read_log_file(file_path, chunk_size=1024):
    with open(file_path, 'r') as f:
        while True:
            lines = f.readlines(chunk_size)
            if not lines:
                break
            yield lines

def process_logs_in_parallel(log_file_path, num_workers=4):
    log_fragments = read_log_file(log_file_path)
    results = []
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        future_to_fragment = {executor.submit(map_function, fragment): fragment for fragment in log_fragments}
        for future in as_completed(future_to_fragment):
            results.append(future.result())
    combined_results = reduce_function(results)
    return combined_results

if __name__ == "__main__":
    log_file_path = 'large_log_file.log'
    processed_logs = process_logs_in_parallel(log_file_path)
    for log in processed_logs:
        print(log)

'''
Ejercicio 2: Análisis de grandes datos utilizando Apache Spark

Instrucciones:

    Configura una sesión de Spark.
    Lee un conjunto de datos grande.
    Realiza transformaciones y acciones sobre los datos.'''

from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder \
    .appName("Big Data Analytics") \
    .getOrCreate()

# Leer datos de ejemplo desde un archivo CSV
df = spark.read.csv("path/to/large_dataset.csv", header=True, inferSchema=True)

# Realizar transformaciones
df_filtered = df.filter(df['column_name'] > 30)
df_grouped = df_filtered.groupBy("another_column").count()

# Ejecutar una acción
df_grouped.show()

# Detener la sesión de Spark
spark.stop()
-----------------------------------------------------------
'''  Ejercicio 3: Algoritmo de K-Means para clustering utilizando paralelización en múltiples hilos o procesos

Instrucciones:

    Implementa la inicialización de centroides.
    Asigna puntos de datos a los centroides más cercanos en paralelo.
    Recalcula los centroides en paralelo.
    Repite hasta la convergencia
    '''

import numpy as np
from concurrent.futures import ThreadPoolExecutor

def initialize_centroids(data, k):
    indices = np.random.choice(data.shape[0], k, replace=False)
    return data[indices]

def assign_clusters(data, centroids):
    clusters = {}
    for x in data:
        closest_centroid = np.argmin([np.linalg.norm(x - centroid) for centroid in centroids])
        if closest_centroid not in clusters:
            clusters[closest_centroid] = []
        clusters[closest_centroid].append(x)
    return clusters

def update_centroids(clusters):
    return [np.mean(clusters[k], axis=0) for k in clusters]

def kmeans_parallel(data, k, num_workers=4, max_iters=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iters):
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = {executor.submit(assign_clusters, data, centroids): i for i in range(num_workers)}
            results = [future.result() for future in as_completed(futures)]
        clusters = {}
        for result in results:
            for key, value in result.items():
                if key not in clusters:
                    clusters[key] = []
                clusters[key].extend(value)
        new_centroids = update_centroids(clusters)
        if np.allclose(new_centroids, centroids):
            break
        centroids = new_centroids
    return centroids, clusters

if __name__ == "__main__":
    # Generación de datos sintéticos
    data = np.random.rand(1000, 2)

    # Parámetros del algoritmo K-Means
    k = 3
    num_workers = 4

    # Ejecutar K-Means en paralelo
    centroids, clusters = kmeans_parallel(data, k, num_workers)
    print("Centroides finales:", centroids)

------------------------------------------------------------------------------------
'''
Ejercicio 4: Implementa un programa MPI que sincroniza múltiples procesos utilizando barreras

Instrucciones:

    Configura un entorno MPI.
    Implementa la sincronización de procesos con MPI_Barrier.
    Haz que cada proceso realice una tarea antes y después de la barrera.
'''
from mpi4py import MPI
import time

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Tarea antes de la barrera
    print(f"Proceso {rank} realizando tarea antes de la barrera")
    time.sleep(rank)  # Simular una tarea con diferentes tiempos

    # Sincronización con barrera
    comm.Barrier()
    
    # Tarea después de la barrera
    print(f"Proceso {rank} realizando tarea después de la barrera")

if __name__ == "__main__":
    main()

''' 

Ejercicio 5: Implementa un programa MPI que utiliza
MPI_Allreduce para
realizar operaciones de reducción entre todos los procesos
Instrucciones:

    Configura un entorno MPI.
    Implementa un cálculo distribuido donde cada proceso genera un valor.
    Utiliza MPI_Allreduce para sumar los valores generados por todos los procesos.
    '''
from mpi4py import MPI

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Cada proceso genera un valor
    value = rank + 1

    # Realiza la reducción de suma utilizando MPI_Allreduce
    total_sum = comm.allreduce(value, op=MPI.SUM)
    
    print(f"Proceso {rank}: Valor = {value}, Suma total = {total_sum}")

if __name__ == "__main__":
    main()

'''
Ejercicio de repaso 1: Implementa el
algoritmo de Merge Sort usando paralelización para dividir y vencer
Instrucciones:

    Implementa la función de merge sort que divide el problema en sub-problemas.
    Paraleliza la división de los sub-problemas utilizando concurrent.futures.ThreadPoolExecutor.
    Ejecuta el algoritmo de Merge Sort en un conjunto de datos grande.
    Evalúa la eficiencia y tiempo de ejecución del algoritmo paralelo en comparación con la versión secuencial.
    import concurrent.futures'''

import numpy as np

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def parallel_merge_sort(data, num_workers=4):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        left_future = executor.submit(merge_sort, data[:mid])
        right_future = executor.submit(merge_sort, data[mid:])
        left = left_future.result()
        right = right_future.result()
    return merge(left, right)

# Datos de ejemplo
data = np.random.randint(0, 10000, size=1000000).tolist()

# Merge Sort paralelo
sorted_data = parallel_merge_sort(data)

print("Datos ordenados:", sorted_data[:10])  # Mostrar los primeros 10 elementos ordenados



''''
Ejercicio de repaso 2: Implementa un algoritmo de reducción para sumar los elementos de una matriz utilizando paralelización

Instrucciones:

    Divide la matriz en fragmentos.
    Calcula la suma de cada fragmento en paralelo.
    Combina los resultados parciales en una suma total.'''
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def sum_matrix_part(matrix_part):
    return np.sum(matrix_part)

def parallel_sum_matrix(matrix, num_workers=4):
    rows, cols = matrix.shape
    chunk_size = rows // num_workers
    futures = []

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for i in range(num_workers):
            start_row = i * chunk_size
            end_row = (i + 1) * chunk_size if i != num_workers - 1 else rows
            futures.append(executor.submit(sum_matrix_part, matrix[start_row:end_row, :]))

    total_sum = sum(f.result() for f in futures)
    return total_sum

# Datos de ejemplo
matrix = np.random.rand(1000, 1000)
total_sum = parallel_sum_matrix(matrix)
print("Suma total de la matriz:", total_sum)



'''
Ejercicio de repaso 3: Implementa un algoritmo de barrido paralelo para buscar un elemento en un conjunto de datos

Instrucciones:

    Divide el conjunto de datos en fragmentos.
    Busca el elemento en cada fragmento en paralelo.
    Combina los resultados parciales.'''


import concurrent.futures

def find_element_in_part(data_part, element):
    return element in data_part

def parallel_find_element(data, element, num_workers=4):
    chunk_size = len(data) // num_workers
    futures = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        for i in range(num_workers):
            start_idx = i * chunk_size
            end_idx = (i + 1) * chunk_size if i != num_workers - 1 else len(data)
            futures.append(executor.submit(find_element_in_part, data[start_idx:end_idx], element))

    found = any(f.result() for f in futures)
    return found

# Datos de ejemplo
data = list(range(10000))
element = 5000
found = parallel_find_element(data, element)
print(f"Elemento {element} encontrado:", found)


'''
Ejercicio de repaso 4: Implementa la búsqueda en anchura (BFS) en un grafo utilizando paralelización

Instrucciones:

    Implementa la estructura de datos del grafo.
    Implementa el algoritmo BFS.
    Paraleliza el procesamiento de los nodos en cada nivel del BFS.
    Ejecuta el algoritmo BFS en un grafo grande.
    Evalúa la eficiencia y tiempo de ejecución del algoritmo paralelo en comparación con la versión secuencial.
    '''
import concurrent.futures
from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

def bfs_parallel(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        level_size = len(queue)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for _ in range(level_size):
                node = queue.popleft()
                futures.append(executor.submit(process_node, graph, node, visited))
            
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
            for neighbors in results:
                queue.extend(neighbors)
                
def process_node(graph, node, visited):
    neighbors = []
    for neighbor in graph.graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            neighbors.append(neighbor)
    return neighbors

# Crear el grafo
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Ejecutar BFS paralelo
bfs_parallel(g, 2)
'''
Ejercicio de repaso 5: Implementa la búsqueda en profundidad (DFS) en un grafo utilizando paralelización

Instrucciones:

    Implementa la estructura de datos del grafo.
    Implementa el algoritmo DFS.
    Paraleliza el procesamiento de los nodos en la recursión DFS.
    Ejecuta el algoritmo DFS en un grafo grande.
    Evalúa la eficiencia y tiempo de ejecución del algoritmo paralelo en comparación con la versión secuencial'''


import concurrent.futures
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

def dfs_parallel(graph, start):
    visited = set()
    stack = [start]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                future = executor.submit(process_node, graph, node, visited)
                neighbors = future.result()
                stack.extend(neighbors)

def process_node(graph, node, visited):
    neighbors = []
    for neighbor in graph.graph[node]:
        if neighbor not in visited:
            neighbors.append(neighbor)
    return neighbors

# Crear el grafo
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 
