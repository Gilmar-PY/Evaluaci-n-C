
class VectorClock:
    def __init__(self, num_nodes, node_id):
        self.clock = [0] * num_nodes  # Inicializa el vector de reloj con ceros para cada nodo
        self.node_id = node_id  # Identificador único del nodo

    def tick(self):
        self.clock[self.node_id] += 1  # Incrementa el contador del nodo actual

    def send_event(self):
        self.tick()  # Ejecuta un tick antes de enviar el evento
        return self.clock[:]  # Retorna una copia del vector de reloj actual

    def receive_event(self, received_vector):
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], received_vector[i])  # Sincroniza el reloj vectorial actual con el recibido
        self.clock[self.node_id] += 1  # Incrementa el contador del nodo actual después de recibir el evento


num_nodes = 3  # Número total de nodos en el sistema
node1 = VectorClock(num_nodes, 0)  # Crea el nodo 1 con ID 0
node2 = VectorClock(num_nodes, 1)  # Crea el nodo 2 con ID 1
node3 = VectorClock(num_nodes, 2)  # Crea el nodo 3 con ID 2

# Evento en el nodo 1
node1.tick()  # Incrementa el contador de eventos en el nodo 1
print(f"Reloj Nodo 1: {node1.clock}")  # Imprime el estado del reloj vectorial del nodo 1

# Nodo 1 envía un mensaje a nodo 2
msg = node1.send_event()  # Simula el envío de un evento desde el nodo 1 al nodo 2
node2.receive_event(msg)  # El nodo 2 recibe y procesa el evento enviado desde el nodo 1
print(f"Reloj Nodo 2 después de recibir: {node2.clock}")  # Imprime el estado del reloj vectorial del nodo 2 después de recibir el evento
'''
simulan cómo los nodos en un sistema distribuido pueden mantener y actualizar 
su estado de reloj vectorial para mantener un orden parcial de eventos entre ellos.
'''
