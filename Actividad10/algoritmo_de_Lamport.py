class LamportClock:
    def __init__(self, pid):
        self.clock = 0  # Inicializa el reloj de Lamport en 0
        self.pid = pid  # Identificador del proceso

    def increment(self):
        self.clock += 1  # Incrementa el reloj de Lamport en 1

    def update(self, timestamp):
        self.clock = max(self.clock, timestamp) + 1  # Actualiza el reloj con el mayor valor entre el reloj local y el timestamp recibido, incrementado en 1

    def get_time(self):
        return self.clock  # Devuelve el valor actual del reloj de Lamport

class Process:
    def __init__(self, pid, total_processes):
        self.pid = pid  # Identificador del proceso
        self.clock = LamportClock(pid)  # Instancia del reloj de Lamport para el proceso
        self.total_processes = total_processes  # Número total de procesos
        self.request_queue = []  # Cola de solicitudes del proceso

    def request_resource(self):
        self.clock.increment()  # Incrementa el reloj de Lamport
        timestamp = self.clock.get_time()  # Obtiene el valor actual del reloj
        request = (timestamp, self.pid)  # Crea una solicitud con el timestamp y el PID del proceso
        self.request_queue.append(request)  # Añade la solicitud a la cola
        self.request_queue.sort()  # Ordena la cola por timestamp
        return request  # Devuelve la solicitud

    def receive_request(self, timestamp, pid):
        self.clock.update(timestamp)  # Actualiza el reloj de Lamport con el timestamp recibido
        self.request_queue.append((timestamp, pid))  # Añade la solicitud recibida a la cola
        self.request_queue.sort()  # Ordena la cola por timestamp

    def release_resource(self):
        self.request_queue.pop(0)  # Elimina la primera solicitud en la cola (la propia) al liberar el recurso

    def can_enter_critical_section(self):
        if self.request_queue:
            return self.request_queue[0][1] == self.pid  # Comprueba si el proceso puede entrar en la sección crítica (su solicitud es la primera en la cola)
        return False  # Si la cola está vacía, no puede entrar en la sección crítica


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
        
        print(f"Process {process.pid} entering critical section at time {process.clock.get_time()}")
        time.sleep(random.uniform(0.5, 1.5))  # Simula el tiempo en la sección crítica
        print(f"Process {process.pid} leaving critical section at time {process.clock.get_time()}")
        process.release_resource()  # Libera el recurso

total_processes = 3  # Número total de procesos
processes = [Process(i, total_processes) for i in range(total_processes)]  # Crea una lista de instancias de procesos
threads = [threading.Thread(target=simulate_process, args=(p,)) for p in processes]  # Crea una lista de hilos para cada proceso

for thread in threads:
    thread.start()  # Inicia cada hilo
for thread in threads:
    thread.join()  # Espera a que todos los hilos terminen

''''

Inicialización de Procesos: Cada proceso se inicializa con su propio reloj de Lamport y una cola de solicitudes.
Solicitud de Recurso: Cada proceso incrementa su reloj, crea una solicitud y la envía a todos los otros procesos.
Recepción de Solicitudes: Cada proceso recibe solicitudes de otros procesos, actualiza su reloj y añade la solicitud a su cola.
Verificación para Entrar en la Sección Crítica: Cada proceso verifica si puede entrar en la sección crítica (si su solicitud es la primera en la cola).
Entrada y Salida de la Sección Crítica: El proceso entra en la sección crítica, incrementa su reloj, y luego libera el recurso.
Liberación de Recurso: El proceso libera el recurso eliminando su solicitud de la cola.'''


