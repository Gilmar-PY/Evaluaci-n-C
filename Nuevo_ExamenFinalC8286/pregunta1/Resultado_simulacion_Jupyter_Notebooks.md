#### Resultado 
      INFO:__main__:Evento agregado: execute - Celda 1 con prioridad 2
      INFO:__main__:Evento agregado: execute - Celda 2 con prioridad 1
      INFO:__main__:Evento agregado: execute - Celda 3 con prioridad 3
      INFO:__main__:Ejecutando celda: Celda 2
      INFO:__main__:Celda Celda 2 ejecutada con éxito
      INFO:__main__:Ejecutando celda: Celda 1
      INFO:__main__:Celda Celda 1 ejecutada con éxito
      INFO:__main__:Ejecutando celda: Celda 3
      INFO:__main__:Celda Celda 3 ejecutada con éxito

#### Interpretación del Resultado

La salida muestra un conjunto de eventos que han sido agregados a un sistema de procesamiento basado en prioridades, y luego ejecutados en el orden correcto. A continuación, desglosamos la interpretación de cada parte de la salida:

Eventos Agregados con Prioridad

     
    INFO:__main__:Evento agregado: execute - Celda 1 con prioridad 2
    INFO:__main__:Evento agregado: execute - Celda 2 con prioridad 1
    INFO:__main__:Evento agregado: execute - Celda 3 con prioridad 3

#### Interpretación:
Aquí se observa que tres eventos han sido agregados al sistema, cada uno con una prioridad distinta.
Celda 1 tiene prioridad 2, Celda 2 tiene prioridad 1, y Celda 3 tiene prioridad 3.

En un sistema de prioridades, los eventos con menor valor de prioridad (en este caso, la prioridad 1 es mayor que la prioridad 2 y así sucesivamente) deben ejecutarse primero.

Ejecución de las Celdas según su Prioridad
    
    INFO:__main__:Ejecutando celda: Celda 2
    INFO:__main__:Celda Celda 2 ejecutada con éxito
    INFO:__main__:Ejecutando celda: Celda 1
    INFO:__main__:Celda Celda 1 ejecutada con éxito
    INFO:__main__:Ejecutando celda: Celda 3
    INFO:__main__:Celda Celda 3 ejecutada con éxito
    
Interpretación:
Las celdas se están ejecutando en el orden de sus prioridades.
Celda 2, con prioridad 1, es la primera en ejecutarse.
Celda 1, con prioridad 2, se ejecuta después.
Finalmente, Celda 3, con prioridad 3, se ejecuta al final.
Cada celda, una vez ejecutada, registra un mensaje de éxito indicando que se ha completado correctamente.


