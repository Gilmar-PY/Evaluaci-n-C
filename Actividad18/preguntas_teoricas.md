
Ejercicios

Apache Kafka

    Explica la diferencia entre un productor y un consumidor en Kafka.
    Describe cómo funciona el particionamiento en Kafka y cómo se asignan las particiones a los brokers.
    ¿Qué es un "consumer group" y cómo ayuda a escalar la lectura de datos en Kafka?
    Discute las garantías de consistencia que ofrece Kafka. ¿Qué significa exactamente la semántica "at least once", "at most once", y "exactly once"?
    ¿Cómo maneja Kafka la durabilidad de los mensajes? Explica el concepto de replicación en Kafka.
    Compara Kafka con RabbitMQ y otras tecnologías de mensajería en términos de casos de uso, rendimiento, y arquitectura.

## Tus respuestas


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


Envío y recepción de mensajes:

    Desarrolla un productor que envíe mensajes a un exchange específico.
    Desarrolla un consumidor que lea mensajes de una cola vinculada al exchange.
    Implementa diferentes tipos de exchanges y demuestra cómo se enrutan los mensajes en cada caso.

Alta disponibilidad:

    Configura un clúster de RabbitMQ con nodos de alta disponibilidad.
    Implementa una estrategia de replicación y failover y demuestra cómo RabbitMQ maneja la recuperación de fallos.





Comparación de Kafka y RabbitMQ
Modelos de publicación-suscripción y enrutamiento de mensajes

    Kafka:
        Modelo de publicación-suscripción: Los productores publican mensajes a temas y los consumidores se suscriben a esos temas. El almacenamiento basado en logs garantiza que los consumidores pueden leer mensajes a su propio ritmo.
        Enrutamiento de mensajes: Basado en particiones y claves de mensajes que determinan la partición a la que se asigna un mensaje.

    RabbitMQ:
        Modelo de publicación-suscripción: Utiliza exchanges para enrutar mensajes a una o más colas basadas en reglas de enrutamiento definidas.
        Enrutamiento de mensajes: Los diferentes tipos de exchanges (direct, fanout, topic, headers) permiten una flexibilidad significativa en cómo se enrutan los mensajes.

Diseño de un sistema de mensajería para una aplicación de comercio electrónico utilizando Apache Kafka

    Partición de mensajes:
        Usa particiones para distribuir los mensajes entre diferentes brokers.
        Particiona por diferentes atributos como ID de pedido, ID de usuario, etc., para balancear la carga de trabajo.

    Replicación:
        Configura la replicación para garantizar la durabilidad y alta disponibilidad.
        Ajusta el replication.factor para que los datos estén replicados en varios brokers.

    Casos de uso:
        Procesamiento de pedidos en tiempo real.
        Seguimiento de eventos de usuarios.
        Agregación de datos de ventas para análisis en tiempo real.

RabbitMQ
Arquitectura de RabbitMQ y la función de los exchanges, colas, productores, y consumidores

    Exchanges: Enrutadores de mensajes que reciben mensajes de los productores y los enrutan a las colas basándose en reglas de enrutamiento.
    Colas: Almacenan los mensajes que serán consumidos por los consumidores.
    Productores: Aplicaciones que envían mensajes a los exchanges.
    Consumidores: Aplicaciones que leen mensajes de las colas y los procesan.

Tipos de exchanges en RabbitMQ

    Direct Exchange: Enruta mensajes a las colas que tienen un binding key que coincide exactamente con la routing key del mensaje.
    Fanout Exchange: Enruta mensajes a todas las colas vinculadas sin tener en cuenta la routing key.
    Topic Exchange: Enruta mensajes a una o más colas basadas en coincidencias de patrones con la routing key.
    Headers Exchange: Enruta mensajes basados en coincidencias de cabeceras en lugar de la routing key.

Estrategias de aseguramiento de entrega de mensajes en RabbitMQ

    Persistencia de mensajes: Almacena mensajes en disco para asegurar que no se pierdan en caso de fallo del servidor.
    Confirmaciones de mensajes: Los productores reciben confirmaciones de que los mensajes han sido entregados a las colas.
    Transacciones: Aseguran que un conjunto de operaciones de mensajes se complete de manera atómica.

Comparación de RabbitMQ con Kafka

    Casos de uso: RabbitMQ es adecuado para colas de trabajo y aplicaciones que requieren entrega inmediata. Kafka es ideal para el procesamiento de flujos de datos y análisis en tiempo real.
    Rendimiento: Kafka generalmente tiene un rendimiento superior en términos de throughput debido a su arquitectura basada en logs.
    Arquitectura: RabbitMQ utiliza un modelo de colas y exchanges, mientras que Kafka utiliza un modelo de temas y particiones.

