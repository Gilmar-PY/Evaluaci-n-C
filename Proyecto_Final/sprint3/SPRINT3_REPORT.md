
# Reporte del Sprint 3

## 1. Introducción

### Objetivos del Sprint

El objetivo principal del Sprint 3 fue optimizar el sistema de almacenamiento distribuido, realizar pruebas de seguridad y resiliencia para garantizar la protección y disponibilidad de los datos.
## 2. Planificación

### Tareas planificadas

- Realizar pruebas de seguridad para identificar posibles vulnerabilidades.
- Ejecutar pruebas de resiliencia para simular fallos de nodos y verificar la recuperación de datos.
- Optimizar el algoritmo de replicación para reducir la latencia y mejorar el rendimiento.

### Asignación de tareas

- **Pruebas de seguridad:** 
- **Pruebas de resiliencia:** 
- **Optimización del algoritmo de replicación:** 

### Cronograma

- **Inicio:** 
- **Fin:** 30 de Junio

## 3. Implementación

### Descripción del trabajo realizado

#### Pruebas de seguridad
Se implementaron pruebas para garantizar que los datos cifrados no pudieran ser accedidos sin la clave adecuada. Estas pruebas confirmaron la efectividad del cifrado AES implementado.

#### Explicación del script

Este script se utiliza para probar la seguridad del sistema de almacenamiento distribuido asegurándose de que los datos cifrados no se puedan acceder sin la clave correcta. A continuación, se presenta una explicación general del código:

#### Código Completo

     ```python
     import requests
     from Crypto.Cipher import AES
     import os

     # Configuración
     key = b'This_is_a16b_key'
     UPLOAD_FOLDER = 'cargas'
     os.makedirs(UPLOAD_FOLDER, exist_ok=True)
     url_cargar = 'http://localhost:5000/cargar'

     # Cargar archivo
      files = {'archivo': open('Actividad.txt', 'rb')}
     response = requests.post(url_cargar, files=files)
     print(response.text)

     print("Carga exitosa. Probando acceso sin clave...")

     # Intentar descifrar sin clave correcta
     ruta_archivo = os.path.join(UPLOAD_FOLDER, 'Actividad.txt')
     try:
        with open(ruta_archivo, 'rb') as file_enc:
            nonce = file_enc.read(16)
            tag = file_enc.read(16)
            ciphertext = file_enc.read()
    
         cipher = AES.new(b'Incorrect_Key123', AES.MODE_EAX, nonce=nonce)
         data = cipher.decrypt_and_verify(ciphertext, tag)
         print("Prueba de seguridad fallida: Se pudo descifrar el archivo con una clave incorrecta.")
     except Exception as e:
         print("Prueba de seguridad exitosa: No se pudo descifrar el archivo con una clave incorrecta.")



#### Pruebas de resiliencia

Se simularon fallos en los nodos para verificar que los datos pudieran ser recuperados desde los nodos replicados. Las pruebas mostraron que el sistema es capaz de manejar fallos de nodos sin pérdida de datos.

### Explicación 

Este script `test_resiliencia.py` se utiliza para probar la resiliencia del sistema de almacenamiento distribuido simulando un fallo en uno de los nodos y verificando que el sistema sigue siendo capaz de descargar los archivos replicados desde otros nodos. A continuación, se presenta una explicación detallada del código:

        ```python
         # test_resiliencia.py
         import requests
         import docker
         import time

         # Configuración
         client = docker.from_env()
         url_cargar = 'http://localhost:5000/cargar'
         url_descargar = 'http://localhost:5000/descargar/Actividad.txt'

         # Cargar archivo
         files = {'archivo': open('Actividad.txt', 'rb')}
         response = requests.post(url_cargar, files=files)
         print("Archivo cargado exitosamente. Ejecutando prueba de fallo de nodo...")

         # Simular fallo de nodo
         try:
             container = client.containers.get('storage-node-1')
             container.stop()
             print("Nodo storage-node-1 detenido.")
    
             # Esperar un momento
              time.sleep(5)
    
              # Intentar descargar el archivo
              response = requests.get(url_descargar)
              with open('descargado_resiliencia.txt', 'wb') as f:
                  f.write(response.content)
    
                   print("Archivo descargado exitosamente después del fallo del nodo.")
    
              # Reiniciar el nodo
               container.start()
               print("Nodo storage-node-1 reiniciado.")
               except Exception as e:
               print(f"Error durante la prueba de fallo de nodo: {e}")


#### Optimización del Sistema

Se realizaron mejoras en el algoritmo de replicación para reducir la latencia y el tiempo de recuperación de datos. Se verificó que los datos se replicaran en tiempo real en todos los nodos.

### Funcionalidades desarrolladas

- Pruebas de seguridad para garantizar la protección de datos cifrados.
- Pruebas de resiliencia para asegurar la disponibilidad de datos en caso de fallos de nodo.
- Optimización del algoritmo de replicación para mejorar el rendimiento.

#### 4. Resultados

#### Demostración de funcionalidades


![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfA_lz9I6ro0eq6YKkqTt8JMvaafec7Ntj6fU8mDVKniwx-QWfBPgJx4dHeqL9Xx9cBTeCeAhpBybLznXal31fzEGJl62dbu6SNO-iOlBA-HLI3hy_STbAyqkX9pcKr7KJNwWHVZpCsBFoEkPIrg44cdjo?key=nQL0RT6dNr_BeWtx8fgyhA)

#### Pruebas de Resiliencia

#### ejecutamos docker-compose 

#### node1

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdH4KDwoLZXf2PCmou8N-wpk8BXpX-dpKweq77nV58K_Ou3T6RfGdx_xioHBPinArSglmpnj0P0HTsdoEaKywOA1-rlE_PFEgKSGeKyys1jEYu22OggnHbc4ppL8Kn0LO7jikcDIgOdsWeOAU4uwyApVD5U?key=nQL0RT6dNr_BeWtx8fgyhA)

#### node2

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdy65xYCNimIFP8olKgo5TZeH6laWYGV89kPxpZxUw9kC36TfdVHl_5gmXeDmqVy8rkTp-x8pY_3TB1lFRaEkD07vFGcsml9koMXIwZZGfp2UHJfkDY9RQHwrGaIDIL6JV9LqppeEl85fxFaR-knhx9g84S?key=nQL0RT6dNr_BeWtx8fgyhA)

#### node3

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfcodrdPXXlolfBeAe_vYTy1-QPIg5Wa2CIaejhruXgsTG8XKGV0YlYIiB6RWTULaNjgbxGk0dFJ7KzpFNc54ZNQZBd8QYnujKA7ffToVdTlLbj63DTmpHcIGBZiMeBOTbOg49G3jmgWs4BIxhPYcmKegma?key=nQL0RT6dNr_BeWtx8fgyhA)

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXf-FXJaUi8Hua7TMbZ1hmOXhAa9ZiKyhPu9Oy2chBdghQsW-BEW-Xn3pKfEOo4pD3zw5vqLgBtWr1hSV8e_3pfhnsstZnQs1yzpYPRCsZen_zKHFUs8pzs75P-q0iDYWCBd1ICev53CW315R_NLRuoBdQQ?key=nQL0RT6dNr_BeWtx8fgyhA)

  

####  prueba de tes_recilencia:

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfFmoGprJlawg2w4srL3RHF2aM3T1bbBsNWaDMh1M0nvC2UtZ2gO0YlgjAcpJavN9J2uf_pQHF-rKQHD6C79v_6ZjpMvpT_Bs-qvhaYIWNDiOwjNvF_vwptetgBsDWIirUnfhS_lIL8_QhW_U2oOPOcRwA?key=nQL0RT6dNr_BeWtx8fgyhA)

#### verificación en los nodos

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXd_dCC3-yW9bQs1yrdCTfx22IaJVZdoWWJsUG4v0nLexiHgBHHNTc1geqCchJwjg3pvaeUt1ZG4Ry8fvATAo6Qhr7ePaTewfpCOCdd8B7e3Y5q3QXaQwc8yc8BHPXfDaWIE3qJDUDKRbdw_g8fMly5I55vC?key=nQL0RT6dNr_BeWtx8fgyhA)

  

#### Pruebas de Carga:


![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeJs6xOSegyis_FIG4nx14mzKqZm1_rhTUCdpUFsauws0-2Pfj5Vf3lmrmWJpW-GOIICbZh2_Tykgm_Hdw_yax3MvFMtrIFoLRGIvXove-SvGKDrQZ_mg5Ml9bFETTmv4LIeQ3SNg-72NsuKzIpPhW5C44?key=nQL0RT6dNr_BeWtx8fgyhA)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdDNH8OpEbm9J6BnD1ZKKk_HdPxYPeqGba_JpRBGr8U2SQ5cZDPTyVm6aFCHKQCtV5yTH7MJYvYWFWNaQHZU2cBIaDwTKWaaIGjCXjnB34Iuwe5yCPBpwywcmFt2UMd0wAZN0woofNynMv9pZ1khWMC9OLX?key=nQL0RT6dNr_BeWtx8fgyhA)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXc4qyUAkXzHCoBvC8PBa61-gsd1MUg_VmnHjgGIiRWT6bUOyZn9JDfUTo5JOh_1isPPMfzBhZoY1MhxfxSbE-P5TWjRBOBYYkC7I53qWO1ldvDzctJvL5kblepFTvaQnA5bv2DER8jXO8Xwn_K3Mhk42ZI?key=nQL0RT6dNr_BeWtx8fgyhA)![](https://lh7-us.googleusercontent.com/docsz/AD_4nXejVYpWcgLTjk3nSAe1hx3VC8PSxFA6oYRNvLm74wuQS3rwZ-BGyAzpjlP9eE97s-29fipPRZHBiGHKWeYpbuv0OAcxNRE1m1IuQp3aykwnREo20thyiz89cHtDuTON0jcdjgNsIdsIVAxW4YlJiVO7K_g?key=nQL0RT6dNr_BeWtx8fgyhA)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfpzw0Mfl3enkeUi8EOLy4VOXLGhagoau3clQcqQTgg3r8PmrZ8cN9NdzYL-aGqylm2DhU8OmGWANr2AzEKU_wMTcv69kojc79y9Va9ALqaHF2c-9dYeB0xXTcVx3KhjiWUg9BLYzc8HT6LToERqnVQ2K6Y?key=nQL0RT6dNr_BeWtx8fgyhA)


#### 5. Análisis y Evaluación

#### Comparación con los objetivos del Sprint

El trabajo realizado Se lograron implementar las funcionalidades de pruebas de seguridad y resiliencia, así como la optimización del sistema no fue completamente, pero si mejoro.

#### Lecciones aprendidas

- **Gestión de excepciones:** La importancia de manejar adecuadamente las excepciones en sistemas distribuidos para garantizar la recuperación de fallos sin comprometer la integridad de los datos.
- **Optimización de recursos:** La necesidad de optimizar el uso de recursos para manejar grandes volúmenes de datos de manera eficiente.
- **Seguridad en la gestión de claves:** La importancia de gestionar las claves de cifrado de manera segura.


#### 6. Plan para el próximo Sprint

#### Objetivos del próximo Sprint

El siguiente sprint se enfocará en consolidar y finalizar todas las funcionalidades del sistema de almacenamiento distribuido. Los objetivos específicos incluyen:

- **Refinamiento del sistema:** Realizar ajustes y mejoras basadas en los resultados de las pruebas realizadas en el Sprint 3.
- **Documentación completa:** Elaborar documentación exhaustiva del sistema, incluyendo manuales de usuario y de instalación.
- **Presentación del proyecto:** Preparar y ensayar la presentación final del proyecto para stakeholders y posibles usuarios.

### Ajustes necesarios

- **Mejora de la gestión de claves de cifrado:** Implementar medidas adicionales para asegurar la gestión segura de las claves de cifrado, basándonos en las lecciones aprendidas durante el Sprint 3.
- **Optimización de la replicación:** Continuar mejorando el algoritmo de replicación para reducir aún más la latencia y asegurar la consistencia de los datos.
- **Documentación técnica:** Asegurar que toda la documentación técnica esté actualizada y sea fácil de entender, para facilitar la adopción y el mantenimiento del sistema por parte de otros desarrolladores y usuarios.

Con estos ajustes y tareas planificadas, el próximo sprint se centrará en pulir y completar el proyecto, asegurando que esté listo para su presentación y posible implementación.


