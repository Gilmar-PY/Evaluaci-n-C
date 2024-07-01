# INTRODUCCIÓN

## Resumen del Proyecto

El proyecto consiste en desarrollar un sistema de almacenamiento distribuido seguro. Este sistema garantiza la seguridad y disponibilidad de los datos mediante técnicas de cifrado y replicación. Además, se optimiza para funcionar en un entorno de múltiples nodos, utilizando Docker para la implementación y gestión de contenedores.

## Objetivos

### SPRINT 1
- Configurar el entorno de desarrollo con las bibliotecas necesarias.
- Implementar una API RESTful para la gestión de archivos (carga, descarga y eliminación).
- Configurar la comunicación básica entre nodos.

### SPRINT 2
- Implementar funciones de cifrado de datos utilizando bibliotecas de criptografía en Python.
- Implementar técnicas de replicación de datos para garantizar la disponibilidad.
- Utilizar asyncio y threading para manejar la sincronización entre nodos.

### SPRINT 3
- Realizar pruebas de seguridad y resiliencia del sistema.
- Optimizar la replicación y recuperación de datos.
- Preparar una presentación detallada del proyecto.

## Relevancia

La relevancia del proyecto radica en la utilización de técnicas de cifrado y replicación de datos para garantizar la seguridad y disponibilidad en un sistema distribuido. Estas técnicas permiten proteger los datos contra accesos no autorizados y asegurar que los datos estén disponibles incluso en caso de fallos en los nodos.

# METODOLOGÍA

## Metodología Ágil

Se utilizó la metodología ágil para el desarrollo incremental del proyecto, dividiendo el trabajo en sprints que permitieron enfocarse en objetivos específicos y adaptarse a los cambios de manera efectiva.

## Estructura de los Sprints

### Sprint 1
- **Tareas planificadas:**
  - Tarea 1: Configurar el entorno de desarrollo.
  - Tarea 2: Implementar la API RESTful para gestión de archivos.
  - Tarea 3: Configurar la comunicación básica entre nodos.

### Sprint 2
- **Tareas planificadas:**
  - Tarea 1: Implementar cifrado de datos con AES.
  - Tarea 2: Desarrollar funciones de replicación de archivos entre nodos.
  - Tarea 3: Configurar la sincronización asíncrona y concurrente.

### Sprint 3
- **Tareas planificadas:**
  - Tarea 1: Realizar pruebas de seguridad.
  - Tarea 2: Realizar pruebas de resiliencia.
  - Tarea 3: Optimizar el algoritmo de replicación.
  - Tarea 4: Preparar la presentación del proyecto.

# DESARROLLO DEL PROYECTO

## SPRINT 1

### Tareas planificadas

- **Tarea 1: Configurar el entorno de desarrollo**
  - Instalación de Flask para la creación de la API RESTful.
  - Configuración de Docker para la creación y gestión de contenedores.

- **Tarea 2: Implementar la API RESTful para gestión de archivos**
  - Creación de rutas para cargar, descargar y eliminar archivos.

- **Tarea 3: Configurar la comunicación básica entre nodos**
  - Establecimiento de la estructura de red para la comunicación entre contenedores Docker.

## SPRINT 2

### Tareas planificadas

- **Tarea 1: Implementar cifrado de datos con AES**
  - Desarrollo de funciones para cifrar y descifrar archivos utilizando el algoritmo AES.

- **Tarea 2: Desarrollar funciones de replicación de archivos entre nodos**
  - Implementación de funciones asíncronas para replicar archivos en otros nodos.

- **Tarea 3: Configurar la sincronización asíncrona y concurrente**
  - Uso de asyncio y threading para manejar la sincronización entre nodos.

## SPRINT 3

### Tareas planificadas

- **Tarea 1: Realizar pruebas de seguridad**
  - Identificación de vulnerabilidades y prueba de acceso a datos cifrados.

- **Tarea 2: Realizar pruebas de resiliencia**
  - Simulación de fallos de nodo y evaluación del rendimiento del sistema.

- **Tarea 3: Optimizar el algoritmo de replicación**
  - Mejora del algoritmo de replicación para reducir la latencia y el tiempo de recuperación de datos.

- **Tarea 4: Preparar la presentación del proyecto**
  - Creación de una presentación que detalle objetivos, metodología, resultados y conclusiones del proyecto.

# RESULTADOS Y DEMOSTRACIÓN

## Optimización del Sistema

Se realizaron mejoras en el algoritmo de replicación para reducir la latencia y el tiempo de recuperación de datos. Se verificó que los datos se replicaran en tiempo real en todos los nodos.

### Funcionalidades desarrolladas

- Pruebas de seguridad para garantizar la protección de datos cifrados.
- Pruebas de resiliencia para asegurar la disponibilidad de datos en caso de fallos de nodo.
- Optimización del algoritmo de replicación para mejorar el rendimiento.

### Demostración de funcionalidades

- **Carga de archivos:**
  ```bash
  curl -X POST -F 'archivo=@Actividad.txt' http://localhost:5000/cargar
