# Reporte del Sprint 2

## 1. Introducción

### Objetivos del Sprint
El objetivo principal del Sprint 2 fue implementar funciones de seguridad y replicación de datos en el sistema de almacenamiento distribuido. Estos objetivos se alinean con los objetivos generales del proyecto al asegurar la disponibilidad y la tolerancia a fallos del sistema. Los objetivos específicos fueron:

- Añadir cifrado de datos utilizando bibliotecas de criptografía en Python.
- Implementar técnicas de replicación de datos para garantizar la disponibilidad.
- Utilizar asyncio y threading para manejar la sincronización entre nodos.

## 2. Planificación

### Tareas planificadas
- Implementar cifrado de datos con AES.
- Desarrollar funciones de replicación de archivos entre nodos.
- Configurar la sincronización asíncrona y concurrente.
- Realizar pruebas de carga, descarga y eliminación de archivos.
  
### Asignación de tareas
- **Cifrado de datos:** 
- **Replicación de datos:** 
- **Sincronización entre nodos:** 
- **Pruebas y documentación:**

### Cronograma
| Tarea                               | Inicio | Fin   | Hitos Importantes              |
|-------------------------------------|--------|       |--------------------------------|
| Implementación del cifrado de datos |        |       | Cifrado funcional              |
| Desarrollo de replicación de datos  |        |       | Replicación funcional          |
| Configuración de sincronización     |        |       | Sincronización configurada     |
| Pruebas y documentación             |        |       | Documentación completa         |

## 3. Implementación

### Descripción del trabajo realizado
Durante este sprint, se implementaron las funciones de cifrado y replicación de datos. Se tomó la decisión de utilizar AES para el cifrado debido a su eficiencia y seguridad. La replicación de archivos entre nodos se manejó mediante una combinación de asyncio y threading para asegurar la concurrencia y la comunicación asíncrona.

### Algoritmos y métodos
- **Cifrado AES:**
  ```python
  def cifrar_archivo(data):
      cipher = AES.new(key, AES.MODE_EAX)
      ciphertext, tag = cipher.encrypt_and_digest(data)
      return cipher.nonce, tag, ciphertext


