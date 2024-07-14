import threading
import queue
import time
from collections import defaultdict
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Clase Message
class Message:
    def __init__(self, sender, content, timestamp=None):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp or datetime.now()

    def __repr__(self):
        return f"Message(sender={self.sender}, content={self.content}, timestamp={self.timestamp})"

# Clase DijkstraScholten
class DijkstraScholten:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.parent = [None] * num_processes  # Padre de cada proceso en el árbol de comunicación
        self.active_children = [0] * num_processes  # Número de hijos activos para cada proceso
        self.is_active = [False] * num_processes  # Estado activo de cada proceso

    def send_message(self, sender, receiver):
        self.is_active[receiver] = True  # Marca al receptor como activo
        self.active_children[sender] += 1  # Incrementa el contador de hijos activos del remitente
        self.parent[receiver] = sender  # Establece al remitente como padre del receptor
        logger.info(f"Proceso {sender} envió un mensaje a {receiver}")

    def receive_message(self, receiver):
        if self.is_active[receiver] and self.active_children[receiver] == 0:
            self.report_termination(receiver)  # Reporta la terminación del proceso si está activo y no tiene hijos activos

    def report_termination(self, process):
        if self.parent[process] is not None:
            parent = self.parent[process]  # Obtiene el padre del proceso actual
            self.active_children[parent] -= 1  # Decrementa el contador de hijos activos del padre
            logger.info(f"Proceso {process} reportó terminación a {parent}")
            if self.active_children[parent] == 0 and self.is_active[parent]:
                self.report_termination(parent)  # Si el padre no tiene hijos activos y está activo, reporta su terminación
        self.is_active[process] = False  # Marca el proceso actual como inactivo después de reportar su terminación
        logger.info(f"Proceso {process} marcado como inactivo")

# Clase Node
class Node:
    def __init__(self, node_id, total_nodes, network, ds):
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.network = network
        self.ds = ds
        self.clock = datetime.now()
        self.message_queue = queue.Queue()
        self.lock = threading.Lock()
        self.neighbors = set(range(total_nodes)) - {node_id}
        self.reply_deferred = defaultdict(bool)
        self.request_queue = []
        self.replies_needed = total_nodes - 1
        self.terminated = False
        self.in_critical_section = False
        self.requesting = False
        self.token_holder = False

    def send_message(self, recipient, content):
        timestamp = self.clock
        message = Message(self.node_id, content, timestamp)
        self.network.deliver_message(recipient, message)
        self.ds.send_message(self.node_id, recipient)  # Dijkstra-Scholten integration
        logger.info(f"Node {self.node_id} sent message to Node {recipient}: {content}")

    def receive_message(self, message):
        with self.lock:
            self.message_queue.put(message)
        logger.info(f"Node {self.node_id} received message from Node {message.sender}: {message.content}")

    def ricart_agrawala_request(self):
        self.request_queue.append((self.clock, self.node_id))
        self.request_queue.sort()
        for neighbor in self.neighbors:
            self.send_message(neighbor, "REQUEST")
        logger.info(f"Node {self.node_id} sent REQUEST to all neighbors")
        while self.replies_needed > 0:
            time.sleep(0.1)
        self.in_critical_section = True
        logger.info(f"Node {self.node_id} entering critical section")

    def ricart_agrawala_release(self):
        self.in_critical_section = False
        for neighbor in self.neighbors:
            if self.reply_deferred[neighbor]:
                self.send_message(neighbor, "REPLY")
                self.reply_deferred[neighbor] = False
        logger.info(f"Node {self.node_id} leaving critical section")

    def handle_request(self, sender, timestamp):
        self.clock = max(self.clock, timestamp + timedelta(seconds=1))
        if (self.in_critical_section or
                (self.request_queue and self.request_queue[0] < (timestamp, sender))):
            self.reply_deferred[sender] = True
        else:
            self.send_message(sender, "REPLY")

    def handle_reply(self):
        self.replies_needed -= 1
        logger.info(f"Node {self.node_id} received REPLY, replies needed: {self.replies_needed}")

    def synchronize_clocks(self):
        self.clock = datetime.now()
        for neighbor in self.neighbors:
            self.send_message(neighbor, "SYNC")
        while not self.message_queue.empty():
            message = self.message_queue.get()
            if message.content == "SYNC":
                self.clock = max(self.clock, message.timestamp + timedelta(seconds=1))
        logger.info(f"Node {self.node_id} synchronized clock")

    def cheney_garbage_collection(self):
        logger.info(f"Node {self.node_id} realizando recolección de basura")
        time.sleep(1)
        logger.info(f"Node {self.node_id} completó la recolección de basura")

    def run(self):
        while not self.terminated:
            if not self.message_queue.empty():
                message = self.message_queue.get()
                if message.content == "REQUEST":
                    self.handle_request(message.sender, message.timestamp)
                elif message.content == "REPLY":
                    self.handle_reply()
                elif message.content == "SYNC":
                    self.clock = max(self.clock, message.timestamp + timedelta(seconds=1))
                self.ds.receive_message(self.node_id)  # Dijkstra-Scholten integration
            time.sleep(0.1)

    def terminate(self):
        self.terminated = True

# Clase Network
class Network:
    def __init__(self, total_nodes):
        self.total_nodes = total_nodes
        self.ds = DijkstraScholten(total_nodes)
        self.nodes = [Node(node_id, total_nodes, self, self.ds) for node_id in range(total_nodes)]
        self.threads = []

    def deliver_message(self, recipient, message):
        self.nodes[recipient].receive_message(message)

    def start_network(self):
        for node in self.nodes:
            thread = threading.Thread(target=node.run)
            thread.start()
            self.threads.append(thread)
        logger.info("Network started")

    def synchronize_all_clocks(self):
        for node in self.nodes:
            node.synchronize_clocks()
        logger.info("All clocks synchronized")

    def request_critical_section_all_nodes(self):
        for node in self.nodes:
            node.ricart_agrawala_request()
        logger.info("All nodes requested critical section")

    def release_critical_section_all_nodes(self):
        for node in self.nodes:
            node.ricart_agrawala_release()
        logger.info("All nodes released critical section")

    def garbage_collection_all_nodes(self):
        for node in self.nodes:
            node.cheney_garbage_collection()
        logger.info("Garbage collection completed for all nodes")

    def stop_network(self):
        for node in self.nodes:
            node.terminate()
        for thread in self.threads:
            thread.join()
        logger.info("Network stopped")

def main():
    total_nodes = 5
    network = Network(total_nodes)

    network.start_network()
    time.sleep(2) 

    network.synchronize_all_clocks()
    network.request_critical_section_all_nodes()
    network.release_critical_section_all_nodes()
    network.garbage_collection_all_nodes()
    network.stop_network()

if __name__ == "__main__":
    main()

