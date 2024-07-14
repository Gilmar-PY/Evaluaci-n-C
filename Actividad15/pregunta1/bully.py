class BullyElection:
    def __init__(self, node_id, nodes):
        self.node_id = node_id  # Asigna el ID del nodo que inicia la instancia de la clase
        self.nodes = nodes      # Asigna la lista de nodos a la instancia de la clase
        self.coordinator = max(nodes)  # Establece el coordinador como el nodo con el ID más alto en la lista de nodos

    def start_election(self):
        for node in self.nodes:  # Itera sobre cada nodo en la lista de nodos
            if node > self.node_id:  # Comprueba si el ID del nodo actual es mayor que el ID del nodo que inició la elección
                self.coordinator = node  # Si es mayor, establece este nodo como el nuevo coordinador

# Ejemplo de uso
nodes = [1, 2, 3, 4, 5]  # Lista de nodos
election = BullyElection(3, nodes)  # Crea una instancia de la clase BullyElection con node_id=3 y nodes=[1, 2, 3, 4, 5]
election.start_election()  # Inicia el proceso de elección
print(f"El coordinador es: {election.coordinator}")  # Imprime el coordinador después de la elección
