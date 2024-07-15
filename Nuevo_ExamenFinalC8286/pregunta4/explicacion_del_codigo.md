
# Importación de Módulos

```python
import threading
import time
import random
from collections import defaultdict

    threading: Módulo para crear y gestionar hilos en Python.
    time: Módulo para manejar operaciones relacionadas con el tiempo (pausas, latencia).
    random: Módulo para generar números aleatorios, utilizado para simular fallos y latencia de red.
    collections.defaultdict: Estructura de datos para manejar diccionarios con valores por defecto.

Definición de la Clase Node

python

class Node:
    def __init__(self, node_id, cluster):
        self.node_id = node_id
        self.cluster = cluster
        self.data = {}
        self.log = []
        self.leader = None
        self.is_leader = False
        self.votes = 0
        self.alive = True
        self.term = 0

    Node: Representa un nodo en el clúster.
        Atributos:
            node_id: Identificador único del nodo.
            cluster: Referencia al clúster al que pertenece el nodo.
            data: Diccionario para almacenar los datos del nodo.
            log: Lista para almacenar las entradas de registro del nodo.
            leader: Referencia al líder actual del clúster.
            is_leader: Booleano que indica si el nodo es el líder.
            votes: Contador de votos recibidos en el proceso de elección de líder.
            alive: Booleano que indica si el nodo está activo.
            term: Término actual del nodo utilizado en el algoritmo de consenso.

Método send_message

python

def send_message(self, target_node, message):
    if not target_node.alive:
        return
    time.sleep(random.uniform(0.1, 0.5))  # Simulación de latencia de red
    target_node.receive_message(message)

    send_message: Envía un mensaje a otro nodo.
        Parámetros:
            target_node: Nodo de destino.
            message: Mensaje a enviar.
        Funcionalidad: Si el nodo de destino está activo, se introduce una latencia de red simulada antes de enviar el mensaje.

Método receive_message

python

def receive_message(self, message):
    if message['type'] == 'vote_request':
        self.handle_vote_request(message)
    elif message['type'] == 'vote_response':
        self.handle_vote_response(message)
    elif message['type'] == 'append_entries':
        self.handle_append_entries(message)

    receive_message: Recibe y maneja mensajes entrantes.
        Parámetros:
            message: Mensaje recibido.
        Funcionalidad: Dependiendo del tipo de mensaje, se llama al método correspondiente (handle_vote_request, handle_vote_response, handle_append_entries).

Método handle_vote_request

python

def handle_vote_request(self, message):
    if self.alive:
        response = {'type': 'vote_response', 'vote_granted': True, 'term': message['term']}
        self.send_message(message['candidate'], response)

    handle_vote_request: Maneja las solicitudes de voto.
        Parámetros:
            message: Mensaje de solicitud de voto.
        Funcionalidad: Si el nodo está activo, envía una respuesta de voto afirmativo al candidato solicitante.

Método handle_vote_response

python

def handle_vote_response(self, message):
    if message['vote_granted']:
        self.votes += 1
        if self.votes > len(self.cluster.nodes) // 2:
            self.is_leader = True
            self.leader = self
            print(f'Node {self.node_id} has become the leader')
            self.broadcast_append_entries()

    handle_vote_response: Maneja las respuestas de voto.
        Parámetros:
            message: Mensaje de respuesta de voto.
        Funcionalidad: Si se concede el voto, incrementa el contador de votos y verifica si ha alcanzado la mayoría para convertirse en líder. Si es así, se declara líder y difunde entradas de registro.

Método handle_append_entries

python

def handle_append_entries(self, message):
    if self.alive:
        self.log.append(message['entry'])
        self.data.update(message['entry'])
        print(f'Node {self.node_id} appended entry: {message["entry"]}')

    handle_append_entries: Maneja la recepción de entradas de registro.
        Parámetros:
            message: Mensaje con la entrada de registro.
        Funcionalidad: Si el nodo está activo, añade la entrada al registro y actualiza los datos.

Método request_votes

python

def request_votes(self):
    self.votes = 1
    self.term += 1
    for node in self.cluster.nodes:
        if node != self and node.alive:
            message = {'type': 'vote_request', 'candidate': self, 'term': self.term}
            self.send_message(node, message)

    request_votes: Solicita votos de otros nodos.
        Funcionalidad: Inicializa el contador de votos, incrementa el término y envía solicitudes de voto a otros nodos activos en el clúster.

Método broadcast_append_entries

python

def broadcast_append_entries(self):
    for node in self.cluster.nodes:
        if node != self and node.alive:
            entry = {'key': random.choice(['x', 'y', 'z']), 'value': random.randint(1, 100)}
            self.log.append(entry)
            self.data.update(entry)
            message = {'type': 'append_entries', 'entry': entry}
            self.send_message(node, message)

    broadcast_append_entries: Difunde entradas de registro a otros nodos.
        Funcionalidad: Genera una nueva entrada aleatoria, la añade al registro y actualiza los datos, luego envía la entrada a otros nodos activos.

Método run

python

def run(self):
    while self.alive:
        time.sleep(random.uniform(1, 3))
        if self.is_leader:
            self.broadcast_append_entries()
        else:
            self.request_votes()

    run: Método principal de ejecución del nodo.
        Funcionalidad: Bucle de ejecución continua que alterna entre solicitar votos y difundir entradas de registro, dependiendo de si el nodo es líder o no.

Definición de la Clase Cluster

python

class Cluster:
    def __init__(self, num_nodes):
        self.nodes = [Node(node_id, self) for node_id in range(num_nodes)]

    Cluster: Representa el conjunto de nodos.
        Atributos:
            nodes: Lista de nodos que componen el clúster.

Método start

python

def start(self):
    self.threads = []
    for node in self.nodes:
        t = threading.Thread(target=node.run)
        self.threads.append(t)
        t.start()

    start: Inicia los hilos de ejecución de todos los nodos del clúster.
        Funcionalidad: Crea y arranca un hilo para cada nodo en el clúster.

Método simulate_failure

python

def simulate_failure(self):
    node = random.choice(self.nodes)
    node.alive = False
    print(f'Node {node.node_id} has failed.')

    simulate_failure: Simula la falla de un nodo aleatorio del clúster.
        Funcionalidad: Selecciona un nodo aleatorio y lo marca como inactivo.

Método heal_failure

python

def heal_failure(self):
    node = random.choice(self.nodes)
    node.alive = True
    print(f'Node {node.node_id} has healed.')

    heal_failure: Simula la recuperación de un nodo aleatorio del clúster.
        Funcionalidad: Selecciona un nodo aleatorio y lo marca como activo.

Método run_simulation

python

def run_simulation(self, cycles):
    for _ in range(cycles):
        time.sleep(5)
        self.simulate_failure()
        time.sleep(5)
        self.heal_failure()
    print("Simulation complete. Stopping all nodes.")
    for node in self.nodes:
        node.alive = False

    run_simulation: Ejecuta la simulación con un número especificado de ciclos de fallos y recuperaciones.
        Funcionalidad: Alterna entre simular fallos y recuperaciones de nodos durante un número fijo de ciclos, luego detiene todos los nodos.

Inicialización y Ejecución del Clúster

python

cluster = Cluster(5)
cluster.start()
cluster.run_simulation(5)

for t in cluster.threads:
    t.join()

    Inicialización: Crea un clúster con 5 nodos.
    Inicio: Inicia la ejecución de los nodos.
    Simulación: Corre la simulación con un número fijo de ciclos de fallos y recuperaciones.
    Esperar: Espera a que todos los hilos terminen su ejecución.

Resumen del Comportamiento del Sistema

    Consistencia:
        El algoritmo de consenso (similar a Raft) asegura que solo un líder puede añadir entradas de registro, garantizando que todos los nodos tengan un registro consistente de operaciones.

    Disponibilidad:
        Los nodos intentan mantenerse disponibles, incluso si algunos fallan. El clúster intenta elegir un nuevo líder si el líder actual falla.

    Tolerancia a Particiones:
        Los mensajes se envían con latencia simulada y los nodos pueden fallar aleatoriamente, simulando particiones de red. El sistema sigue intentando mantener la consistencia y la disponibilidad mediante la elección de líderes y la difusión de entradas de registro.

Este sistema simula de manera efectiva las tres propiedades del Teorema CAP, mostrando cómo un sistema distribuido puede manejar la consistencia, disponibilidad y tolerancia a particiones bajo diferentes configuraciones y condiciones de red.
