
class Paxos:
    def __init__(self):
        self.proposal_number = 0
        self.accepted_proposal = None

    def propose(self, value):
        self.proposal_number += 1
        proposal = (self.proposal_number, value)
        if self.accept(proposal):
            self.accepted_proposal = proposal
            return proposal
        return None

    def accept(self, proposal):
        if self.accepted_proposal is None or proposal[0] > self.accepted_proposal[0]:
            return True
        return False

# Ejemplo de uso
paxos = Paxos()
print(paxos.propose('update1'))
print(paxos.propose('update2'))
