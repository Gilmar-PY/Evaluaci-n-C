### Salida completa:

    INFO:__main__:Network started
    INFO:__main__:Node 1 received message from Node 0: SYNC
    INFO:__main__:Proceso 0 envió un mensaje a 1
    INFO:__main__:Node 0 sent message to Node 1: SYNC
    INFO:__main__:Node 2 received message from Node 0: SYNC
    INFO:__main__:Proceso 0 envió un mensaje a 2
    INFO:__main__:Node 0 sent message to Node 2: SYNC
    INFO:__main__:Node 3 received message from Node 0: SYNC
    INFO:__main__:Proceso 0 envió un mensaje a 3
    INFO:__main__:Node 0 sent message to Node 3: SYNC
    INFO:__main__:Node 4 received message from Node 0: SYNC
    INFO:__main__:Proceso 0 envió un mensaje a 4
    INFO:__main__:Node 0 sent message to Node 4: SYNC
    INFO:__main__:Node 0 synchronized clock
    INFO:__main__:Node 0 received message from Node 1: SYNC
    INFO:__main__:Proceso 1 envió un mensaje a 0
    INFO:__main__:Node 1 sent message to Node 0: SYNC
    INFO:__main__:Node 2 received message from Node 1: SYNC
    INFO:__main__:Proceso 1 envió un mensaje a 2
    INFO:__main__:Node 1 sent message to Node 2: SYNC
    INFO:__main__:Node 3 received message from Node 1: SYNC
    INFO:__main__:Proceso 1 envió un mensaje a 3
    INFO:__main__:Node 1 sent message to Node 3: SYNC
    INFO:__main__:Node 4 received message from Node 1: SYNC
    INFO:__main__:Proceso 1 envió un mensaje a 4
    INFO:__main__:Node 1 sent message to Node 4: SYNC
    INFO:__main__:Node 1 synchronized clock
    INFO:__main__:Node 0 received message from Node 2: SYNC
    INFO:__main__:Proceso 3 reportó terminación a 1
    INFO:__main__:Proceso 2 envió un mensaje a 0
    INFO:__main__:Proceso 4 reportó terminación a 1
    INFO:__main__:Proceso 3 marcado como inactivo
    INFO:__main__:Node 2 sent message to Node 0: SYNC
    INFO:__main__:Proceso 4 marcado como inactivo
    INFO:__main__:Node 1 received message from Node 2: SYNC
    INFO:__main__:Proceso 2 envió un mensaje a 1
    INFO:__main__:Node 2 sent message to Node 1: SYNC
    INFO:__main__:Node 3 received message from Node 2: SYNC
    INFO:__main__:Proceso 2 envió un mensaje a 3
    INFO:__main__:Node 2 sent message to Node 3: SYNC
    INFO:__main__:Node 4 received message from Node 2: SYNC
    INFO:__main__:Proceso 2 envió un mensaje a 4
    INFO:__main__:Node 2 sent message to Node 4: SYNC
    INFO:__main__:Node 2 synchronized clock
    INFO:__main__:Node 0 received message from Node 3: SYNC
    INFO:__main__:Proceso 3 envió un mensaje a 0
    INFO:__main__:Node 3 sent message to Node 0: SYNC
    INFO:__main__:Node 1 received message from Node 3: SYNC
    INFO:__main__:Proceso 3 envió un mensaje a 1
    INFO:__main__:Node 3 sent message to Node 1: SYNC
    INFO:__main__:Node 2 received message from Node 3: SYNC
    INFO:__main__:Proceso 3 envió un mensaje a 2
    INFO:__main__:Node 3 sent message to Node 2: SYNC
    INFO:__main__:Node 4 received message from Node 3: SYNC
    INFO:__main__:Proceso 3 envió un mensaje a 4
    INFO:__main__:Node 3 sent message to Node 4: SYNC
    INFO:__main__:Node 3 synchronized clock
    INFO:__main__:Node 0 received message from Node 4: SYNC
    INFO:__main__:Proceso 4 envió un mensaje a 0
    INFO:__main__:Node 4 sent message to Node 0: SYNC
    INFO:__main__:Node 1 received message from Node 4: SYNC
    INFO:__main__:Proceso 4 envió un mensaje a 1
    INFO:__main__:Node 4 sent message to Node 1: SYNC
    INFO:__main__:Node 2 received message from Node 4: SYNC
    INFO:__main__:Proceso 4 envió un mensaje a 2
    INFO:__main__:Node 4 sent message to Node 2: SYNC
    INFO:__main__:Node 3 received message from Node 4: SYNC
    INFO:__main__:Proceso 4 envió un mensaje a 3
    INFO:__main__:Node 4 sent message to Node 3: SYNC
    INFO:__main__:Node 4 synchronized clock
    INFO:__main__:All clocks synchronized
    INFO:__main__:Node 1 received message from Node 0: REQUEST
    INFO:__main__:Proceso 0 envió un mensaje a 1
    INFO:__main__:Node 0 sent message to Node 1: REQUEST
    INFO:__main__:Node 2 received message from Node 0: REQUEST
    INFO:__main__:Proceso 0 envió un mensaje a 2
    INFO:__main__:Node 0 sent message to Node 2: REQUEST
    INFO:__main__:Node 3 received message from Node 0: REQUEST
    INFO:__main__:Proceso 0 envió un mensaje a 3
    INFO:__main__:Node 0 sent message to Node 3: REQUEST
    INFO:__main__:Node 4 received message from Node 0: REQUEST
    INFO:__main__:Proceso 0 envió un mensaje a 4
    INFO:__main__:Node 0 sent message to Node 4: REQUEST
    INFO:__main__:Node 0 sent REQUEST to all neighbors
    INFO:__main__:Node 0 received message from Node 4: REPLY
    INFO:__main__:Proceso 4 envió un mensaje a 0
    INFO:__main__:Node 4 sent message to Node 0: REPLY
    INFO:__main__:Node 0 received message from Node 3: REPLY
    INFO:__main__:Proceso 3 envió un mensaje a 0
    INFO:__main__:Node 3 sent message to Node 0: REPLY
    INFO:__main__:Node 0 received message from Node 2: REPLY
    INFO:__main__:Proceso 2 envió un mensaje a 0
    INFO:__main__:Node 2 sent message to Node 0: REPLY
    INFO:__main__:Node 0 received message from Node 1: REPLY
    INFO:__main__:Proceso 1 envió un mensaje a 0
    INFO:__main__:Node 1 sent message to Node 0: REPLY
    INFO:__main__:Node 0 received REPLY, replies needed: 3
    INFO:__main__:Node 0 received REPLY, replies needed: 2
    INFO:__main__:Node 0 received REPLY, replies needed: 1
    INFO:__main__:Node 0 received REPLY, replies needed: 0
    INFO:__main__:Node 0 entering critical section
    INFO:__main__:Node 0 received message from Node 1: REQUEST
    INFO:__main__:Proceso 1 envió un mensaje a 0
    INFO:__main__:Node 1 sent message to Node 0: REQUEST
    INFO:__main__:Node 2 received message from Node 1: REQUEST
    INFO:__main__:Proceso 1 envió un mensaje a 2
    INFO:__main__:Node 1 sent message to Node 2: REQUEST
    INFO:__main__:Node 3 received message from Node 1: REQUEST
    INFO:__main__:Proceso 1 envió un mensaje a 3
    INFO:__main__:Node 1 sent message to Node 3: REQUEST
    INFO:__main__:Node 4 received message from Node 1: REQUEST
    INFO:__main__:Proceso 1 envió un mensaje a 4
    INFO:__main__:Node 1 sent message to Node 4: REQUEST
    INFO:__main__:Node 1 sent REQUEST to all neighbors
    INFO:__main__:Node 1 received message from Node 2: REPLY
    INFO:__main__:Proceso 2 envió un mensaje a 1
    INFO:__main__:Node 2 sent message to Node 1: REPLY
    INFO:__main__:Node 1 received message from Node 3: REPLY
    INFO:__main__:Proceso 3 envió un mensaje a 1
    INFO:__main__:Node 3 sent message to Node 1: REPLY
    INFO:__main__:Node 1 received message from Node 4: REPLY
    INFO:__main__:Proceso 4 envió un mensaje a 1
    INFO:__main__:Node 4 sent message to Node 1: REPLY
    INFO:__main__:Node 1 received REPLY, replies needed: 3
    INFO:__main__:Node 1 received REPLY, replies needed: 2
    INFO:__main__:Node 1 received REPLY, replies needed: 1




Inicio de la red:

    INFO:__main__:Network started

inicio de red y todos los nodos están operativos.

#### Sincronización de relojes:

    INFO:__main__:Node 0 sent message to Node 1: SYNC
    INFO:__main__:Node 1 sent message to Node 2: SYNC
    ...
    INFO:__main__:Node 4 synchronized clock
    INFO:__main__:All clocks synchronized

Cada nodo envía mensajes de sincronización (SYNC) a todos los demás nodos, y los nodos ajustan sus relojes en función de los mensajes recibidos. Finalmente, se confirma que todos los relojes están sincronizados.

#### Solicitud de acceso a la sección crítica (Algoritmo de Ricart-Agrawala):

    INFO:__main__:Node 0 sent REQUEST to all neighbors
    INFO:__main__:Node 0 received REPLY, replies needed: 3
    INFO:__main__:Node 0 received REPLY, replies needed: 2
    INFO:__main__:Node 0 received REPLY, replies needed: 1
    INFO:__main__:Node 0 received REPLY, replies needed: 0
    INFO:__main__:Node 0 entering critical section

El nodo 0 envía una solicitud (REQUEST) a todos sus vecinos y espera respuestas (REPLY). Una vez que recibe todas las respuestas necesarias, entra en la sección crítica.

#### Solicitud de acceso a la sección crítica por otro nodo (Nodo 1):

    INFO:__main__:Node 1 sent REQUEST to all neighbors
    INFO:__main__:Node 1 received REPLY, replies needed: 3
    INFO:__main__:Node 1 received REPLY, replies needed: 2
    INFO:__main__:Node 1 received REPLY, replies needed: 1

El nodo 1 también envía una solicitud de acceso a la sección crítica y comienza a recibir respuestas de sus vecinos.


#### Detección de terminación de procesos distribuidos (Algoritmo de Dijkstra-Scholten):

    INFO:__main__:Proceso 3 reportó terminación a 1
    INFO:__main__:Proceso 4 reportó terminación a 1
    INFO:__main__:Proceso 3 marcado como inactivo
    INFO:__main__:Proceso 4 marcado como inactivo

Los procesos 3 y 4 reportan su terminación al proceso 1 y son marcados como inactivos. Este es el mecanismo mediante el cual se detecta la terminación de procesos distribuidos.

Mensajes generales de comunicación:

    INFO:__main__:Proceso 0 envió un mensaje a 1
    INFO:__main__:Proceso 2 envió un mensaje a 3
   


