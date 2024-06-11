Actividad 7: Repaso concurrencia, paralelismo, y el uso de los

módulos Python y Docker.

  

1. ¿Cuáles son las diferencias entre concurrencia y paralelismo?. ¿En qué escenario es preferible usar concurrencia sobre paralelismo y viceversa?

  

Concurrencia se refiere a la capacidad de un sistema para gestionar múltiples tareas al mismo tiempo, de tal manera que el progreso de una tarea no impida el progreso de otra. Esto puede implicar que las tareas se ejecuten secuencialmente o en solapamiento, sin necesariamente ejecutarse simultáneamente.

Paralelismo implica la ejecución simultánea de múltiples tareas, aprovechando múltiples núcleos de procesador o múltiples máquinas para llevar a cabo varias operaciones a la vez.

Escenarios preferibles:

-   Concurrencia sobre paralelismo: Ideal para sistemas donde se manejan muchas operaciones de I/O (entrada/salida) como servidores web, donde la latencia de I/O puede ser alta y la ejecución de tareas no requiere necesariamente un alto poder de cómputo.
    
-   Paralelismo sobre concurrencia: Preferible en tareas computacionalmente intensivas que pueden ser divididas en sub tareas independientes, como el procesamiento de imágenes, cálculos científicos, o simulaciones.
    

  
  
  

2. Presenta un repaso sobre los módulos multiprocessing, asyncio, y concurrent.futures.

-   multiprocessing: Permite la creación de procesos separados que pueden ejecutarse en paralelo en diferentes núcleos de CPU. Utiliza procesos en lugar de hilos, lo que evita los problemas del Global Interpreter Lock (GIL) de Python.
    

-   Ventajas: Aprovecha múltiples núcleos de CPU; evita el GIL.
    
-   Desventajas: Mayor consumo de recursos; más complejo de gestionar que los hilos.
    

-   asyncio: Biblioteca estándar de Python para la programación asíncrona utilizando corutinas. Adecuada para I/O asíncrono, networking, y tareas donde la latencia de I/O es una preocupación principal.
    

-   Ventajas: Ideal para tareas I/O intensivas; permite la escritura de código asíncrono de manera secuencial.
    
-   Desventajas: No es adecuado para tareas de CPU intensivas; aprendizaje adicional para dominar el paradigma asíncrono.
    

-   concurrent.futures: Proporciona una API de alto nivel para ejecutar llamadas de forma asíncrona utilizando hilos o procesos.
    

-   Ventajas: Simplifica el uso de hilos y procesos; fácil de integrar con otras partes del código.
    
-   Desventajas: La implementación de hilos está limitada por el GIL; los procesos pueden ser más pesados en términos de recursos.
    

  
  

3. Explica cómo Docker puede ser usado para simular entornos distribuidos y la importancia de

la contenerización en proyectos paralelos y distribuidos.

  

### 3. Docker y su uso en entornos distribuidos

Docker permite la creación de contenedores que encapsulan una aplicación y todas sus dependencias, asegurando que se ejecute de manera consistente en cualquier entorno.

-   Simulación de entornos distribuidos: Docker puede ser usado para crear múltiples contenedores que representan diferentes componentes de un sistema distribuido. Estos contenedores pueden ser orquestados para simular interacciones en un entorno realista.
    
-   Importancia de la contenerización:
    

-   Aislamiento: Cada contenedor opera en su propio entorno aislado, lo que evita conflictos entre dependencias y garantiza consistencia.
    
-   Portabilidad: Los contenedores pueden ser ejecutados en cualquier sistema que soporte Docker, facilitando la implementación en diferentes entornos.
    
-   Escalabilidad: Con herramientas de orquestación como Kubernetes, es posible escalar aplicaciones distribuidas de manera eficiente.
    

  

### Ensayo Comparativo de Modelos de Concurrencia

Modelo de Actores:

-   Manejo de concurrencia: Cada actor tiene su propio estado y se comunica con otros actores mediante mensajes. Esto evita el uso compartido de estado y los problemas de sincronización.
    
-   Ventajas: Fácil de razonar; evita problemas de sincronización.
    
-   Desventajas: Puede ser menos eficiente para ciertas tareas; complejidad en la gestión de muchos actores.
    
-   Casos de uso: Sistemas de telecomunicaciones, juegos en línea, servicios web.
    

Communicating Sequential Processes (CSP):

-   Manejo de concurrencia: Los procesos se comunican mediante canales de mensajes. Cada proceso es secuencial, y la comunicación es explícita.
    
-   Ventajas: Facilita el análisis formal de sistemas concurrentes; evita el uso compartido de memoria.
    
-   Desventajas: Puede ser difícil de implementar en sistemas grandes; requiere un diseño cuidadoso de la comunicación.
    
-   Casos de uso: Redes de sensores, sistemas de control industrial, sistemas embebidos.
    

Concurrencia basada en eventos:

-   Manejo de concurrencia: Utiliza un bucle de eventos central para manejar múltiples tareas a través de callbacks o promesas.
    
-   Ventajas: Eficiente para tareas I/O intensivas; bajo overhead.
    
-   Desventajas: El código puede ser difícil de leer y mantener debido a los callbacks anidados ("callback hell").
    
-   Casos de uso: Servidores web, interfaces de usuario, aplicaciones de tiempo real.
    

### Preguntas Guía

1.  Manejo de problemas de concurrencia:
    

-   Actores: Deadlock es poco común debido a la ausencia de estado compartido, pero puede ocurrir si los actores están esperando mensajes entre sí. Livelock puede ser gestionado mediante diseño de mensajes.
    
-   CSP: Deadlock puede ser manejado mediante análisis formal y diseño de protocolos. Livelock se evita asegurando que los procesos progresen correctamente.
    
-   Eventos: Deadlock es raro, pero puede ocurrir si hay dependencias cíclicas en los eventos. Livelock puede ser manejado mediante monitoreo y gestión de la cola de eventos.
    

3.  Tipo de aplicaciones:
    

-   Actores: Sistemas distribuidos, juegos, aplicaciones en tiempo real.
    
-   CSP: Sistemas embebidos, redes de sensores, control industrial.
    
-   Eventos: Servidores web, aplicaciones de interfaz de usuario, sistemas de tiempo real.
    

5.  Influencia en rendimiento y escalabilidad:
    

-   Actores: Buena escalabilidad debido a la independencia de actores; rendimiento puede variar según la implementación.
    
-   CSP: Alto rendimiento en sistemas donde la comunicación es clave; escalabilidad limitada por el diseño de canales.
    
-   Eventos: Excelente rendimiento para I/O intensivo; escalabilidad alta si se gestiona adecuadamente el bucle de eventos.
    

Ejercicio 3: Análisis crítico de la arquitectura de microservicios

### Desafíos y beneficios de implementar una arquitectura de microservicios en grandes empresas

Desafíos técnicos y organizativos:

1.  Complejidad en la gestión y despliegue:
    

-   Desafío: Los microservicios dividen una aplicación en muchos servicios pequeños, cada uno con su propio ciclo de vida y dependencia, lo que aumenta la complejidad.
    
-   Solución: Utilizar herramientas de orquestación como Kubernetes y sistemas de gestión de contenedores para automatizar el despliegue y escalado de microservicios.
    

3.  Intercomunicación entre servicios:
    

-   Desafío: La comunicación entre servicios puede introducir latencia y fallos si no se gestiona adecuadamente.
    
-   Solución: Implementar patrones de diseño como API Gateway y Circuit Breaker para manejar la comunicación y la tolerancia a fallos.
    

5.  Seguridad:
    

-   Desafío: Cada microservicio necesita ser asegurado, y las comunicaciones entre ellos deben ser encriptadas.
    
-   Solución: Adoptar una arquitectura de seguridad de "zero trust", utilizando TLS para comunicación entre servicios y autenticación fuerte como OAuth.
    

7.  Consistencia de datos:
    

-   Desafío: Mantener la consistencia de datos entre microservicios distribuidos puede ser complicado.
    
-   Solución: Utilizar patrones de consistencia eventual y herramientas de sincronización de datos como Apache Kafka.
    

9.  Cultura y habilidades:
    

-   Desafío: Cambiar a una arquitectura de microservicios requiere una cultura de DevOps y habilidades en tecnologías de contenedores y orquestación.
    
-   Solución: Invertir en capacitación y fomentar una cultura de colaboración y automatización.
    

Beneficios para la agilidad y escalabilidad:

1.  Agilidad en el desarrollo:
    

-   Beneficio: Los equipos pueden desarrollar, desplegar y escalar servicios de forma independiente, permitiendo ciclos de desarrollo más rápidos.
    
-   Impacto: Mejora el time-to-market y permite iteraciones rápidas en las características del producto.
    

3.  Escalabilidad:
    

-   Beneficio: Cada microservicio puede ser escalado de forma independiente según sus necesidades específicas de carga.
    
-   Impacto: Optimiza el uso de recursos y reduce costos operativos al escalar solo las partes de la aplicación que lo requieren.
    

5.  Resiliencia:
    

-   Beneficio: Los fallos en un microservicio no afectan a toda la aplicación, mejorando la disponibilidad general.
    
-   Impacto: Aumenta la resiliencia del sistema y mejora la experiencia del usuario al minimizar el tiempo de inactividad.
    

Impacto en el mantenimiento y gestión de la deuda técnica:

-   Mantenimiento: La modularidad de los microservicios facilita la actualización y el mantenimiento de partes específicas de la aplicación sin afectar al sistema completo.
    
-   Deuda técnica: La adopción de microservicios puede reducir la deuda técnica a largo plazo, pero a corto plazo, la transición puede generar deuda técnica temporal debido a la reescritura y refactorización de código.
    

Ejercicio 4: Patrones de diseño en sistemas concurrentes y distribuidos

  

### Patrones de diseño específicos

Patrón de Singleton Distribuido:

-   Problema: Necesidad de un único punto de control o recurso en un sistema distribuido.
    
-   Solución: Implementa un mecanismo para garantizar que solo una instancia del recurso esté activa en cualquier momento.
    
-   Ejemplo: Coordinadores de transacciones en sistemas de bases de datos distribuidas.
    

Patrón de Saga:

-   Problema: Gestión de transacciones distribuidas largas y complejas.
    
-   Solución: Divide la transacción en una serie de transacciones menores que pueden compensarse si una parte falla.
    
-   Ejemplo: Procesamiento de pedidos en e-commerce donde cada etapa (pago, envío, inventario) puede ser una saga.
    

Patrón de Circuit Breaker:

-   Problema: Prevención de fallos cascada en sistemas con múltiples servicios.
    
-   Solución: Monitorea las llamadas a servicios y corta el circuito si un servicio está fallando repetidamente para evitar sobrecarga.
    
-   Ejemplo: Implementación en servicios de API para mejorar la resiliencia frente a servicios dependientes fallidos.
    

### Preguntas Guía

1.  Manejo de problemas específicos:
    

-   Singleton Distribuido: Asegura la singularidad del recurso mediante coordinadores centralizados o algoritmos de elección de líder.
    
-   Saga: Maneja transacciones distribuidas con compensaciones en lugar de deshacer todo el sistema.
    
-   Circuit Breaker: Protege servicios de fallos continuos mediante el monitoreo y la interrupción de conexiones fallidas.
    

3.  Manejo de fallos en sistemas altamente disponibles:
    

-   Circuit Breaker: Es fundamental para sistemas que requieren alta disponibilidad, ya que evita la saturación de servicios fallidos y permite la recuperación.
    
-   Saga: Asegura la coherencia y la recuperación en transacciones distribuidas mediante compensaciones efectivas.
    

5.  Ejemplos en aplicaciones comerciales:
    

-   Singleton Distribuido: Servicios de autenticación centralizada como OAuth.
    
-   Saga: Procesos de compra en Amazon, donde cada paso del pedido es manejado como una transacción independiente.
    
-   Circuit Breaker: Implementaciones en Netflix para asegurar la disponibilidad del servicio de streaming ante fallos de microservicios.
    

  

## Ejercicio 5: Estudio de caso sobre la tolerancia a fallos en sistemas distribuidos

### Estrategias de tolerancia a fallos en sistemas distribuidos

Estudio de Caso: Apache Cassandra

-   Técnicas de tolerancia a fallos:
    

-   Replicación de datos: Los datos se replican en múltiples nodos para asegurar disponibilidad y durabilidad.
    
-   Particionamiento: Los datos se distribuyen a través de varios nodos para balancear la carga.
    
-   Manejo de errores: Usa un modelo eventual consistente y mecanismos de detección y recuperación de fallos.
    

Preguntas Guía

1.  Técnicas efectivas de tolerancia a fallos:
    

-   Replicación: Garantiza que los datos estén disponibles incluso si algunos nodos fallan.
    
-   Particionamiento: Distribuye la carga de trabajo y evita puntos únicos de fallo.
    
-   Detección y recuperación: Monitorea continuamente los nodos y recupera automáticamente los datos de nodos fallidos.
    

3.  Manejo de fallos de red o hardware:
    

-   Red: Utiliza topologías de red redundantes y algoritmos de consenso para asegurar la disponibilidad.
    
-   Hardware: Implementa estrategias de failover y replicación para redirigir el tráfico y evitar la pérdida de datos.
    

5.  Compensaciones CAP Theorem:
    

-   Consistencia: Sacrifica la consistencia estricta a favor de la disponibilidad y la tolerancia a particiones.
    
-   Disponibilidad: Priorizada para asegurar que el sistema siga funcionando y respondiendo a solicitudes.
    
-   Tolerancia a particiones: Implementada para mantener el sistema operativo incluso cuando hay particiones de red.
    

## Ejercicio 6: Docker y Microservicios: Desafíos de Seguridad

### Desafíos de Seguridad en la Implementación de Microservicios utilizando Docker

### Desafíos de Seguridad

1.  Aislamiento de Contenedores:
    

-   Riesgo: Aunque Docker utiliza namespaces y control groups (cgroups) para aislar los contenedores, las vulnerabilidades en el kernel pueden ser explotadas para escapar del contenedor y acceder al host.
    
-   Mitigación:
    

-   Utilizar herramientas como SELinux, AppArmor o seccomp para mejorar el aislamiento de contenedores.
    
-   Ejecutar contenedores con el menor privilegio posible (por ejemplo, utilizando usuarios no root).
    
-   Mantener el software del host y Docker actualizado para protegerse contra vulnerabilidades conocidas.
    

3.  Gestión de Secretos:
    

-   Riesgo: Almacenar secretos (como credenciales, claves API y certificados) de manera insegura dentro de los contenedores puede llevar a la exposición de datos sensibles.
    
-   Mitigación:
    

-   Utilizar herramientas de gestión de secretos como HashiCorp Vault, AWS Secrets Manager o Kubernetes Secrets.
    
-   Evitar almacenar secretos en imágenes de contenedores o en variables de entorno. Utilizar mecanismos seguros de inyección de secretos en tiempo de ejecución.
    
-   Rotar los secretos regularmente y restringir el acceso a ellos mediante políticas de control de acceso.
    

5.  Políticas de Red:
    

-   Riesgo: La comunicación entre microservicios puede ser interceptada o manipulada si no se aseguran adecuadamente las conexiones de red.
    
-   Mitigación:
    

-   Implementar políticas de red estrictas que limiten el tráfico solo a los servicios necesarios. Esto puede hacerse utilizando Network Policies en Kubernetes.
    
-   Encriptar el tráfico entre microservicios utilizando TLS para prevenir ataques de intermediario (man-in-the-middle).
    
-   Utilizar firewalls de aplicaciones web (WAF) y herramientas de monitoreo para detectar y mitigar ataques en tiempo real.
    

### Preguntas Guía

1.  Principales riesgos de seguridad y mitigaciones:
    

-   Riesgos:
    

-   Escape de contenedores.
    
-   Almacenamiento inseguro de secretos.
    
-   Comunicación no segura entre microservicios.
    

-   Mitigaciones:
    

-   Uso de perfiles de seguridad (SELinux, AppArmor).
    
-   Herramientas de gestión de secretos (HashiCorp Vault, Kubernetes Secrets).
    
-   Políticas de red estrictas y encriptación de tráfico (Network Policies, TLS).
    

3.  Importancia de la gestión de secretos en microservicios:
    

-   Los secretos son esenciales para la autenticación y autorización en sistemas distribuidos. Una mala gestión puede resultar en filtraciones de datos sensibles y comprometer la seguridad de todo el sistema.
    
-   La gestión adecuada de secretos asegura que solo los servicios autorizados puedan acceder a información crítica, minimizando el riesgo de ataques internos y externos.
    

5.  Políticas de red y orquestación para mejorar la seguridad:
    

-   Políticas de Red:
    

-   Controlan el tráfico entre contenedores, asegurando que solo las comunicaciones necesarias estén permitidas, reduciendo la superficie de ataque.
    

-   Herramientas de Orquestación (Kubernetes):
    

-   Ofrecen mecanismos para definir y aplicar políticas de seguridad, gestionar la rotación de secretos y monitorizar la actividad en tiempo real.
    
-   Facilitan el aislamiento de recursos y la implementación de prácticas de seguridad de "zero trust".
    

## Ejercicio 7: Performance y escalabilidad en Kubernetes

### Mecanismos de Kubernetes para mejorar la performance y la escalabilidad

### 1. Programación de Pods

Decisiones de programación:

-   Programación eficiente: El programador (scheduler) de Kubernetes asigna Pods a nodos en función de varios criterios como la disponibilidad de recursos (CPU, memoria), afinidad y anti-afinidad de Pods, y requisitos específicos de los contenedores.
    
-   Impacto en la performance:
    

-   Distribución de carga: Una buena estrategia de programación asegura que la carga de trabajo se distribuya equitativamente entre los nodos, evitando la sobrecarga de unos mientras otros están infrautilizados.
    
-   Afinidad y anti-afinidad: Estas reglas permiten definir relaciones de colocación de Pods, mejorando la latencia de comunicación entre ellos al ubicarlos en nodos cercanos o separándolos para evitar puntos únicos de fallo.
    

### 2. Autoescalado

Proceso de autoescalado:

-   Horizontal Pod Autoscaler (HPA):
    

-   Función: Escala automáticamente el número de réplicas de un Pod basado en métricas observadas, como la utilización de CPU o la latencia de respuesta.
    
-   Beneficio: Permite que las aplicaciones escalen automáticamente para manejar incrementos en la carga, mejorando tanto la disponibilidad como la performance.
    

-   Cluster Autoscaler:
    

-   Función: Añade o elimina nodos en el clúster en función de la demanda de recursos.
    
-   Beneficio: Optimiza el uso de recursos al ajustar dinámicamente el tamaño del clúster, asegurando que siempre haya suficientes recursos disponibles sin incurrir en costos innecesarios.
    

### 3. Balanceo de Carga

Impacto en la escalabilidad y la disponibilidad:

-   Servicios de Kubernetes:
    

-   ClusterIP: Proporciona una IP interna y distribuye el tráfico entre los Pods en el clúster.
    
-   NodePort: Expone el servicio en un puerto específico de cada nodo del clúster, permitiendo el acceso desde fuera del clúster.
    
-   LoadBalancer: Crea un balanceador de carga externo para distribuir el tráfico entre los Pods.
    

-   Balanceo de carga interno:
    

-   Mecanismo: Kubernetes utiliza iptables o IPVS para distribuir el tráfico entre los Pods de un servicio.
    
-   Beneficio: Asegura que el tráfico se distribuya uniformemente, previniendo que un solo Pod se convierta en un cuello de botella y mejorando la disponibilidad del servicio.
    

-   External Load Balancers:
    

-   Función: Se integran con servicios de balanceo de carga proporcionados por los proveedores de nube (como AWS ELB, Google Cloud Load Balancer).
    
-   Beneficio: Facilitan el escalado horizontal al distribuir el tráfico entrante entre múltiples nodos y regiones, mejorando tanto la escalabilidad como la resiliencia frente a fallos de red o de hardware.
    

### Preguntas Guía

1.  Impacto de la programación de Pods en la performance general:
    

-   Distribución de carga: Una programación eficiente evita la sobrecarga de nodos específicos, mejorando la utilización de recursos y la performance.
    
-   Afinidad/anti-afinidad: Mejora la latencia de comunicación y la resiliencia al configurar Pods cercanos o distribuidos según las necesidades de la aplicación.
    

3.  Proceso de autoescalado y gestión eficiente de recursos:
    

-   Horizontal Pod Autoscaler: Escala dinámicamente las réplicas de los Pods basándose en métricas de utilización, garantizando que las aplicaciones puedan manejar la carga variable.
    
-   Cluster Autoscaler: Ajusta el tamaño del clúster agregando o eliminando nodos según la demanda, optimizando el uso de recursos y reduciendo costos operativos.
    

5.  Impacto del balanceo de carga en la escalabilidad y disponibilidad:
    

-   Escalabilidad: Distribuye el tráfico de manera uniforme entre los Pods, permitiendo que la aplicación maneje un mayor volumen de solicitudes.
    
-   Disponibilidad: Asegura que el fallo de un Pod o nodo no afecte la disponibilidad del servicio, ya que el tráfico se redistribuye automáticamente entre los Pods restantes.
    

  

## Ejercicio 8: Principios de diseño de sistemas distribuidos

### 1. Transparencia en Sistemas Distribuidos

Definición e Importancia:

-   Transparencia: Se refiere a la ocultación de la complejidad del sistema distribuido a los usuarios y aplicaciones. Incluye varios tipos de transparencia como de acceso, de ubicación, de migración, de replicación, de concurrencia y de fallos.
    
-   Importancia: La transparencia mejora la usabilidad y la fiabilidad del sistema, permitiendo a los usuarios interactuar con él como si fuera un sistema único y cohesionado.
    

### 2. Escalabilidad en Sistemas Distribuidos

Logro de la Escalabilidad sin Comprometer la Seguridad:

-   Escalabilidad Horizontal: Añadir más nodos al sistema para manejar incrementos en la carga de trabajo.
    
-   Seguridad: Implementar autenticación y autorización robustas, cifrado de datos y segmentación de red.
    

### 3. Manejo de Fallos en Sistemas Distribuidos

Influencia del Diseño en el Manejo de Fallos:

-   Redundancia y Replicación: Diseñar el sistema con redundancia y replicación de datos para asegurar la disponibilidad en caso de fallos.
    
-   Detección y Recuperación: Implementar mecanismos para detectar fallos y recuperar el estado del sistema rápidamente.
    

### Preguntas Guía

1.  Transparencia en Sistemas Distribuidos:
    

-   Definición: La transparencia en un sistema distribuido es la capacidad de ocultar la complejidad subyacente y proporcionar una interfaz simple y consistente al usuario.
    
-   Importancia: Facilita la interacción con el sistema, mejora la experiencia del usuario y reduce los errores relacionados con la complejidad del sistema.
    

3.  Escalabilidad sin Comprometer la Seguridad:
    

-   Estrategias:
    

-   Implementar controles de acceso y políticas de seguridad que escalen junto con el sistema.
    
-   Usar tecnologías que soporten el cifrado de datos en tránsito y en reposo.
    

-   Ejemplos: Kubernetes y Apache Kafka, que ofrecen mecanismos integrados de escalabilidad y seguridad.
    

5.  Diseño para Manejo de Fallos:
    

-   Estrategias de Diseño:
    

-   Redundancia: Asegurar que no haya un solo punto de fallo mediante la replicación de componentes críticos.
    
-   Detección y Recuperación: Implementar monitoreo continuo y estrategias de recuperación automática para mantener la disponibilidad del sistema.
    

-   Ejemplos: AWS y GFS, que utilizan redundancia y replicación junto con detección de fallos para mantener la disponibilidad y la integridad de los servicios.
    

### Ejercicio 4: Cálculo del factorial de números grandes con multiprocessing

![](https://lh7-us.googleusercontent.com/g3sD_6LUBu9JNuMZaVvJxA34MrbNu3eBpoK_03zFSjiPbVQcrClQv2m2CoMDty82kQT3plqOcigzyhytny7s2z9hB9NWEBpfLB7C2v7O4RDIwnoNP__u2zwjKkV9esJsj4XzH9jewfjXQ88ZqGLqHmw)![](https://lh7-us.googleusercontent.com/0HBQdOLplOpaXwujCX28OMYQ8cHsnUJU3KV3bBpWOtL-OtysEkYAksG7O-yUm6xd0KCzBUlEaFdUoEpGb68xSEN-LUfhfmLxq_q8poy1ukCNRSfpY21BuRpREWkMu_mNKkJBPs-XoKPslHvxU3gRKxI)

### Ejercicio 5: Web scraper concurrente con asyncio

![](https://lh7-us.googleusercontent.com/zm-NWFs5V2pQ_q5HGtiNZdPNnvagY7TA_UrIfLFTFSgOpnbE4Z-dHO5mGg5K11Iw0ODvvUJd49jQAatKwH5JfEWNbSgpsNb0Xi33cCczuSOj-YaMaVR56hYEtBRdbzE2vGfQelpUKRL_MnQnyNCnOys)

### Ejercicio 6: Aplicar un filtro a varias imágenes con concurrent.futures

![](https://lh7-us.googleusercontent.com/TT77wDwLu2M-lMibxzgFv1iT7ASEk8dILseDjhUcaBB4SuHlqSBCtNpoMvKPeDZNNz2oVRyL0K9AdhxEteDZvAhHqWMFe5vrwts1ahJ7oboVbHBfID6T6_FU024zW0Ns5oebJYxUGRn0VoQOpuqc69o)

Parte 3: Integración con Docker

7. Contenerización de una aplicación:

• Creaa un Dockerfile para alguna de las aplicaciones desarrolladas en los ejercicios

anteriores.

• Explicación y ejecución de la aplicación dentro de un contenedor Docker.

  

![](https://lh7-us.googleusercontent.com/Ef3auq_IAIAuZFpRjwWOlZly_AlUhCN7DnT-6GkTTp2L-wpydEhdzNrnzVkJ37Kh5i1gdZlCGbmL26_VNeVppaGg7iooG4OMsahOR8gmkfAxzcU5gRtnr3oaZOrqGfe_S9MMR7t1Fx_eH1-9PVzxD4k)

  

Más ejercicios

Escalado de aplicaciones con concurrent.futures

  

![](https://lh7-us.googleusercontent.com/-XwCTGHBVE1Glo12maWSfMVNq_98y1OyY49SjscQE_UwKhQm8mxhyvVpuXr0mf1SX89wTQ72lcq3vyMRFNMUi0X4G51blM4Jsx7JSeIdPZ6LMzki6B5_gRfsPG_jfXw8tA5oTTlqkb4A3AZN2tWfaOs)![](https://lh7-us.googleusercontent.com/486-68Ahfp7I-o8V2E4XYYMA6__Sm1qeUJ4IzC4P4Yc3xd5m4mC6A3mbBFXIMxEEHXsOJVvAdVX7H4C_zDia78TwjTvvDafwcWuDU1dAuThJBu8b-BnIq8Hmo4X_2IGZyK5EGzV9sRh0NMdmnjIusJc)

  

![](https://lh7-us.googleusercontent.com/Rs7IlVjeoulLxpybQ2nmTiyyTPg5KDYJTpOa19kGEBuesxKH9yS3s8-xQe6Ir1vnPCey8vEn9TI83eGjglFc8asCVkrCMXRiRzA1ktBjcNLm-UN-HuTlluROCoNjA4Y72uGynqIp1a5y2iH069eCiac)![](https://lh7-us.googleusercontent.com/bgjfCObZXHgB7PITqeQjQsEmR5aL6SMgNs6YQ0L9mSgmDdFoJnBtQz8SndCAEYrXAlSyazVclW7Q2GzZYInWJLtYsD141PaSt54Y52gYzjHXvjwZiN-dFodRilYJh3cWHR9PcCXwKtBmYbdF93k_C6o)

![](https://lh7-us.googleusercontent.com/z_gdAOOhHY8jBsDBAgzCoJQBPd44C-L7XXtdViOFR2O6IxbASpr3e7WLbL6HF9P2sXy1D6y-kIUfZBSbEFjtcdDMZOkGTHdj_GDRoWT-Xg8_Ak-tCcPPjvROWZKTelvLFTE7SJxNJWq5PBopPSMB_r4)

  

![](https://lh7-us.googleusercontent.com/npYriP5kYaD4LhhTERuWyBs6Ju-eEMDMu-Q1CrKGqb59WRTCyubdL_AIctcfwKZcskQahjYLpDVYS0lmDs-p-20r312ju2gbkcZCI6gdFAzJ8KKTtpx9sqzM7zouCk5G5lBHepDTibVVB6cwbL6IFs8)

## Rutas del Servidor

-   /: Sirve una página HTML simple que actúa como la página de inicio.
    
-   /status: Muestra un JSON con el estado actual del servidor, incluyendo uptime y número de solicitudes manejadas.
    
-   /background-tasks: Muestra una lista de tareas programadas y su estado actual.
    

  

![](https://lh7-us.googleusercontent.com/uciwUendi8xhRlcwPqQiNCukLCHKNGF8vadKnzrR8IdgKADzL9lljeBxweStMvNXiSHCse9R2xh9EZumnbY7Y6oBufs0eZaa2nLnjwnfNYwZDljiUlHh_vnJ4ARSMTz06wEQQXgwZ57pVQRWNYvhQxM)

  
![](https://lh7-us.googleusercontent.com/AalMaahh8JoFK8cZaxwjQHByZZsqTZ_FjjB8UmVwFUmF8UUtvj6sLC3S7oWvMUBKWigdj5OgV7zue4Yqx-01sny7DqGNxoVud_IaDr3R58zVpo_rpvFgQZaWZ8_8IfgiULcFMxuYXl69g_YS2UngBqU)![](https://lh7-us.googleusercontent.com/Qx7OhkyuGZcR3o7YF6d9L2ZJKBj34eDBmwCjEmDsEJsQdpvk3Uo6Syn-5Zz3w6sA38Gg4e_-fsYhAWeKNMqZNhwYt0hPgR1DMsRapl0g-SRqNg1tMVPn02cchTU4kvmDtiOnm2v_mdpdO03YTLmuN94)