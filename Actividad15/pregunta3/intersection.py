
class IntersectionNode:
    def __init__(self, node_id, time, uncertainty):
        self.node_id = node_id
        self.time = time
        self.uncertainty = uncertainty

    def get_time_interval(self):
        return (self.time - self.uncertainty, self.time + self.uncertainty)

def calculate_intersection(nodes):
    intervals = [node.get_time_interval() for node in nodes]
    max_start = max(interval[0] for interval in intervals)
    min_end = min(interval[1] for interval in intervals)
    if max_start <= min_end:
        return (max_start + min_end) / 2
    else:
        return None

# Ejemplo de uso
nodes = [IntersectionNode(i, time, uncertainty) for i, (time, uncertainty) in enumerate([(10, 2), (12, 1), (14, 3)])]
intersection_time = calculate_intersection(nodes)
print(intersection_time)
