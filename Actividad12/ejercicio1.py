###implementamos una pila sin bloque usando la operacion CAS. Utiliza el modilo 
multiprocessing para simular hilos concurrentes.

import threading  # Importa el módulo threading para manejar hilos
import time  # Importa el módulo time para manejar tiempos de espera
from typing import Optional  # Importa Optional para anotaciones de tipo

# Clase que representa un nodo en la pila
class Node:
    def __init__(self, value: int):
        self.value = value  # Almacena el valor del nodo
        self.next = None  # Puntero al siguiente nodo en la pila

# Clase que representa una pila lock-free
class LockFreeStack:
    def __init__(self):
        self.top: Optional[Node] = None  # Puntero al nodo superior de la pila
        self.lock = threading.Lock()  # Bloqueo para simular CAS de forma segura

    # Método que simula una operación de CAS (Compare-And-Swap)
    def cas(self, old, new):
        with self.lock:  # Adquiere el bloqueo para asegurar la operación atómica
            if self.top == old:  # Compara si el valor actual de top es igual a old
                self.top = new  # Si es igual, actualiza top a new
                return True  # Retorna True indicando que la operación fue exitosa
            return False  # Retorna False indicando que la operación falló

    # Método para empujar un valor en la pila
    def push(self, value: int):
        new_node = Node(value)  # Crea un nuevo nodo con el valor dado
        while True:
            old_top = self.top  # Guarda el valor actual de top
            new_node.next = old_top  # Enlaza el nuevo nodo al nodo actual de top
            if self.cas(old_top, new_node):  # Intenta realizar la operación CAS
                return  # Si CAS es exitoso, sale del bucle

    # Método para sacar un valor de la pila
    def pop(self) -> Optional[int]:
        while True:
            old_top = self.top  # Guarda el valor actual de top
            if old_top is None:  # Si la pila está vacía
                return None  # Retorna None indicando que no hay elementos
            new_top = old_top.next  # Nuevo top será el siguiente nodo
            if self.cas(old_top, new_top):  # Intenta realizar la operación CAS
                return old_top.value  # Si CAS es exitoso, retorna el valor del nodo

# Instancia de la pila lock-free
stack = LockFreeStack()

# Función para que los hilos empujen valores en la pila
def worker_push():
    for i in range(100):
        stack.push(i)  # Empuja el valor i en la pila
        time.sleep(0.01)  # Espera un tiempo para simular concurrencia

# Función para que los hilos saquen valores de la pila
def worker_pop():
    for _ in range(100):
        print(stack.pop())  # Imprime el valor sacado de la pila
        time.sleep(0.01)  # Espera un tiempo para simular concurrencia

threads = []
for _ in range(2):
    t1 = threading.Thread(target=worker_push)  # Crea un hilo para empujar valores
    t2 = threading.Thread(target=worker_pop)  # Crea un hilo para sacar valores
    threads.append(t1)  # Añade el hilo a la lista
    threads.append(t2)  # Añade el hilo a la lista
    t1.start()  # Inicia el hilo
    t2.start()  # Inicia el hilo

for t in threads:
    t.join()  # Espera a que todos los hilos terminen



















    
      
      
