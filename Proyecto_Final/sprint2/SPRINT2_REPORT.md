# Reporte del Sprint 2

## Introducción
Este informe documenta el progreso del Sprint 2 del proyecto "Sistema de almacenamiento distribuido seguro". En este sprint, se enfocó en la implementación de las funciones de seguridad y replicación de datos, asegurando la disponibilidad y la tolerancia a fallos en el sistema de almacenamiento distribuido.

## Objetivos del Sprint 2
- Añadir cifrado de datos utilizando bibliotecas de criptografía en Python.
- Implementar técnicas de replicación de datos para garantizar la disponibilidad.
- Utilizar `asyncio` y `threading` para manejar la sincronización entre nodos.

## Progreso y Logros
- **Cifrado de Datos**:
  - Implementación de funciones para cifrar y descifrar archivos antes de almacenarlos en los nodos utilizando el algoritmo AES.
  - Aseguramiento de que las claves de cifrado se gestionen de manera segura y no se almacenen en texto plano.
  ```python
  def cifrar_archivo(data):
      cipher = AES.new(key, AES.MODE_EAX)
      ciphertext, tag = cipher.encrypt_and_digest(data)
      return cipher.nonce, tag, ciphertext

  def descifrar_archivo(nonce, tag, ciphertext):
      cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
      data = cipher.decrypt_and_verify(ciphertext, tag)
      return data

#### Replicación de Datos

- Desarrollo de un mecanismo de replicación que copia los archivos en varios nodos para garantizar la alta disponibilidad y la tolerancia a fallos.
- Implementación de políticas de replicación para optimizar el rendimiento y la redundancia.

```python
async def replicar_archivo_async(nodo, ruta_archivo):
    try:
        form = aiohttp.FormData()
        form.add_field('archivo', open(ruta_archivo, 'rb'), filename=os.path.basename(ruta_archivo))
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{nodo}/cargar", data=form) as response:
                logging.debug(f"Replicación en {nodo} completada con estado {response.status}")
    except Exception as e:
        logging.error(f"Error replicando en {nodo}: {e}")

def replicar_archivo(nodo, ruta_archivo):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(replicar_archivo_async(nodo, ruta_archivo))
    loop.close()


#### Sincronización entre Nodos

- Uso de `asyncio` para gestionar la comunicación asíncrona entre nodos y manejar la replicación en tiempo real.
- Implementación de `threading` para permitir la concurrencia y la ejecución de múltiples operaciones de entrada/salida simultáneamente.

```python
@app.route('/cargar', methods=['POST'])
def cargar_archivo():
    archivo = request.files['archivo']
    ruta_archivo = os.path.join(UPLOAD_FOLDER, archivo.filename)
    
    try:
        data = archivo.read()
        nonce, tag, ciphertext = cifrar_archivo(data)
        
        with open(ruta_archivo, 'wb') as file_enc:
            file_enc.write(nonce)
            file_enc.write(tag)
            file_enc.write(ciphertext)
        
        threads = [threading.Thread(target=replicar_archivo, args=(nodo, ruta_archivo)) for nodo in NODOS]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        
        logging.debug(f"Archivo {archivo.filename} cargado y cifrado exitosamente en {ruta_archivo}.")
        return 'Archivo cargado y cifrado exitosamente', 200
    except Exception as e:
        logging.error(f"Error al cargar y cifrar el archivo: {e}")
        return jsonify({'error': f'Error al cargar y cifrar el archivo: {e}'}), 500

    ## Desafíos y Soluciones

- **Gestión de Concurrencia**:
  - Superado utilizando `threading` para manejar múltiples operaciones simultáneas de entrada/salida.
- **Comunicación Asíncrona**:
  - Implementada con éxito utilizando `asyncio` y `aiohttp` para permitir la replicación en tiempo real.

## Próximos Pasos

- **Optimización del Sistema**:
  - Mejorar el rendimiento del sistema, optimizando la replicación y recuperación de datos.
- **Pruebas Adicionales**:
  - Realizar pruebas de carga y estrés para validar la robustez del sistema bajo diferentes condiciones.
- **Documentación y Presentación**:
  - Documentar todos los avances y preparar una presentación detallada con demostraciones en vivo del sistema funcionando.

## Conclusión

El Sprint 2 ha sido exitoso, logrando implementar las funcionalidades de cifrado y replicación de datos, cumpliendo con los objetivos planteados. El sistema ahora asegura la disponibilidad y la seguridad de los datos, sentando una base sólida para los siguientes sprint3.

