
class MarkSweepCollector:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size
        self.marked = [False] * size
        self.object_to_address = {}

    def allocate(self, obj):
        for i in range(self.size):
            if self.memory[i] is None:
                self.memory[i] = obj
                self.object_to_address[obj] = i
                return i
        self.collect()
        return self.allocate(obj)

    def mark(self, roots):
        for root in roots:
            self._mark(root)

    def _mark(self, obj):
        if obj is not None and obj in self.object_to_address:
            addr = self.object_to_address[obj]
            if not self.marked[addr]:
                self.marked[addr] = True

    def sweep(self):
        for i in range(self.size):
            if not self.marked[i]:
                obj = self.memory[i]
                if obj is not None:
                    del self.object_to_address[obj]
                self.memory[i] = None
            else:
                self.marked[i] = False

    def collect(self):
        self.mark(self.memory)
        self.sweep()

# Ejemplo de uso
collector = MarkSweepCollector(10)
addr1 = collector.allocate("obj1")
print(f"Asignado al obj1 en: {addr1}")
collector.collect()
print("Recolección de basura completa")
