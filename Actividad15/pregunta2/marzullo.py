class MarzulloNode:
    def __init__(self, node_id, time, uncertainty):
        self.node_id = node_id  # Identificador del nodo
        self.time = time  # Tiempo del nodo
        self.uncertainty = uncertainty  # Incertidumbre del tiempo

    def get_time_interval(self):
        return (self.time - self.uncertainty, self.time + self.uncertainty)

def marzullo_algorithm(nodes):
    intervals = [node.get_time_interval() for node in nodes]  # Obtiene los intervalos de tiempo para cada nodo
    events = []
    for start, end in intervals:
        events.append((start, +1))  # Evento de inicio del intervalo (+1)
        events.append((end, -1))    # Evento de fin del intervalo (-1)
    events.sort()  # Ordena los eventos por tiempo

    max_count = 0
    count = 0
    best_interval = None
    for event in events:
        count += event[1]  # Ajusta el contador según el tipo de evento (+1 o -1)
        if count > max_count:
            max_count = count
            best_interval = event[0]  # Actualiza el mejor intervalo cuando se alcanza el máximo de superposiciones
    
    return best_interval  # Devuelve el punto en el tiempo con la mayor superposición de intervalos

# Ejemplo de uso
nodes = [MarzulloNode(i, time, uncertainty) for i, (time, uncertainty) in enumerate([(10, 2), (12, 1), (14, 3)])]
best_time = marzullo_algorithm(nodes)
print(best_time)


'''
Este algoritmo es útil para situaciones donde se deben coordinar eventos 
temporales entre múltiples nodos con incertidumbres en sus tiempos, 
permitiendo encontrar un momento óptimo que maximice la superposición de intervalos.'''
