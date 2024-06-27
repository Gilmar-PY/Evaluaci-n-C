# Reporte del Sprint 1

## Introducción
Este informe documenta el progreso del Sprint 1 del proyecto "Sistema de almacenamiento distribuido seguro".

## Objetivos del Sprint 1
- Investigar técnicas de almacenamiento distribuido y criptografía.
- Configurar un entorno distribuido con múltiples nodos utilizando Docker.
- Implementar un sistema básico de almacenamiento de archivos.

#### Alcance del Sprint 1:

En este primer sprint, está enfocada en la investigación y configuración inicial del sistema. Los objetivos específicos incluyen investigar técnicas de almacenamiento distribuido y criptografía, donde se  configura un entorno distribuido con múltiples nodos utilizando Docker, e implementar un sistema básico de almacenamiento de archivos. Estos pasos sentarán las bases para los sprints siguientes, donde se añadirán capas adicionales de seguridad y replicación de datos.

#### Técnicas de Almacenamiento Distribuido

#### HDFS (Hadoop Distributed File System)

HDFS es un sistema de archivos distribuido diseñado para ejecutarse en hardware común y soportar grandes volúmenes de datos. Está compuesto por un NameNode, que gestiona la metadata del sistema de archivos, y múltiples DataNodes, que almacenan los datos reales.

Características:

Alta tolerancia a fallos: HDFS divide los archivos en bloques y los replica en múltiples nodos, lo que permite la recuperación de datos en caso de fallos de hardware.

Alta disponibilidad: Gracias a la replicación de datos, HDFS asegura que los datos estén disponibles incluso si uno o más nodos fallan.

Escalabilidad: HDFS puede manejar eficientemente grandes cantidades de datos distribuidos en muchos nodos.

Ventajas.-Eficiencia en el manejo de grandes volúmenes de datos,robustez ante fallos de hardware.

Desventajas.-Complejidad en la administración y configuración,latencia en la escritura de datos.

#### Ceph

Ceph es una plataforma de almacenamiento distribuido que ofrece almacenamiento de objetos, bloques y archivos en un único clúster unificado. Es conocido por su escalabilidad y resiliencia.

Características:

a.-Escalabilidad horizontal: Permite agregar más nodos al clúster para aumentar la capacidad y el rendimiento.

b.-Alta disponibilidad y resiliencia: Ceph tiene mecanismos de auto-recuperación que garantizan la disponibilidad continua de los datos.

c.-Flexibilidad: Soporte para almacenamiento de objetos, bloques y archivos en el mismo clúster.

Ventajas:

b.-Escalabilidad y flexibilidad para adaptarse a diferentes necesidades de almacenamiento.

a.-Recuperación automática de datos en caso de fallos.

  

Desventajas:

a.-Requiere una configuración y mantenimiento complejos.

b.-Alta demanda de recursos de hardware.

Bibliotecas de Criptografía en Python

#### PyCryptodome

PyCryptodome es una biblioteca de criptografía en Python que proporciona una amplia gama de funcionalidades criptográficas, incluyendo cifrado y descifrado de datos.

Características:

Cifrado simétrico: Soporte para algoritmos como AES, DES y 3DES.

Cifrado asimétrico: Soporte para RSA, DSA y ECC.

Hashing: Soporte para algoritmos de hashing como SHA y MD5.

Ventajas:

a.-Amplia gama de algoritmos y funcionalidades.

b.-Fácil de usar e integrar en proyectos Python.

Desventajas:

Puede ser menos eficiente en términos de rendimiento comparado con bibliotecas nativas.


#### 2.-cryptography

Cryptography es una biblioteca que proporciona herramientas criptográficas para desarrolladores en Python. Es conocida por su facilidad de uso y documentación extensiva.

Características:

- a.-Cifrado simétrico y asimétrico: Soporte para AES, RSA, DSA y más.

- b.-Hashing: Soporte para algoritmos como SHA-256 y SHA-512.

- c.-Protocolos: Soporte para TLS/SSL, Fernet, etc.

Ventajas:

- Interfaz moderna y fácil de usar.

- bien mantenida y documentada.

Desventajas:

- en un comienzo puede ser compleja en comparación con PyCryptodome.


#### Configuración del Entorno Distribuido con Docker


## Progreso y Logros
- **Investigación**: Se investigaron HDFS y Ceph para almacenamiento distribuido y se exploraron las bibliotecas pycryptodome y cryptography para criptografía.
- **Configuración del Entorno con Docker**: Se configuraron nodos Docker y se crearon imágenes personalizadas.
- **Implementación del Sistema de Almacenamiento**: Se desarrolló una API RESTful para cargar, descargar y eliminar archivos, incluyendo funcionalidad de cifrado.



# Conclusiones y Siguientes Pasos

## Logros del Sprint 1

- Configuración del entorno distribuido con Docker.
- Implementación de un sistema básico de almacenamiento de archivos.
- Creación de una API RESTful para interactuar con el sistema de almacenamiento.

## Desafíos Encontrados

- Configuración Inicial de Docker: Superado mediante la creación de Dockerfiles detallados.
- Cifrado y Descifrado de Archivos: Implementado con éxito utilizando la biblioteca pycryptodome.

## Próximos Pasos para el Sprint 2

- Implementar cifrado de datos utilizando bibliotecas de criptografía.
- Desarrollar técnicas de replicación de datos para garantizar la disponibilidad.
- Mejorar la sincronización entre nodos utilizando `asyncio` y threading.



