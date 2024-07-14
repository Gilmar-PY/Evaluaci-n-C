
import asyncio
import logging
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Event:
    def __init__(self, event_type, data, priority=1):
        self.event_type = event_type
        self.data = data
        self.priority = priority

class Notebook:
    def __init__(self):
        self.cells = []
        self.state = {}

    async def execute_cell(self, cell):
        logger.info(f"Ejecutando celda: {cell}")
        await asyncio.sleep(1)
        self.state[cell] = "Ejecutada"
        logger.info(f"Celda {cell} ejecutada con éxito")

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
                await asyncio.sleep(0.1)  # Evitar busy waiting

async def main():
    event_system = EventSystem()
    
    # Simulación de eventos
    event_system.add_event(Event("execute", "Celda 1", priority=2))
    event_system.add_event(Event("execute", "Celda 2", priority=1))
    event_system.add_event(Event("execute", "Celda 3", priority=3))
    
    await event_system.event_loop()

if __name__ == "__main__":
    asyncio.run(main())
