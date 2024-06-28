
class MarkSweepCollector:
    def __init__(self, size):
        self.size = size  # Tamaño total de la memoria
        self.memory = [None] * size  # Lista que simula la memoria, inicialmente vacía
        self.marked = [False] * size  # Lista para marcar objetos en memoria
        self.object_to_address = {}  # Diccionario para almacenar la dirección de memoria de cada objeto

    def allocate(self, obj):
        for i in range(self.size):
            if self.memory[i] is None:
                self.memory[i] = obj  # Asigna el objeto a la primera posición vacía en la memoria
                self.object_to_address[obj] = i  # Registra la dirección de memoria del objeto en el diccionario
                return i  # Devuelve la dirección de memoria asignada
        self.collect()  # Si no hay espacio en memoria, realiza una recolección de basura
        return self.allocate(obj)  # Llama recursivamente a allocate para intentar asignar el objeto después de la recolección

    def mark(self, roots):
        for root in roots:
            self._mark(root)  # Marca todos los objetos alcanzables desde los roots (raíces)

    def _mark(self, obj):
        if obj is not None and obj in self.object_to_address:  # Verifica si el objeto existe en el diccionario
            addr = self.object_to_address[obj]  # Obtiene la dirección de memoria del objeto
            if not self.marked[addr]:  # Si el objeto no ha sido marcado aún
                self.marked[addr] = True  # Marca el objeto

    def sweep(self):
        for i in range(self.size):
            if not self.marked[i]:  # Si el objeto en la posición i no está marcado
                obj = self.memory[i]  # Obtiene el objeto en esa posición
                if obj is not None:
                    del self.object_to_address[obj]  # Elimina la referencia del objeto en el diccionario
                self.memory[i] = None  # Libera la posición de memoria
            else:
                self.marked[i] = False  # Reinicia la marca para la próxima recolección de basura

    def collect(self):
        self.mark(self.memory)  # Marca todos los objetos en la memoria
        self.sweep()  # Realiza el barrido para liberar memoria no marcada

# Ejemplo de uso
collector = MarkSweepCollector(10)
addr1 = collector.allocate("obj1")
print(f"Asignado al obj1 en: {addr1}")
collector.collect()
print("Recolección de basura completa")


'''
colector de basura implementa el algoritmo Mark-Sweep, que marca todos los objetos alcanzables
desde las raíces y luego barrido la memoria para liberar
los objetos no marcados, asegurando así la gestión eficiente de la memoria y evitando fugas de memoria en el sistema.
'''
