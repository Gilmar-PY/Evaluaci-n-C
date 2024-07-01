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
- **Cifrado de datos:** Implementación del cifrado y descifrado utilizando AES.
- **Replicación de datos:** Desarrollo de funciones para replicar archivos entre nodos utilizando asyncio y aiohttp.
- **Sincronización entre nodos:** Configuración de threading para manejar la concurrencia.
- **Pruebas y documentación:** Realización de pruebas de carga, descarga y eliminación, y documentación del proceso.

## 3. Implementación

### Descripción del trabajo realizado
Durante este sprint, se implementaron las funciones de cifrado y replicación de datos. Se tomó la decisión de utilizar AES para el cifrado debido a su eficiencia y seguridad. La replicación de archivos entre nodos se manejó mediante una combinación de asyncio y threading para asegurar la concurrencia y la comunicación asíncrona.

### Cifrado de datos

#### Descripción
El cifrado de datos es fundamental para garantizar la seguridad de los archivos almacenados en el sistema distribuido. En este sprint, implementamos funciones para cifrar y descifrar archivos antes de almacenarlos en los nodos, utilizando el algoritmo de cifrado simétrico AES (Advanced Encryption Standard).

#### Implementación
Las funciones de cifrado y descifrado se integraron en el proceso de carga y descarga de archivos. Esto asegura que los archivos sean cifrados antes de ser almacenados y descifrados al ser recuperados.

##### Código

- **Función para cifrar archivos:**
  ```python
  def cifrar_archivo(data):
      cipher = AES.new(key, AES.MODE_EAX)
      ciphertext, tag = cipher.encrypt_and_digest(data)
      return cipher.nonce, tag, ciphertext

----------------------------------------------------------------------------------------
## Replicación de datos

### Descripción

La replicación de datos es esencial para asegurar la alta disponibilidad y la tolerancia a fallos en el sistema de almacenamiento distribuido. En este sprint, se desarrolló un mecanismo de replicación que copia los archivos en varios nodos, utilizando llamadas asíncronas con `asyncio` y `aiohttp`.

### Implementación

Las funciones de replicación se diseñaron para copiar los archivos cifrados a otros nodos en tiempo real, asegurando que los datos estén disponibles incluso en caso de fallo de uno de los nodos.

#### Código

- **Función asíncrona para replicar archivos:**
  ```python
  async def replicar_archivo_async(nodo, ruta_archivo, nonce, tag):
      try:
          form = aiohttp.FormData()
          with open(ruta_archivo, 'rb') as file_enc:
              data = file_enc.read()
          form.add_field('archivo', data, filename=os.path.basename(ruta_archivo))
          form.add_field('nonce', nonce.hex())
          form.add_field('tag', tag.hex())
          async with aiohttp.ClientSession() as session:
              async with session.post(f"{nodo}/cargar", data=form) as response:
                  if response.status != 200:
                      logging.error(f"Error replicando en {nodo}: {response.status}")
                  else:
                      logging.debug(f"Replicación en {nodo} completada con estado {response.status}")
      except Exception as e:
          logging.error(f"Error replicando en {nodo}: {e}")

### Sincronización entre nodos

#### Descripción

La sincronización entre nodos es crucial para garantizar que los datos estén disponibles y actualizados en todos los nodos del sistema distribuido. En este sprint, implementamos la sincronización utilizando `asyncio` para manejar la comunicación asíncrona entre nodos y `threading` para permitir la concurrencia y la ejecución de múltiples operaciones de entrada/salida simultáneamente.

#### Implementación

Para lograr la sincronización, se crearon funciones que permiten replicar los archivos cargados en el nodo principal a otros nodos del sistema. Esto se hace en tiempo real para asegurar la alta disponibilidad y la redundancia de los datos.

#### Código

- **Función para cargar archivos y replicarlos en otros nodos:**
  ```python
  @app.route('/cargar', methods=['POST'])
  def cargar_archivo():
      archivo = request.files['archivo']
      ruta_archivo = os.path.join(UPLOAD_FOLDER, archivo.filename)
      
      try:
          # Cifrar el archivo
          cipher = AES.new(key, AES.MODE_EAX)
          data = archivo.read()
          ciphertext, tag = cipher.encrypt_and_digest(data)
          
          # Guardar el archivo cifrado
          with open(ruta_archivo, 'wb') as file_enc:
              file_enc.write(cipher.nonce)
              file_enc.write(tag)
              file_enc.write(ciphertext)
          
          # Replicar el archivo en otros nodos
          for nodo in NODOS:
              queue.put((nodo, ruta_archivo, cipher.nonce, tag))
          
          logging.debug(f"Archivo {archivo.filename} cargado y cifrado exitosamente")
          return 'Archivo cargado y cifrado exitosamente', 200
      except Exception as e:
          logging.error(f"Error al cargar y cifrar el archivo: {e}")
          return jsonify({'error': f'Error al cargar y cifrar el archivo: {e}'}), 500

## Desafíos encontrados

- **Gestión de claves de cifrado:** Se encontró que la gestión de claves debía ser segura y no estar almacenada en texto plano.
- **Sincronización de nodos:** La configuración de la comunicación asíncrona presentó desafíos de manejo de excepciones y errores de red.
- **Integridad de archivos replicados:** Se identificó la necesidad de verificar la integridad de los archivos replicados.

## Resultados

### Funcionalidades desarrolladas

- Cifrado de archivos con AES.
- Replicación de archivos entre nodos utilizando asyncio y threading.
- Sincronización de archivos en tiempo real.

### Pruebas realizadas

- **Pruebas de carga:** Verificación del rendimiento del sistema al cargar archivos.
- **Pruebas de descarga:** Aseguramiento de que los archivos cifrados se pueden descargar y descifrar correctamente.
- **Pruebas de eliminación:** Confirmación de que los archivos se eliminan correctamente y se replica esta acción en todos los nodos.
------------------------------------------------------------------------------------------------------------------------------
### Demostración de funcionalidades

- **Carga de archivos:**
  ```bash
  curl -X POST -F 'archivo=@Actividad.txt' http://localhost:5000/cargar

    ```bash
    curl -O http://localhost:5000/descargar/Actividad.txt

- **Eliminar archivos:**
  ```bash
  curl -X DELETE http://localhost:5000/eliminar/Actividad.txt

-----------------------------------------------------------------------------------------------------------------------------
## Análisis y evaluación

Se lograron implementar las funcionalidades de cifrado y replicación, y se comprobó que la sincronización y la disponibilidad de los datos son efectivas. Se identificaron áreas de mejora para la eficiencia del algoritmo de replicación y la gestión de claves de cifrado.

### Lecciones aprendidas

- **Gestión de excepciones:** Es crucial implementar un manejo de excepciones robusto para garantizar que el sistema pueda recuperarse de fallos inesperados sin comprometer la integridad de los datos.
- **Optimización de recursos:** La importancia de optimizar tanto el uso de la CPU como la memoria para manejar grandes volúmenes de datos de manera eficiente.
- **Seguridad en la gestión de claves:** Es esencial asegurar que las claves de cifrado no se almacenen en texto plano y que se implementen medidas adicionales para protegerlas.

## Plan para el próximo Sprint

### Objetivos del próximo Sprint

- Realizar pruebas de seguridad y resiliencia del sistema.
- Optimizar la replicación y recuperación de datos.

### Ajustes necesarios

- Mejorar la gestión de claves de cifrado para mayor seguridad.
- Optimizar la replicación de datos para reducir la latencia.
