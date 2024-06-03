
//**Implementa un programa en C utilizando POSIX threads (pthread) que demuestre el 
uso de mutexes para proteger una variable compartida. El programa debe crear 
varios hilos que incrementen una variable global compartida de manera segura.*//





#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 5
#define NUM_INCREMENTS 1000000

pthread_mutex_t mutex;
int shared_variable = 0;

void* increment(void* arg) {
    for (int i = 0; i < NUM_INCREMENTS; i++) {
        pthread_mutex_lock(&mutex);
        shared_variable++;
        pthread_mutex_unlock(&mutex);
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];
    pthread_mutex_init(&mutex, NULL);

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, increment, NULL);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&mutex);
    printf("Final value of shared_variable: %d\n", shared_variable);
    return 0;
}

