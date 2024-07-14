
import threading
import time
import random
from collections import defaultdict

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

    def send_message(self, target_node, message):
        if not target_node.alive:
            return
        # Simulación de latencia de red
        time.sleep(random.uniform(0.1, 0.5))
        target_node.receive_message(message)

    def receive_message(self, message):
        if message['type'] == 'vote_request':
            self.handle_vote_request(message)
        elif message['type'] == 'vote_response':
            self.handle_vote_response(message)
        elif message['type'] == 'append_entries':
            self.handle_append_entries(message)

    def handle_vote_request(self, message):
        if self.alive:
            response = {'type': 'vote_response', 'vote_granted': True, 'term': message['term']}
            self.send_message(message['candidate'], response)

    def handle_vote_response(self, message):
        if message['vote_granted']:
            self.votes += 1
            if self.votes > len(self.cluster.nodes) // 2:
                self.is_leader = True
                self.leader = self
                print(f'Node {self.node_id} has become the leader')
                self.broadcast_append_entries()

    def handle_append_entries(self, message):
        if self.alive:
            self.log.append(message['entry'])
            self.data.update(message['entry'])
            print(f'Node {self.node_id} appended entry: {message["entry"]}')

    def request_votes(self):
        self.votes = 1
        self.term += 1
        for node in self.cluster.nodes:
            if node != self and node.alive:
                message = {'type': 'vote_request', 'candidate': self, 'term': self.term}
                self.send_message(node, message)

    def broadcast_append_entries(self):
        for node in self.cluster.nodes:
            if node != self and node.alive:
                entry = {'key': random.choice(['x', 'y', 'z']), 'value': random.randint(1, 100)}
                self.log.append(entry)
                self.data.update(entry)
                message = {'type': 'append_entries', 'entry': entry}
                self.send_message(node, message)

    def run(self):
        while self.alive:
            time.sleep(random.uniform(1, 3))
            if self.is_leader:
                self.broadcast_append_entries()
            else:
                self.request_votes()

class Cluster:
    def __init__(self, num_nodes):
        self.nodes = [Node(node_id, self) for node_id in range(num_nodes)]

    def start(self):
        self.threads = []
        for node in self.nodes:
            t = threading.Thread(target=node.run)
            self.threads.append(t)
            t.start()

    def simulate_failure(self):
        node = random.choice(self.nodes)
        node.alive = False
        print(f'Node {node.node_id} has failed.')

    def heal_failure(self):
        node = random.choice(self.nodes)
        node.alive = True
        print(f'Node {node.node_id} has healed.')

    def run_simulation(self, cycles):
        for _ in range(cycles):
            time.sleep(5)
            self.simulate_failure()
            time.sleep(5)
            self.heal_failure()
        print("Simulation complete. Stopping all nodes.")
        for node in self.nodes:
            node.alive = False

# Cluster con 5 nodos
cluster = Cluster(5)
cluster.start()

# Correr la simulación con un número fijo de ciclos de fallos y recuperaciones
cluster.run_simulation(5)

# Esperar a que todos los hilos terminen
for t in cluster.threads:
    t.join()
