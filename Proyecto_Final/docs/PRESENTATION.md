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



  -------------------------------------------------------------------------------------------------------

  # ANÁLISIS Y EVALUACIÓN

## Comparación con los objetivos del Sprint

El trabajo realizado se alinea bien con los objetivos del sprint. Se lograron implementar las funcionalidades de pruebas de seguridad y resiliencia, así como la optimización del sistema.

## Lecciones aprendidas

- **Gestión de excepciones:** La importancia de manejar adecuadamente las excepciones en sistemas distribuidos para garantizar la recuperación de fallos sin comprometer la integridad de los datos.
- **Optimización de recursos:** La necesidad de optimizar el uso de recursos para manejar grandes volúmenes de datos de manera eficiente.
- **Seguridad en la gestión de claves:** La importancia de gestionar las claves de cifrado de manera segura.

# CONCLUSIÓN Y FUTURO TRABAJO

## Logros

- Las funciones de preprocesamiento de datos y cifrado cumplieron con los objetivos planteados.
- Se logró crear una arquitectura de red para la gestión de archivos en un entorno distribuido.
- Se implementaron técnicas de replicación y sincronización para asegurar la disponibilidad de los datos.
- Se mejoró el rendimiento del sistema mediante la optimización del algoritmo de replicación.

## Mejoras

- Implementar una cola de tareas para mejorar la gestión de las cargas de trabajo.
- Considerar la cuantización aware-training para optimizar la precisión y el tiempo de procesamiento.

# Plan para el próximo Sprint

## Objetivos del próximo Sprint

- Integrar pruebas de carga y estrés para evaluar el rendimiento del sistema bajo condiciones extremas.
- Implementar mecanismos de monitoreo y alerta para detectar y responder a fallos en tiempo real.
- Documentar y presentar los resultados finales del proyecto.

## Tareas planificadas

- **Pruebas de carga y estrés:** Realizar pruebas intensivas para evaluar el rendimiento y la estabilidad del sistema.
- **Monitoreo y alerta:** Implementar herramientas para monitorear el estado del sistema y alertar en caso de problemas.
- **Documentación final:** Preparar la documentación detallada del proyecto, incluyendo los resultados de las pruebas y las conclusiones.

## Ajustes necesarios

- Mejorar la gestión de excepciones para manejar mejor los fallos inesperados.
- Optimizar la replicación de datos para reducir aún más la latencia.
- Documentar más detalladamente el código y los procesos implementados.

