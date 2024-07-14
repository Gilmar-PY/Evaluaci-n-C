''' 
8 . Implementa una cola sin bloqueo usando 
CAS para modificar los punteros de cabeza y cola. Simula la concurrencia 
utilizando threading.'''

import threading  # Importa el módulo threading para manejar hilos
import time  # Importa el módulo time para manejar tiempos de espera
from typing import Optional  # Importa Optional para anotaciones de tipo

# Clase que representa un nodo en la cola
class Node:
    def __init__(self, value: int):
        self.value = value  # Almacena el valor del nodo
        self.next = None  # Puntero al siguiente nodo en la cola

# Clase que representa una cola lock-free
class LockFreeQueue:
    def __init__(self):
        self.head: Optional[Node] = Node(None)  # Nodo ficticio inicial como cabeza de la cola
        self.tail: Optional[Node] = self.head  # Inicialmente, cola es igual a cabeza
        self.lock = threading.Lock()  # Bloqueo para simular CAS de forma segura

    # Método que simula una operación de CAS (Compare-And-Swap)
    def cas(self, attr, old, new):
        with self.lock:  # Adquiere el bloqueo para asegurar la operación atómica
            if getattr(self, attr) == old:  # Compara si el valor actual del atributo es igual a old
                setattr(self, attr, new)  # Si es igual, actualiza el atributo a new
                return True  # Retorna True indicando que la operación fue exitosa
            return False  # Retorna False indicando que la operación falló

    # Método para encolar un valor
    def enqueue(self, value: int):
        new_node = Node(value)  # Crea un nuevo nodo con el valor dado
        while True:
            old_tail = self.tail  # Guarda el valor actual de tail
            next_tail = old_tail.next  # Obtiene el siguiente nodo de tail
            if old_tail == self.tail:  # Verifica que tail no haya cambiado
                if next_tail is None:  # Verifica que el siguiente nodo de tail sea None
                    if self.cas('tail.next', next_tail, new_node):  # Intenta enlazar el nuevo nodo al final
                        self.cas('tail', old_tail, new_node)  # Intenta actualizar tail al nuevo nodo
                        return  # Si ambas operaciones CAS son exitosas, sale del bucle
                else:
                    self.cas('tail', old_tail, next_tail)  # Si next_tail no es None, mueve tail al siguiente nodo

    # Método para desencolar un valor
    def dequeue(self) -> Optional[int]:
        while True:
            old_head = self.head  # Guarda el valor actual de head
            old_tail = self.tail  # Guarda el valor actual de tail
            next_head = old_head.next  # Obtiene el siguiente nodo de head
            if old_head == self.head:  # Verifica que head no haya cambiado
                if old_head == old_tail:  # Si head es igual a tail
                    if next_head is None:  # Verifica si la cola está vacía
                        return None  # Retorna None indicando que no hay elementos
                    self.cas('tail', old_tail, next_head)  # Si no está vacía, mueve tail al siguiente nodo
                else:
                    value = next_head.value  # Obtiene el valor del siguiente nodo
                    if self.cas('head', old_head, next_head):  # Intenta mover head al siguiente nodo
                        return value  # Si CAS es exitoso, retorna el valor

# Instancia de la cola lock-free
queue = LockFreeQueue()

# Función para que los hilos encolen valores
def worker_enqueue():
    for i in range(100):
        queue.enqueue(i)  # Encola el valor i
        time.sleep(0.01)  # Espera un poco

# Función para que los hilos desencolen valores
def worker_dequeue():
    for _ in range(100):
        print(queue.dequeue())  # Muestra el valor desencolado
        time.sleep(0.01)  # Espera un poco

# Creamos hilos para encolar y desencolar valores
threads = []
for _ in range(2):
    t1 = threading.Thread(target=worker_enqueue)  # Hilo para encolar valores
    t2 = threading.Thread(target=worker_dequeue)  # Hilo para desencolar valores
    threads.append(t1)  # Añadimos el hilo a la lista
    threads.append(t2)  # Añadimos el hilo a la lista
    t1.start()  # Iniciamos el hilo
    t2.start()  # Iniciamos el hilo

# Esperamos a que todos los hilos terminen
for t in threads:
    t.join()
  
    
