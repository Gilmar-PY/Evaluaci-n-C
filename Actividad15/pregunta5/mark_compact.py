
class MarkCompactCollector:
    def __init__(self, size):
        self.size = size
        self.memory = [None] * size
        self.marked = [False] * size

    def allocate(self, obj):
        for i in range(self.size):
            if self.memory[i] is None:
                self.memory[i] = obj
                return i
        self.collect()
        return self.allocate(obj)

    def mark(self, roots):
        for root in roots:
            self._mark(root)

    def _mark(self, obj):
        if obj is not None:
            addr = obj
            if not self.marked[addr]:
                self.marked[addr] = True

    def compact(self):
        new_memory = [None] * self.size
        j = 0
        for i in range(self.size):
            if self.marked[i]:
                new_memory[j] = self.memory[i]
                j += 1
        self.memory = new_memory

    def collect(self):
        self.mark(self.memory)
        self.compact()
        self.marked = [False] * self.size

# Ejemplo de uso
collector = MarkCompactCollector(10)
addr1 = collector.allocate("obj1")
print(f"Asignado el obj1 en: {addr1}")
collector.collect()
print("Recolección de basura completa")
