<!-- CARÁTULA -->
**C8286-20241 - COMPUTACIÓN PARALELA Y DISTRIBUIDA**

![Image](https://lh7-us.googleusercontent.com/docsz/AD_4nXfrF5z2SZXfh0QVGOUAUsQIRgev3J93RP_tghpuiExazSEneb_iP3RK1A9x0MlTeqOylm_7txn9c7yhX-cdXED7Qj6CJ-ThAPvAmDHeSp4Sj8d4Hbxv-oSuYOV85ldqw57AVVIZzToar2gCcXNett_2C1V1?key=CgRdnKUJcB5u-lHC6I5GQg)

#### PROYECTO FINAL:

#### SISTEMA DE ALMACENAMIENTO DISTRIBUIDO SEGURO

#### NOMBRE:

#### GILMAR RONY OVIEDO CHAHUA

#### PROFESOR:

#### CESAR JESUS LARA AVILA

#### CURSO:

#### COMPUTACIÓN PARALELA Y DISTRIBUIDA

---

<!-- FIN DE LA CARÁTULA -->



<!-- ÍNDICE -->
#### Índice

- [Sprint 1](#sprint-1)
  - [Introducción](#introducción)
    - [Objetivo del proyecto](#objetivo-del-proyecto)
    - [Alcance del Sprint 1](#alcance-del-sprint-1)
  - [Investigación](#investigación)
    - [Técnicas de Almacenamiento Distribuido](#técnicas-de-almacenamiento-distribuido)
    - [Bibliotecas de Criptografía en Python](#bibliotecas-de-criptografía-en-python)
  - [Configuración del Entorno Distribuido](#configuración-del-entorno-distribuido)
    - [Instalación y Configuración de Docker](#instalación-y-configuración-de-docker)
    - [Creación de Imágenes Docker Personalizadas](#creación-de-imágenes-docker-personalizadas)
  - [Implementación del Sistema de Almacenamiento](#implementación-del-sistema-de-almacenamiento)
    - [Sistema Básico de Almacenamiento de Archivos](#sistema-básico-de-almacenamiento-de-archivos)
    - [API RESTful](#api-restful)
    - [Comunicación entre Nodos](#comunicación-entre-nodos)
- [Sprint 2](#sprint-2)
- [Sprint 3](#sprint-3)

---

<!-- FIN DEL ÍNDICE -->





#### Introducción:

  

#### Objetivo del Proyecto:

El objetivo general del proyecto es desarrollar un sistema de almacenamiento distribuido que asegure la disponibilidad y la seguridad de los datos mediante técnicas de criptografía y replicación, optimizado para funcionar en un entorno de múltiples nodos. Esto garantizará que los datos estén siempre accesibles y protegidos contra accesos no autorizados, incluso en caso de fallos en algunos de los nodos del sistema.

  

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

a.-Cifrado simétrico y asimétrico: Soporte para AES, RSA, DSA y más.

b.-Hashing: Soporte para algoritmos como SHA-256 y SHA-512.

c.-Protocolos: Soporte para TLS/SSL, Fernet, etc.

Ventajas:

Interfaz moderna y fácil de usar.

bien mantenida y documentada.

Desventajas:

en un comienzo puede ser compleja en comparación con PyCryptodome.

  
  
  

#### Configuración del Entorno Distribuido con Docker

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcUNtySyNTXL_FyHkCofQxiKKi4kSnXyPp5-t9y0As2xX7h7HimrShISDPmoQSVi4YGEGBza4mazqT1PMNbpwS-LNj-cE0abYfW2czthuSendFkDZY6LWrh8BphW5kFMQk3K6e0cqOBzaa44AiDsHHMFKc?key=CgRdnKUJcB5u-lHC6I5GQg)

#### Paso 3: Construir y Ejecutar la Imagen Docker

Construir la imagen Docker


![](https://lh7-us.googleusercontent.com/docsz/AD_4nXc4cYIPb4HDTGgzdD9aPuOEduvR2QP9tIYPFVDW84SxkuoeS-Z9iVs34O3wJS1xvtjhTw1KwehxMNFhyKo1Z2640fSSAW5nc8L_BvhtNU4D6X9cJMINmShtCPCUktI7bx8dcBVl4m9y5ZTMPjzgHWrfXILF?key=CgRdnKUJcB5u-lHC6I5GQg)




![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeE-Dkct0nAY07TCss0rN8kH2E57GlAS9HHsOxD-qkin-nDhwG0nAZF65ejEVeVlX6B4dGKfpgzBgtOgp8Yyrv_1zJhWxpURsrxSvtEwomn2ESJizcEpDm8-32gmIrFTboVDhV85KHD6Lb4t80K2w0dImiT?key=CgRdnKUJcB5u-lHC6I5GQg)

Ejecutar el contenedor Docker

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXckv8hJDx-8X90ObYr-W4Ve_quto7m2BV7D0siBAnibFpCfOhCU07VSRESrYI4bjWw1a9rjotlTPl0iMzNC708xOKOhAdTP8ZjQ789pFuLPu3RL7D8bXGTbqqQGtpjVEvvl9JKUwryYQ-qZvYELcgeTCz0?key=CgRdnKUJcB5u-lHC6I5GQg)

#### Pruebas del Sistema de Almacenamiento

Subir un archivo

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXffbFgL5zRO6Bm4heUSvvrfrvPxKvdN07wNQvmI-6Q3q87lGjeKdQMVC801kZrIa3_hyBc0fL105ZtBBxcKXeX7gBiWiSYVyo9PAAEuWlY4qtnXzk62D-eGhjRYBDjS8X2688wJ65Ie-gx5sSKpNTx9qv1s?key=CgRdnKUJcB5u-lHC6I5GQg)

Descargar un archivo

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdc8DsoRX2VWpb4lCQ4njS9ExYJMdW7nZeN8oOLbjjoz10wOy4KSzv6Gq65rnAFFqguyhV4r5F5V6eLAkd6eGzn-r5mk7aPyg7SgGnHBZyPY6yozbQ4tWHBoAnUrYrmNdWfUL8bgO0ho37UUfJ-VD8iHlw?key=CgRdnKUJcB5u-lHC6I5GQg)

Eliminar un archivo

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdoYt-HqB8qN7x6YicaXRKYhVNvBVu0p9mAOPH4RcFqIXBm3Fb3PkO7BcUVPnfg_s6qCOqWDZIYV-B3E7OPfgI5MdlzR_hMDYLjI4fZk6yPoEQu1B1xtjCSugGb7GFQ6rEmqAMuNpz42IEOruveP7tIp1c?key=CgRdnKUJcB5u-lHC6I5GQg)

#### Construcción y Ejecución de la Imagen:

Este Dockerfile configura un entorno con Python y Flask, instalando las bibliotecas necesarias lo cual estará en el contenedor. Esto permite desplegar el sistema de almacenamiento de archivos en múltiples nodos de manera uniforme.

#### Implementación del Sistema de Almacenamiento de Archivos

Desarrollo del Sistema 

Cargar, Descargar y Eliminar Archivos:



![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdNEh1CYPibnPir3cGC8OGdUb6qc1h6pBNK7u8pJK4CnNZnGE-txq5ODVy3s6qaCOZ3Hk5iKr-JXs1SpesqN8FTstJXSKc6Scg2Qis6lbohz2-ilDMvucOqW5emCMlO_xw64KLM4elco3VGkmPLNb6pHaNW?key=CgRdnKUJcB5u-lHC6I5GQg)




“app/__init__.py”


![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeMSIZ1vIiYgFIzA45WYuepRm2QC4HiCGZDGUpNWBC4D8ZQpWK0Ih2JtLvreLCnPSXjNCi_t6tnicDmKy09UEzc_3ilV7-QzvonJuy_4BlljiSVFKnqTHcCuArWZ5QKUVugV1-3gIeMqylweqi6ndiimcQX?key=CgRdnKUJcB5u-lHC6I5GQg)



![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcdG6iq-TxkyYWx4VcAITPBJ3MAVhJ1EUF4X6irktvrqswmghK6QsbixDB27XqgEQOY7fY8u5jA9pdPDuQt0nLpVueGAOC5kiJ2-70Hemp_0czZCGqVi5f8kcoYAuJz2HFB5lv-5w4nzxi4Ai8q0icWO56k?key=CgRdnKUJcB5u-lHC6I5GQg)
  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcfuKXjHE4FHTeZOMkSmF0GNqLQMcCOzFkB00QmjLStBCI0pOAQp1glCtB8ZBCMP0xo8QntjpUx1zLdSbqSUgLYwjwMZ5b8wynUedm2wIFy8fX-5tQ9JRpE-oSXdrmXEEzl0xOOUc_7e5ah77KR3k44Lqg?key=CgRdnKUJcB5u-lHC6I5GQg)

Este código implementa un sistema de almacenamiento de archivos usando Flask. Permite a los usuarios cargar, descargar y eliminar archivos a través de una API RESTful.

  

#### API RESTful con Flask

a.-Cargar archivos: Endpoint /upload para recibir y guardar archivos.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeJCNP5pKEVUFEGeGXWdKmAvpWB7hVJqE6xXQWhm6Oh5W8xkyuXd794VuHeaC7zD2O0V6sZheO-t1-F-cjf6wHGJdnoJFGhEKt_hn4vqyBSFitqU_7QU5d1khFH6zFIk1_JB2VBfcTEs7frNlncXjHAwSrH?key=CgRdnKUJcB5u-lHC6I5GQg)

b.-Descargar archivos: Endpoint /download/<filename> para enviar archivos al cliente.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcE5WkgXeLLQPBl3pQfN7lrVS24nuw0DBXKKYUeV_hROnAngtli6ehQVAlGayb8zpGwNVkAKDb0gcx_uxxFKvn5VkB_oK8xnP3QnfF-p7dSElWepOGSArGXoAI7mwmzYtCa_cCTH5pOL_lnzvvG6XC0JDSO?key=CgRdnKUJcB5u-lHC6I5GQg)

c.-Eliminar archivos: Endpoint /delete/<filename> para borrar archivos del servidor.

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXd8Zy6M53NGE0AZ8W4e2SpxVlvTg0mhmr8-BdxgFKAMh2KyY-s3p9wYU8-4L9CkkBdZFIG8CzD-IR7ZzenTyx9yAjHcmESLIrRmOf3yNANvnebbuNLThYCKx5AFGuNsuuNJG6jN2KMqQIO7vW9Ww73za-w?key=CgRdnKUJcB5u-lHC6I5GQg)


La API RESTful facilita la interacción con el sistema de almacenamiento, permitiendo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los archivos almacenados.

#### Comunicación entre Nodos

Transferencia de Archivos y Metadatos:

Se Configurara endpoints para manejar la sincronización y transferencia de archivos entre diferentes nodos utilizando Flask o Fast API.


  
  ---

<!-- REFERENCIAS -->
### Referencias

#### Bibliotecas de Criptografía en Python

1. **PyCryptodome**
   - PyCryptodome — PyCryptodome 3.160b1 documentation. (n.d.). Retrieved from [https://www.pycryptodome.org/src/introduction](https://www.pycryptodome.org/src/introduction)
   - Eijs, H. (2022, December 6). Legrandin/pycryptodome. GitHub. Retrieved from [https://github.com/Legrandin/pycryptodome](https://github.com/Legrandin/pycryptodome)

2. **Cryptography**
   - Cryptography with Python - Quick Guide. (n.d.). Tutorialspoint. Retrieved from [https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm)

#### Configuración del Entorno Distribuido con Docker

1. Docker Documentation. (2019, October 31). Docker. Retrieved from [https://docs.docker.com/](https://docs.docker.com/)

#### Implementación del Sistema de Almacenamiento de Archivos

1. Flask Documentation. (2010). Welcome to Flask — Flask Documentation (3.0.x). Retrieved from [https://flask.palletsprojects.com/en/3.0.x/](https://flask.palletsprojects.com/en/3.0.x/)
2. pallets. (2019, October 18). pallets/flask. GitHub. Retrieved from [https://github.com/pallets/flask](https://github.com/pallets/flask)

#### Comunicación entre Nodos

1. FastAPI. (n.d.). FastAPI Documentation. Retrieved from [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

---

<!-- FIN DE REFERENCIAS -->

  
