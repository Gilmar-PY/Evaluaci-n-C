
import threading
import time
import random

# Clase que implementa el algoritmo de Ricart-Agrawala
class RicartAgrawala:
    def __init__(self, pid, total_processes):
        self.pid = pid  # Identificador del proceso
        self.clock = 0  # Reloj lógico del proceso
        self.total_processes = total_processes  # Número total de procesos
        self.request_queue = []  # Cola de solicitudes del proceso
        self.deferred_replies = []  # Lista de respuestas diferidas
        self.requesting_cs = False  # Indicador de solicitud de sección crítica
        self.lock = threading.Lock()  # Lock para la sincronización

    # Método para solicitar el recurso
    def request_resource(self):
        with self.lock:
            self.clock += 1  # Incrementa el reloj lógico
            self.requesting_cs = True  # Indica que se está solicitando la sección crítica
            request = (self.clock, self.pid)  # Crea una solicitud con el timestamp y el PID
            self.request_queue.append(request)  # Añade la solicitud a la cola
            self.request_queue.sort()  # Ordena la cola por timestamp
            return request  # Devuelve la solicitud

    # Método para recibir una solicitud de otro proceso
    def receive_request(self, timestamp, pid):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1  # Actualiza el reloj con el mayor valor +1
            request = (timestamp, pid)  # Crea una solicitud con el timestamp recibido y el PID
            self.request_queue.append(request)  # Añade la solicitud a la cola
            self.request_queue.sort()  # Ordena la cola por timestamp
            # Si el proceso está solicitando la sección crítica y la solicitud recibida tiene prioridad
            if self.requesting_cs and (timestamp, pid) < (self.clock, self.pid):
                self.deferred_replies.append(pid)  # Añade el PID a las respuestas diferidas
            else:
                return True  # Si no, se puede enviar una respuesta inmediata
        return False  # Indica que no se puede enviar una respuesta inmediata

    # Método para recibir una respuesta de otro proceso
    def receive_reply(self, pid):
        with self.lock:
            self.deferred_replies.remove(pid)  # Elimina el PID de las respuestas diferidas

    # Método para liberar el recurso
    def release_resource(self):
        with self.lock:
            self.request_queue.pop(0)  # Elimina la primera solicitud de la cola
            self.requesting_cs = False  # Indica que ya no se está solicitando la sección crítica
            replies = self.deferred_replies[:]  # Copia las respuestas diferidas
            self.deferred_replies.clear()  # Limpia las respuestas diferidas
        return replies  # Devuelve las respuestas diferidas

    # Método para comprobar si el proceso puede entrar en la sección crítica
    def can_enter_critical_section(self):
        with self.lock:
            if self.request_queue:
                return self.request_queue[0][1] == self.pid  # Comprueba si la primera solicitud en la cola es del propio proceso
            return False  # Si la cola está vacía, no puede entrar en la sección crítica

# Función que simula el comportamiento de un proceso
def simulate_process(process):
    while True:
        time.sleep(random.uniform(0.5, 2))  # Espera un tiempo aleatorio antes de solicitar el recurso
        request = process.request_resource()  # Solicita el recurso
        print(f"Process {process.pid} requested resource at time {request[0]}")

        # Simula la recepción de solicitudes de otros procesos
        for i in range(process.total_processes):
            if i != process.pid:
                process.receive_request(random.randint(0, 10), i)

        while not process.can_enter_critical_section():
            time.sleep(0.1)  # Espera en bucle hasta que pueda entrar en la sección crítica
        
        print(f"Process {process.pid} entering critical section at time {process.clock}")
        time.sleep(random.uniform(0.5, 1.5))  # Simula el tiempo en la sección crítica
        print(f"Process {process.pid} leaving critical section at time {process.clock}")
        deferred_replies = process.release_resource()  # Libera el recurso y obtiene las respuestas diferidas

        # Simula el envío de respuestas a los procesos diferidos
        for pid in deferred_replies:
            print(f"Process {process.pid} sending reply to process {pid}")

# Número total de procesos
total_processes = 3
# Crea una lista de instancias del algoritmo de Ricart-Agrawala para cada proceso
processes = [RicartAgrawala(i, total_processes) for i in range(total_processes)]
# Crea una lista de hilos para simular cada proceso
threads = [threading.Thread(target=simulate_process, args=(p,)) for p in processes]

# Inicia todos los hilos
for thread in threads:
    thread.start()
# Espera a que todos los hilos terminen
for thread in threads:
    thread.join()
