#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (rank == 0) {
        char message[] = "Hello from rank 0";
        for (int i = 1; i < size; i++) {
            MPI_Send(message, sizeof(message), MPI_CHAR, i, 0, MPI_COMM_WORLD);
        }
    } else {
        char message[20];
        MPI_Recv(message, 20, MPI_CHAR, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Rank %d received message: %s\n", rank, message);
    }

    MPI_Finalize();
    return 0;
}
