

//Ejercicio 4: Multiplicación de matrices paralela con OpenMP Descripción: Implementa la multiplicación de matrices utilizando
// OpenMP para paralelizar el cálculo.
//Tareas:
//    Crear dos matrices grandes.
//    Paralelizar la multiplicación de matrices utilizando directivas de OpenMP.
//    Compilar y ejecutar el programa en un sistema con múltiples núcleos.
//Pistas:
//    Usa #pragma omp parallel for para paralelizar los bucles.

#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void parallel_matrix_multiplication(int N) {
    int i, j, k;
    double **A = (double **)malloc(N * sizeof(double *));
    double **B = (double **)malloc(N * sizeof(double *));
    double **C = (double **)malloc(N * sizeof(double *));
    
    // Inicializar matrices A, B y C
    for (i = 0; i < N; i++) {
        A[i] = (double *)malloc(N * sizeof(double));
        B[i] = (double *)malloc(N * sizeof(double));
        C[i] = (double *)malloc(N * sizeof(double));
        for (j = 0; j < N; j++) {
            A[i][j] = rand() % 100;
            B[i][j] = rand() % 100;
            C[i][j] = 0.0;
        }
    }

    // Multiplicación de matrices en paralelo
    #pragma omp parallel for private(i, j, k) shared(A, B, C)
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            for (k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    // Imprimir una pequeña parte de la matriz resultado
    for (i = 0; i < 5; i++) {
        for (j = 0; j < 5; j++) {
            printf("%f ", C[i][j]);
        }
        printf("\n");
    }

    // Liberar memoria
    for (i = 0; i < N; i++) {
        free(A[i]);
        free(B[i]);
        free(C[i]);
    }
    free(A);
    free(B);
    free(C);
}

int main() {
    int N = 1000;
    parallel_matrix_multiplication(N);
    return 0;
}
