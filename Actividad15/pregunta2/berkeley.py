class BerkeleyNode:
    def __init__(self, node_id, time):
        self.node_id = node_id  # ID único del nodo
        self.time = time  # Tiempo actual del nodo

    def adjust_time(self, offset):
        self.time += offset  # Ajusta el tiempo del nodo sumando el offset

class BerkeleyMaster:
    def __init__(self, nodes):
        self.nodes = nodes  # Lista de nodos a sincronizar

    def synchronize_clocks(self):
        times = [node.time for node in self.nodes]  # Obtiene los tiempos actuales de todos los nodos
        average_time = sum(times) / len(times)  # Calcula el tiempo promedio de todos los nodos
        for node in self.nodes:
            offset = average_time - node.time  # Calcula el offset para cada nodo
            node.adjust_time(offset)  # Ajusta el tiempo de cada nodo según el offset calculado
        return [(node.node_id, node.time) for node in self.nodes]  # Retorna una lista de tuplas (ID del nodo, tiempo sincronizado)

# Ejemplo de uso
nodes = [BerkeleyNode(i, time) for i, time in enumerate([10, 20, 30])]  # Crea una lista de nodos con tiempos iniciales
master = BerkeleyMaster(nodes)  # Crea una instancia del maestro de Berkeley con los nodos
synchronized_times = master.synchronize_clocks()  # Sincroniza los relojes de los nodos
print(synchronized_times)  # Imprime los tiempos sincronizados de cada nodo

'''
Este algoritmo de Berkeley busca ajustar los relojes de los nodos para que se acerquen
al tiempo promedio de todos los nodos, minimizando las
discrepancias entre ellos y mejorando la sincronización en un sistema distribuido. '''
