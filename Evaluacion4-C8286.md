## LABORATORIO 2

1.  Características y funciones de Amazon S3:
-   Almacenamiento de objetos: Amazon S3 es un servicio de almacenamiento basado en objetos que permite almacenar cantidades prácticamente ilimitadas de datos.
    
-   Durabilidad y disponibilidad: Ofrece una durabilidad del 99.9% y múltiples opciones de disponibilidad a través de zonas de disponibilidad geográficamente separadas.
    
-   Escalabilidad: Capacidad para manejar grandes volúmenes de datos sin degradación del rendimiento.
    
-   Seguridad: Soporta políticas de IAM, cifrado en tránsito y en reposo.
    
-   Acceso a través de API: Integración con AWS SDK que permite realizar operaciones como subir, bajar, y listar objetos mediante programación.
    
3.  Uso de Amazon S3 para almacenar y recuperar datos:
    
-   Almacenamiento escalable: Capacidad para ajustar el almacenamiento automáticamente conforme cambian las necesidades.
    
-   Recuperación eficiente: Uso de etiquetado y versionado para mejorar la organización y recuperación de datos.
    
-   Transfer Acceleration: Mejora de la velocidad de transferencia de datos utilizando redes optimizadas.
    
5.  Configuración de un bucket de Amazon S3:
-   Creación y configuración: Proceso para crear un bucket y establecer políticas de acceso.
-   Optimización: Estrategias para mejorar el rendimiento, como el uso de diferentes clases de almacenamiento (S3 Standard, IA, Glacier) según la frecuencia de acceso.
    
7.  Ventajas de Amazon S3 frente a otras soluciones:

-   Costo-efectividad: Menor costo por GB comparado con soluciones en las instalaciones.
    
-   Rendimiento: Capacidad para manejar cargas de trabajo de alto rendimiento con baja latencia y altas tasas de transferencia.
    
-   Flexibilidad: Adaptación a varios tipos de datos y patrones de acceso.
    
9.  Seguridad y privacidad en Amazon S3:
    
-   Controles de acceso: Uso de ACL y políticas de bucket para controlar quién puede acceder a los datos.
    
-   Cifrado: Opciones de cifrado en reposo y en tránsito para proteger los datos.
    
-   Conformidad: Cumplimiento con normativas como GDPR, HIPAA, mediante la gestión adecuada de datos.
11.  Los cinco Vs de los datos:
    
-   Volumen: Cantidad de datos generados y almacenados.
    
-   Velocidad: Rapidez con la que se recopilan y procesan los datos.
    
-   Variedad: Diversidad de tipos y fuentes de datos.
    
-   Veracidad: Fiabilidad y precisión de los datos.
    
-   Valor: Utilidad de los datos para generar insights y decisiones.
    
13.  Impacto de los cinco Vs en la gestión de datos:
    
-   Captura y almacenamiento: Adaptar infraestructuras para manejar volumen y velocidad.
    
-   Procesamiento: Utilizar tecnologías capaces de procesar variedad y asegurar la veracidad.
    
-   Visualización: Herramientas que permitan interpretar datos grandes y complejos, transformándolos en información valiosa.
    
15.  Planificación de una pipeline de datos:
    
-   Diseño técnico: Seleccionar tecnologías y arquitecturas que soporten los cinco Vs adecuadamente.
    
-   Implementación: Configuración de flujos de datos que maximicen la eficiencia en la captura, procesamiento y análisis.
    

17.  Influencia de la variabilidad de datos en decisiones tecnológicas:
    

-   Selección de herramientas: Elección basada en la necesidad de manejar volúmenes altos o la necesidad de procesamiento en tiempo real.
    
-   Arquitectura de datos: Diseño de sistemas que puedan adaptarse a cambios en la velocidad y volumen de datos.
    
19.  Plan estratégico para una pipeline de datos efectiva:
    
-   Evaluación de necesidades: Comprender las necesidades específicas de la organización en términos de datos.
    
-   Implementación de tecnologías: Utilizar soluciones como Amazon S3 y herramientas de big data para crear una infraestructura robusta.
    
-   Maximización del valor de los datos: Asegurar que los datos se transformen en información útil para decisiones estratégicas.
    
## Tarea 1: Crear una plantilla y una pila de CloudFormation

Navegue hasta el entorno de desarrollo integrado (IDE) de AWS Cloud9.

![](https://lh7-us.googleusercontent.com/jnB-A5j8X5TQMdbvMkcxeRBT3LEoUOssV_i18Njf65NXmd7yRr2rlHgju-KXCfQw-ImDHXzQ7kWw2aKhTAKWtt12FzkLdAkFDPzcl8TGt3Py8Pn2eYUNKxrUf7ZpZOB9kPwB4wlT1Q2AQmEdBDrPIcc)

Cree una nueva plantilla de CloudFormation.

-   En el IDE de AWS Cloud9, elija Archivo > Nuevo archivo .
    
-   Guarde el archivo vacío como create bucket.yml pero mantenlo abierto.
    
-   Copie y pegue el siguiente código en el archivo:
    

![](https://lh7-us.googleusercontent.com/8XQb1a_pD9hu5RpECZlCX-RfSR9g2inZEdqAGpl0fvr4IrElYShOPb8R25zmDjkiNa40JtnwkNDk6YfiapB5CCeq3SRRRozla43OxmKZ-Gp6GgziMLBb7qYQx7gxJNnr52eEH42foqxYPP2q4B2k_Fo)

![](https://lh7-us.googleusercontent.com/IU2bNgeKtpwEoDE-OBrSEVNZdg5jm2aRY7s9GxhDmti9Wu2z1tb1utDvNcD0bYMg805SttQJ8GbpFnDGflC99Hd0iOl_-Jciq1FSQ-jV7GkfXkojMskxW14Iu8Gcsl8vj7AZrHkZZjUn2g-xhvPhW8U)

  

![](https://lh7-us.googleusercontent.com/hqlUwDLuMQmUy3wVQeTD9kiLcAZX6L-kIzvtXMmqZuY4Cf7FoT1qR6wRTrSOj8d55BdPfQW9JicPSxwL0gu2jyBex-tkTVLCQzG89A-RnU1Ttw9RnanxBtsCpzxtBb888oJZYU3LMwCzZlDevyqrhYg)

  
  

![](https://lh7-us.googleusercontent.com/wKl_YwgfGQ6ej0YCBCdmq-WY6gOHmP5XElQgx1dgOB9ya6uprD1ikFpmIUcZhxqCS-_1sEOrUtZHUpVx3GtEfsyLrADDcR2a58aEVWsQ7TooQtCvPReTa3978etuZoM0cwtmt6DHKiweAts_880JCjs)

aws cloudformation list-stacks

![](https://lh7-us.googleusercontent.com/QhB0ndQfDt-dZesk3VKtgh_5srS-GZNQnaZhy2pgDjafrYVofar_of6Ma6L6Fky16JgVApt_FrMInN_uG_YiOmfrj3gBxtTknBliismorohBEJj9spmLO_e9ZRX0dpd9tzvbwROnwJiCeGplX4NgFN4)

  
  

![](https://lh7-us.googleusercontent.com/nn3v17AC7_ukpF7067unRll_dND5e5KZ-RAVws2m_cq9QWTqgNNjbzQP8eQ0AERspiwyQ9LInyoRS78wS29DuZ_3g_pleaEIm5SGPpHtgWEox-lBYt6IFAB4zidk16vIIW1h5X66Kz3NALUlD4FgYFU)![](https://lh7-us.googleusercontent.com/QGLRVQ0B5v7NI5ap5vLW5bLq1x8oQkjfQrk2IckgeLuisDZ4-d2q-t_wHJthG9OulN7702rmRr7zMQzGkrQQQLWQWo1D0iRxAFZHWKqBpkFvi44L06qCLwemXbMEAPpIaajEoOO6FPMK3LOyLBxH7Ro)

  

## Tarea 2: cargar datos de muestra en un depósito de S3

![](https://lh7-us.googleusercontent.com/P7pBdNZFcOpNiBWvIHN12E042WXK1B2UzDf4WVqvXfjdQL692uGHWaNY_KmthZOx2-aTQk0ar8z56Es3BVKhLVXO9FzGAvWufhZbh_WaysEaRyfmuW6HRX_AWsRU62C8_UqFwq7bKcZXxlmJ43wEc1k)

![](https://lh7-us.googleusercontent.com/0O6fXY7iMh1W86fl0rgJTBDtOZRHbw37ywn1EKsTKLPHRCtZJlGR5daqk2_k7PiiEBziO7gSEr8aveOG29y62p_w3pMDg_lmQCz9J7e1tEyPOuy273sABwGrHYmaRgnmE3Bm-GoWdL1zw6iGZUdY4Ko)

ade-s3lab-bucket--4320a250

![](https://lh7-us.googleusercontent.com/iWvVoxpjkwgOs80IxmityIuTVKMsTCkWdu37AnetN-mRcIhrrAzgtUmJN8nk9yn9hvyLmtM6DrJy_y1QPPdyFn-fYKPWR_HO0RbSw_DL9uYqJes-NWxhrtu0iocceFLqklMKKBg3k3hyWMCaj3bekbU)

  

![](https://lh7-us.googleusercontent.com/kzNpgjzfSdEj0Ndd8Kf34xSCxRzyoHnFOfz2WXkDDWliB4N6Eg6c5NXyJt5eWAYOoKAd8vlWXDXwCJr-ThQWl1V3s3VAiVWiVVZ2mEC7uqpkPfgskmQ9JbVnfopG1S7pkCE-F3FhHW_T-LJ2H_Rdr4Y)

  
  

## Tarea 3: Consultar los datos

![](https://lh7-us.googleusercontent.com/W2-kpSWCp_SgUV_K16TdmEmlU_pMDPjJbEIQ0hUr2ze8jN8r4k6efHXKqv3RCVFQ9IOwOejxDeZDg6gAY1vOTU-13vMEX5Gn1p1hAX89FrKaHjy056uMRXkzh5WO8nxHf8aT7CUHGCZbGAss6TtYPcc)

  

![](https://lh7-us.googleusercontent.com/Qy_tDA3FtFjy-H7_o2CV1XifhzQPturIcPrZgxw8P5SQ31WKes-jm-wyrfzIjFCUJjjw_LY4dXdrZzCNIw-8ta-WFyUl0vbcYs9Mi8uMiFVkrY5eaKY20yM1S7AzjnuQvrQdvWPZJ0oUzZfN5f26k90)

  

![](https://lh7-us.googleusercontent.com/zm58Lty1NVSF0XxxGhqpOjkiC6DHwe8EQpgW550ciatPS984YlKLRo0ra4gjoOLrjfFKsI7O_FlTRdERQDvCr89KDpVzVz00hO6VJ_UpdvSUWBqDX0Ls4Fmn--2UrryZmZzobC01zwbJLxmAwNlm5go)

  

![](https://lh7-us.googleusercontent.com/iMYNo-0O03TySCVPhJb6uGSaV3nzk3hM1eO2Gsz8yGzSz1i7-pE2mibyYbvwAUcZLg95HO0luHvkCJ8B5NtOmFDQkIOcYXzJ9TN2XhDCmc2ofv0Ld7aqPafCDYORWOfmbTFo0iZ2bEUTzdgT2sVgbxg)

  

## Tarea 4: Modificar las propiedades de cifrado y el tipo de almacenamiento de un objeto

![](https://lh7-us.googleusercontent.com/w5OMOZjmVbk_1rNsKOf9oWnE0UrtzZ2qXSEZn9du_zmBQYJXMM_DhIS0pe1ri35nSzSGvUkB9MkvsEV4GFDcaXWI-lJ2nxquyg7214sb6vIpD03cvqza99bjcC4_YbLQAhBOpNviYLm2Y2AnfwvIAMw)

## Tarea 5: comprimir y consultar el conjunto de datos

![](https://lh7-us.googleusercontent.com/c1Ag9AxTij2NMZE2GSAKvLDodFjLCNsNA6cAjrPeO313vJTWQFDrWCVNE1TttgXfdciiEWokIRiWDXlPCL78Q2qbg3-cbkvsHgtSwqVS8x2R0ftpG_nKXz-VPnxRJ30w7x5qqKkbR2dPtmvpNTRe1I8)

![](https://lh7-us.googleusercontent.com/aw34wiVwVqMwW7ZHpVxSZ-2T6KbWMQpcEz-P0GB2qfdAkNqVo2lHg-Z_yKf3lRyELZxj_GFCmRs9qxojlc1BwuqRdbpLER5psHeS9k-zvDyhddIR08-POS5n4gVfdba9rO2ZnKga3fEbQQExWcYcmMQ)

![](https://lh7-us.googleusercontent.com/IOz43Ax0I6nox2B4OHamp15lSa1KJvEuUItmn1yEBs_y-sASOsJkWDbobXOsjP16mWiMhUcqbf967PJFnMZt1dGiSf44IFCTFwNEmS4vAipcKM6SOR1RplgLlejgZPN1fNxcadVBB-cPAjp9lrI7slg)

![](https://lh7-us.googleusercontent.com/5UsIVJ46b8maRFB-ez-5VgOXicXs_96El6Nyhrxbg52lwkwG6EWv34NYAwY3XyA6nJ_IBJmE7ki_-2fE8PUh3HKJuZcnyQIhTANG5rAS9jFtrHWTSmY9OiWBSA8Vt56fB0WCafPl9d8hyUPz6BdD3uY)

![](https://lh7-us.googleusercontent.com/5cfIjkRoyKdORD43f-gGC1WmgBccuc9viF6c0qUKpdtoVmU4HZpshDowaGKs23XhlQ1C53Qo4F9RhrF--26zj5hq4K4nserBpQTtMA6UbmDtO47wln_rreETiBgw_25Oe_CyIWHyn_Pk7NUkEDGzZaw)

  
# Module 3 Knowledge Check

![](https://lh7-us.googleusercontent.com/yQR3di8MQQhuoLMy-on_lIbJBlxk0dxmwIpvQ1KTf0KjxiDsR059Ef3W4S8UMs321wtQlyVFiBgirJ2yMrCGbCVfwtXsiw1sa3wcxH1_3ulINWa4Of-4oEfQURuML3d5qzDhrtZTlrHuHhl5kTc6Jbk)