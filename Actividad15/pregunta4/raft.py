
class RaftNode:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.term = 0
        self.voted_for = None
        self.log = []
        self.state = 'follower'

    def request_vote(self):
        self.term += 1
        self.voted_for = self.node_id
        votes = 1
        for peer in self.peers:
            if peer.grant_vote(self.term, self.node_id):
                votes += 1
        if votes > len(self.peers) // 2:
            self.state = 'leader'
        return self.state == 'leader'

    def grant_vote(self, term, candidate_id):
        if term > self.term:
            self.term = term
            self.voted_for = candidate_id
            return True
        return False

# Ejemplo de uso
nodes = [RaftNode(i, []) for i in range(3)]
for node in nodes:
    node.peers = [n for n in nodes if n != node]
nodes[0].request_vote()
print(f"Estado del nodo 0: {nodes[0].state}")
