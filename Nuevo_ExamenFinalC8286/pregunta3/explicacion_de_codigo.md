# Sistema de Coordinación de Tareas para Nodos Distribuidos

## Descripción

Este script implementa un sistema de coordinación de tareas para nodos distribuidos utilizando el algoritmo de Ricart-Agrawala para exclusión mutua y el algoritmo de Dijkstra-Scholten para detección de terminación distribuida.
## Importaciones y Configuración

1. **Importaciones**:
    ```python
    import threading
    import queue
    import time
    from collections import defaultdict
    from datetime import datetime, timedelta
    import logging
    ```

    - `threading`: Para crear y manejar hilos.
    - `queue`: Para manejar colas.
    - `time`: Para controlar el tiempo de espera y simular retrasos.
    - `defaultdict`: Para estructuras de datos con valores por defecto.
    - `datetime`: Para manejar fechas y horas.
    - `logging`: Para registrar eventos y mensajes de log.

2. **Configuración del registro de eventos**:
    ```python
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    ```

    - Se configura el sistema de logging para que muestre mensajes de información (`logging.INFO`).

## Clase `Message`

3. **Clase `Message`**:
    ```python
    class Message:
        def __init__(self, sender, content, timestamp=None):
            self.sender = sender
            self.content = content
            self.timestamp = timestamp or datetime.now()

        def __repr__(self):
            return f"Message(sender={self.sender}, content={self.content}, timestamp={self.timestamp})"
    ```

    - **Propósito**: Representar un mensaje en el sistema distribuido.
    - **Funcionalidad**:
        - Cada mensaje tiene un remitente (`sender`), un contenido (`content`), y un sello de tiempo (`timestamp`).
        - El constructor inicializa estos atributos, utilizando la hora actual si no se proporciona un `timestamp`.

## Clase `DijkstraScholten`

4. **Clase `DijkstraScholten`**:
    ```python
    class DijkstraScholten:
        def __init__(self, num_processes):
            self.num_processes = num_processes
            self.parent = [None] * num_processes
            self.active_children = [0] * num_processes
            self.is_active = [False] * num_processes

        def send_message(self, sender, receiver):
            self.is_active[receiver] = True
            self.active_children[sender] += 1
            self.parent[receiver] = sender
            logger.info(f"Proceso {sender} envió un mensaje a {receiver}")

        def receive_message(self, receiver):
            if self.is_active[receiver] and self.active_children[receiver] == 0:
                self.report_termination(receiver)

        def report_termination(self, process):
            if self.parent[process] is not None:
                parent = self.parent[process]
                self.active_children[parent] -= 1
                logger.info(f"Proceso {process} reportó terminación a {parent}")
                if self.active_children[parent] == 0 and self.is_active[parent]:
                    self.report_termination(parent)
            self.is_active[process] = False
            logger.info(f"Proceso {process} marcado como inactivo")
    ```

    - **Propósito**: Implementar el algoritmo de Dijkstra-Scholten para la detección de terminación distribuida.
    - **Funcionalidad**:
        - `__init__`: Inicializa las estructuras de datos para rastrear los procesos y su estado.
        - `send_message`: Marca al receptor como activo y actualiza el estado del árbol de comunicación.
        - `receive_message`: Maneja la recepción de mensajes y verifica si el proceso puede reportar terminación.
        - `report_termination`: Reporta la terminación a su padre en el árbol de comunicación y actualiza el estado.

## Clase `Node`

5. **Clase `Node`**:
    ```python
    class Node:
        def __init__(self, node_id, total_nodes, network, ds):
            self.node_id = node_id
            self.total_nodes = total_nodes
            self.network = network
            self.ds = ds
            self.clock = datetime.now()
            self.message_queue = queue.Queue()
            self.lock = threading.Lock()
            self.neighbors = set(range(total_nodes)) - {node_id}
            self.reply_deferred = defaultdict(bool)
            self.request_queue = []
            self.replies_needed = total_nodes - 1
            self.terminated = False
            self.in_critical_section = False
            self.requesting = False
            self.token_holder = False

        def send_message(self, recipient, content):
            timestamp = self.clock
            message = Message(self.node_id, content, timestamp)
            self.network.deliver_message(recipient, message)
            self.ds.send_message(self.node_id, recipient)
            logger.info(f"Node {self.node_id} sent message to Node {recipient}: {content}")

        def receive_message(self, message):
            with self.lock:
                self.message_queue.put(message)
            logger.info(f"Node {self.node_id} received message from Node {message.sender}: {message.content}")

        def ricart_agrawala_request(self):
            self.request_queue.append((self.clock, self.node_id))
            self.request_queue.sort()
            for neighbor in self.neighbors:
                self.send_message(neighbor, "REQUEST")
            logger.info(f"Node {self.node_id} sent REQUEST to all neighbors")
            while self.replies_needed > 0:
                time.sleep(0.1)
            self.in_critical_section = True
            logger.info(f"Node {self.node_id} entering critical section")

        def ricart_agrawala_release(self):
            self.in_critical_section = False
            for neighbor in self.neighbors:
                if self.reply_deferred[neighbor]:
                    self.send_message(neighbor, "REPLY")
                    self.reply_deferred[neighbor] = False
            logger.info(f"Node {self.node_id} leaving critical section")

        def handle_request(self, sender, timestamp):
            self.clock = max(self.clock, timestamp + timedelta(seconds=1))
            if (self.in_critical_section or
                    (self.request_queue and self.request_queue[0] < (timestamp, sender))):
                self.reply_deferred[sender] = True
            else:
                self.send_message(sender, "REPLY")

        def handle_reply(self):
            self.replies_needed -= 1
            logger.info(f"Node {self.node_id} received REPLY, replies needed: {self.replies_needed}")

        def synchronize_clocks(self):
            self.clock = datetime.now()
            for neighbor in self.neighbors:
                self.send_message(neighbor, "SYNC")
            while not self.message_queue.empty():
                message = self.message_queue.get()
                if message.content == "SYNC":
                    self.clock = max(self.clock, message.timestamp + timedelta(seconds=1))
            logger.info(f"Node {self.node_id} synchronized clock")

        def cheney_garbage_collection(self):
            logger.info(f"Node {self.node_id} realizando recolección de basura")
            time.sleep(1)
            logger.info(f"Node {self.node_id} completó la recolección de basura")

        def run(self):
            while not self.terminated:
                if not self.message_queue.empty():
                    message = self.message_queue.get()
                    if message.content == "REQUEST":
                        self.handle_request(message.sender, message.timestamp)
                    elif message.content == "REPLY":
                        self.handle_reply()
                    elif message.content == "SYNC":
                        self.clock = max(self.clock, message.timestamp + timedelta(seconds=1))
                    self.ds.receive_message(self.node_id)
                time.sleep(0.1)

        def terminate(self):
            self.terminated = True
    ```

    - **Propósito**: Representar un nodo en el sistema distribuido.
    - **Funcionalidad**:
        - `__init__`: Inicializa los atributos del nodo, incluyendo su identificador, reloj lógico, cola de mensajes, y estructuras para manejar solicitudes y respuestas.
        - `send_message`: Envía un mensaje a otro nodo y actualiza el estado del algoritmo de Dijkstra-Scholten.
        - `receive_message`: Recibe un mensaje y lo coloca en la cola de mensajes.
        - `ricart_agrawala_request`: Solicita acceso a la sección crítica utilizando el algoritmo de Ricart-Agrawala.
        - `ricart_agrawala_release`: Libera la sección crítica y envía respuestas diferidas.
        - `handle_request`: Maneja las solicitudes de otros nodos.
        - `handle_reply`: Maneja las respuestas de otros nodos.
        - `synchronize_clocks`: Sincroniza el reloj lógico del nodo con sus vecinos.
        - `cheney_garbage_collection`: Simula la recolección de basura.
        - `run`: Controla el ciclo de vida del nodo, procesando mensajes y ejecutando tareas.
        - `terminate`: Marca el nodo como terminado.

## Clase `Network`

6. **Clase `Network`**:
    ```python
    class Network:
        def __init__(self, total_nodes):
            self.total_nodes = total_nodes
            self.ds = DijkstraScholten(total_nodes)
            self.nodes = [Node(node_id, total_nodes, self, self.ds) for node_id in range(total_nodes)]
            self.threads = []

        def deliver_message(self, recipient, message):
            self.nodes[recipient].receive_message(message)

        def start_network(self):
            for node in self.nodes:
                thread = threading.Thread(target=node.run)
                thread.start()
                self.threads.append(thread)
            logger.info("Network started")

        def synchronize_all_clocks(self):
            for node in self.nodes:
                node.synchronize_clocks()
            logger.info("All clocks synchronized")

        def request_critical_section_all_nodes(self):
            for node in self.nodes:
                node.ricart_agrawala_request()
            logger.info("All nodes requested critical section")

        def release_critical_section_all_nodes(self):
            for node in self.nodes:
                node.ricart_agrawala_release()
            logger.info("All nodes released critical section")

        def garbage_collection_all_nodes(self):
            for node in self.nodes:
                node.cheney_garbage_collection()
            logger.info("Garbage collection completed for all nodes")

        def stop_network(self):
            for node in self.nodes:
                node.terminate()
            for thread in self.threads:
                thread.join()
            logger.info("Network stopped")
    ```

    - **Propósito**: Representar la red que contiene todos los nodos y el algoritmo de Dijkstra-Scholten.
    - **Funcionalidad**:
        - `__init__`: Inicializa la red con el número total de nodos y crea una instancia de DijkstraScholten.
        - `deliver_message`: Entrega mensajes entre nodos.
        - `start_network`: Inicia la red ejecutando cada nodo en un hilo separado.
        - `synchronize_all_clocks`: Sincroniza los relojes de todos los nodos.
        - `request_critical_section_all_nodes`: Solicita la sección crítica para todos los nodos.
        - `release_critical_section_all_nodes`: Libera la sección crítica para todos los nodos.
        - `garbage_collection_all_nodes`: Ejecuta la recolección de basura en todos los nodos.
        - `stop_network`: Detiene la red y espera a que todos los hilos terminen.

## Función Principal

7. **Función `main`**:
    ```python
    def main():
        total_nodes = 5
        network = Network(total_nodes)

        network.start_network()
        time.sleep(2) 

        network.synchronize_all_clocks()
        network.request_critical_section_all_nodes()
        network.release_critical_section_all_nodes()
        network.garbage_collection_all_nodes()
        network.stop_network()

    if __name__ == "__main__":
        main()
    ```

    - **Propósito**: Configurar y ejecutar la red con cinco nodos.
    - **Funcionalidad**:
        - Inicializa la red con cinco nodos.
        - Inicia la red.
        - Sincroniza los relojes de todos los nodos.
        - Solicita y libera la sección crítica para todos los nodos.
        - Realiza la recolección de basura.
        - Detiene la red.

## Resumen del Funcionamiento

1. **Inicialización**: Se configuran las herramientas necesarias (`threading`, `queue`, `time`, `defaultdict`, `datetime`, `logging`).
2. **Creación de Clases**: Se definen las clases `Message`, `DijkstraScholten`, `Node`, y `Network`.
3. **Implementación de Algoritmos**: Los nodos utilizan el algoritmo de Ricart-Agrawala para solicitar y liberar acceso a la sección crítica, y el algoritmo de Dijkstra-Scholten para detección de terminación distribuida.
4. **Función Principal**: Configura y ejecuta la red de nodos, sincroniza relojes, maneja secciones críticas, realiza la recolección de basura y detiene la red.


