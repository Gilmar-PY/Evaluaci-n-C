class Paxos:
    def __init__(self):
        self.proposal_number = 0  # Número de propuesta inicializado a 0
        self.accepted_proposal = None  # Propuesta aceptada inicialmente como None

    def propose(self, value):
        self.proposal_number += 1  # Incrementa el número de propuesta en cada intento de proposición
        proposal = (self.proposal_number, value)  # Crea una tupla (número de propuesta, valor)
        if self.accept(proposal):  # Llama al método accept para verificar si la propuesta puede ser aceptada
            self.accepted_proposal = proposal  # Si es aceptada, actualiza la propuesta aceptada
            return proposal  # Retorna la propuesta aceptada
        return None  # Retorna None si la propuesta no fue aceptada

    def accept(self, proposal):
        if self.accepted_proposal is None or proposal[0] > self.accepted_proposal[0]:
            # Si no hay propuesta aceptada o la propuesta actual tiene un número mayor que la propuesta aceptada,
            return True  # entonces acepta la nueva propuesta
        return False  # Retorna False si la propuesta no puede ser aceptada

# Ejemplo de uso
paxos = Paxos()  # Crea una instancia de la clase Paxos
print(paxos.propose('update1'))  # Intenta proponer un valor 'update1' y muestra el resultado
print(paxos.propose('update2'))  # Intenta proponer un valor 'update2' y muestra el resultado


'''
simula el proceso básico de proposición y aceptación de propuestas en el algoritmo Paxos, donde 
cada propuesta tiene un número único y se verifica si puede ser aceptada en función del número de propuesta
y la propuesta actualmente aceptada
'''
