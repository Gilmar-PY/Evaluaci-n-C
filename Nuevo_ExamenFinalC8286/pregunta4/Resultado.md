
### 1. Elección del Líder

Durante la ejecución, varios nodos se convierten en líderes. Aquí hay algunas líneas que indican este comportamiento:
  
    Node 2 has become the leader
    Node 1 has become the leader
    Node 3 has become the leader
    Node 0 has become the leader
    Node 4 has become the leader

  
Cada vez que un nodo se convierte en líder, se asegura de que haya un líder activo en el sistema. Esto es fundamental para la consistencia, ya que el líder es responsable de replicar los datos en los nodos seguidores.
La frecuencia con la que los líderes cambian puede indicar la estabilidad del sistema o la cantidad de fallos simulados. Si los líderes cambian frecuentemente, podría significar que los nodos líderes fallan o que hay particiones en la red que desencadenan nuevas elecciones de líder.

 #### Adición de Entradas al Log

Durante la simulación, los nodos líderes añaden entradas al log, lo cual se refleja en líneas como las siguientes:
  
      Node 0 appended entry: {'key': 'y', 'value': 18}
      Node 1 appended entry: {'key': 'z', 'value': 34}
      Node 4 appended entry: {'key': 'y', 'value': 73}
  
#### Interpretación:
Los líderes están realizando operaciones y replicando estos cambios en los nodos seguidores. Cada entrada indica una operación de escritura que se está propagando a través del clúster.
Esto demuestra la consistencia del sistema, ya que las operaciones de los líderes se reflejan en los nodos seguidores, garantizando que todos los nodos tengan la misma información.

3. Fallos y Recuperaciones de Nodos

La simulación incluye fallos y recuperaciones de nodos:
  
      Node 2 has failed.
      Node 3 has healed.
      Node 1 has failed.
      Node 1 has healed.

### Interpretación:
Estos mensajes simulan fallos de red y la recuperación de nodos. La capacidad de los nodos para fallar y recuperarse demuestra la tolerancia a particiones del sistema.
tambien cuando los nodos fallan, otros nodos pueden asumir el rol de líder y continuar operando, lo que demuestra la disponibilidad del sistema. La recuperación de nodos permite que el sistema vuelva a su estado normal después de una partición o fallo.

#### Consistencia y Replicación de Datos

Cada vez que un nodo líder añade una entrada al log, lo cual asegura de que los datos sean replicados en los nodos seguidores:
    
      Node 0 appended entry: {'key': 'z', 'value': 23}
      Node 1 appended entry: {'key': 'x', 'value': 30}
      Node 4 appended entry: {'key': 'y', 'value': 73}

### Interpretación:
La replicación de datos asegura que todos los nodos tengan una visión consistente del estado del sistema. Esto es crítico para mantener la consistencia en un sistema distribuido.
La replicación de entradas al log garantiza que, incluso si un líder falla, el nuevo líder elegido puede continuar desde el último estado conocido sin perder datos.

### 5. Finalización de la Simulación
Simulation complete. Stopping all nodes.
