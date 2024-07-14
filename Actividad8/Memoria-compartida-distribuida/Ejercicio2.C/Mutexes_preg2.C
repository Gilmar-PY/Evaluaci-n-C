
//**Implementa un programa en C utilizando POSIX threads (pthread) que demuestre el 
uso de mutexes para proteger una variable compartida. El programa debe crear 
varios hilos que incrementen una variable global compartida de manera segura.*//


#include <stdio.h>       // Biblioteca estándar de entrada y salida
#include <stdlib.h>      // Biblioteca estándar para funciones de utilidad, como malloc y rand
#include <pthread.h>     // Biblioteca para la creación y gestión de hilos

#define NUM_THREADS 5    // Define el número de hilos a utilizar
#define NUM_INCREMENTS 1000000  // Define el número de incrementos por hilo

pthread_mutex_t mutex;   // Declara un mutex (bloqueo mutuo) para proteger el acceso a shared_variable
int shared_variable = 0; // Variable compartida entre hilos que será incrementada

// Función que incrementa la variable compartida en un bucle
void* increment(void* arg) {
    for (int i = 0; i < NUM_INCREMENTS; i++) { // Bucle que se ejecuta NUM_INCREMENTS veces
        pthread_mutex_lock(&mutex); // Adquiere el bloqueo del mutex para acceso exclusivo a shared_variable
        shared_variable++; // Incrementa la variable compartida
        pthread_mutex_unlock(&mutex); // Libera el bloqueo del mutex
    }
    pthread_exit(NULL); // Termina el hilo
}

int main() {
    pthread_t threads[NUM_THREADS]; // Arreglo para los identificadores de los hilos
    pthread_mutex_init(&mutex, NULL); // Inicializa el mutex con los atributos por defecto

    // Crea los hilos y les asigna la función increment
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_create(&threads[i], NULL, increment, NULL); // Crea un hilo que ejecuta la función increment
    }

    // Espera a que todos los hilos terminen
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL); // Espera a que el hilo i termine
    }

    pthread_mutex_destroy(&mutex); // Destruye el mutex
    printf("Final value of shared_variable: %d\n", shared_variable); // Imprime el valor final de la variable compartida
    return 0; // Termina el programa
}




