
Ejercicios

Apache Kafka

    Explica la diferencia entre un productor y un consumidor en Kafka.
    Describe cómo funciona el particionamiento en Kafka y cómo se asignan las particiones a los brokers.
    ¿Qué es un "consumer group" y cómo ayuda a escalar la lectura de datos en Kafka?
    Discute las garantías de consistencia que ofrece Kafka. ¿Qué significa exactamente la semántica "at least once", "at most once", y "exactly once"?
    ¿Cómo maneja Kafka la durabilidad de los mensajes? Explica el concepto de replicación en Kafka.
    Compara Kafka con RabbitMQ y otras tecnologías de mensajería en términos de casos de uso, rendimiento, y arquitectura.

## Tus respuestas

Configuración de Kafka:

    Instala y configura un clúster de Kafka en tu máquina local o en un entorno de nube.
    Configura varios brokers y asegúrate de que se comuniquen correctamente.

Producción y consumo de mensajes:

    Desarrolla un productor que envíe mensajes a un tema específico.
    Desarrolla un consumidor que lea mensajes del mismo tema y procese los datos.
    Implementa un grupo de consumidores y demuestra cómo se distribuyen las cargas de trabajo entre ellos.

Procesamiento de Stream:

    Utiliza Kafka Streams API para crear una aplicación que procese datos en tiempo real.
    Implementa una simple agregación en tiempo real (por ejemplo, conteo de eventos por minuto) y escribe los resultados en un nuevo tema de Kafka.

## Tus respuestas

    Pregunta: Compara los modelos de publicación-suscripción y enrutamiento de mensajes de Apache Kafka y RabbitMQ.
    Ejercicio: Diseña un sistema de mensajería para una aplicación de comercio electrónico utilizando Apache Kafka, explicando cómo manejaría la partición y replicación de mensajes.

## Tus respuestas

RabbitMQ

    Describe la arquitectura de RabbitMQ y la función de los exchanges, colas, productores, y consumidores.
    Explica los diferentes tipos de exchanges en RabbitMQ (direct, fanout, topic, headers) y cuándo se utilizaría cada uno.
    Discute las diferentes estrategias de aseguramiento de entrega de mensajes en RabbitMQ, como persistencia de mensajes, confirmaciones de mensajes, y transacciones.
    Compara RabbitMQ con Kafka y otras tecnologías de mensajería en términos de casos de uso, rendimiento, y arquitectura.

## Tus respuestas

Configuración de RabbitMQ:

    Instala y configura RabbitMQ en tu máquina local o en un entorno de nube.
    Configura varios nodos y asegúrate de que se comuniquen correctamente.

Envío y recepción de mensajes:

    Desarrolla un productor que envíe mensajes a un exchange específico.
    Desarrolla un consumidor que lea mensajes de una cola vinculada al exchange.
    Implementa diferentes tipos de exchanges y demuestra cómo se enrutan los mensajes en cada caso.

Alta disponibilidad:

    Configura un clúster de RabbitMQ con nodos de alta disponibilidad.
    Implementa una estrategia de replicación y failover y demuestra cómo RabbitMQ maneja la recuperación de fallos.

## Tus respuestas

