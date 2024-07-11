''' 
Modifica la implementación anterior para incluir fallos de nodos (por ejemplo, proposers y acceptors que no 
responden) y observa cómo afecta al proceso de consenso. 
¿Cómo maneja Paxos estos fallos?
'''
import random
import threading
import time

class Proposer:
    def __init__(self, proposer_id, acceptors, learners):
        self.proposer_id = proposer_id
        self.acceptors = acceptors
        self.learners = learners
        self.proposal_number = 0
        self.proposed_value = None
        self.active = True  # Estado del nodo

    def propose(self, value):
        if not self.active:
            return
        self.proposal_number += 1
        self.proposed_value = value
        promises = []
        for acceptor in self.acceptors:
            if acceptor.active:
                promise = acceptor.prepare(self.proposal_number, self.proposer_id)
                promises.append(promise)
        if promises.count(True) > len(self.acceptors) // 2:
            acceptances = []
            for acceptor in self.acceptors:
                if acceptor.active:
                    acceptance = acceptor.accept(self.proposal_number, self.proposed_value)
                    acceptances.append(acceptance)
            if acceptances.count(True) > len(self.acceptors) // 2:
                for learner in self.learners:
                    if learner.active:
                        learner.learn(self.proposed_value)

class Acceptor:
    def __init__(self, acceptor_id):
        self.acceptor_id = acceptor_id
        self.promised_proposal_number = -1
        self.accepted_proposal_number = -1
        self.accepted_value = None
        self.active = True  # Estado del nodo

    def prepare(self, proposal_number, proposer_id):
        if not self.active:
            return False
        if proposal_number > self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            return True
        return False

    def accept(self, proposal_number, value):
        if not self.active:
            return False
        if proposal_number >= self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            self.accepted_proposal_number = proposal_number
            self.accepted_value = value
            return True
        return False

class Learner:
    def __init__(self, learner_id):
        self.learner_id = learner_id
        self.learned_value = None
        self.active = True  # Estado del nodo

    def learn(self, value):
        if self.active:
            self.learned_value = value
            print(f"Learner {self.learner_id} learned value: {value}")

def simulate_paxos_with_failures():
    acceptors = [Acceptor(i) for i in range(5)]
    learners = [Learner(i) for i in range(2)]
    proposers = [Proposer(i, acceptors, learners) for i in range(3)]

    # Simular fallos de nodos
    acceptors[2].active = False
    learners[1].active = False
    proposers[1].active = False

    for proposer in proposers:
        threading.Thread(target=proposer.propose, args=(random.randint(0, 100),)).start()

if __name__ == "__main__":
    simulate_paxos_with_failures()

