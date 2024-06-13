#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_THREADS 5
#define NUM_ITERATIONS 1000000

// Contador global
int counter = 0;
// Mutex para sincronización
pthread_mutex_t mutex;

void* increment_counter(void* arg) {
    for (int i = 0; i < NUM_ITERATIONS; i++) {
        // Bloquear el mutex antes de acceder al contador
        pthread_mutex_lock(&mutex);
        counter++;
        // Desbloquear el mutex después de acceder al contador
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];
    int thread_ids[NUM_THREADS];
    int rc;

    // Inicializar el mutex
    pthread_mutex_init(&mutex, NULL);

    // Crear los hilos
    for (int i = 0; i < NUM_THREADS; i++) {
        thread_ids[i] = i;
        rc = pthread_create(&threads[i], NULL, increment_counter, (void*)&thread_ids[i]);
        if (rc) {
            printf("Error: No se pudo crear el hilo %d\n", i);
            exit(-1);
        }
    }

    // Esperar a que los hilos terminen
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    // Destruir el mutex
    pthread_mutex_destroy(&mutex);

    // Imprimir el valor final del contador
    printf("Valor final del contador: %d\n", counter);

    // Finalizar el programa
    pthread_exit(NULL);
}
