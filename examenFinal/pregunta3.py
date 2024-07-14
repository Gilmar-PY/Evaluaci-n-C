
import threading
import queue
import time
from collections import defaultdict
from datetime import datetime
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

# Clase Node
class Node:
    def __init__(self, node_id, total_nodes, network):
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.network = network
        self.clock = datetime.now()
        self.message_queue = queue.Queue()
        self.lock = threading.Lock()
        self.neighbors = set(range(total_nodes)) - {node_id}
        self.reply_deferred = defaultdict(bool)
        self.request_queue = []
        self.replies_needed = total_nodes - 1
        self.terminated = False
        self.in_critical_section = False

    def send_message(self, recipient, content):
        timestamp = self.clock
        message = Message(self.node_id, content, timestamp)
        self.network.deliver_message(recipient, message)

    def receive_message(self, message):
        with self.lock:
            self.message_queue.put(message)

    def ricart_agrawala_request(self):
        self.request_queue.append((self.clock, self.node_id))
        self.request_queue.sort()
        for neighbor in self.neighbors:
            self.send_message(neighbor, "REQUEST")
        while self.replies_needed > 0:
            time.sleep(0.1)
        self.in_critical_section = True

    def ricart_agrawala_release(self):
        self.in_critical_section = False
        for neighbor in self.neighbors:
            if self.reply_deferred[neighbor]:
                self.send_message(neighbor, "REPLY")
                self.reply_deferred[neighbor] = False

    def handle_request(self, sender, timestamp):
        self.clock = max(self.clock, timestamp) + 1
        if (self.in_critical_section or
                (self.request_queue and self.request_queue[0] < (timestamp, sender))):
            self.reply_deferred[sender] = True
        else:
            self.send_message(sender, "REPLY")

    def handle_reply(self):
        self.replies_needed -= 1
    def dijkstra_scholten(self):
        pass  
    def synchronize_clocks(self):
        self.clock = datetime.now()
        for neighbor in self.neighbors:
            self.send_message(neighbor, "SYNC")
        while not self.message_queue.empty():
            message = self.message_queue.get()
            if message.content == "SYNC":
                self.clock = max(self.clock, message.timestamp) + 1

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
                    self.clock = max(self.clock, message.timestamp) + 1
            time.sleep(0.1)

    def terminate(self):
        self.terminated = True

# Clase Network
class Network:
    def __init__(self, total_nodes):
        self.total_nodes = total_nodes
        self.nodes = [Node(node_id, total_nodes, self) for node_id in range(total_nodes)]
        self.threads = []

    def deliver_message(self, recipient, message):
        self.nodes[recipient].receive_message(message)

    def start_network(self):
        for node in self.nodes:
            thread = threading.Thread(target=node.run)
            thread.start()
            self.threads.append(thread)

    def synchronize_all_clocks(self):
        for node in self.nodes:
            node.synchronize_clocks()

    def request_critical_section_all_nodes(self):
        for node in self.nodes:
            node.ricart_agrawala_request()

    def release_critical_section_all_nodes(self):
        for node in self.nodes:
            node.ricart_agrawala_release()

    def garbage_collection_all_nodes(self):
        for node in self.nodes:
            node.cheney_garbage_collection()

    def stop_network(self):
        for node in self.nodes:
            node.terminate()
        for thread in self.threads:
            thread.join()

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
