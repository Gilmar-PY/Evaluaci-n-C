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
Construcción de la imagen Docker:

docker build -t storage-system .

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfXaW8o3BQJcakM_856YcE-HweiDjL-h0qqMIEM2Mf_qkIcsmUlMC8n8aUf_Q96VkOY-hkXc5GlyNjc3xLf6ax1D4JUjC7dp-dFhAg4mXq5deq-QwLWKuYxZQJXbcpJaO2SnDrP_FtwkjofeDWb19T-i_dR?key=nQL0RT6dNr_BeWtx8fgyhA)
creacion de la rede de docker 👍

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcFUJtLOgDyr8kynCaT4_IaZyaDlJwFYT4KAk0QlFx70JAq8AgzclNtTlpqJJhdysUSH8foS5vrJkbwib08UGeR6nFouBbIbz4-W9kS2igRwign-rz59GGSSuqA5a0mw-YQiFffh-762dvNmOdvGlPLv0ec?key=nQL0RT6dNr_BeWtx8fgyhA)
  

Ejecución del contenedor:

docker run -d --name storage-node-1 -p 5000:5000 storage-system

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXf0mXs_4STvIK96ppUBUEYfTdGkBwDRkN8-NyJmsklj0p69RYwY7NytwsjdjTPaTn3cm9c1QV6hwTRCo2p6kXx3VrsFM3uZ_qO32zQk9IBrn7W4js7FynCYVrmaRPdr87Rn85HHSab1zmC7Lv4smrb9qX6F?key=nQL0RT6dNr_BeWtx8fgyhA)

  

Carga del archivo:

curl -X POST -F 'archivo=@Algoritmos.txt' http://localhost:5000/cargar

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfM9ERn_0F1Pdb9kwcsKKfrnqLnM3Zo_-6poAfMklqNLlC8kQ1NvIfCGEi0-yY40xcuRpTWFwoFVtKMsQSHvJ5J5Qvg2KMqbcT-v3PIPpdXy1vF1OvNIuT_dqf9_Uig5dli1xkNm7fvZr18YT0aP2Aqhxq7?key=nQL0RT6dNr_BeWtx8fgyhA)

  

Descarga del archivo:

curl -O http://localhost:5000/descargar/Algoritmos.txt

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdGAG0ER6au7T54brjCCX9DvH6rJAYNYl-am1iG5gZCsQ7eUsR_jXaT-d9mZWKICv7EOS6SAqAf9fxkXqfMeD_D9Iac0p7WwGZC3v5yRxWIur2egN5RiJ3YNybW2_FJeED3IxxqdsKJ_OEq_7ncPGX3vdjg?key=nQL0RT6dNr_BeWtx8fgyhA)

  

Eliminación del archivo:

curl -X DELETE [http://localhost:5000/eliminar/Algoritmos.txt](http://localhost:5000/eliminar/Algoritmos.txt)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfJe_BFkGEErGCUSYLVC2uFutjSq16aviU7Kymth_x4BbMzYll6I3rwKlkPqTVq4tfvsQyXhDWp6ZIZ4EYxbSHVSV6jSEJfI-_lv1Eul7CKnB4nwjQVPRCeG3o8m37NCrt-SN5MTRFe4Rv-fQJXaTcNFrzl?key=nQL0RT6dNr_BeWtx8fgyhA)

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXei9uToL_d6WYSqj30Z4LcCVV8vbhaXvHdshGCu2vzUkxK9YtGUPDFKoNWWAwK7Vb_S-cR1gWwlMcIdFlSo8cHW1LsHKwIyKtJHlub5r5-aP4vUBtEjR3fvYZvDcibcoxkWJwJOnIGcIfzC-uXPS1rkAI4f?key=nQL0RT6dNr_BeWtx8fgyhA)

  
  
  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeHILW4uVywubaztQsphUjy2-OeQxCjjl7X5u09N5svH2ImkMZ3aBLbFHmAwAx5dPytiSkvjSQK_0GdjhRk7d1_IivradVi5UI8w0HqFlMcj2df61W-PfzPVtxVSYRRcM3iK_4u3NHy9hfQY0WwKQbbeDI?key=nQL0RT6dNr_BeWtx8fgyhA)

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



