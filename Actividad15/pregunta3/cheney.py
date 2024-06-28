class CheneyCollector:
    def __init__(self, size):
        self.size = size
        self.from_space = [None] * size  # Espacio de origen para los objetos
        self.to_space = [None] * size    # Espacio de destino para los objetos
        self.free_ptr = 0                # Puntero libre para asignación de objetos nuevos

    def allocate(self, obj):
        if self.free_ptr >= self.size:
            self.collect()  # Si el espacio libre está lleno, realizar la recolección de basura
        addr = self.free_ptr
        self.from_space[addr] = obj
        self.free_ptr += 1
        return addr

    def collect(self):
        self.to_space = [None] * self.size  # Limpiar el espacio de destino
        self.free_ptr = 0  # Reiniciar el puntero libre para la nueva asignación
        for obj in self.from_space:
            if obj is not None:
                self.copy(obj)  # Copiar objetos válidos al nuevo espacio de destino
        self.from_space, self.to_space = self.to_space, self.from_space  # Intercambiar espacios de origen y destino

    def copy(self, obj):
        addr = self.free_ptr
        self.to_space[addr] = obj
        self.free_ptr += 1
        return addr

# Ejemplo de uso
collector = CheneyCollector(10)
addr1 = collector.allocate("obj1")
print(f"Asignado el obj1 en: {addr1}")
collector.collect()
print("Recolección de basura completa")

'''

Este algoritmo de recolección de basura tipo Cheney utiliza dos espacios 
de memoria (from_space y to_space) para alternar entre ellos durante la recolección de basura, permitiendo 
así mantener la integridad de los objetos válidos y liberar la memoria no utilizada de manera eficiente.'''
