
class RicartAgrawalaMutex:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.request_queue = []
        self.replies_received = 0

    def request_access(self):
        self.clock += 1
        self.request_queue.append((self.clock, self.node_id))
        for node in nodes:
            if node.node_id != self.node_id:
                node.receive_request(self.clock, self.node_id)

    def receive_request(self, timestamp, sender_id):
        self.clock = max(self.clock, timestamp) + 1
        self.request_queue.append((timestamp, sender_id))
        self.request_queue.sort()
        self.send_reply(sender_id)

    def send_reply(self, target_id):
        for node in nodes:
            if node.node_id == target_id:
                node.receive_reply(self.node_id)

    def receive_reply(self, sender_id):
        self.replies_received += 1
        if self.replies_received == self.num_nodes - 1:
            self.enter_critical_section()

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la sección crítica")
        self.leave_critical_section()

    def leave_critical_section(self):
        self.replies_received = 0
        self.request_queue = [(t, n) for t, n in self.request_queue if n != self.node_id]
        for timestamp, node_id in self.request_queue:
            self.send_reply(node_id)
        print(f"Nodo {self.node_id} dejando la sección crítica")

# Ejemplo de uso
num_nodes = 3
nodes = [RicartAgrawalaMutex(i, num_nodes) for i in range(num_nodes)]

# Simulate node 0 requesting access
nodes[0].request_access()
time.sleep(2)
nodes[0].leave_critical_section()
