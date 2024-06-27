# Reporte del Sprint 1

## Introducción
Este informe documenta el progreso del Sprint 1 del proyecto "Sistema de almacenamiento distribuido seguro".

## Objetivos del Sprint 1
- Investigar técnicas de almacenamiento distribuido y criptografía.
- Configurar un entorno distribuido con múltiples nodos utilizando Docker.
- Implementar un sistema básico de almacenamiento de archivos.

## Progreso y Logros
- **Investigación Completa**: Se investigaron HDFS y Ceph para almacenamiento distribuido y se exploraron las bibliotecas pycryptodome y cryptography para criptografía.
- **Configuración del Entorno con Docker**: Se configuraron nodos Docker y se crearon imágenes personalizadas.
- **Implementación del Sistema de Almacenamiento**: Se desarrolló una API RESTful para cargar, descargar y eliminar archivos, incluyendo funcionalidad de cifrado.

## Desafíos y Soluciones
- **Configuración Inicial de Docker**: Superado mediante la creación de Dockerfiles detallados.
- **Cifrado y Descifrado de Archivos**: Implementado con éxito utilizando la biblioteca pycryptodome.

## Próximos Pasos
- **Implementar Replicación de Datos**: Asegurar la disponibilidad de los datos replicándolos en múltiples nodos.
- **Mejorar la Gestión de Claves**: Implementar un sistema seguro para la gestión y almacenamiento de claves.
- **Pruebas Adicionales**: Realizar pruebas de carga y estrés para validar la robustez del sistema.



