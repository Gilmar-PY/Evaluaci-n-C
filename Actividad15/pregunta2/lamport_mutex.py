
import threading
import time
from queue import PriorityQueue

class LamportMutex:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id  # ID único del nodo
        self.num_nodes = num_nodes  # Número total de nodos en el sistema
        self.clock = 0  # Reloj de Lamport inicializado en 0
        self.request_queue = PriorityQueue()  # Cola de prioridad para gestionar las solicitudes de entrada
        self.replies_received = 0  # Contador de respuestas recibidas
        self.lock = threading.Lock()  # Candado para manejar la concurrencia en la sección crítica

    def send_request(self):
        self.clock += 1  # Incrementa el reloj de Lamport
        self.request_queue.put((self.clock, self.node_id))  # Agrega la solicitud actual a la cola de prioridad
        for i in range(self.num_nodes):
            if i != self.node_id:
                self.send_message(i, 'REQUEST', self.clock, self.node_id)  # Envía mensajes de solicitud a todos los otros nodos

    def send_message(self, target, msg_type, timestamp, sender_id):
        print(f"Nodo {self.node_id} enviando {msg_type} al Nodo {target} con timestamp {timestamp}")
        time.sleep(0.1)  # Simula el tiempo de envío del mensaje

    def receive_message(self, msg_type, timestamp, sender_id):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1  # Actualiza el reloj de Lamport al recibir un mensaje
            if msg_type == 'REQUEST':
                self.request_queue.put((timestamp, sender_id))  # Agrega la solicitud recibida a la cola de prioridad
                self.send_message(sender_id, 'REPLY', self.clock, self.node_id)  # Responde con un mensaje REPLY al nodo que envió la solicitud
            elif msg_type == 'REPLY':
                self.replies_received += 1  # Incrementa el contador de respuestas recibidas

    def enter_critical_section(self):
        self.send_request()  # Envía la solicitud de entrada a la sección crítica
        while self.replies_received < self.num_nodes - 1:  # Espera a recibir respuestas de todos los otros nodos
            time.sleep(0.1)
        print(f"Nodo {self.node_id} ingresando a la sección crítica")

    def leave_critical_section(self):
        with self.lock:
            self.request_queue.get()  # Elimina la solicitud actual de la cola de prioridad
        for i in range(self.num_nodes):
            if i != self.node_id:
                self.send_message(i, 'RELEASE', self.clock, self.node_id)  # Envía mensajes de liberación a todos los otros nodos
        print(f"Nodo {self.node_id} dejando la sección crítica")

# Ejemplo de uso
num_nodes = 3
nodes = [LamportMutex(i, num_nodes) for i in range(num_nodes)]

# Simular que el nodo 0 entra a la sección crítica
nodes[0].enter_critical_section()
time.sleep(2)  # Simular tiempo en la sección crítica
nodes[0].leave_critical_section()


'''
algoritmo de Lamport permite a los nodos coordinar el acceso a una sección crítica utilizando un enfoque
de mensajes de solicitud, respuesta y liberación, asegurando que solo un nodo acceda a la sección crítica en
cualquier momento y evitando condiciones de carrera en un entorno distribuido.'''

