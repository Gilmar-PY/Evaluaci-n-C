## Codigo inicial del algoritmo de Ricart-Agrawala
import threading  # Importa el módulo threading para manejar hilos
import time  # Importa el módulo time para manejar tiempos de espera
import random  # Importa el módulo random para generar tiempos aleatorios

# Clase que implementa el algoritmo de Ricart-Agrawala
class RicartAgrawala:
    def __init__(self, pid, total_processes):
        self.pid = pid  # ID del proceso
        self.clock = 0  # Reloj lógico del proceso
        self.total_processes = total_processes  # Total de procesos en el sistema
        self.request_queue = []  # Cola de solicitudes de recursos
        self.deferred_replies = []  # Lista de respuestas diferidas
        self.requesting_cs = False  # Indicador de si el proceso está solicitando la sección crítica
        self.lock = threading.Lock()  # Bloqueo para acceso concurrente seguro

    # Método para solicitar un recurso
    def request_resource(self):
        with self.lock:
            self.clock += 1  # Incrementa el reloj lógico
            self.requesting_cs = True  # Marca que está solicitando la sección crítica
            request = (self.clock, self.pid)  # Crea la solicitud con el reloj y el ID del proceso
            self.request_queue.append(request)  # Añade la solicitud a la cola
            self.request_queue.sort()  # Ordena la cola de solicitudes
            return request

    # Método para recibir una solicitud de otro proceso
    def receive_request(self, timestamp, pid):
        with self.lock:
            self.clock = max(self.clock, timestamp) + 1  # Actualiza el reloj lógico
            request = (timestamp, pid)  # Crea la solicitud recibida
            self.request_queue.append(request)  # Añade la solicitud a la cola
            self.request_queue.sort()  # Ordena la cola de solicitudes
            if self.requesting_cs and (timestamp, pid) < (self.clock, self.pid):
                self.deferred_replies.append(pid)  # Añade la solicitud a las respuestas diferidas si es necesario
            else:
                return True  # Responde inmediatamente si no está solicitando la sección crítica
        return False

    # Método para recibir una respuesta de otro proceso
    def receive_reply(self, pid):
        with self.lock:
            self.deferred_replies.remove(pid)  # Elimina la respuesta diferida de la lista

    # Método para liberar un recurso
    def release_resource(self):
        with self.lock:
            self.request_queue.pop(0)  # Elimina la solicitud propia de la cola
            self.requesting_cs = False  # Marca que ya no está solicitando la sección crítica
            replies = self.deferred_replies[:]  # Copia las respuestas diferidas
            self.deferred_replies.clear()  # Limpia la lista de respuestas diferidas
        return replies

    # Método para verificar si puede entrar a la sección crítica
    def can_enter_critical_section(self):
        with self.lock:
            if self.request_queue:
                return self.request_queue[0][1] == self.pid  # Verifica si su solicitud es la primera en la cola
            return False

# Función para simular el comportamiento de un proceso
def simulate_process(process):
    while True:
        time.sleep(random.uniform(0.5, 2))  # Espera un tiempo aleatorio entre 0.5 y 2 segundos
        request = process.request_resource()  # Solicita un recurso
        print(f"Process {process.pid} requested resource at time {request[0]}")

        # Simula la recepción de solicitudes de otros procesos
        for i in range(process.total_processes):
            if i != process.pid:
                process.receive_request(random.randint(0, 10), i)

        while not process.can_enter_critical_section():
            time.sleep(0.1)  # Espera brevemente antes de verificar nuevamente
        
        print(f"Process {process.pid} entering critical section at time {process.clock}")
        time.sleep(random.uniform(0.5, 1.5))  # Permanece en la sección crítica por un tiempo aleatorio
        print(f"Process {process.pid} leaving critical section at time {process.clock}")
        deferred_replies = process.release_resource()

        # Simula el envío de respuestas a los procesos diferidos
        for pid in deferred_replies:
            print(f"Process {process.pid} sending reply to process {pid}")

# Configuración inicial
total_processes = 3  # Número total de procesos
processes = [RicartAgrawala(i, total_processes) for i in range(total_processes)]  # Crea instancias de procesos
threads = [threading.Thread(target=simulate_process, args=(p,)) for p in processes]  # Crea hilos para cada proceso

# Inicia los hilos
for thread in threads:
    thread.start()

# Espera a que todos los hilos terminen
for thread in threads:
    thread.join()

