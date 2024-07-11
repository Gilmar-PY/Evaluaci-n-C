'''

Describe las fases del algoritmo Raft: elección de líder, replicación de log y 
aplicación de entradas.
¿Cómo garantiza Raft la consistencia del log replicado entre los seguidores?'''
----------------------------------------------------------------------------------------------
'''
Ejercicio 5: Descripción de las fases del algoritmo Raft

Fases del Algoritmo Raft

    Elección de Líder (Leader Election):
        Los nodos comienzan como seguidores (followers).
        Si un follower no recibe mensajes del líder durante un tiempo, se convierte en candidato (candidate) e inicia una elección.
        Los candidatos envían solicitudes de voto (RequestVote) a otros nodos.
        Los nodos votan por el primer candidato que recibe su solicitud de voto.
        Si un candidato recibe votos de la mayoría de los nodos, se convierte en líder (leader).

    Replicación de Log (Log Replication):
        El líder envía entradas de log (log entries) a los seguidores para replicarlas.
        Los seguidores responden con confirmaciones.
        Una vez que la mayoría de los seguidores confirman la replicación, la entrada se considera comprometida (committed).

    Aplicación de Entradas (Log Application):
        Las entradas comprometidas se aplican a la máquina de estado (state machine) del líder.
        El líder notifica a los seguidores para que también apliquen las entradas comprometidas a sus máquinas de estado.

Garantías de Consistencia de Raft:

    Raft garantiza que una entrada de log comprometida en un nodo también está comprometida en todos los demás nodos.
    Los líderes siempre tienen logs consistentes, asegurando que los seguidores mantengan logs consistentes también.
-----------------------------------------------------------------------------------------------------------------------------
Compara y contrasta Paxos y Raft en términos de simplicidad, eficiencia y capacidad de
recuperación ante fallos.¿Por qué podría ser preferible usar Raft en ciertas aplicaciones?

Ejercicio 6: Comparación entre Paxos y Raft

Simplicidad:

    Raft: Diseñado para ser más fácil de entender e implementar que Paxos.
    Paxos: Considerado más complejo y difícil de implementar correctamente.

Eficiencia:

    Raft: Divide claramente las fases de elección de líder y replicación de log, mejorando la eficiencia en entornos prácticos.
    Paxos: Puede ser menos eficiente debido a su complejidad y la necesidad de múltiples rondas de comunicación.

Capacidad de Recuperación ante Fallos:

    Raft: Maneja fallos de líderes y nodos de manera eficiente, con una clara estrategia de elección de líder.
    Paxos: También es tolerante a fallos, pero su complejidad puede dificultar su implementación en algunos casos.

Preferencia de Uso:

    Raft: Preferido en aplicaciones donde la simplicidad y la claridad de implementación son críticas.
    Paxos: Usado en situaciones donde se requiere un enfoque más teórico y riguroso para el consenso distribuido.
