## Codigo inicial del algoritmo de Lamport
import threading  # Importa el módulo threading para manejar hilos
import time  # Importa el módulo time para manejar tiempos de espera
import random  # Importa el módulo random para generar tiempos aleatorios

# Clase para el reloj de Lamport
class LamportClock:
    def __init__(self, pid):
        self.clock = 0  # Inicializa el reloj en 0
        self.pid = pid  # Asigna un ID de proceso único

    def increment(self):
        self.clock += 1  # Incrementa el reloj en 1

    def update(self, timestamp):
        self.clock = max(self.clock, timestamp) + 1  # Actualiza el reloj al máximo entre el reloj actual y el timestamp recibido, más 1

    def get_time(self):
        return self.clock  # Retorna el valor actual del reloj

# Clase para representar un proceso
class Process:
    def __init__(self, pid, total_processes):
        self.pid = pid  # Asigna un ID de proceso único
        self.clock = LamportClock(pid)  # Inicializa el reloj de Lamport para el proceso
        self.total_processes = total_processes  # Total de procesos en el sistema
        self.request_queue = []  # Cola de solicitudes de recursos

    # Método para solicitar un recurso
    def request_resource(self):
        self.clock.increment()  # Incrementa el reloj
        timestamp = self.clock.get_time()  # Obtiene el tiempo actual del reloj
        request = (timestamp, self.pid)  # Crea una solicitud con el timestamp y el ID del proceso
        self.request_queue.append(request)  # Añade la solicitud a la cola
        self.request_queue.sort()  # Ordena la cola de solicitudes por timestamp
        return request

    # Método para recibir una solicitud de otro proceso
    def receive_request(self, timestamp, pid):
        self.clock.update(timestamp)  # Actualiza el reloj con el timestamp recibido
        self.request_queue.append((timestamp, pid))  # Añade la solicitud a la cola
        self.request_queue.sort()  # Ordena la cola de solicitudes por timestamp

    # Método para liberar un recurso
    def release_resource(self):
        self.request_queue.pop(0)  # Elimina la primera solicitud de la cola (la propia)

    # Método para verificar si puede entrar a la sección crítica
    def can_enter_critical_section(self):
        if self.request_queue:
            return self.request_queue[0][1] == self.pid  # Verifica si la solicitud propia está al frente de la cola
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
        
        print(f"Process {process.pid} entering critical section at time {process.clock.get_time()}")
        time.sleep(random.uniform(0.5, 1.5))  # Permanece en la sección crítica por un tiempo aleatorio
        print(f"Process {process.pid} leaving critical section at time {process.clock.get_time()}")
        process.release_resource()  # Libera el recurso

# Configuración inicial
total_processes = 3  # Número total de procesos
processes = [Process(i, total_processes) for i in range(total_processes)]  # Crea instancias de procesos
threads = [threading.Thread(target=simulate_process, args=(p,)) for p in processes]  # Crea hilos para cada proceso

# Inicia los hilos
for thread in threads:
    thread.start()

# Espera a que todos los hilos terminen
for thread in threads:
    thread.join()

