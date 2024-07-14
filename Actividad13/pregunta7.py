'''
Implementa un simulador de Raft en Python. Incluye la lógica para la elección de líder, replicación de log y 
aplicación de entradas en una máquina de estado. Simula un cluster de cinco nodos. '''


import threading
import time
import random

class Node:
    def __init__(self, node_id, cluster_size):
        self.node_id = node_id
        self.state = 'follower'
        self.voted_for = None
        self.current_term = 0
        self.log = []
        self.commit_index = 0
        self.last_applied = 0
        self.cluster_size = cluster_size
        self.votes_received = 0
        self.lock = threading.Lock()

    def start_election(self):
        with self.lock:
            self.state = 'candidate'
            self.current_term += 1
            self.voted_for = self.node_id
            self.votes_received = 1
            print(f"Node {self.node_id} starts election for term {self.current_term}")

            for peer in range(self.cluster_size):
                if peer != self.node_id:
                    threading.Thread(target=self.send_request_vote, args=(peer,)).start()

    def send_request_vote(self, peer_id):
        time.sleep(random.uniform(0.1, 0.3))  # Simulate network delay
        # Request vote logic here
        if random.random() > 0.5: 
            self.receive_vote(peer_id, self.current_term)

    def receive_vote(self, peer_id, term):
        with self.lock:
            if self.state == 'candidate' and self.current_term == term:
                self.votes_received += 1
                print(f"Node {self.node_id} received vote from Node {peer_id}")
                if self.votes_received > self.cluster_size // 2:
                    self.state = 'leader'
                    print(f"Node {self.node_id} becomes leader for term {self.current_term}")
                    self.send_heartbeats()

    def send_heartbeats(self):
        while self.state == 'leader':
            print(f"Node {self.node_id} sends heartbeats")
            for peer in range(self.cluster_size):
                if peer != self.node_id:
                    threading.Thread(target=self.send_append_entries, args=(peer,)).start()
            time.sleep(1)  # Heartbeat interval

    def send_append_entries(self, peer_id):
        time.sleep(random.uniform(0.1, 0.3)) 
        # Append entries logic here
        print(f"Node {self.node_id} sends append entries to Node {peer_id}")

def simulate_raft_cluster(cluster_size=5):
    nodes = [Node(i, cluster_size) for i in range(cluster_size)]

    # Start the election process
    threading.Thread(target=nodes[

