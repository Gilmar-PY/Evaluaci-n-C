/**Ejercicio 5: Suma paralela de un vector con Pthreads
Descripción: Implementa la suma de los elementos de un vector utilizando pthread para paralelizar el cálculo.
Tareas:
  Crear un vector grande.
   Dividir el vector en segmentos y asignar cada segmento a un hilo diferente.
    Utilizar pthread para realizar la suma en paralelo y combinar los resultados.
Pistas:
   Usa pthread_create y pthread_join para gestionar los hilos. */


#include <stdio.h>       // Biblioteca estándar de entrada y salida
#include <stdlib.h>      // Biblioteca estándar para funciones de utilidad, como malloc y rand
#include <pthread.h>     // Biblioteca para la creación y gestión de hilos

#define NUM_THREADS 4    // Define el número de hilos a utilizar
#define VECTOR_SIZE 1000000  // Define el tamaño del vector

// Estructura para pasar datos a los hilos
typedef struct {
    int start;           // Índice de inicio del segmento del vector que este hilo va a procesar
    int end;             // Índice de fin del segmento del vector que este hilo va a procesar
    double *vector;      // Puntero al vector que contiene los datos
    double sum;          // Suma parcial calculada por este hilo
} ThreadData;

// Función que calcula la suma parcial de un segmento del vector
void *partial_sum(void *arg) {
    ThreadData *data = (ThreadData *)arg;  // Cast del argumento a la estructura ThreadData
    data->sum = 0.0;                       // Inicializa la suma parcial a 0
    for (int i = data->start; i < data->end; i++) {
        data->sum += data->vector[i];      // Suma los elementos del segmento
    }
    pthread_exit(NULL);                    // Termina el hilo
}

int main() {
    // Reserva memoria para el vector de datos
    double *vector = (double *)malloc(VECTOR_SIZE * sizeof(double));
    // Inicializa el vector con valores aleatorios entre 0 y 99
    for (int i = 0; i < VECTOR_SIZE; i++) {
        vector[i] = rand() % 100;
    }

    pthread_t threads[NUM_THREADS];        // Arreglo para los identificadores de los hilos
    ThreadData thread_data[NUM_THREADS];   // Arreglo para los datos que se pasarán a cada hilo
    int segment_size = VECTOR_SIZE / NUM_THREADS;  // Calcula el tamaño de cada segmento

    // Crea los hilos y les asigna su parte del trabajo
    for (int i = 0; i < NUM_THREADS; i++) {
        thread_data[i].start = i * segment_size;   // Índice de inicio para este hilo
        // Índice de fin para este hilo, el último hilo puede tener un segmento más grande si VECTOR_SIZE no es divisible por NUM_THREADS
        thread_data[i].end = (i == NUM_THREADS - 1) ? VECTOR_SIZE : (i + 1) * segment_size;
        thread_data[i].vector = vector;            // Asigna el vector al hilo
        pthread_create(&threads[i], NULL, partial_sum, (void *)&thread_data[i]);  // Crea el hilo
    }

    double total_sum = 0.0;  // Inicializa la suma total a 0
    // Espera a que todos los hilos terminen y acumula las sumas parciales
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);    // Espera a que el hilo termine
        total_sum += thread_data[i].sum;   // Acumula la suma parcial del hilo
    }

    // Imprime la suma total de los elementos del vector
    printf("Total sum: %f\n", total_sum);
    free(vector);  // Libera la memoria del vector
    return 0;      // Termina el programa
}
