
class DijkstraScholten:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.parent = [None] * num_processes
        self.active_children = [0] * num_processes
        self.is_active = [False] * num_processes

    def send_message(self, sender, receiver):
        self.is_active[receiver] = True
        self.active_children[sender] += 1
        self.parent[receiver] = sender

    def receive_message(self, receiver):
        if self.is_active[receiver] and self.active_children[receiver] == 0:
            self.report_termination(receiver)

    def report_termination(self, process):
        if self.parent[process] is not None:
            parent = self.parent[process]
            self.active_children[parent] -= 1
            if self.active_children[parent] == 0 and self.is_active[parent]:
                self.report_termination(parent)
        self.is_active[process] = False

# Ejemplo de uso
num_processes = 3
ds = DijkstraScholten(num_processes)

# Simulación de mensajes
ds.send_message(0, 1)
ds.receive_message(1)
ds.send_message(1, 2)
ds.receive_message(2)
ds.receive_message(1)
ds.receive_message(0)
