import numpy as np
from joblib import Parallel, delayed

def multiply_sub_matrices(A, B):
    return np.dot(A, B)

def parallel_matrix_multiplication():
    # Crear dos matrices grandes
    A = np.random.rand(1000, 1000)
    B = np.random.rand(1000, 1000)
    
    # Dividir las matrices en sub-matrices
    A_subs = np.array_split(A, 4, axis=0)
    B_subs = np.array_split(B, 4, axis=1)

    # Multiplicar las sub-matrices en paralelo
    results = Parallel(n_jobs=4)(delayed(multiply_sub_matrices)(A_sub, B_sub) for A_sub in A_subs for B_sub in B_subs)
    
    # Crear la matriz resultante
    C = np.zeros((1000, 1000))
    for i, res in enumerate(results):
        row = i // 4
        col = i % 4
        C[row*250:(row+1)*250, col*250:(col+1)*250] = res

    return C

# Ejecutar la multiplicación de matrices en paralelo y imprimir el resultado
C = parallel_matrix_multiplication()
print("Matriz resultante:")
print(C)

