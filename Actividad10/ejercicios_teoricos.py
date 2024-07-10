'''
¿Qué es un Deadlock y Bajo Qué Condiciones Puede Ocurrir en un Sistema Multihilo?

Un deadlock es una situación en la programación multihilo donde dos o más hilos se bloquean mutuamente, cada uno esperando que el otro libere un recurso que necesita para continuar su ejecución. Es como si cada hilo estuviera sosteniendo una llave que el otro necesita, y ninguno está dispuesto a soltar la llave que tiene.
Condiciones para que Ocurra un Deadlock:

    Exclusión Mutua (Mutual Exclusion): Los recursos involucrados no pueden ser compartidos; es decir, solo un hilo puede utilizarlos a la vez.
    Retención y Espera (Hold and Wait): Un hilo que ya ha adquirido al menos un recurso puede solicitar recursos adicionales que están siendo retenidos por otros hilos.
    No Preemptividad (No Preemption): Los recursos no pueden ser forzadamente retirados de los hilos que los están reteniendo. Solo pueden ser liberados voluntariamente por el hilo que los tiene.
    Espera Circular (Circular Wait): Existe un conjunto de hilos {T1, T2, ..., Tn} tal que T1 espera un recurso que posee T2, T2 espera un recurso que posee T3, y así sucesivamente, hasta que Tn espera un recurso que posee T1.

Escenario Teórico de Livelocks en un Sistema de Manejo de Base de Datos

Un livelock es una situación en la que dos o más hilos están activamente cambiando su estado o realizando operaciones, pero ninguno de ellos hace un progreso real hacia la finalización de sus tareas.
Escenario Teórico:

Imaginemos un sistema de base de datos donde dos transacciones intentan acceder a los mismos registros de datos:

    Transacción A intenta actualizar Registro X y luego Registro Y.
    Transacción B intenta actualizar Registro Y y luego Registro X.

Para evitar un deadlock, ambas transacciones tienen un mecanismo para liberar los recursos y reintentarlo si no pueden obtener todos
los recursos que necesitan.

Transacción A          Transacción B
----------------       ----------------
Adquiere Registro X    Adquiere Registro Y
No puede adquirir Y    No puede adquirir X
Libera Registro X      Libera Registro Y
Reintenta              Reintenta

Ambas transacciones continúan intentando y liberando los recursos sin hacer progreso, creando un livelock.
Prevención de Livelocks:

    Backoff Aleatorio: Implementar un tiempo de espera aleatorio antes de reintentar adquirir los recursos.
    Prioridad: Asignar prioridades a las transacciones para que una transacción tenga más oportunidades de completar su tarea.
    Tiempo de Espera Máximo: Establecer un tiempo máximo de espera después del cual una transacción aborta y reintenta.


¿Por Qué Son Problemáticas las Condiciones de Carrera y Qué Estrategias Podrían Utilizarse para Evitarlas?

Las condiciones de carrera ocurren cuando el resultado de 
un programa depende del orden no determinístico en que se ejecutan las
instrucciones de los hilos. Son problemáticas porque pueden causar
comportamientos inesperados y difíciles de reproducir, introduciendo errores
sutiles en el software.

  Thread A            Thread B
-----------         -----------
Read Counter = 0    Read Counter = 0
Increment           Increment
Write Counter = 1   Write Counter = 1

Ambos hilos leen el valor inicial 0, lo incrementan a 1 y lo escriben, perdiendo uno de los incrementos.
Estrategias para Evitar Condiciones de Carrera:

    Bloqueos y Sincronización: Utilizar mutexes, semáforos y otros mecanismos de sincronización para controlar el acceso a recursos compartidos.
    Variables Atómicas: Usar operaciones atómicas que aseguren que las actualizaciones a las variables compartidas sean indivisibles.
    Diseño Consciente de la Concurrencia: Diseñar el software de manera que minimice la necesidad de acceso concurrente a recursos compartidos. Utilizar modelos claros de propiedad y transferencia de recursos.
    Evitar Datos Compartidos: Siempre que sea posible, evitar el uso de datos compartidos entre hilos. Usar estructuras de datos inmutables o locales a cada hilo.
'''
##  1 . Simule un escenario simple de deadlock y luego resolverlo.

  import threading

# Recursos
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print("Hilo 1: ha adquirido lock1")
        with lock2:
            print("Hilo 1: ha adquirido lock2")

def thread2():
    with lock1:
        print("Hilo 2: ha adquirido lock1")
        with lock2:
            print("Hilo 2: ha adquirido lock2")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()

##2 . Demostrar una condición de carrera y aplicar una solución.

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

def decrement():
    global counter
    for _ in range(100000):
        with lock:
            counter -= 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

t1.start()
t2.start()

t1.join()
t2.join()

print("Valor final del contador:", counter)
''' Cada hilo debe adquirir el lock antes de modificar counter, y 
lo libera después de la modificación. Esto asegura que solo un hilo pueda 
modificar counter a la vez, eliminando la condición de carrera.''
