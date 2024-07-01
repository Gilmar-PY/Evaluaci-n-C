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



## 3. Implementación

### Descripción del trabajo realizado
Durante este sprint, se implementaron las funciones de cifrado y replicación de datos. Se tomó la decisión de utilizar AES para el cifrado debido a su eficiencia y seguridad. La replicación de archivos entre nodos se manejó mediante una combinación de asyncio y threading para asegurar la concurrencia y la comunicación asíncrona.

## Cifrado de datos

### Descripción
El cifrado de datos es fundamental para garantizar la seguridad de los archivos almacenados en el sistema distribuido. En este sprint, implementamos funciones para cifrar y descifrar archivos antes de almacenarlos en los nodos, utilizando el algoritmo de cifrado simétrico AES (Advanced Encryption Standard).

### Implementación
Las funciones de cifrado y descifrado se integraron en el proceso de carga y descarga de archivos. Esto asegura que los archivos sean cifrados antes de ser almacenados y descifrados al ser recuperados.

#### Código

- **Función para cifrar archivos:**
  ```python
  def cifrar_archivo(data):
      cipher = AES.new(key, AES.MODE_EAX)
      ciphertext, tag = cipher.encrypt_and_digest(data)
      return cipher.nonce, tag, ciphertext

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




## Sincronización entre nodos

### Descripción
La sincronización entre nodos es crucial para garantizar que los datos estén disponibles y actualizados en todos los nodos del sistema distribuido. En este sprint, implementamos la sincronización utilizando `asyncio` para manejar la comunicación asíncrona entre nodos y `threading` para permitir la concurrencia y la ejecución de múltiples operaciones de entrada/salida simultáneamente.

### Implementación
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


