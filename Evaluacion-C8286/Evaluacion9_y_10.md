
MÓDULO 9

  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcWVJMgbi4AsNsLkMnEjhy50NeLHjeN1SG_OExZFSVuvljPKiVJZsWUp4E7YgZNBoR8q0IumTGGVBaViK42F19uh3m-fpb8uo7J-n5jlwhXDK7v23ngYy3YN8fBkJViC8n8SeA1j-FuMNJCWqUryqzyuT7WwG780OZpRy-O?key=5OBIL_W6iV16g3AESCwYOQ)

  

#### 1. Ciclo de Vida del Aprendizaje Automático (ML)

-   Definición de Problema: Identificar y definir el problema que se resolverá con ML.
    
-   Recopilación de Datos: Obtener datos relevantes y de calidad para entrenar el modelo.
    
-   Preprocesamiento: Limpiar y preparar los datos para el entrenamiento.
    
-   Ingeniería de Características: Transformar datos brutos en características útiles para el modelo.
    
-   Entrenamiento: Utilizar datos para entrenar el modelo ML.
    
-   Evaluación: Validar y ajustar el modelo para mejorar su rendimiento.
    
-   Despliegue: Implementar el modelo en producción.
    
-   Mantenimiento: Monitorear y mantener el modelo post-despliegue.
    

#### 2. AWS SageMaker

-   SageMaker Ground Truth: Herramienta para etiquetar datos de manera eficiente y rentable.
    
-   Preprocesamiento y Ingeniería de Características: Utilización de SageMaker para preparar y transformar datos.
    
-   Entrenamiento de Modelos: Usar SageMaker para entrenar modelos de ML.
    
-   Despliegue de Modelos: Desplegar modelos entrenados en SageMaker en un entorno de producción.
    

#### 3. Almacenamiento y Procesamiento de Datos

-   Presto: Motor de consulta SQL en memoria, ideal para consultas rápidas.
    
-   Apache Hadoop: Framework escalable y de código abierto para almacenar y procesar grandes volúmenes de datos.
    

-   HDFS (Hadoop Distributed File System): Sistema de archivos distribuido que permite almacenar grandes conjuntos de datos.
    
-   MapReduce: Modelo de programación para procesamiento paralelo de grandes conjuntos de datos.
    

-   Apache Spark: Framework de procesamiento distribuido que utiliza RDDs (Resilient Distributed Datasets) para la tolerancia a fallos y la eficiencia.
    

-   Spark MLlib: Biblioteca de ML para Spark, diseñada para algoritmos iterativos y de múltiples etapas.
    

#### 4. Integración y Migración de Datos

-   Amazon EMR (Elastic MapReduce): Servicio de AWS para ejecutar clústeres de Hadoop y Spark.
    

-   Ventajas: Provisión rápida, escalabilidad y manejo de grandes clústeres.
    
-   Seguridad: Creación de grupos de seguridad para controlar el acceso a los nodos del clúster.
    

#### 5. Tipos de Almacenamiento en Apache Hudi

-   Merge-on-Read (MoR): Permite escrituras rápidas y fusión de datos en el momento de la lectura.
    
-   Copy-on-Write (CoW): Reescribe archivos completos con cada transacción, permitiendo lecturas rápidas.
    

### Aplicación Práctica

1.  Uso de Amazon SageMaker:
    

-   Ground Truth: Etiquetado de datos para entrenamiento.
    
-   Entrenamiento y Despliegue: Preparación de datos, entrenamiento del modelo y despliegue en producción utilizando SageMaker y SageMaker Canvas.
    

3.  Migración a Amazon EMR:
    

-   Migración de cargas de trabajo de Hadoop locales a Amazon EMR para aprovechar la escalabilidad y capacidad de Amazon Web Services.
    

5.  Uso de Presto y Apache Spark:
    

-   Realización de consultas rápidas y procesamiento de datos a gran escala utilizando Presto y Apache Spark.
    

7.  Almacenamiento de Datos con Apache Hudi:
    

-   Gestión eficiente de actualizaciones y borrados en grandes conjuntos de datos utilizando MoR y CoW.
    

  
  
  

MODULO 10

  
  

![](https://lh7-us.googleusercontent.com/docsz/AD_4nXcxoWkPktuGlRkykoHx7Zf-kKqIOa4KxHomLwI5pP-xWlW9jNtSshC9VdC_lsMVJGzDEyfnSjWNrUBzUbiCLOSQxc_vu1jlB7TRA6B7dnAOmjSZfy2oryiMb4tPsnpshCeNAEsqM5YkL86UvBkd97MadMBgJeU65jZTUNoZ2A?key=5OBIL_W6iV16g3AESCwYOQ)

### Ciclo de Vida del Aprendizaje Automático (ML)

1.  Definición del Problema de Negocio:
    

-   Identificar claramente el problema que se desea resolver con ML.
    
-   Enmarcar el problema de ML para alinearlo con los objetivos empresariales.
    

3.  Recopilación de Datos:
    

-   Recolectar datos relevantes y de calidad que serán utilizados para entrenar el modelo.
    
-   Asegurar que los datos sean representativos y suficientes para el problema a resolver.
    

5.  Etiquetado de Datos:
    

-   Aplicar etiquetas a los datos de entrenamiento, que son las respuestas o resultados conocidos que el modelo debe aprender a predecir.
    
-   Utilizar herramientas como SageMaker Ground Truth para actividades de etiquetado.
    

7.  Preprocesamiento de Datos:
    

-   Limpiar y transformar los datos para que sean adecuados para el modelo de ML.
    
-   Incluir técnicas como balanceo de datos y eliminación de sesgos.
    

9.  Ingeniería de Características:
    

-   Crear y seleccionar características (features) relevantes que mejoren el rendimiento del modelo.
    
-   Realizar transformación y selección de características para optimizar el modelo.
    

11.  Desarrollo del Modelo:
    

-   Seleccionar y entrenar un algoritmo de ML adecuado para el problema.
    
-   Evaluar el rendimiento del modelo utilizando métricas apropiadas.
    

13.  Despliegue del Modelo:
    

-   Implementar el modelo en un entorno de producción donde pueda realizar predicciones en tiempo real o por lotes.
    
-   Utilizar servicios como Amazon SageMaker para facilitar el despliegue.
    

15.  Monitoreo y Mantenimiento:
    

-   Monitorear el rendimiento del modelo en producción y realizar ajustes según sea necesario.
    
-   Asegurar que el modelo continúe funcionando correctamente y adaptarse a cambios en los datos.
    

### Infraestructura de ML en AWS

1.  Amazon SageMaker:
    

-   Servicio completo para construir, entrenar y desplegar modelos de ML.
    
-   Facilita el manejo del ciclo de vida completo del ML, incluyendo preprocesamiento, etiquetado, entrenamiento y despliegue.
    

3.  AWS SageMaker Ground Truth:
    

-   Herramienta para etiquetar datos de forma eficiente y precisa.
    
-   Permite la creación de conjuntos de datos de entrenamiento de alta calidad.
    

5.  Amazon SageMaker Canvas:
    

-   Interfaz de usuario sin código para que los analistas de negocios construyan modelos de ML.
    
-   Simplifica el proceso de experimentación y validación de hipótesis.
    

7.  AWS Kinesis Data Firehose y OpenSearch:
    

-   Herramientas para análisis y visualización de datos en streaming.
    
-   Permiten la ingesta, procesamiento y visualización de datos en tiempo real.
    

9.  Amazon QuickSight:
    

-   Servicio de BI para crear visualizaciones interactivas y dashboards.
    
-   Ayuda a analizar y visualizar datos para tomar decisiones informadas.
    

### Factores Clave en la Selección de Herramientas de Análisis y Visualización

1.  Requerimientos del Caso de Uso:
    

-   Considerar la naturaleza de los datos (por ejemplo, datos en tiempo real vs. datos históricos).
    
-   Evaluar las necesidades específicas del negocio y los objetivos del análisis.
    

3.  Compatibilidad y Escalabilidad:
    

-   Asegurar que las herramientas seleccionadas se integren bien con la infraestructura existente.
    
-   Evaluar la capacidad de las herramientas para escalar con el crecimiento de los datos y las demandas del negocio.
    

5.  Facilidad de Uso y Flexibilidad:
    

-   Optar por herramientas que ofrezcan una interfaz de usuario intuitiva y funciones robustas.
    
-   Considerar la facilidad de uso para los equipos de datos y los usuarios finales.
