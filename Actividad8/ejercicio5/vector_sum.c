
//Ejercicio 5: Suma paralela de un vector con Pthreads
//Descripción: Implementa la suma de los elementos de un vector utilizando pthread para paralelizar el cálculo.
//Tareas:
//    Crear un vector grande.
//    Dividir el vector en segmentos y asignar cada segmento a un hilo diferente.
//    Utilizar pthread para realizar la suma en paralelo y combinar los resultados.
//Pistas:
//    Usa pthread_create y pthread_join para gestionar los hilos.
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 4
#define VECTOR_SIZE 1000000

typedef struct {
    int start;
    int end;
    double *vector;
    double sum;
} ThreadData;

void *partial_sum(void *arg) {
    ThreadData *data = (ThreadData *)arg;
    data->sum = 0.0;
    for (int i = data->start; i < data->end; i++) {
        data->sum += data->vector[i];
    }
    pthread_exit(NULL);
}

int main() {
    double *vector = (double *)malloc(VECTOR_SIZE * sizeof(double));
    for (int i = 0; i < VECTOR_SIZE; i++) {
        vector[i] = rand() % 100;
    }

    pthread_t threads[NUM_THREADS];
    ThreadData thread_data[NUM_THREADS];
    int segment_size = VECTOR_SIZE / NUM_THREADS;

    for (int i = 0; i < NUM_THREADS; i++) {
        thread_data[i].start = i * segment_size;
        thread_data[i].end = (i == NUM_THREADS - 1) ? VECTOR_SIZE : (i + 1) * segment_size;
        thread_data[i].vector = vector;
        pthread_create(&threads[i], NULL, partial_sum, (void *)&thread_data[i]);
    }

    double total_sum = 0.0;
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
        total_sum += thread_data[i].sum;
    }

    printf("Total sum: %f\n", total_sum);
    free(vector);
    return 0;
}
