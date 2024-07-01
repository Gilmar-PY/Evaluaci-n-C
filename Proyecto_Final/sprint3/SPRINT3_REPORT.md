# reporte del Sprint 3

## 1. Introducción

### Objetivos del Sprint

- Realizar pruebas de seguridad y resiliencia del sistema.
- Optimizar la replicación y recuperación de datos.
- Preparar una presentación detallada del proyecto, destacando la seguridad y eficiencia del sistema.

## 2. Planificación

### Tareas Planificadas

- Pruebas de seguridad.
- Pruebas de resiliencia.
- Optimización de la replicación.
- Preparación de la presentación.


## 3. Implementación

### Descripción del Trabajo Realizado

- **Pruebas de carga:** Se realizaron pruebas con ApacheBench para evaluar el rendimiento del sistema.
- **Optimización de la replicación:** Se optimizó el algoritmo de replicación para mejorar la consistencia y la latencia.

### Algoritmos y Métodos

- **Cifrado de Archivos:** Se utilizó el algoritmo AES para cifrar los archivos antes de la replicación.
- **Replicación Asíncrona:** Se implementó utilizando asyncio y aiohttp.

### Desafíos Encontrados

- Problemas de consistencia en la replicación de archivos.
- Alto número de solicitudes fallidas durante las pruebas de descarga.

## 4. Resultados

### Funcionalidades Desarrolladas

- Subida, descarga y eliminación de archivos con cifrado.
- Replicación de archivos en múltiples nodos.

### Pruebas Realizadas

- **Subida de Archivos:** 100 solicitudes con 0 fallos.
- **Descarga de Archivos:** 100 solicitudes con 98 fallos.

### Demostración de Funcionalidades

- Capturas de pantalla de las pruebas realizadas.
- Logs de los nodos mostrando las operaciones realizadas.

## 5. Análisis y Evaluación

### Comparación con los Objetivos del Sprint

- **Pruebas de seguridad:** Pendiente de realizar.
- **Pruebas de resiliencia:** Pendiente de realizar.
- **Optimización de la replicación:** Parcialmente completada.
  

### Lecciones Aprendidas

- La replicación de archivos requiere mecanismos de verificación para garantizar la consistencia.
- La optimización del rendimiento es crítica para manejar cargas de trabajo concurrentes.


## 6. Plan para el Próximo Sprint

### Objetivos del Próximo Sprint

- Completar las pruebas de seguridad y resiliencia.
- Optimizar el sistema para mejorar el rendimiento en la descarga de archivos.
- Finalizar y presentar la presentación del proyecto.

### Tareas Planificadas

- Pruebas de seguridad y resiliencia.
- Optimización de la descarga de archivos.
- Preparación de la presentación final.

### Ajustes Necesarios

- Implementar mecanismos de reintento y verificación para la replicación.
- Realizar un análisis detallado de los logs para identificar y resolver problemas de rendimiento.


