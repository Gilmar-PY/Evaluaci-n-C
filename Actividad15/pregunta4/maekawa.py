class MaekawaMutex:
    def __init__(self, node_id, quorum):
        self.node_id = node_id
        self.quorum = quorum
        self.voted = False
        self.votes_received = 0

    def request_access(self):
        self.votes_received = 0
        for node in self.quorum:
            node.receive_request(self)

    def receive_request(self, requester):
        if not self.voted:
            self.voted = True
            requester.receive_vote(self)

    def receive_vote(self, voter):
        self.votes_received += 1
        if self.votes_received == len(self.quorum):
            self.enter_critical_section()

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la sección crítica")
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Nodo {self.node_id} dejando la sección crítica")
        for node in self.quorum:
            node.release_vote(self)

    def release_vote(self, requester):
        self.voted = False

# Ejemplo de uso
num_nodes = 3
quorum = [
    [0, 1],
    [1, 2],
    [0, 2]
]
nodes = [MaekawaMutex(i, [nodes[j] for j in q if j != i]) for i, q in enumerate(quorum)]

nodes[0].request_access()
time.sleep(2)
nodes[0].leave_critical_section()

