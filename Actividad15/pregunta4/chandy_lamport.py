import threading
import time
from collections import defaultdict

class Process:
    def __init__(self, process_id):
        self.process_id = process_id
        self.state = None
        self.channels = defaultdict(list)
        self.neighbors = []
        self.marker_received = {}
        self.local_snapshot = None
        self.lock = threading.Lock()

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
        for neighbor in neighbors:
            self.marker_received[neighbor.process_id] = False

    def initiate_snapshot(self):
        with self.lock:
            self.local_snapshot = self.state
            print(f"Process {self.process_id} taking local snapshot: {self.local_snapshot}")
            self.send_marker_messages()

    def send_marker_messages(self):
        for neighbor in self.neighbors:
            self.send_message(neighbor, 'MARKER')

    def send_message(self, neighbor, message_type, content=None):
        message = (message_type, self.process_id, content)
        neighbor.receive_message(message)

    def receive_message(self, message):
        message_type, sender_id, content = message
        with self.lock:
            if message_type == 'MARKER':
                if not self.marker_received[sender_id]:
                    self.marker_received[sender_id] = True
                    if self.local_snapshot is None:
                        self.local_snapshot = self.state
                        print(f"Process {self.process_id} taking local snapshot: {self.local_snapshot}")
                        self.send_marker_messages()
                    else:
                        self.channels[sender_id].append(content)
                else:
                    self.channels[sender_id].append(content)
            else:
                if self.local_snapshot is not None:
                    self.channels[sender_id].append(content)
                else:
                    self.process_message(message)

    def process_message(self, message):
        print(f"Process {self.process_id} received message from Process {message[1]}: {message[2]}")

    def update_state(self, new_state):
        self.state = new_state

# Ejemplo de uso
processes = [Process(i) for i in range(3)]
for i, process in enumerate(processes):
    neighbors = [p for j, p in enumerate(processes) if i != j]
    process.set_neighbors(neighbors)

processes[0].update_state("State A")
processes[1].update_state("State B")
processes[2].update_state("State C")

processes[0].initiate_snapshot()

time.sleep(1)
processes[1].send_message(processes[0], 'MESSAGE', "Message 1 from P1 to P0")
time.sleep(1)
processes[2].send_message(processes[0], 'MESSAGE', "Message 2 from P2 to P0")
time.sleep(1)
processes[2].send_message(processes[1], 'MESSAGE', "Message 3 from P2 to P1")

