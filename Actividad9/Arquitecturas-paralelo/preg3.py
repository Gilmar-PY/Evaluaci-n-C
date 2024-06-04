'''3 . Combina MPI y OpenMP en un programa Python
utilizando mpi4py y threading. Simula una tarea que se 
distribuye entre nodos y luego se paraleliza dentro de cada nodo.'''



from mpi4py import MPI    #comunicacion proccess
from threading import Thread

def thread_task(rank):
    print(f"Thread in rank {rank} is running")

comm = MPI.COMM_WORLD # obt el copmunicador global 
rank = comm.Get_rank()#proceso actual identificador
size = comm.Get_size()# número total 

threads = []
for _ in range(4):
    t = Thread(target=thread_task, args=(rank,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

if rank == 0:
    print("All threads completed.")

'''   
sudo apt-get install -y openmpi-bin openmpi-common libopenmpi-dev
pip3 install mpi4py
mpirun -np 4 python3 preg3.py
'''



