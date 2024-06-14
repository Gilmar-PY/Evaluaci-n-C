''' 9 . Implementa una simulación de las operaciones 
Load-Link (LL) y Store-Conditional (SC) en Python para una lista
enlazada sin bloqueo.'''



import threading  # Importa el módulo threading para manejar hilos
import time  # Importa el módulo time para manejar tiempos de espera

# Clase que representa un nodo en la lista enlazada
class Node:
    def __init__(self, value: int):
        self.value = value  # Almacena el valor del nodo
        self.next = None  # Puntero al siguiente nodo en la lista

# Clase que representa una lista enlazada lock-free
class LockFreeLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None  # Inicializa la cabeza de la lista como None
        self.lock = threading.Lock()  # Bloqueo para simular CAS de forma segura

    # Método para cargar el enlace (nodo actual)
    def load_link(self, node):
        return node  # Retorna el nodo actual

    # Método que simula una operación de CAS (Compare-And-Swap)
    def store_conditional(self, old_node, new_node):
        with self.lock:  # Adquiere el bloqueo para asegurar la operación atómica
            if self.head == old_node:  # Compara si el valor actual de head es igual a old_node
                self.head = new_node  # Si es igual, actualiza head a new_node
                return True  # Retorna True indicando que la operación fue exitosa
            return False  # Retorna False indicando que la operación falló

    # Método para insertar un valor en la lista
    def insert(self, value: int):
        new_node = Node(value)  # Crea un nuevo nodo con el valor dado
        while True:
            old_head = self.load_link(self.head)  # Carga el nodo actual de head
            new_node.next = old_head  # Enlaza el nuevo nodo al nodo actual de head
            if self.store_conditional(old_head, new_node):  # Intenta realizar la operación CAS
                return  # Si CAS es exitoso, sale del bucle

    # Método para eliminar un valor de la lista
    def remove(self) -> Optional[int]:
        while True:
            old_head = self.load_link(self.head)  # Carga el nodo actual de head
            if old_head is None:  # Si la lista está vacía
                return None  # Retorna None indicando que no hay elementos
            new_head = old_head.next  # El nuevo head será el siguiente nodo
            if self.store_conditional(old_head, new_head):  # Intenta realizar la operación CAS
                return old_head.value  # Si CAS es exitoso, retorna el valor del nodo

# Instancia de la lista enlazada lock-free
linked_list = LockFreeLinkedList()

# Función para que los hilos inserten valores en la lista
def worker_insert():
    for i in range(100):
        linked_list.insert(i)  # Inserta el valor i en la lista
        time.sleep(0.01)  # Espera un poco

# Función para que los hilos eliminen valores de la lista
def worker_remove():
    for _ in range(100):
        print(linked_list.remove())  # Muestra el valor eliminado de la lista
        time.sleep(0.01)  # Espera un poco

# Creamos hilos para insertar y eliminar valores
threads = []
for _ in range(2):
    t1 = threading.Thread(target=worker_insert)  # Hilo para insertar valores
    t2 = threading.Thread(target=worker_remove)  # Hilo para eliminar valores
    threads.append(t1)  # Añadimos el hilo a la lista
    threads.append(t2)  # Añadimos el hilo a la lista
    t1.start()  # Iniciamos el hilo
    t2.start()  # Iniciamos el hilo

# Esperamos a que todos los hilos terminen
for t in threads:
    t.join()
