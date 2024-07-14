#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int vector_size = 1000000;
    int local_size = vector_size / size;

    double* local_A = (double*)malloc(local_size * sizeof(double));
    double* local_B = (double*)malloc(local_size * sizeof(double));
    double* local_C = (double*)malloc(local_size * sizeof(double));

    for (int i = 0; i < local_size; i++) {
        local_A[i] = rank + 1;
        local_B[i] = rank + 2;
    }

    MPI_Allreduce(local_A, local_C, local_size, MPI_DOUBLE, MPI_SUM, MPI_COMM_WORLD);

    for (int i = 0; i < local_size; i++) {
        local_C[i] = local_A[i] + local_B[i];
    }

    free(local_A);
    free(local_B);
    free(local_C);

    MPI_Finalize();
    return 0;
}
