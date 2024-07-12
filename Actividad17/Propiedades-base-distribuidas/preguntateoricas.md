## Bases de Datos SQL Distribuidas: Google Spanner y CockroachDB


Explica cómo Google Spanner utiliza TrueTime para lograr la consistencia global y compare su enfoque con el uso de Raft en CockroachDB.

## Google Spanner y TrueTime:

    TrueTime: Es un servicio de reloj global distribuido que proporciona un intervalo de tiempo preciso con garantías de errores acotados. TrueTime permite a Spanner asignar timestamps con garantías de orden global, permitiendo la consistencia fuerte y la serialización externa de transacciones.
    Consistencia Global: Spanner utiliza TrueTime para asignar timestamps a las transacciones, garantizando que todas las réplicas en diferentes centros de datos vean las transacciones en el mismo orden. Esto se logra mediante el uso de commit wait, donde una transacción espera hasta que todos los relojes en el sistema están suficientemente avanzados para evitar conflictos.

## CockroachDB y Raft:

    Raft: Es un algoritmo de consenso que asegura la replicación y consistencia de datos en un clúster distribuido. Cada grupo de réplicas en CockroachDB utiliza Raft para garantizar que las escrituras sean atómicas y consistentes.
    Consistencia: Raft asegura que las decisiones de replicación (como la aceptación de una transacción) son acordadas por la mayoría de las réplicas, lo que garantiza la consistencia de las transacciones distribuidas.

Comparación:

    TrueTime vs. Raft: TrueTime proporciona una manera de asegurar la consistencia global a través de un servicio de reloj preciso, mientras que Raft se basa en el consenso de mayoría para asegurar la consistencia de datos replicados.
    Latencia: TrueTime puede introducir latencia adicional debido a la espera de commit, mientras que Raft puede enfrentar latencias relacionadas con la comunicación y consenso entre réplicas.

Ejercicio: Diseño de base de datos distribuida para una aplicación global de reserva de vuelos utilizando Google Spanner

Diseño Propuesto:

    Particionamiento Automático:
        Clientes y Reservas: Dividir las tablas de clientes y reservas por regiones geográficas (e.g., continentes) utilizando claves de partición. Esto mejora la localización de datos y minimiza la latencia de acceso.
        Vuelos: Particionar la tabla de vuelos por aeropuertos de salida y llegada, utilizando la fecha de vuelo como un segundo nivel de partición para equilibrar la carga.

    Replicación Geográfica:
        Multi-Región: Configurar Spanner para replicar datos en múltiples regiones, asegurando alta disponibilidad y tolerancia a fallos.
        Reglas de Localidad: Utilizar reglas de localidad para mantener datos relacionados geográficamente cerca de los usuarios que más los necesitan, reduciendo la latencia de acceso.

    Transacciones Distribuidas:
        TrueTime: Aprovechar TrueTime para manejar transacciones distribuidas con consistencia fuerte y serialización externa.
        Commit Wait: Implementar commit wait para asegurar que las transacciones se confirmen sólo cuando todos los relojes están suficientemente avanzados, evitando conflictos.

    Optimización:
        Índices Secundarios: Crear índices secundarios en campos de búsqueda comunes, como nombres de aeropuertos y fechas de vuelo, para mejorar el rendimiento de las consultas.
        Compresión de Datos: Utilizar compresión de datos para reducir el tamaño de almacenamiento y mejorar el rendimiento de I/O.

Analiza cómo Google Spanner y CockroachDB manejan las transacciones distribuidas y garantizan la consistencia fuerte.

Google Spanner:

    TrueTime: Proporciona una base de tiempo global para asegurar que todas las transacciones se ordenen de manera consistente a través de diferentes réplicas.
    Commit Wait: Asegura que una transacción sólo se complete cuando todos los relojes en el sistema han avanzado lo suficiente para evitar conflictos de escritura.
    Transacciones ACID: Soporta transacciones multi-fila y multi-tabla, garantizando las propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad).

CockroachDB:

    Raft: Utiliza Raft para replicar y acordar transacciones entre réplicas, asegurando la consistencia fuerte.
    Transacciones Distribuidas: Implementa un protocolo de commit en dos fases (2PC) para coordinar transacciones distribuidas.
    Serialización: Emplea un sistema de versionado basado en timestamps para garantizar que todas las operaciones de lectura y escritura se ordenen de manera consistente.

Ejercicio: Diseño de una aplicación de comercio electrónico global utilizando CockroachDB

Diseño Propuesto:

    Particionamiento de Datos:
        Usuarios: Particionar la tabla de usuarios por región geográfica para mejorar la localización de datos y reducir la latencia.
        Productos y Pedidos: Particionar por categorías de productos y fechas de pedido para equilibrar la carga y mejorar el rendimiento de las consultas.

    Replicación y Tolerancia a Fallos:
        Multi-Región: Configurar CockroachDB para replicar datos en múltiples regiones, asegurando alta disponibilidad y tolerancia a fallos.
        Consenso Raft: Utilizar Raft para asegurar que todas las réplicas están consistentes y para manejar fallos de nodos de manera efectiva.

    Transacciones Distribuidas:
        Commit en Dos Fases (2PC): Implementar 2PC para coordinar transacciones distribuidas, garantizando que todas las réplicas acuerden el resultado de una transacción antes de confirmarla.
        Timestamps y Versionado: Utilizar timestamps para versionar datos y asegurar la serialización de las transacciones.

    Optimización y Escalabilidad:
        Índices Distribuidos: Crear índices en campos de búsqueda comunes, como ID de producto y fecha de pedido, para mejorar el rendimiento de las consultas.
        Caching y Compresión: Implementar caching de resultados de consultas frecuentes y compresión de datos para mejorar el rendimiento y reducir el uso de almacenamiento.

Optimización y Escalabilidad
Discute las técnicas de escalado horizontal vs. vertical y su aplicabilidad en diferentes escenarios.

    Escalado Horizontal (Sharding):
        Definición: Añadir más máquinas para distribuir la carga de trabajo y los datos.
        Aplicabilidad: Ideal para aplicaciones distribuidas y de alto volumen de datos, como sistemas de big data, servicios web globales, y bases de datos distribuidas.
        Ventajas: Mejor capacidad de manejo de grandes volúmenes de datos, mayor tolerancia a fallos.
        Desventajas: Complejidad de administración y particionamiento de datos, necesidad de mecanismos de balanceo de carga.

    Escalado Vertical:
        Definición: Mejorar la capacidad de una máquina existente (e.g., más CPU, más memoria).
        Aplicabilidad: Adecuado para aplicaciones que tienen limitaciones de latencia estrictas y no pueden ser fácilmente particionadas.
        Ventajas: Simplicidad de implementación, menos sobrecarga de red.
        Desventajas: Límites físicos de hardware, punto único de fallo.

Ejercicio: Optimización de una consulta compleja en una base de datos distribuida utilizando índices distribuidos

Consulta Compleja:

sql

SELECT product_id, SUM(quantity) as total_sales
FROM orders
WHERE order_date >= '2024-01-01' AND order_date <= '2024-01-31'
GROUP BY product_id
ORDER BY total_sales DESC;

Optimización:

    Índices Distribuidos:
        Crear un índice en order_date y product_id: 

        sql

    CREATE INDEX idx_order_date_product ON orders (order_date, product_id);

Desnormalización:

    Almacenar la suma de ventas diarias en una tabla separada para reducir el costo de cálculo en tiempo de consulta.


    CREATE TABLE daily_sales (
        product_id INT,
        order_date DATE,
        total_sales INT
    );

Consulta Optimizada:

    Consultar la tabla desnormalizada:



        SELECT product_id, SUM(total_sales) as total_sales
        FROM daily_sales
        WHERE order_date >= '2024-01-01' AND order_date <= '2024-01-31'
        GROUP BY product_id
        ORDER BY total_sales DESC;

Pregunta: Analiza las diferencias entre escalado horizontal y vertical en el contexto de una base de datos distribuida de alta demanda.

    Escalado Horizontal:
        Distribución de Carga: Permite distribuir la carga de trabajo entre múltiples nodos, mejorando el rendimiento en aplicaciones de alta demanda.
        Disponibilidad: Aumenta la disponibilidad al eliminar puntos únicos de fallo.
        Desafíos: Complejidad en el particionamiento de datos y la coherencia entre nodos.

    Escalado Vertical:
        Capacidad de Máquina Única: Incrementa la capacidad de procesamiento y almacenamiento de una sola máquina, adecuado para tareas de baja latencia.
        Límites Físicos: Está limitado por las capacidades físicas del hardware disponible.
        Simplicidad: Menos complejo de administrar comparado con el escalado horizontal, pero menos flexible para manejar grandes volúmenes de datos.

Ejercicio: Optimiza una consulta SQL compleja en una base de datos distribuida utilizando técnicas avanzadas de indexación y caching

Consulta Compleja:



SELECT user_id, COUNT(*) as login_count
FROM user_logins
WHERE login_date >= '2024-01-01' AND login_date <= '2024-01-31'
GROUP BY user_id
ORDER BY login_count DESC;

Optimización:

    Índices Avanzados:
        Crear un índice compuesto en login_date y user_id:

  

    CREATE INDEX idx_login_date_user ON user_logins (login_date, user_id);

Caching de Resultados:

    Implementar un sistema de caching para almacenar resultados de consultas frecuentes.
        Utilizar Redis para caching:



        import redis
        r = redis.Redis()

        # Almacenar en caché
        r.set('login_count_cache', query_result)

        # Recuperar del caché
        cached_result = r.get('login_count_cache')

Desnormalización:

    Almacenar conteos diarios en una tabla separada para reducir el costo de cálculo.

  

    CREATE TABLE daily_login_counts (
        user_id INT,
        login_date DATE,
        login_count INT
    );

Consulta Optimizada:

    Consultar la tabla desnormalizada:

  
        SELECT user_id, SUM(login_count) as login_count
        FROM daily_login_counts
        WHERE login_date >= '2024-01-01' AND login_date <= '2024-01-31'
        GROUP BY user_id
        ORDER BY login_count DESC;

Seguridad y Privacidad en Bases de Datos Distribuidas
Analiza los métodos de autenticación y autorización distribuidas en bases de datos distribuidas.

    Autenticación:
        Métodos: Usuario/contraseña, certificados SSL/TLS, tokens de acceso, autenticación multifactor (MFA).
        Implementación Distribuida: Utilizar servicios de identidad centralizados como LDAP, OAuth2, o Kerberos para gestionar identidades y accesos distribuidos.

    Autorización:
        Roles y Permisos: Definir roles y permisos granulares para controlar el acceso a recursos específicos en la base de datos.
        Control de Acceso Basado en Atributos (ABAC): Utilizar atributos de usuario y contexto para determinar permisos de acceso dinámicamente.

Ejercicio: Diseña un esquema de seguridad para una base de datos distribuida que incluya encriptación de datos en tránsito y en reposo, y gestione identidades y accesos.

    Encriptación de Datos en Tránsito:
        Utilizar SSL/TLS para todas las conexiones entre clientes y servidores de la base de datos.

   

    # Ejemplo de configuración de SSL en PostgreSQL
    ssl = on
    ssl_cert_file = 'server.crt'
    ssl_key_file = 'server.key'
    ssl_ca_file = 'root.crt'

Encriptación de Datos en Reposo:

    Configurar encriptación a nivel de disco o tabla.

 

    CREATE TABLE sensitive_data (
        id INT PRIMARY KEY,
        data TEXT
    ) WITH (encryption='on');

Gestión de Identidades y Accesos:

    Utilizar un servicio de identidad centralizado como LDAP para autenticar usuarios.
    Definir roles y permisos en la base de datos.

   

        CREATE ROLE admin_role;
        GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO admin_role;
        CREATE USER admin WITH PASSWORD 'securepassword';
        GRANT admin_role TO admin;

Pregunta: Discute las técnicas avanzadas de autenticación y autorización en sistemas distribuidos.

    Autenticación de Dos Factores (2FA): Añadir una capa adicional de seguridad mediante la combinación de algo que el usuario sabe (contraseña) y algo que el usuario tiene (código de un dispositivo).
    Single Sign-On (SSO): Permitir a los usuarios autenticarse una vez y acceder a múltiples sistemas y aplicaciones sin necesidad de autenticarse de nuevo.
    Autenticación Basada en Certificados: Utilizar certificados digitales para autenticar usuarios y dispositivos de manera segura.
    OAuth2 y OpenID Connect: Proporcionar un marco para la delegación de acceso seguro y autenticación federada, permitiendo a los usuarios acceder a recursos protegidos sin compartir sus credenciales directamente.
