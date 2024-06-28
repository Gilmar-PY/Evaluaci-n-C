class MarzulloNode:
    def __init__(self, node_id, time, uncertainty):
        self.node_id = node_id
        self.time = time
        self.uncertainty = uncertainty

    def get_time_interval(self):
        return (self.time - self.uncertainty, self.time + self.uncertainty)

def marzullo_algorithm(nodes):
    intervals = [node.get_time_interval() for node in nodes]
    events = []
    for start, end in intervals:
        events.append((start, +1))
        events.append((end, -1))
    events.sort()

    max_count = 0
    count = 0
    best_interval = None
    for event in events:
        count += event[1]
        if count > max_count:
            max_count = count
            best_interval = event[0]
    
    return best_interval

# Ejemplo de uso
nodes = [MarzulloNode(i, time, uncertainty) for i, (time, uncertainty) in enumerate([(10, 2), (12, 1), (14, 3)])]
best_time = marzullo_algorithm(nodes)
print(best_time)

