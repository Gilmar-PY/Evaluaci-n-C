
class RaymondMutex:
    def __init__(self, node_id, parent=None):
        self.node_id = node_id
        self.parent = parent
        self.token_holder = (parent is None)
        self.request_queue = []

    def request_access(self):
        if self.token_holder:
            self.enter_critical_section()
        else:
            self.request_queue.append(self.node_id)
            self.send_request_to_parent()

    def send_request_to_parent(self):
        if self.parent:
            self.parent.receive_request(self)

    def receive_request(self, requester):
        if not self.token_holder:
            self.request_queue.append(requester.node_id)
            self.send_request_to_parent()
        elif requester.node_id == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token(requester)

    def send_token(self, requester):
        self.token_holder = False
        requester.receive_token(self)

    def receive_token(self, sender):
        self.token_holder = True
        if self.request_queue and self.request_queue[0] == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token_to_next_in_queue()

    def send_token_to_next_in_queue(self):
        next_node_id = self.request_queue.pop(0)
        next_node = [node for node in nodes if node.node_id == next_node_id][0]
        self.send_token(next_node)

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la sección crítica")
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Nodo {self.node_id} dejando la sección crítica")
        if self.request_queue:
            self.send_token_to_next_in_queue()

# Ejemplo de uso
nodes = [RaymondMutex(i) for i in range(3)]
nodes[0].parent = nodes[1]
nodes[1].parent = nodes[2]

nodes[0].request_access()
time.sleep(2)
nodes[0].leave_critical_section()
