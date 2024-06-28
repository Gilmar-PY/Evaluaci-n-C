
class BerkeleyNode:
    def __init__(self, node_id, time):
        self.node_id = node_id
        self.time = time

    def adjust_time(self, offset):
        self.time += offset

class BerkeleyMaster:
    def __init__(self, nodes):
        self.nodes = nodes

    def synchronize_clocks(self):
        times = [node.time for node in self.nodes]
        average_time = sum(times) / len(times)
        for node in self.nodes:
            offset = average_time - node.time
            node.adjust_time(offset)
        return [(node.node_id, node.time) for node in self.nodes]

# Ejemplo de uso
nodes = [BerkeleyNode(i, time) for i, time in enumerate([10, 20, 30])]
master = BerkeleyMaster(nodes)
synchronized_times = master.synchronize_clocks()
print(synchronized_times)
