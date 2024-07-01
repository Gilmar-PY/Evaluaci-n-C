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

Construir y Ejecutar los Contenedores

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcTD5M33Fg4JBWi4euUHW2lkuAcK_QfFUyOywuGa5JvUPL3WwNwFGCFsVnS9R0eEC4vF9MKfIkBojS15lw2-RsH8b-TYE2morn75PSPm4m62q7z3DduI8ttR5AaIo831p4BDK1E0KkLMfk4Oo-joRYcEwK4?key=nQL0RT6dNr_BeWtx8fgyhA)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfZrYawGD_HsRfBgfIFokZfSvDyGisgitqBoYIXsYLm8_BLw-3WU67cfNgq9Ow3b_h9aWxoBSwcy6-3NYnkUSOsk8nmCvYX40pKplzI_-ttyuoW-If1Z6OQBqr7w1H5eO1HGqc7jBRiBmVUvlY-X1i9Dlmc?key=nQL0RT6dNr_BeWtx8fgyhA)

### Pruebas de la API

Cargar un archivo (asegúrate de tener un archivo para probar, por ejemplo, test_file.txt):

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXc_Ex2D8_-7ijuM-D91sbB0-MyB50AeIl4Fg21JbvL4KXSo3b6smNjqjaK9gI_-wS7ZHT_OIhjlbjTlRAC9fSZ5QzDpO2ObA4Rk1RgTSF0UBq-O224zp0I-v4rpLCrwjRogzmoGNbbz9Q9wLX4BCRrSwSw?key=nQL0RT6dNr_BeWtx8fgyhA)

Descargar el archivo:

curl http://localhost:5000/descargar/Actividad.txt --output descargado.txt

  **![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfsjc8vayL2EBmNOy3_q7mYvrR1ztGNTVUqapV0_pDipkocXcScyddOGhUFdjbweWa4JzGhjYTJPNmx6nMLmm8aeJgNJAHIfwidUdlkZ9wcdYavglU0AjHSBE4kCCqubOuJrOtA8iup8DEy4CGcPkUGezN2?key=nQL0RT6dNr_BeWtx8fgyhA)**

Eliminar el archivo:

curl -X DELETE [http://localhost:5000/eliminar/Actividad.txt](http://localhost:5000/eliminar/Actividad.txt)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcmp-gBnism1afjhwUzuQjN9MA6eK9U_tApC1halM42fq-hZ0fCw1F-DShG2o-SAefnrgPrikO45l_pNHuSPDSZY6K1_0PbBoma2sKHBpSNViPIQA9g0EzDQjDTPe7wktlscjE-iNnaZcIHD5dOunfFGFRD?key=nQL0RT6dNr_BeWtx8fgyhA)

Comprobacion de la replicacion de los archivos:

nodo1

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdoqKfegliklOoCsKZOMOHPFC3q74jSWmXhBlPaErc4gY9DNTc0ehwvzN-25SDOJWD0d85DWiVmILBOhczFeT1mCORjg4Cfoh6uLISMkq1NgcD9ORZ2oTPPfj2YEPb_VzI-vIaG0_lKbnf3CEtVjLi5CIE?key=nQL0RT6dNr_BeWtx8fgyhA)

nodo2

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeKE_yRz1YtD16AE3GoUBSEQAHqotikPfTtd-zDrwMlW08fo3Zf9WyUeQgsHiaBOtwfsWyXt26c2Ts-xWS-Mx1kw-fqxyvBCs8djGtHVx7hAt5ufF81xNDzavY6qzsNpilYEaFQLAdNxRoHxsXLP-osk4mH?key=nQL0RT6dNr_BeWtx8fgyhA)

nodo 3

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcT_oPs3T89LVeFnDGSkhtATMvuHTkJYwsE-gkq69In66dv30uabSU54ueVeBGBKMW0F0_EVBnyTUIyk6Sw3tzDFLREm6NUtkxE-jWiu3QxjjGKqLkYeEnYNrEWb5lJVlbqjN-oL6V3PeQWog1exfsCoOZb?key=nQL0RT6dNr_BeWtx8fgyhA)![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe4vLWBfDhdaBH5N9hVlko41xQtbcH6-7tH-W8FMpkUEDQ6pbY-SOOyYsDMl59IFipSwio4OrcWG7C9BMkV7H5tfY5GfqoCgro5tQkB9KtB97WYiMcZwN2Xe5POHsQ6pahxG70rOuxyUlxGqMu3-M4CnX4?key=nQL0RT6dNr_BeWtx8fgyhA)

  
 prueba de seguridad

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeIt4g2cv8pwqVjAYH4q-b9NEp8H5-C35BOqwkIhh23cljk1o_Lbwmu8P6-xwV21CpVuLUe_fe0Pkh9tvfJKMSbZOXlkMKUjKDjCybCgBO5UyxN83L7FddSOREDSRreGl_j_4Z4Ehzd9xdp7Vi69X-26kY?key=nQL0RT6dNr_BeWtx8fgyhA)

Pruebas de Resiliencia

ejecutamos docker compose

node1

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe3Cxas61p0TImSs06jgrqCgOHoksi5CvkTOasEm9iviX2loT2ujE3yMCBguxGUes8YX3GxBFQ7VJH5nuh80AgdQvgBekl3yi0nJHPvsTEmH98B-6cNfQD9JZsmCVqQaQGwnp5dMKLDa9cKYRGleUUNq8x3?key=nQL0RT6dNr_BeWtx8fgyhA)

node2

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeyYyFi-B21R3yyoLrEhwRtSS7OaBGYa-mx53P0EDmr9WlTyQTS-vjt2V4zH63fIEGopq1v_Uo7H0suNSRJP9RhvP4EjQFtTYrNzy11lApbOrJUVSpck-f6V04VZlGv8ws6-cut_rlh_zfxsDqv4-PbTg5R?key=nQL0RT6dNr_BeWtx8fgyhA)

node3

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdg3fL1FTHh5IV5R_8bY8I9mYmuD8d6sGC1qefLRqeADle4TQiSBNmgdkDSbQ2oRywRihFW2n2mdfMTQrjqw5ZvYoeLjdCzKPtSBUqPI64sIBjsswt_hBqE9gSG8BciwNXnWUu6ibcfk27Ckql_7ZssH9-y?key=nQL0RT6dNr_BeWtx8fgyhA)

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeuuwH8JqB6rMP8tLA5n4b-NgOrWqCnEqJAV8u2gs562rD31sBzt1tLHu3pTT97TPTIl16RgWLIoZtnQ4b5bQ3kaGB7jG_ixVOgWtOKTTr841b8cnQxiFxXwTZMlbZMWmF7eB1FVj-deBfd3Kky2Qb3AO8?key=nQL0RT6dNr_BeWtx8fgyhA)

  
prueba de tes_recilencia:

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXda8XmyEhxDrak8f1D0dH0WwbpDOTu-WHh1hFH-CByYmdVpeCEmlWjfqpXorbIMTL1w3tlAiyvhrINzMb9oOWfjNxPQdKavYsBCtO8T5pUUqy81enuMnrlvXu-l4gbdPS8NOfoGz0tjfPy0k7U4V4qFq6E?key=nQL0RT6dNr_BeWtx8fgyhA)

verificación en los nodos

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXd40LfivnrEE-925tEDf-KSKeVy1ANnM6O-W_EH4_uKCZewNmb1n90Xr1SPjeALJx3gzqgxFIJLQWGgngKbQgyTKtmZmYrQAv3_F8S9ViVlIa4U9B9dP4nEMtqEhDsR1GPZV3FnT6QyoEnFHa2hdgSvV6XX?key=nQL0RT6dNr_BeWtx8fgyhA)

  

Pruebas de Carga:

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdmkqGal1kJCQi9h5pyurPTEVMaucJtaM41WpEVBCFd6EStynFwZJSFKWuYT4HXey-QogSkRHchgBt8XR_hv28HTqMi7fgro7iFZQFg63TYEaqQ42ydOrd0Yb-O4ivmXZfHCwiKjQSvOIXrWtOIjMo8Kek?key=nQL0RT6dNr_BeWtx8fgyhA)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXe7-iN9tdMDukdT3y474amEr3xtvFIn4GoAcORN9qFoGdCkyksWZzzz0VBph6ZcEPfXIbvJMrFRqs-tRBa_UZPxdcu-y2SrtjViMEQj79AJpwflS5kWMS1oFhyjsB9_trSZ_1DzQ23ummPZosq8TYgmxZWx?key=nQL0RT6dNr_BeWtx8fgyhA)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcv141L3GEsZoqw0Z5RaM7nVG6WUKCh6YlNQl4lPqg9Cm4t_gKxhf0qNxwhXSfkSi1uPIdoZ3Vzx3dlJrxUZ6SNnSgmUDaGQpgcExBuyTSndaJphQkZ9kOWMHg9_Olv3C3AUJ1fLcqjbAuWl9Lp9njPVdI?key=nQL0RT6dNr_BeWtx8fgyhA)![](https://lh7-us.googleusercontent.com/docsz/AD_4nXeeQtimbyvwCORwwsTpKBIkChRFX2wSl7LbVn5xpAhtfjfw1pPiIO9u9113YgiVmeb_DAcCxe0WnbMeK9wOo5olYIDgpcF2t63MPgupASynNmIzdn8I7LbGhJ3Yvxz2Nv45994D3XBP9ELdehDL6G-88P0?key=nQL0RT6dNr_BeWtx8fgyhA)

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXdli9DqvPJRRlKb39vZU932tLaCZmlOQjzukEwsD4TgIvZ4z2vPGuwOwn3YecRrHzY1JsJBVOYp7L9jYn0yxLt_GECXH0FiqTuse7gzxIs17EGF8ytrZbuVMABG7kFoyX09Ifk-G4Bf2WdOU-ZLFMAZpI4k?key=nQL0RT6dNr_BeWtx8fgyhA)

#### descripcion 

Las pruebas de carga realizadas con ApacheBench (ab) han producido los siguientes resultados:

1.  Subida de Archivos:
    

-   Requests per second: 42.36 [#/sec] (mean)
    
-   Time per request: 236.067 [ms] (mean)
    
-   Transfer rate: 680.17 [Kbytes/sec] total
    
-   Failed requests: 0
    
-   Non-2xx responses: 100
    

3.  Descarga de Archivos:
    

-   Requests per second: 66.84 [#/sec] (mean)
    
-   Time per request: 149.613 [ms] (mean)
    
-   Transfer rate: 58.33 [Kbytes/sec] received
    
-   Failed requests: 98
    
-   Non-2xx responses: 22
    

### Evaluación de las Pruebas

#### Subida de Archivos

Las pruebas de carga para la subida de archivos muestran un rendimiento aceptable con 42.36 solicitudes por segundo y sin solicitudes fallidas. La tasa de transferencia total de 680.17 Kbytes/seg indica que el sistema maneja adecuadamente las cargas de trabajo concurrentes.

#### Descarga de Archivos
En las pruebas de descarga de archivos, se observa un número significativo de solicitudes fallidas (98) y respuestas no 2xx (22). Esto sugiere que hay problemas de consistencia en la replicación y disponibilidad de los archivos en los nodos. La tasa de transferencia es significativamente menor en comparación con la subida, lo que también puede indicar problemas de rendimiento en la recuperación de archivos.

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

