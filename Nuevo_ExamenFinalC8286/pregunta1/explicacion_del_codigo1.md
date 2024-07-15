Importaciones y Configuración

    Importaciones:

```python

import asyncio 
import logging  
from collections import deque  
from concurrent.futures import ThreadPoolExecutor 
from threading import Lock  

    asyncio: Proporciona soporte para programación asíncrona en Python.
    logging: Utilizado para registrar eventos y mensajes de log.
    deque: Una cola doble eficiente para la gestión de eventos.
    ThreadPoolExecutor: Permite la ejecución de tareas en hilos.
    Lock: Proporciona mecanismos de bloqueo para asegurar la sincronización entre hilos.

Configuración del registro de eventos:

python

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

        Se configura el módulo logging para registrar mensajes de nivel INFO y superiores.

Clase Event

    Clase Event:

    python

    class Event:
        def __init__(self, event_type, data, priority=1):
            self.event_type = event_type  
            self.data = data  
            self.priority = priority  

        Representa un evento con tipo, datos asociados y una prioridad.

Clase Notebook

    Clase Notebook:

    python

    class Notebook:
        def __init__(self):
            self.cells = []  
            self.state = {}  

        async def execute_cell(self, cell):
            logger.info(f"Ejecutando celda: {cell}")  
            await asyncio.sleep(1)  
            self.state[cell] = "Ejecutada"  
            logger.info(f"Celda {cell} ejecutada con éxito")  

        Representa un "notebook" con celdas para ejecutar.
        execute_cell: Método asíncrono que simula la ejecución de una celda.

Clase EventSystem

    Clase EventSystem:

    python

    class EventSystem:
        def __init__(self):
            self.event_queue = deque()  
            self.lock = Lock()  
            self.notebook = Notebook()  
            self.executor = ThreadPoolExecutor()  

        def add_event(self, event):
            with self.lock:  
                self.event_queue.append(event)  
                self.event_queue = deque(sorted(self.event_queue, key=lambda e: e.priority))  
                logger.info(f"Evento agregado: {event.event_type} - {event.data} con prioridad {event.priority}")  

        async def handle_event(self, event):
            try:
                if event.event_type == "execute":  
                    await self.notebook.execute_cell(event.data)  
                else:
                    logger.warning(f"Tipo de evento desconocido: {event.event_type}")  
            except Exception as e:  
                logger.error(f"Error manejando el evento {event}: {e}")  

        async def event_loop(self):
            while True: 
                if self.event_queue:  
                    with self.lock:  
                        event = self.event_queue.popleft()  
                    await self.handle_event(event)  
                else:
                    await asyncio.sleep(0.1)  

        __init__: Inicializa la cola de eventos, el bloqueo, una instancia de Notebook y un ThreadPoolExecutor.
        add_event: Agrega eventos a la cola y los ordena por prioridad.
        handle_event: Maneja los eventos, ejecutando celdas si el tipo de evento es execute.
        event_loop: Bucle infinito que procesa eventos de la cola, manejando cada evento uno por uno.

Función Principal Asíncrona

    Función main:

    python

    async def main():
        event_system = EventSystem()  
        
        event_system.add_event(Event("execute", "Celda 1", priority=2))  
        event_system.add_event(Event("execute", "Celda 2", priority=1))  
        event_system.add_event(Event("execute", "Celda 3", priority=3))  
        
        await event_system.event_loop()  

        Crea una instancia de EventSystem.
        Agrega eventos de ejecución de celdas con diferentes prioridades.
        Inicia el bucle de eventos.

Punto de Entrada del Script

    Punto de entrada:

    python

    if __name__ == "__main__":
        asyncio.run(main())  

        Ejecuta la función main utilizando asyncio.run cuando el script se ejecuta directamente.

Resumen del Funcionamiento

    Inicialización: Se configuran las herramientas necesarias (deque, Lock, ThreadPoolExecutor).
    Creación de Eventos: Se crean eventos con tipo execute para ejecutar diferentes celdas.
    Manejo de Eventos: Los eventos se agregan a una cola priorizada.
    Bucle de Eventos: Un bucle asíncrono procesa los eventos, ejecutando las celdas en el Notebook.
    Registro: Se registran mensajes informativos y de error para monitorear la ejecución del sistema.
