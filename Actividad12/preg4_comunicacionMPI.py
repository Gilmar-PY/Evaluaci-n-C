from mpi4py import MPI
import time
import random

def main():
    comm = MPI.COMM_WORLD  # Comienza el comunicador 
    rank = comm.Get_rank()  # Obtiene el rango del proceso actual
    size = comm.Get_size()  # Obtiene el tamaño total del comunicador

    # Tarea antes de la barrera
    tarea_antes_de_barrera(rank)

    # Sincronización de barrera
    comm.Barrier()

    # Tarea después de la barrera
    tarea_despues_de_barrera(rank)

    # Segunda tarea después de la barrera
    segunda_tarea_despues_de_barrera(rank)

def tarea_antes_de_barrera(rank):
    tiempo_de_espera = random.uniform(0.1, 1.0)
    print(f"Proceso {rank} haciendo tarea antes de la barrera, durmiendo por {tiempo_de_espera:.2f} segundos.")
    time.sleep(tiempo_de_espera)

def tarea_despues_de_barrera(rank):
    print(f"Proceso {rank} haciendo tarea después de la barrera.")
    # Simula la realización de otra tarea
    time.sleep(random.uniform(0.1, 1.0))
    print(f"Proceso {rank} completó la tarea después de la barrera.")
  
def segunda_tarea_despues_de_barrera(rank):
    print(f"Proceso {rank} haciendo segunda tarea después de la barrera.")
    # Simula la realización de otra tarea
    time.sleep(random.uniform(0.1, 1.0))
    print(f"Proceso {rank} completó la segunda tarea después de la barrera.")

if __name__ == "__main__":
    main()

''' # Verificar la instalación de MPI
mpiexec --version

# Instalar MPI si no está instalado
sudo apt update
sudo apt install mpich

# Crear un entorno virtual de Python
python3 -m venv mpi_env

# Activar el entorno virtual
source mpi_env/bin/activate

# Instalar mpi4py
pip install mpi4py

# Ejecutar el script MPI
mpiexec -n 4 python3 preg4_comunicacionMPI.py
'''
