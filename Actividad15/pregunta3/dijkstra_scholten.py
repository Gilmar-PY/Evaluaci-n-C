class DijkstraScholten:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.parent = [None] * num_processes  # Padre de cada proceso en el árbol de comunicación
        self.active_children = [0] * num_processes  # Número de hijos activos para cada proceso
        self.is_active = [False] * num_processes  # Estado activo de cada proceso

    def send_message(self, sender, receiver):
        self.is_active[receiver] = True  # Marca al receptor como activo
        self.active_children[sender] += 1  # Incrementa el contador de hijos activos del remitente
        self.parent[receiver] = sender  # Establece al remitente como padre del receptor

    def receive_message(self, receiver):
        if self.is_active[receiver] and self.active_children[receiver] == 0:
            self.report_termination(receiver)  # Reporta la terminación del proceso si está activo y no tiene hijos activos

    def report_termination(self, process):
        if self.parent[process] is not None:
            parent = self.parent[process]  # Obtiene el padre del proceso actual
            self.active_children[parent] -= 1  # Decrementa el contador de hijos activos del padre
            if self.active_children[parent] == 0 and self.is_active[parent]:
                self.report_termination(parent)  # Si el padre no tiene hijos activos y está activo, reporta su terminación
        self.is_active[process] = False  # Marca el proceso actual como inactivo después de reportar su terminación

# Ejemplo de uso
num_processes = 3
ds = DijkstraScholten(num_processes)

# Simulación de mensajes
ds.send_message(0, 1)  # Proceso 0 envía mensaje a proceso 1
ds.receive_message(1)  # Proceso 1 recibe mensaje y verifica si puede reportar su terminación
ds.send_message(1, 2)  # Proceso 1 envía mensaje a proceso 2
ds.receive_message(2)  # Proceso 2 recibe mensaje y verifica si puede reportar su terminación
ds.receive_message(1)  # Proceso 1 recibe mensaje y verifica si puede reportar su terminación
ds.receive_message(0)  # Proceso 0 recibe mensaje y verifica si puede reportar su terminación

'''
Este algoritmo permite a los procesos distribuidos detectar la terminación de manera 
eficiente mediante el seguimiento del estado activo de cada proceso y el recuento de hijos activos '''
en un árbol de comunicación jerárquico.
