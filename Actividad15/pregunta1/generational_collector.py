
class GenerationalCollector:
    def __init__(self, size):
        self.size = size
        self.young_gen = [None] * size
        self.old_gen = [None] * size
        self.young_ptr = 0
        self.old_ptr = 0

    def allocate(self, obj, old=False):
        if old:
            if self.old_ptr >= self.size:
                self.collect_old()
            addr = self.old_ptr
            self.old_gen[addr] = obj
            self.old_ptr += 1
        else:
            if self.young_ptr >= self.size:
                self.collect_young()
            addr = self.young_ptr
            self.young_gen[addr] = obj
            self.young_ptr += 1
        return addr

    def collect_young(self):
        self.old_gen.extend([obj for obj in self.young_gen if obj is not None])
        self.young_gen = [None] * self.size
        self.young_ptr = 0

    def collect_old(self):
        self.old_gen = [obj for obj in self.old_gen if obj is not None]
        self.old_ptr = len(self.old_gen)
        self.old_gen.extend([None] * (self.size - self.old_ptr))

# Ejemplo de uso
collector = GenerationalCollector(10)
addr1 = collector.allocate("obj1")
print(f"Asignado en el obj1: {addr1}")
collector.collect_young()
print("Se completa la recolección de basura de la generación joven")
