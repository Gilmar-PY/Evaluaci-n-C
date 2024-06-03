#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    long long num_samples = 1000000;
    long long local_samples = num_samples / size;
    long long local_count = 0;
    unsigned int seed = rank;

    for (long long i = 0; i < local_samples; i++) {
        double x = (double)rand_r(&seed) / RAND_MAX;
        double y = (double)rand_r(&seed) / RAND_MAX;
        if (x * x + y * y <= 1.0) {
            local_count++;
        }
    }

    long long total_count;
    MPI_Reduce(&local_count, &total_count, 1, MPI_LONG_LONG_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        double pi_estimate = (4.0 * total_count) / num_samples;
        printf("Estimated Pi: %f\n", pi_estimate);
    }

    MPI_Finalize();
    return 0;
}
