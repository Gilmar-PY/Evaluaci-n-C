
class VectorClock:
    def __init__(self, num_nodes, node_id):
        self.clock = [0] * num_nodes
        self.node_id = node_id

    def tick(self):
        self.clock[self.node_id] += 1

    def send_event(self):
        self.tick()
        return self.clock[:]

    def receive_event(self, received_vector):
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], received_vector[i])
        self.clock[self.node_id] += 1

# Ejemplo de uso
num_nodes = 3
node1 = VectorClock(num_nodes, 0)
node2 = VectorClock(num_nodes, 1)
node3 = VectorClock(num_nodes, 2)

# Evento en el nodo 1
node1.tick()
print(f"Reloj Nodo 1: {node1.clock}")

# Nodo 1 envía un mensaje a nodo 2
msg = node1.send_event()
node2.receive_event(msg)
print(f"Reloj Nodo 2 después de recibir: {node2.clock}")
