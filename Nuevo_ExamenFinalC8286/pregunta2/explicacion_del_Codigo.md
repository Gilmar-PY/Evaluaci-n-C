
#### Bloque 1: Importación de Módulos

#### Bloque 1: Importación de Módulos

   ```python
   import threading
   import time
   import random
   from queue import PriorityQueue
   import copy


threading: Para crear y manejar hilos.
time: Para controlar el tiempo de espera y simular retrasos.
random: Para seleccionar tareas y destinatarios de mensajes de forma aleatoria.
PriorityQueue: Para manejar colas de prioridad, aunque no se usa directamente en este código.
copy: Para realizar copias profundas de objetos.


#### Bloque 2: Clase de Reloj Vectorial
   

            # Clase de Reloj Vectorial
            class VectorClock:
                def __init__(self, num_nodes, node_id):
                    self.clock = [0] * num_nodes  # Inicializa el reloj vectorial con ceros
                    self.node_id = node_id  # ID del nodo
            
                def tick(self):
                    self.clock[self.node_id] += 1  # Incrementa el contador del reloj local
            
                def send_event(self):
                    self.tick()  # Incrementa el reloj local antes de enviar
                    return self.clock[:]  # Devuelve una copia del reloj vectorial actual
            
                def receive_event(self, received_vector):
                    for i in range(len(self.clock)):
                        self.clock[i] = max(self.clock[i], received_vector[i])  # Actualiza el reloj local con el máximo entre el local y el recibido

                    self.clock[self.node_id] += 1  # Incrementa el contador del reloj local

#### Explicación:


__init__: Inicializa el reloj vectorial con ceros y asigna el ID del nodo.
tick: Incrementa el contador del reloj del nodo local.
send_event: Incrementa el reloj local y devuelve una copia del reloj vectorial para ser enviada con un mensaje.
receive_event: Actualiza el reloj local tomando el máximo entre su valor actual y el valor recibido, luego incrementa el contador local.



#### Bloque 3: Clase de Recolector de Basura Generacional

      # Clase de Recolector de Basura Generacional
      class GenerationalCollector:
          def __init__(self, size):
              self.size = size  # Tamaño del espacio de memoria
              self.young_gen = [None] * size  # Inicializa la generación joven
              self.old_gen = [None] * size  # Inicializa la generación vieja
              self.young_ptr = 0  # Puntero para la generación joven
              self.old_ptr = 0  # Puntero para la generación vieja
      
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


#### Explicación:
__init__: Inicializa las generaciones joven y vieja con un tamaño dado y punteros para la asignación de memoria.
allocate: Asigna un objeto a la generación joven o vieja según el parámetro old.
collect_young: Mueve los objetos vivos de la generación joven a la vieja y reinicia la generación joven.
collect_old: Recolecta los objetos no referenciados en la generación vieja y ajusta el puntero de asignación.



#### Bloque 4: Algoritmo de Raymond para la Exclusión Mutua

      # Algoritmo de Raymond para la Exclusión Mutua
      class RaymondMutex:
          def __init__(self, node_id, parent=None):
              self.node_id = node_id  # ID del nodo
              self.parent = parent  # Nodo padre
              self.token_holder = (parent is None)  # Indica si el nodo tiene el token
              self.request_queue = []  # Cola de solicitudes
              self.neighbors = []  # Vecinos del nodo
      
          def add_neighbor(self, neighbor):
              self.neighbors.append(neighbor)  # Agrega un vecino a la lista
      
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

#### Explicación:
__init__: Inicializa el nodo con su ID, su padre (si lo tiene), una bandera indicando si posee el token, una cola de solicitudes y una lista de vecinos.
add_neighbor: Agrega un vecino a la lista de vecinos.
request_access: Solicita acceso a la sección crítica. Si el nodo tiene el token, entra a la sección crítica, si no, envía la solicitud a su padre.
receive_request: Maneja la recepción de una solicitud de acceso. Si no tiene el token, reenvía la solicitud a su padre, si tiene el token, lo envía al solicitante.
send_token: Envía el token al vecino solicitante.
receive_token: Maneja la recepción del token. Si hay solicitudes pendientes, envía el token al siguiente en la cola.
enter_critical_section: Entra a la sección crítica y simula el tiempo de permanencia.
leave_critical_section: Sale de la sección crítica y envía el token al siguiente en la cola si hay solicitudes pendientes.


#### Bloque 5: Clase de Robot
     
      # Clase de Robot que incluye todas las funcionalidades requeridas
      class Robot:
          def __init__(self, id, total_robots, collector):
              self.id = id  # ID del robot
              self.total_robots = total_robots  # Número total de robots
              self.clock = VectorClock(total_robots, id)  # Reloj vectorial del robot
              self.collector = collector  # Recolector de basura generacional
              self.state = "Idle"  # Estado inicial del robot
              self.channels = {i: [] for i in range(total_robots) if i != id}  # Canales de comunicación con otros robots
              self.snapshots = []  # Lista de instantáneas
              self.mutex = RaymondMutex(id)  # Exclusión mutua usando el algoritmo de Raymond
              self.iterations = 0  # Contador de iteraciones
      
          def set_state(self, state):
              self.state = state  # Establece el estado del robot
      
          def send_message(self, receiver, message):
              self.channels[receiver].append(message)  # Envía un mensaje al receptor
      
          def take_snapshot(self):
              snapshot = {
                  "id": self.id,
                  "state": self.state,
                  "clock": copy.deepcopy(self.clock.clock),  # Toma una copia del reloj vectorial
                  "channels": copy.deepcopy(self.channels)  # Toma una copia de los canales de comunicación
              }
              self.snapshots.append(snapshot)  # Agrega la instantánea a la lista
              print(f"Robot {self.id} tomó una instantánea: {snapshot}")
      
          def execute_task(self):
              while self.iterations < 10:  # Número máximo de iteraciones
                  time.sleep(random.uniform(0.5, 2))
                  task = random.choice(["Soldadura", "Ensamblaje", "Pintura"])  # Selecciona una tarea aleatoria
                  self.set_state(task)
                  print(f"Robot {self.id} está ejecutando tarea: {task}")
                  self.clock.tick()
      
                  # Simula el envío de un mensaje a otro robot
                  receiver = random.choice([i for i in range(self.total_robots) if i != self.id])
                  msg = self.clock.send_event()
                  self.send_message(receiver, msg)
                  print(f"Robot {self.id} envió mensaje al Robot {receiver}: {msg}")
                  self.channels[receiver].append(msg)
      
                  # Solicitar acceso a la sección crítica
                  self.mutex.request_access(self.id)
      
                  # Toma una instantánea de vez en cuando
                  if random.choice([True, False]):
                      self.take_snapshot()
      
                  self.iterations += 1
      
          def start(self):
              thread = threading.Thread(target=self.execute_task)  # Crea un hilo para ejecutar la tarea del robot
              thread.start()  # Inicia el hilo
              return thread

#### Explicación:
__init__: Inicializa el robot con su ID, el número total de robots, su reloj vectorial, su recolector de basura, su estado inicial, sus canales de comunicación, su lista de instantáneas, su exclusión mutua y el contador de iteraciones.
set_state: Establece el estado del robot.
send_message: Envía un mensaje a otro robot y lo registra en los canales de comunicación.
take_snapshot: Toma una instantánea del estado actual del robot y sus canales de comunicación.
execute_task: Ejecuta tareas de manera aleatoria, envía mensajes, solicita acceso a la sección crítica y toma instantáneas en un bucle controlado por el número de iteraciones.
start: Inicia un hilo para ejecutar la tarea del robot.

#### Bloque 6: Función Principal

def main():
    total_robots = 3  # Número total de robots
    collector = GenerationalCollector(10)  # Inicializa el recolector de basura generacional
    robots = [Robot(id, total_robots, collector) for id in range(total_robots)]  # Crea los robots

    # Configurar los vecinos y padres para el algoritmo de Raymond
    robots[0].mutex.add_neighbor(robots[1])
    robots[1].mutex.add_neighbor(robots[0])
    robots[1].mutex.add_neighbor(robots[2])
    robots[2].mutex.add_neighbor(robots[1])
    robots[1].mutex.parent = robots[0]
    robots[2].mutex.parent = robots[1]

    threads = [robot.start() for robot in robots]  # Inicia los hilos de los robots
    for thread in threads:
        thread.join()  # Espera a que todos los hilos terminen

if __name__ == "__main__":
    main()  # Ejecuta la función principal
          

#### Explicación:
main: Configura y ejecuta la simulación de robots.
Inicializa el número total de robots y el recolector de basura generacional.
Crea los robots.
Configura los vecinos y los padres para el algoritmo de exclusión mutua de Raymond.
Inicia los hilos de los robots y espera a que todos terminen.


#### Conclusión
El código implementa un sistema de coordinación de tareas para robots industriales que utilizan relojes vectoriales para mantener la consistencia temporal, un recolector de basura generacional para gestionar la memoria, el algoritmo de exclusión mutua de Raymond para acceder a la sección crítica y el algoritmo de Chandy-Lamport para tomar instantáneas del estado global. Cada robot ejecuta tareas, envía mensajes y toma instantáneas en un entorno multihilo, asegurando que las tareas se realicen de manera coordinada y eficiente.
