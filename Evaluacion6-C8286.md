### Ejercicio 1: Desplegar un Job en Kubernetes

![](https://lh7-us.googleusercontent.com/NA_0Pw0l-WJ4OpqL3naZltSSU5w7WgMCzbiKOCorQUCUSzYdvwXD7wTPXNgtvBz0l-Hl4u8u2OmtDVYFdODvQv45Pi0Ney3-2Z_UzqTzjYXfz2y4u7kbsHATHoBeOG5heCSgYzauPP3xpCVeVQ_XxCg)![](https://lh7-us.googleusercontent.com/pk1IeaJb3IzAb0xN-AYEk7Jitd4yCJ44o0lvwHv8ergY5ZOHklyjS6AwyE0-qc3QpNsxaM3K8y9WcfnfuCXQcvc7UCzQ9nEb0lbH9wUKrJ74GSh-5FWOZMRL0tdS6jxzQpIQz-pM1Fo4ZHDKX89o558)

![](https://lh7-us.googleusercontent.com/hDW5GF8NRGel6JCrXq9wJxOTxYyjiMHhBNVzfrRl4IdTCiQ3aFspl3nHVyk-Islog7HfKI9EMf1LXFWKZHQmPFyp6El179-mnil7lcVdu2rmbPGR0KU-L90Vowr3QsxZqZxERCWFadprdMSpRm-DOls)

  

### Ejercicio 2: Modificar y Redesplegar un Job

  
  

### Ejercicio 3: Eliminar un Job

  
  

### Ejercicio 4: Desplegar y Verificar el Servicio y los Endpoints

![](https://lh7-us.googleusercontent.com/_BLrK3_NOVPHTeddMiUsbofYjGiOYPFtP2kyHqI9iUuHJNSZ2H8_8Mg5_btfxZ1Dj9n523K3BpjpZ54A8nDDz-ZFcTJ_id1LPzAhzyx88OhDjUrf9EUnX3_tq3lPA-CkilpHD3-vEIMkafp1RUCzsjw)

  

Aplicar el archivo y verificar:

kubectl apply -f nginx-service-endpoints.yaml

kubectl get services nginx-service

kubectl get endpoints nginx-service

  

![](https://lh7-us.googleusercontent.com/ihcTbdInCvxcra5dCT096mTuDkxmhCCxQhLoreKakPeC4NM_N6Wi1V94Y6KrxhoyLL8Cw4cJfmhAgoeuFjLoAO7TGKGEradQ8c-ikIM9mc3N9X_Hp7NFdeCmDIzxsDxUnlrYK3yh4WEp5TGLpDZ_R0k)

si refleja los endepoints y la direccion IP

  

Ejercicio 2: Modificar el servicio

Modificar nginx-service-endpoints.yaml para cambiar el targetPort a 8080:

![](https://lh7-us.googleusercontent.com/LuPE4c4qVkrQ0WADqOX-IeC81ezVHVOGWdh33XKSTU1xIgM2zpFiqwUE2v4teBceFcd8w62UWNKyPry5Z7cI9K8QltrF_SFkMYuHgMpRH2euwP6gecEvOJZMdXXJ54yCS0P4aUMgCH4cU8T6N5CyNJA)

  

Verificar que el servicio y los endpoints se hayan actualizado correctamente

  

![](https://lh7-us.googleusercontent.com/RC87ZQKr6nlyfxtET_HDfb16B3UoaXiI42PMkbM451mpc6Le9aq98ELnHI0IbonXzOWaXJQri_OBeaGE1CqEOEyTaI522e9ccteQwUuk6KFSC1PY3vMYaS_8-ttfqSL0jAjl_53K37pSxBL3w6qOx1g)

  
  

Ejercicio 3: Simulación de fallo de Pod

Discusión:

-   Actualización de Endpoints: Al eliminar un pod, Kubernetes actualiza los endpoints del servicio para reflejar que el pod ya no está disponible. El servicio continuará dirigiendo el tráfico solo a los pods restantes.
    
-   Resiliencia del Servicio: Gracias a la arquitectura de Kubernetes, los servicios son resilientes a fallos de pods individuales. Los controladores de implementación aseguran que se mantenga el número deseado de réplicas, y los endpoints se actualizan dinámicamente.
    
-   Manejo de Fallas: Kubernetes detecta la falla de pods mediante probes y eventos de eliminación, y toma acciones correctivas automáticamente. Esto incluye reiniciar pods fallidos y crear nuevos pods para reemplazar los eliminados.
    
-   Disponibilidad Continua: La arquitectura distribuida y los mecanismos de recuperación automática de Kubernetes aseguran que los servicios permanezcan disponibles incluso en caso de fallos de pods, minimizando el impacto en los usuarios finales
    

![](https://lh7-us.googleusercontent.com/cfjyYTtQX254ioIjLxYa_GTCHmPIERtaPBswDaBUm_SW8lIEIYdIgyC_lRzALAG79dKDRebmvB34GMkZ7AM2E2f4WMWYvYvvxh0uCJhjZCfVOUOHIJJr0VL9RIYGfXEz4aHOWYpuCF6Hya7ZUrRQ5YI)

Ejercicio 4: Agregar un segundo Endpoint manualmente

Modifica el archivo nginx-service-endpoints.yaml agregando una segunda dirección IP bajo

addresses:

ip: 192.0.2.43

  

![](https://lh7-us.googleusercontent.com/I0LebCWCjACSqJQxc0hUZjCnq6xO6fOGTspXMHatjX2cY94bN9p4VfzTcCSj2Yloi8GaPB3Ql-h-cS02VQZ8hYkgt7HPLLKAFUkOqc64yVplWH5FBAQZgNo10W8SIycVLJWiBsAx8MQxMmjMB_CUlc0)

  

### Discusión: Efecto en el Balance de Carga

#### Balance de Carga

-   Antes del cambio: El servicio nginx-service estaba balanceando la carga únicamente hacia el endpoint 192.0.2.42:9376.
    
-   Después del cambio: Con la adición del nuevo endpoint 192.0.2.43:9376, el servicio ahora balancea la carga entre dos endpoints.
    

#### Efecto del Cambio

-   Mejora en Alta Disponibilidad: Al tener más de un endpoint, el servicio nginx-service es más resistente a fallos, ya que si un endpoint falla, el tráfico puede ser redirigido al otro endpoint.
    
-   Distribución del Tráfico: El tráfico entrante ahora se distribuye entre ambos endpoints, lo que puede mejorar el rendimiento al reducir la carga en cada endpoint individual.
    

  

Ejercicio

Configura un clúster de Kubernetes mínimo usando Minikube o un entorno similar y despliegue

varios pods usando imágenes estándar como nginx o busybox para pruebas.

![](https://lh7-us.googleusercontent.com/GsY-ibN4D2g5nb6KrVfsMdgK7x0uenUcI-Y6lK9eoFU8r4o-FISXt6YEDJ1CcO4LRnU8h1PnQftUStchWD1lFsoGh1GBTBGBwaJJA9FyxTuSIDI9l6-c8LfEvx8kNVl1khkluEJmROYd-hs6jXjkrFQ)

![](https://lh7-us.googleusercontent.com/gFJDE90xj9z8M50DGdAowZ1aln1h3CXVobiTblXI6hV3k7bvGzW0Yu8pNHQ3DuybRJheD29ByfA89A6B7JWhhq0mEpWDIc4z8tbS2bWZjAELKOw8VX3ESbTg1ZQFlU2z6x4BXDMn73swev5m3VR5zGM)

### Tareas:

### - Crea el ClusterRole. Debes crear un archivo YAML basado en el manifiesto proporcionado y

### aplicarlo al clúster usando kubectl apply -f <filename>.yaml.

### - Crea un ClusterRoleBinding para asociar el ClusterRole creado con un usuario, grupo o

### servicio específico. Esto implica definir otro manifiesto YAML donde especificarán a quién se

### le otorgan los permisos definidos por nodes-reader.

### -Valida los permisos. Debes intentar realizar operaciones permitidas (como kubectl get

### nodes) y operaciones no permitidas (como kubectl delete node <node-name>) para verificar

### que los permisos están funcionando como se espera.

### -Explica cómo implementaron el ClusterRole y el ClusterRoleBinding, describir cualquier

### desafío que encontraron durante el ejercicio y discutir la importancia del RBAC en la

### administración de un clúster de Kubernetes.

  

### Autenticación y Autorización

Crear un ClusterRole

![](https://lh7-us.googleusercontent.com/Xd6wFhFMwd0Gq1ifitHQShJ6QwsSnPGrAcK-JcTxKbGvnN60B5hg0qnk-ZwU8jLbD8EWTeb8mcfqh8Rf9hik4SZ-85zjlwuaR_zy5r9mV66frdbg_c33G7FlVBLLtWG4XrSPg6FxZmAZtNsVzmVkIRY)

Crear un ClusterRoleBinding

![](https://lh7-us.googleusercontent.com/3xkGeezVAl54LNDgsjNzyHgV7LMNGlDfKr0ydO_oMmn8QK_a-btSYhEln1t3R4B5HvVQncl8JgKRWlDe3p-g6GJ6aDVEfXppRzfUHTkEIQuwxb3CzAkNfVgg9bPOxAjAxJ5t-4Uk36G-9F7j28Guvvs)

  

![](https://lh7-us.googleusercontent.com/jj9iivCXp0atkAtt5RLX4ENeQedeMid29zWZW1audARYhh3q9D464dCqcF8O8ERbcUkSfVf07d4BVlWf1wS0-mpsURc2Ik1DvSrBPn4-RJD_b7v8U1i5JfQ4gbVMeL6tGP6-PIty8gYEikmP5iewnDc)

  

Ejercicio

Crear, gestionar y uso de secretos en Kubernetes, especialmente en el contexto de almacenar

credenciales de acceso seguro.

### Manejo de Secretos

![](https://lh7-us.googleusercontent.com/opXkfr-677PULKwcth5R790MHpP_WC0_xRnzge04GaaphwvvyUgIgwhbrPqohQ08hxGorfj0rT0mcLjWlRWBUyg25h1fgGUIQ-luraY_m334AuzkVR240J8vCzJlV5dAFDxkPyCII-mBXFCkQ10hC7E)

  

![](https://lh7-us.googleusercontent.com/akQACbt5V7C_DjBCUvaBlJOXqnfTGbUr1sCoDC-GpzpParAE0BBsBlf4ei3hhJic97Z7lLgqsodv35Eg2BFT-162KULXmCnTnlSns4Z7s2moI1XyVC8JTQh2UR47_i6u8dFYIouptzNQKGPoEmtqd4w)

#### Paso 3: Crear un Pod que Use el Secreto

Crear el manifiesto del Pod usando variables de entorno:

![](https://lh7-us.googleusercontent.com/CdfkIf2-3yR3NoggnvIDSv50KkVRWgZEbunnyFyR5gxzIpgqOaS3zj9mRVjAAKTYoYt453YXxFaia5BI7YN4H9878wBaioDkCGy7OkLn9rH6CvVMoADdmG495f7JGqFjum-lEMAxp2uSH11GLLVJWkQ)

Aplicar el manifiesto para desplegar el Pod:

![](https://lh7-us.googleusercontent.com/oXS_8C8EHlx0jKTPT6IpVVG7WR_FoYsf6oFMlj7rKba4cvxRWIgkbxnJwywExUtScXuTnGWWcSpZG9q9VkpuDZKD6x_UYCv2DSO9VRVpL3TlH3cZozmBQpU3BrR7KmsrnQu6HSU89Radxx1HRAKLa2w)

#### Paso 4: Validar la Configuración

Verificar que el Pod esté en ejecución:

![](https://lh7-us.googleusercontent.com/OWnaTA0D42Zltlr4svBqgjEayAALHfqbu5hd7kC6i3ZYI8oAPhDJwoE2T3NQKg2SFskDwEfubykNvrrGyRGVvK-tEY7tlnJQW9prTDLbbxr-zgj8oludYckh1Oq54GKTyMioGrxb_hgXAqKJqud16Hk)

  

Ingresar al contenedor y verificar las variables de entorno

![](https://lh7-us.googleusercontent.com/GNmQrNnGNoRSbJlDWKnJ4JnrKqgmzGB6j49pVzw6MR9Dhm5aSVmdP5HnbQXoXCQrBIow-MlE0CAi-Mo6MzYRHZipzZk-qF9seeQlGH9bvfXO3fZSRdbxenO1NwTjzeC9DVwOMIatj5gXD8AK0htLWew)

Ingresar al contenedor y verificar las variables de entorno![](https://lh7-us.googleusercontent.com/xnanLTjjzQMi6wckYGV1-6QAR3SFvfoD21mCEOTCl7oUltMGoXTWUjvRVyZZFZOprIcC7qyWxqI_B3uJXBwVCwXMrAyLUeAe87-OcMh2mDbrqOWSmyUOSF--MsL1ybIEIjAHR-2CORniae_K22g6oW8)