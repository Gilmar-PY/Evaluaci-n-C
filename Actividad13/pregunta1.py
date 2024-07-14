'''
Ejercicio 1: Explica el proceso de consenso de Paxos

Proceso de Consenso de Paxos

Paxos es un algoritmo de consenso distribuido diseñado para alcanzar un acuerdo sobre un valor entre un conjunto de nodos en un sistema distribuido. El algoritmo es resistente a fallos y garantiza la consistencia, incluso en presencia de fallos de nodos y mensajes retrasados.
Fases de Paxos

    Fase de Preparación (Prepare Phase):
        Un proposer selecciona un número de propuesta único y lo envía a un conjunto de acceptors.
        Los acceptors comparan el número de propuesta con los números de propuestas anteriores que han visto y responden con:
            La promesa de no aceptar ninguna propuesta con un número inferior al número recibido.
            La respuesta incluye la mayor propuesta que ya han aceptado (si hay alguna).

    Fase de Aceptación (Accept Phase):
        Si un proposer recibe respuestas de una mayoría de acceptors, envía una propuesta con el valor que ha recibido más recientemente y el número de propuesta.
        Los acceptors aceptan la propuesta si no han prometido aceptar ninguna propuesta con un número mayor.
        Una vez que un acceptor acepta una propuesta, envía una confirmación al proposer.

    Fase de Aprendizaje (Learn Phase):
        Si un proposer recibe confirmaciones de una mayoría de acceptors, el valor propuesto se considera acordado.
        Los learners, que son nodos que necesitan conocer el valor acordado, son notificados del consenso alcanzado.

Interacción entre Proposers, Acceptors y Learners

    Proposers: Generan propuestas y las envían a los acceptors.
    Acceptors: Reciben propuestas y deciden si las aceptan o no basándose en las reglas de Paxos.
    Learners: Aprenden el valor acordado una vez que se ha alcanzado el consenso.

Ejercicio 2: Análisis de las ventajas y desventajas de Paxos en un entorno distribuido con alta latencia de red

Ventajas de Paxos:

    Consistencia: Paxos garantiza que todos los nodos acuerden el mismo valor.
    Tolerancia a fallos: Puede funcionar correctamente incluso si algunos nodos fallan.
    Resiliencia a particiones de red: Puede seguir funcionando en presencia de particiones de red.

Desventajas de Paxos:

    Complejidad: Es un algoritmo complejo de implementar y entender.
    Latencia: Requiere múltiples rondas de comunicación, lo que puede ser ineficiente en redes con alta latencia.
    Overhead de Mensajes: La necesidad de múltiples mensajes entre proposers y acceptors aumenta el overhead en la red.

Impacto de la Latencia:

    La alta latencia en la red puede ralentizar significativamente el proceso de consenso, ya que cada fase de Paxos requiere comunicación entre nodos.
    La eficiencia del algoritmo se ve afectada, aumentando el tiempo necesario para alcanzar el consenso.

    '''

