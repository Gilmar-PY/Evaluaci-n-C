
class BullyElection:
    def __init__(self, node_id, nodes):
        self.node_id = node_id
        self.nodes = nodes
        self.coordinator = max(nodes)

    def start_election(self):
        for node in self.nodes:
            if node > self.node_id:
                self.coordinator = node

# Ejemplo de uso
nodes = [1, 2, 3, 4, 5]
election = BullyElection(3, nodes)
election.start_election()
print(f"El coordinador es: {election.coordinator}")
