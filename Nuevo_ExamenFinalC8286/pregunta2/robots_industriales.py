import threading
import time
import random
from queue import PriorityQueue
import copy

# Clase de Reloj Vectorial
class VectorClock:
    def __init__(self, num_nodes, node_id):
        self.clock = [0] * num_nodes  # Inicializa el reloj vectorial 
        self.node_id = node_id  

    def tick(self):
        self.clock[self.node_id] += 1  # Incrementa el contador del reloj local

    def send_event(self):
        self.tick()  
        return self.clock[:]  # Devuelve una copia del reloj vectorial actual

    def receive_event(self, received_vector):
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], received_vector[i])  # Actualiza el reloj local con el máximo entre el local y el recibido
        self.clock[self.node_id] += 1  

# Clase de Recolector de Basura Generacional
class GenerationalCollector:
    def __init__(self, size):
        self.size = size  
        self.young_gen = [None] * size  # Inicializa la generación joven
        self.old_gen = [None] * size  # Inicializa la generación vieja
        self.young_ptr = 0  
        self.old_ptr = 0  

    def allocate(self, obj, old=False):
        if old:
            if self.old_ptr >= self.size:
                self.collect_old()  # Recolecta la generación vieja si está llena
            addr = self.old_ptr
            self.old_gen[addr] = obj
            self.old_ptr += 1
        else:
            if self.young_ptr >= self.size:
                self.collect_young()  # Recolecta la generación joven si está llena
            addr = self.young_ptr
            self.young_gen[addr] = obj
            self.young_ptr += 1
        return addr

    def collect_young(self):
        self.old_gen.extend([obj for obj in self.young_gen if obj is not None])  # Mueve objetos vivos de la generación joven a la vieja
        self.young_gen = [None] * self.size  # Reinicia la generación joven
        self.young_ptr = 0  # Reinicia el puntero de la generación joven

    def collect_old(self):
        self.old_gen = [obj for obj in self.old_gen if obj is not None]  # Recolecta la generación vieja, eliminando los objetos no referenciados
        self.old_ptr = len(self.old_gen)  # Ajusta el puntero de la generación vieja
        self.old_gen.extend([None] * (self.size - self.old_ptr))  # Extiende la generación vieja con espacios vacíos

# Algoritmo de Raymond para la Exclusión Mutua
class RaymondMutex:
    def __init__(self, node_id, parent=None):
        self.node_id = node_id  # ID del nodo
        self.parent = parent  # Nodo padre
        self.token_holder = (parent is None)  # Indica si el nodo tiene el token
        self.request_queue = []  # Cola de solicitudes
        self.neighbors = []  # Vecinos del nodo

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)  

    def request_access(self, requester_id):
        if self.token_holder:
            self.enter_critical_section()  # Si tiene el token, entra a la sección crítica
        else:
            self.request_queue.append(requester_id)  # Agrega la solicitud a la cola
            if self.parent:
                self.parent.receive_request(self.node_id)  # Envia la solicitud al padre

    def receive_request(self, requester_id):
        if not self.token_holder:
            self.request_queue.append(requester_id)  # Agrega la solicitud a la cola
            if self.parent:
                self.parent.receive_request(self.node_id)  # Envia la solicitud al padre
        elif requester_id == self.node_id:
            self.enter_critical_section()  # Si el solicitante es el mismo nodo, entra a la sección crítica
        else:
            self.send_token(requester_id)  # Envía el token al solicitante

    def send_token(self, requester_id):
        self.token_holder = False  # Marca que ya no tiene el token
        for neighbor in self.neighbors:
            if neighbor.node_id == requester_id:
                neighbor.receive_token(self.node_id)  # Envía el token al vecino solicitante
                break

    def receive_token(self, sender_id):
        self.token_holder = True  # Marca que tiene el token
        if self.request_queue and self.request_queue[0] == self.node_id:
            self.enter_critical_section()  # Entra a la sección crítica si está en la parte superior de la cola
        else:
            self.send_token_to_next_in_queue()  # Envía el token al siguiente en la cola

    def send_token_to_next_in_queue(self):
        if self.request_queue:
            next_node_id = self.request_queue.pop(0)  # Obtiene el siguiente nodo en la cola
            self.send_token(next_node_id)  # Envía el token al siguiente nodo

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la sección crítica")
        time.sleep(random.uniform(0.5, 1.5))  # Simula el tiempo en la sección crítica
        self.leave_critical_section()

    def leave_critical_section(self):
        print(f"Nodo {self.node_id} dejando la sección crítica")
        if self.request_queue:
            self.send_token_to_next_in_queue()  # Envía el token al siguiente en la cola

# Clase de Robot que incluye todas las funcionalidades requeridas
class Robot:
    def __init__(self, id, total_robots, collector):
        self.id = id  # ID del robot
        self.total_robots = total_robots  # Número total de robots
        self.clock = VectorClock(total_robots, id)  # Reloj vectorial del robot
        self.collector = collector  # Recolector de basura generacional
        self.state = "Idle"  # Estado inicial del robot
        self.channels = {i: [] for i in range(total_robots) if i != id}  # Canales de comunicación
        self.snapshots = []  # Lista de instantáneas
        self.mutex = RaymondMutex(id)  # Algoritmo de exclusión mutua de Raymond
        self.iterations = 0  

    def set_state(self, state):
        self.state = state  # Cambia el estado del robot

    def send_message(self, receiver, message):
        self.channels[receiver].append(message)  # Envía un mensaje al canal del receptor

    def take_snapshot(self):
        snapshot = {
            "id": self.id,
            "state": self.state,
            "clock": copy.deepcopy(self.clock.clock),  # Captura el estado del reloj vectorial
            "channels": copy.deepcopy(self.channels)  # Captura el estado de los canales
        }
        self.snapshots.append(snapshot)  # Guarda la instantánea
        print(f"Robot {self.id} tomó una instantánea: {snapshot}")

    def execute_task(self):
        while self.iterations < 10:  # Número máximo de iteraciones
            time.sleep(random.uniform(0.5, 2))  # Simula tiempo de espera entre tareas
            task = random.choice(["Soldadura", "Ensamblaje", "Pintura"])  # Selecciona una tarea al azar
            self.set_state(task)  # Cambia el estado del robot a la tarea seleccionada
            print(f"Robot {self.id} está ejecutando tarea: {task}")
            self.clock.tick()  # Incrementa el reloj vectorial

            # Simula el envío de un mensaje a otro robot
            receiver = random.choice([i for i in range(self.total_robots) if i != self.id])
            msg = self.clock.send_event()  # Envía un evento con el reloj vectorial
            self.send_message(receiver, msg)
            print(f"Robot {self.id} envió mensaje al Robot {receiver}: {msg}")
            self.channels[receiver].append(msg)  # Guarda el mensaje en el canal del receptor

            # Solicitar acceso a la sección crítica
            self.mutex.request_access(self.id)

            # Toma una instantánea de vez en cuando
            if random.choice([True, False]):
                self.take_snapshot()

            self.iterations += 1  

    def start(self):
        thread = threading.Thread(target=self.execute_task)  # Crea un hilo para ejecutar la tarea del robot
        thread.start()  
        return thread  

def main():
    total_robots = 3  # Número total de robots
    collector = GenerationalCollector(10)  # Recolector de basura generacional con tamaño 10
    robots = [Robot(id, total_robots, collector) for id in range(total_robots)]  # Crea la lista de robots

    # Configurar los vecinos y padres para el algoritmo de Raymond
    robots[0].mutex.add_neighbor(robots[1])
    robots[1].mutex.add_neighbor(robots[0])
    robots[1].mutex.add_neighbor(robots[2])
    robots[2].mutex.add_neighbor(robots[1])
    robots[1].mutex.parent = robots[0]
    robots[2].mutex.parent = robots[1]

    threads = [robot.start() for robot in robots]  # Inicia los hilos de los robots
    for thread in threads:
        thread.join()  

if __name__ == "__main__":
    main()  
