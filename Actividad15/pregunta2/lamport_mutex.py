
class LamportMutex:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.request_queue = PriorityQueue()
        self.replies_received = 0
        self.lock = threading.Lock()

    def send_request(self):
        self.clock += 1
        self.request_queue.put((self.clock, self.node_id))
        for i in range(self.num_nodes):
            if i != self.node_id:
                self.send_message(i, 'REQUEST', self.clock, self.node_id)

    def send_message(self, target, msg_type, timestamp, sender_id):
        print(f"Nodo {self.node_id} enviando {msg_type} al Nodo {target} con timestamp {timestamp}")
        time.sleep(0.1)

    def receive_message(self, msg_type, timestamp, sender_id):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1
            if msg_type == 'REQUEST':
                self.request_queue.put((timestamp, sender_id))
                self.send_message(sender_id, 'REPLY', self.clock, self.node_id)
            elif msg_type == 'REPLY':
                self.replies_received += 1

    def enter_critical_section(self):
        self.send_request()
        while self.replies_received < self.num_nodes - 1:
            time.sleep(0.1)
        print(f"Nodo {self.node_id} ingresando a la sección crítica")

    def leave_critical_section(self):
        with self.lock:
            self.request_queue.get()
        for i in range(self.num_nodes):
            if i != self.node_id:
                self.send_message(i, 'RELEASE', self.clock, self.node_id)
        print(f"Nodo {self.node_id} dejando la sección crítica")

# Ejemplo de uso
num_nodes = 3
nodes = [LamportMutex(i, num_nodes) for i in range(num_nodes)]

# Simulate node 0 entering critical section
nodes[0].enter_critical_section()
time.sleep(2)
nodes[0].leave_critical_section()
