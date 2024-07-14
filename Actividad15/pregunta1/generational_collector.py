
class GenerationalCollector:
    def __init__(self, size):
        self.size = size  # Tamaño máximo para cada generación
        self.young_gen = [None] * size  # Lista para la generación joven inicializada con `None`
        self.old_gen = [None] * size  # Lista para la generación vieja inicializada con `None`
        self.young_ptr = 0  # Puntero para el siguiente espacio disponible en la generación joven
        self.old_ptr = 0  # Puntero para el siguiente espacio disponible en la generación vieja

    def allocate(self, obj, old=False):
        if old:
            if self.old_ptr >= self.size:  # Si la generación vieja está llena, se realiza la recolección de basura
                self.collect_old()
            addr = self.old_ptr  # Dirección de memoria asignada para el objeto en la generación vieja
            self.old_gen[addr] = obj  # Asigna el objeto en la dirección calculada
            self.old_ptr += 1  # Incrementa el puntero de la generación vieja
        else:
            if self.young_ptr >= self.size:  # Si la generación joven está llena, se realiza la recolección de basura
                self.collect_young()
            addr = self.young_ptr  # Dirección de memoria asignada para el objeto en la generación joven
            self.young_gen[addr] = obj  # Asigna el objeto en la dirección calculada
            self.young_ptr += 1  # Incrementa el puntero de la generación joven
        return addr  # Retorna la dirección de memoria asignada para el objeto

    def collect_young(self):
        # Mueve los objetos no nulos de la generación joven a la generación vieja extendiendo la lista
        self.old_gen.extend([obj for obj in self.young_gen if obj is not None])
        self.young_gen = [None] * self.size  # Reinicia la generación joven con `None`
        self.young_ptr = 0  # Reinicia el puntero de la generación joven

    def collect_old(self):
        # Filtra los objetos no nulos en la generación vieja y ajusta su tamaño
        self.old_gen = [obj for obj in self.old_gen if obj is not None]
        self.old_ptr = len(self.old_gen)  # Actualiza el puntero de la generación vieja
        self.old_gen.extend([None] * (self.size - self.old_ptr))  # Extiende la generación vieja con `None` hasta el tamaño máximo

# Ejemplo de uso
collector = GenerationalCollector(10)  # Crea un colector de basura con un tamaño máximo de 10 objetos por generación
addr1 = collector.allocate("obj1")  # Asigna el objeto "obj1" en la generación joven
print(f"Asignado en el obj1: {addr1}")  # Imprime la dirección de memoria asignada para "obj1"
collector.collect_young()  # Realiza la recolección de basura en la generación joven
print("Se completa la recolección de basura de la generación joven")  # Imprime un mensaje indicando que se completó la recolección de basura


'''
simula un sistema de gestión de memoria simple con dos generaciones, donde se asignan 
objetos y se realiza la recolección 
de basura según las políticas de generación joven y vieja. '''
