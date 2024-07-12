
from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Dimensiones del dominio global
global_nx, global_ny = 100, 100
# Dimensiones del subdominio local
local_nx, local_ny = global_nx // size, global_ny

# Inicialización del subdominio local con algunos valores iniciales
local_domain = np.zeros((local_nx + 2, local_ny + 2))

# Función para actualizar el dominio local usando el método de los volúmenes finitos
def update_domain(domain):
    new_domain = domain.copy()
    for i in range(1, local_nx + 1):
        for j in range(1, local_ny + 1):
            new_domain[i, j] = 0.25 * (domain[i+1, j] + domain[i-1, j] + domain[i, j+1] + domain[i, j-1])
    return new_domain

# Función para comunicar las fronteras entre nodos
def exchange_borders(domain):
    requests = []
    if rank > 0:
        requests.append(comm.Isend(domain[1, :], dest=rank-1))
        requests.append(comm.Irecv(domain[0, :], source=rank-1))
    if rank < size - 1:
        requests.append(comm.Isend(domain[local_nx, :], dest=rank+1))
        requests.append(comm.Irecv(domain[local_nx + 1, :], source=rank+1))
    MPI.Request.Waitall(requests)

# Simulación principal
start_time = time.time()
for step in range(100):
    exchange_borders(local_domain)
    local_domain[1:-1, 1:-1] = update_domain(local_domain)
end_time = time.time()

# Recolección de resultados para análisis y visualización
global_domain = None
if rank == 0:
    global_domain = np.zeros((global_nx, global_ny))

comm.Gather(local_domain[1:-1, 1:-1], global_domain, root=0)

if rank == 0:
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
    # Aquí podrías agregar código para visualizar los resultados, por ejemplo usando matplotlib

MPI.Finalize()

'''
Inicialización del Dominio:

    El dominio global se divide entre los nodos disponibles. Cada nodo 
    gestiona un subdominio local.
    La matriz local_domain se inicializa con dimensiones extendidas para 
    incluir las celdas frontera necesarias para la comunicación con los vecinos.

Método de los Volúmenes Finitos:

    La función update_domain aplica el método de volúmenes finitos para
    actualizar el estado del dominio local.

Comunicación Eficiente:

    La función exchange_borders gestiona la comunicación de las celdas 
    frontera entre nodos usando MPI_Isend y MPI_Irecv para no bloquear la 
    ejecución mientras se envían y reciben los datos.

Simulación Principal:

    En el bucle principal de la simulación, se actualizan las fronteras y
    se aplica el método de volúmenes finitos a las celdas interiores.

Análisis y Visualización:

    Los resultados locales se reúnen en el proceso raíz (rank 0) usando 
    MPI_Gather para su análisis y visualización.
