
'''
Implementa una versión simplificada del algoritmo Paxos en Python. Crea un simulador con tres proposers, cinco 
acceptors y dos learners. 
Simula un escenario en el que los proposers intentan alcanzar un consenso sobre un valor.'''

import random
import threading

class Proposer:
    def __init__(self, proposer_id, acceptors, learners):
        self.proposer_id = proposer_id
        self.acceptors = acceptors
        self.learners = learners
        self.proposal_number = 0
        self.proposed_value = None

    def propose(self, value):
        self.proposal_number += 1
        self.proposed_value = value
        promises = []
        for acceptor in self.acceptors:
            promise = acceptor.prepare(self.proposal_number, self.proposer_id)
            promises.append(promise)
        if promises.count(True) > len(self.acceptors) // 2:
            acceptances = []
            for acceptor in self.acceptors:
                acceptance = acceptor.accept(self.proposal_number, self.proposed_value)
                acceptances.append(acceptance)
            if acceptances.count(True) > len(self.acceptors) // 2:
                for learner in self.learners:
                    learner.learn(self.proposed_value)

class Acceptor:
    def __init__(self, acceptor_id):
        self.acceptor_id = acceptor_id
        self.promised_proposal_number = -1
        self.accepted_proposal_number = -1
        self.accepted_value = None

    def prepare(self, proposal_number, proposer_id):
        if proposal_number > self.promised_proposal_number:
            self.promised_proposal_number = proposal_number
            return True
        return False

    def accept(self, proposal_number, value):
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

    def learn(self, value):
        self.learned_value = value
        print(f"Learner {self.learner_id} learned value: {value}")

def simulate_paxos():
    acceptors = [Acceptor(i) for i in range(5)]
    learners = [Learner(i) for i in range(2)]
    proposers = [Proposer(i, acceptors, learners) for i in range(3)]

    for proposer in proposers:
        threading.Thread(target=proposer.propose, args=(random.randint(0, 100),)).start()

if __name__ == "__main__":
    simulate_paxos()
