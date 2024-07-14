
class ByzantineNode:
    def __init__(self, node_id, is_faulty=False):
        self.node_id = node_id
        self.is_faulty = is_faulty
        self.peers = []

    def send_message(self, message):
        for peer in self.peers:
            peer.receive_message(message, self.node_id)

    def receive_message(self, message, sender_id):
        if self.is_faulty:
            print(f"Node {self.node_id} received a faulty message from Node {sender_id}")
        else:
            print(f"Node {self.node_id} received message '{message}' from Node {sender_id}")

# Ejemplo de uso
nodes = [ByzantineNode(i, is_faulty=(i == 1)) for i in range(3)]
for node in nodes:
    node.peers = [n for n in nodes if n != node]

nodes[0].send_message("Test Message")
