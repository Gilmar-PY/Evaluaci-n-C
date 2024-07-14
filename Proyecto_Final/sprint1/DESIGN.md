# Diseño del Sistema de Almacenamiento Distribuido Seguro

## Introducción
El objetivo del proyecto es desarrollar un sistema de almacenamiento distribuido que asegure la disponibilidad y 
la seguridad de los datos mediante técnicas de criptografía y replicación, optimizado para funcionar en un entorno de múltiples
nodos.

## Arquitectura del Sistema
- **Nodos Distribuidos**: Utilizamos Docker para configurar y desplegar nodos distribuidos.
- **API RESTful**: Implementada con Flask para la gestión de archivos.
- **Cifrado de Datos**: Utilizamos la biblioteca pycryptodome para cifrar y descifrar archivos.

## Diagrama de Componentes
![](https://lh7-us.googleusercontent.com/docsz/AD_4nXec5Lz7BEYL8ERByqmJ6O6zAFk7rBI8l9DsoiDzs1hAS4nSrJ9Rgh_NP-0AZVqpU2QMhG9CpjjHJrTU1gSe1hO9pMbux8DKkcXhVaEHpCFZWqwoNc9hWKIzji7g9ftLbmqm5rn-vV5g_61kc_oUnuqOTloq?key=nQL0RT6dNr_BeWtx8fgyhA)

## Decisiones de Diseño
- **Uso de Docker**: Para asegurar consistencia y escalabilidad.
- **Cifrado con AES**: Por su robustez y eficiencia.

## Flujo de Trabajo
1. **Carga de Archivos**: Los archivos son cifrados antes de ser almacenados.
2. **Descarga de Archivos**: Los archivos son descifrados antes de ser enviados al usuario.
3. **Eliminación de Archivos**: Los archivos se eliminan del sistema de manera segura.

## Consideraciones de Seguridad
- **Gestión de Claves**: Las claves deben ser gestionadas y almacenadas de manera segura.
- **Logs**: Implementación de logging para monitoreo y auditoría.


