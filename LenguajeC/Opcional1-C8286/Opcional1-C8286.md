## Ejercicios de C


## Directivas del preprocesador

- El preprocesamiento permite diseñar y modificar tu código fuente antes de enviarlo al compilador. Esta característica no está presente en la mayoría de los lenguajes de programación de nivel superior.

- El propósito del preprocesamiento es eliminar las directivas de preprocesamiento y sustituirlas por un código C generado equivalente y preparar un resultado final que esté listo para enviarse al compilador.

- El comportamiento del preprocesador C se puede controlar e influir utilizando un conjunto de directivas.

- Hay varias directivas en C, pero algunas de ellas son muy importantes, especialmente las directivas utilizadas para la definición de macros y las directivas utilizadas para la compilación condicional.

Recuerda [Cómo compilar código C/C++ con GCC](https://medium.com/shared-bytes/c%C3%B3mo-compilar-c%C3%B3digo-c-c-con-gcc-667b70747f1a)

## Macros

Las macros tienen varias aplicaciones como:

- Definición de una constante
- Función en lugar de escribir una función C
- Bucle desenrollado
- Guardias de cabecera
- Generadora de código
- Compilador condicional


### Definiendo una macro

Las macros se definen usando la directiva `#define`. Cada macro tiene un nombre y una posible lista de parámetros. Una macro también puede ser indefinida con la directiva `#undef`.

Lee el siguiente código:

```
Ejemplo1.c

```

En el cuadro de código anterior, ABC no es una variable que contiene un valor entero ni un número entero constante. De hecho, es una macro llamada ABC y su valor correspondiente es 12. Después de la fase de expansión de macro, el código resultante que se puede enviar al compilador de C es similar al que vemos a continuación:

```c
int main(int argc, char** argv) {

    int x = 12;
    int y = 5;
    int z = x + y;
    return 0;

}
```
El código en el cuadro anterior tiene una sintaxis C válida, y ahora el compilador puede continuar y compilarlo. En el ejemplo anterior, el preprocesador realizó la expansión de macro y, como parte de ella, el preprocesador simplemente reemplazó el nombre de la macro con su valor. El preprocesador también ha eliminado los comentarios en las líneas iniciales.

Lee el siguiente código:

```
Ejemplo2.c
```

En el cuadro de código anterior, SUST no es una función. Es solo una macro tipo función que acepta argumentos. Después del preprocesamiento, el código resultante será así:

```c
int main(int argc, char** argv) {

    int x = 12;
    int y = 5;
    int z = x - y;
    return 0;
    }
```


- Las macros solo existen antes de la fase de compilación. Esto significa que el compilador, en teoría, no sabe nada sobre las macros.

- Las macros te permiten generar código antes de la compilación.

Lee el siguiente código:

```
Ejemplo2a.c
```
#### Pregunta

* ¿Qué sucede en este código?


Cuando usas *gcc* o *clang*, puedes usar la opción `-E` para volcar el código después del preprocesamiento.

- Ejecuta el siguiente comando:

```
clang -E Ejemplo2a.c
```

### Unidad de traducción o unidad de compilación

Es el código C preprocesado que está listo para pasar al compilador. En una unidad de traducción, todas las directivas se sustituyen por inclusiones o expansiones de macro y se ha producido código C.

Lee el siguiente código:

```
Ejemplo3.c

```
El siguiente es el resultado preprocesado:

```c
...

... content of stdio.h ...

...

int main(int argc, char** argv) {

    for (int counter = 1; counter <= 10; counter++) {

        printf("%d\n", counter);

    }

    return 0;

}

```
Después del preprocesamiento, en el cuadro anterior, obtuvimos un programa C completamente funcional y correcto. Esta es una aplicación importante de las macros; definir un nuevo lenguaje específico de dominio (DSL) y escribir código usándo este lenguaje.



Veamos ahora el siguiente ejemplo, que presenta dos nuevos operadores con respecto a los parámetros macro; los operadores `#` y `##`:

```
Ejemplo4.c

```

Cuyo resultado es:

```c
...

... content of stdio.h ...

...

... content of string.h ...

...
int main(int argc, char** argv) {
    char copy_cmd[256] = ""; strcpy(copy_cmd, "copy");
    char paste_cmd[256] = ""; strcpy(paste_cmd, "paste");
    char cut_cmd[256] = ""; strcpy(cut_cmd, "cut");
    char cmd[256];
    scanf("%s", cmd);

    if (strcmp(cmd, copy_cmd) == 0) {
    }
    if (strcmp(cmd, paste_cmd) == 0) {
    }
    if (strcmp(cmd, cut_cmd) == 0) {
    }
    return 0;
}

```

Comparar el origen antes y después del preprocesamiento te ayuda a darte cuenta de cómo se aplican los operadores # y ## a los argumentos de la macro. Ten en cuenta que en el código final preprocesado, todas las líneas expandidas desde la misma definición de macro están en la misma línea.


### Macros variables

El siguiente ejemplo, está dedicado a las macros variables, que pueden aceptar un número variable de argumentos de entrada:

```
Ejemplo5.c
```
#### Pregunta:

- Explica que hace ` __VA_ARGS__`, ` LOG_ERROR`.


El siguiente código es el resultado final después de pasar por el preprocesador C:

```c
...


... content of stdio.h ...

...

... content of stdlib.h ...

... content of string.h ...


int main(int argc, char** argv) {
    if (argc < 3) {
        fprintf(stderr, "Invalido numero de argumentos para
         la version %s\n.","2.3.4");
        exit(1);

    }

    if (strcmp(argv[1], "-n") != 0) {
        fprintf(stderr, "%s es un incorrecto parametro en el
         indice %d para la version
         %s.", argv[1], 1, "2.3.4");

    exit(1);

    }

    // ...

    return 0;
}
```

El siguiente ejemplo, es un uso progresivo de macros variables que intenta imitar un bucle.


Lee el siguiente código:

```
Ejemplo6.c
```
El código final después del preprocesamiento, se muestra a continuación:

```c
...

... content of stdio.h ...

...

int main(int argc, char\*\* argv) {

    printf("%s\n", "copy paste cut"); printf("%s\n", "");
printf("%s\n", "");
    printf("%s\n", "copy"); printf("%s\n", "paste");
     printf("%s\n","cut");
printf("%s\n", "copy"); printf("%s\n", "paste");
 printf("%s\n","cut");

    return 0;

}
```

- Si observas el código preprocesado cuidadosamente, verás que la macro LOOP se ha expandido a múltiples instrucciones printf en lugar de instrucciones en bucle como for o while.

- La única forma de crear un bucle con una macro es simplemente poner las instrucciones de iteración una tras otra, y con algunas instrucciones separadas.

- Poner las instrucciones una tras otra en lugar de ponerlas en un bucle, se conoce como **desenrollar bucles**.


Ejecutamos el código:

```
gcc Ejemplo6.c
```

#### Pregunta

* Discutar las ventajas y desventajas de las macros.

## Compilación condicional

Permite tener un código fuente preprocesado diferente basado en diferentes condiciones. Existen diferentes directivas que contribuyen a la compilación condicional. Puedes ver una lista aquí:

- `#ifdef`
- `#ifndef`
- `#else`
- `#elif`
- `#endif`

Lee el siguiente código fuente:

```
Ejemplo7.c
```

Puedes ver el código preprocesado en el siguiente cuadro de código:

```c
int main(int argc, char** argv) {
    int i = 0;
    i++;

    int j= 0;
    return 0;

  }
```

Si la macro no estuviera definida, no veríamos ningún reemplazo para las directivas `#if- #endif`. Por lo tanto, el código preprocesado podría ser algo como lo siguiente:

```c
int main(int argc, char** argv) {


    int j= 0;
    return 0;

}
```

Uno de los usos comunes de `#ifndef` es servir como una **declaración de protección de encabezado (header guard)**. Esta declaración protege un archivo de encabezado para que no se incluya dos veces en la fase de preprocesamiento, y podemos decir que casi todos los archivos de encabezado C y C ++ en casi todos los proyectos tienen esta declaración como su primera instrucción.

El siguiente código, es un ejemplo sobre cómo usar una declaración de protección de encabezado:

```
Ejemplo8.h

```

#### Ejercicio

* Explica que hace el siguiente código con respecto a las directivas `#ifndef-#endif`:

```
#pragma once
void digo_hola();
int _notas();
```

## Variables puntero


La idea detrás de cualquier tipo de puntero es muy simple, es solo una variable simple que mantiene una dirección de memoria. Lo primero que puedes recordar acerca de ellos es el carácter asterisco, `*`, que se utiliza para declarar un puntero en C:

```
Ejemplo9.c
```

El ejemplo anterior tiene todo lo que necesita saber sobre la sintaxis del puntero (explica el código).


### Puntero nulo

- Un puntero nulo no apunta a una dirección de memoria válida. Por lo tanto, se debe evitar desreferenciar un puntero nulo porque se considera como un comportamiento indefinido

-  Se tiene una macro predeterminada `NULL` definida con el valor `0`, y se puede usar para anular punteros en una declaración. Es una buena práctica usar esta macro en lugar de `0` directamente porque facilita la distinción entre las variables y los punteros:

    ```
      char* ptr = NULL;
    ```

- Los punteros en C++ son exactamente los mismos que en C. Deben anularse almacenando `0` o `NULL`.

- `C++ 11` tiene una nueva palabra clave para inicializar los punteros. No es una macro como `NULL` ni un número entero como `0`. La palabra clave es *nullptr* y se puede usar para anular los punteros o verificar si son nulos. El siguiente ejemplo demuestra cómo se usa en C ++ 11:

    ```
      char* ptr = nullptr;
    ```

- Debes recordar que estás escribiendo código para diferentes arquitecturas, antiguas y nuevas, y esto puede causar problemas en los sistemas heredados si es que no inicializas los punteros. Además, obtendrás una lista de errores y advertencias para este tipo de punteros no inicializados en la mayoría de los perfiladores de memoria (memory profilers).

### Aritmética en punteros variables

Las operaciones aritméticas en un puntero son análogas a los movimientos en un array de bytes.

* El tamaño de paso aritmético (arithmetic step size) nos ayuda a entender que cuando se incrementa un puntero en `1`, puede avanzar más de `1` byte en la memoria. En efecto, cada puntero tiene un tamaño de paso aritmético, que indica el número de bytes que se moverá el puntero si se incrementa o disminuye en `1`.

En cada plataforma, tenemos una sola unidad de memoria y todos los punteros almacenan las direcciones dentro de esa memoria. Por lo tanto, todos los punteros deben tener el mismo tamaño en términos de bytes. Pero esto no significa que todos ellos tengan tamaños de paso aritméticos iguales. El tamaño del paso aritmético de un puntero está determinado por su tipo de datos C.

El siguiente ejemplo,  muestra los tamaños de paso aritméticos de dos punteros con dos tipos de datos diferentes:

```
Ejemplo10.c
```
#### Pregunta

* Explica los resultados.


Los ejemplos siguientes imprimen todos los elementos de un array de enteros:

```
Ejemplo11.c
```

y

```
Ejemplo12.c
```

#### No olvidar

Ten en cuenta que en C, un array es en realidad un puntero que apunta a su primer elemento. Por lo tanto, podríamos haber escrito la línea siguiente, como:

```
int* ptr = arr;
```

En lugar de :

```
int* ptr = &arr[0];
```

### Punteros genéricos

Se dice que un puntero de tipo `void*` es un puntero genérico. Puede apuntar a cualquier dirección como todos los demás punteros, pero no sabemos su tipo de datos real, por lo tanto, no sabemos su tamaño de paso aritmético:

El siguiente ejemplo, nos muestra que no es posible desreferenciar un puntero genérico:

```
Ejemplo13.c

```

#### Pregunta

* Explica los resultados de los compiladores `gcc` y `clang`.

Los punteros genéricos son muy útiles para definir funciones genéricas que pueden aceptar una amplia gama de punteros diferentes como argumentos de entrada. El siguiente ejemplo, intenta descubrir los detalles relacionados con las funciones genéricas:

```
Ejemplo14.c
```


#### Pregunta

* Explica el código anterior presentado.


### Tamaño de un puntero

El tamaño de un puntero depende de la arquitectura en lugar de ser un concepto específico de C. Se puede usar la función `sizeof` para obtener el tamaño de un puntero.
Es suficiente para ver el resultado de `sizeof (char*)` en su arquitectura de destino.

### Punteros extraviados

La cuestión de los punteros extraviados es muy famosa. Un puntero generalmente apunta a una dirección en la que hay una variable asignada. Leer o modificar una dirección donde no hay una variable registrada es un  error y puede ocurrir una falla de segmentación (segmentation fault). Esta situación generalmente ocurre cuando estás accediendo a lugares en la memoria que no tienes permitido.

Intentemos producir esta situación como parte del siguiente ejemplo:

```
Ejemplo15.c
```

#### Preguntas

* Explica el resultado que aparece cuando se intenta conseguir un ejecutable.
* ¿cuál es la forma correcta de reescribir el ejemplo?.


El ejemplo a continuación muestra cómo usar la memoria Heap para asignar variables y habilitar las direcciones de paso entre funciones sin enfrentar ningún problema:

```
Ejemplo16.c
```

#### Pregunta

* Explica el código anterior.


## Detalles de las funciones en C

En C, las funciones actúan como procedimientos, y son bloques de construcción de un programa en C y se consideran un caja lógica que tiene un nombre, una lista de parámetros de entrada y una lista de resultados de salida.

### Importante

Las funciones siempre son blocking en C. Esto significa que el agente que llama, tiene que esperar a que termine la función que se llamada y solo entonces puede recopilar el resultado devuelto. Frente a una función blocking, podemos tener una función non-blocking. Al llamar a una función así, el agente que llama no espera a que termine la función y puede continuar su ejecución.

En este esquema, generalmente hay un mecanismo de devolución de llamada (callback) que se activa cuando finaliza la función llamada. Una función non-blocking, también puede denominarse `función asincrónica` o simplemente una función asincrónica (asynchronous function o async function). Como no tenemos funciones asíncronas en C, necesitamos implementarlas usando soluciones de múltiples hilos.

Es interesante agregar que hoy en día, existe un creciente interés en el uso de funciones non-blocking. Suele denominarse programación orientada a eventos y estas funciones son centrales en este enfoque de programación, y la mayoría de las funciones escritas son non-blocking.

En la programación orientada a eventos, las llamadas a funciones reales suceden dentro de un bucle de eventos, y los callbacks se activan cuando se produce un evento. Los frameworks como *libuv* y *libev* promueven esta forma de codificación y permiten diseñar  software en torno a uno o varios bucles de eventos.

## Gestión de la pila

El diseño de memoria de un proceso que se ejecuta en un sistema operativo similar a Unix, todos los procesos comparten un diseño similar.


### El segmento de pila (Stack segment)

Es la ubicación de memoria predeterminada desde donde se asignan todas las variables locales, arrays y estructuras. Así, cuando se declara una variable local en una función, se asigna desde el segmento Pila. Esta asignación siempre ocurre en la parte superior del segmento de Pila.


El segmento de pila también se usa para llamadas a funciones. Cuando llama a una función, un marco de pila (stack frame) que contiene la dirección de retorno y los argumentos se colocan encima del segmento de Pila, y solo entonces se ejecuta la lógica de la función.

Todas las variables locales declaradas en el cuerpo de una función se colocan encima del segmento Pila. Entonces, al salir de la función, todas las variables de Stack se liberan. Es por eso que las llamamos variables locales y es por eso que una función no puede acceder a las variables en otra función. Este mecanismo también explica por qué las variables locales no están definidas antes de ingresar una función y después de abandonarla.

La pila es una porción limitada de memoria, y tu podrías completarla y potencialmente recibir un error de desbordamiento de pila (stack overflow). Esto suele suceder cuando tenemos demasiadas llamadas a funciones que consumen todo el segmento de Pila por sus marcos de pila. Esto es muy común cuando se trata de funciones recursivas, cuando una función se llama a sí misma sin ninguna condición de interrupción o límite.

### Paso por valor versus paso por referencia

No hay referencia en C, por lo que tampoco hay  pasos por referencia. Todo se copia en las variables locales de la función, y no puedes leerlas ni modificarlas después de abandonar una función.

```
Ejemplo17.c
```

#### Pregunta

* Explica el resultado del código anterior.


El siguiente ejemplo, demuestra que pasar por referencia no existe en C:

```
Ejemplo18.c
```

#### Pregunta

* ¿ Por qué el puntero se pasa como un argumento de paso por valor?, ¿ es eficiente pasar el puntero de esa manera?. Explica tus respuestas.

### Punteros de función

Tener punteros de función es otra característica de C.

Tienen muchas aplicaciones, pero dividir un binario grande en binarios más pequeños y cargarlos nuevamente en otro pequeño ejecutable es una de las aplicaciones más importantes. Esto ha llevado a la modularización y al diseño de software. Los punteros de función son bloques de construcción para la implementación del polimorfismo en C ++ y nos permiten ampliar nuestra lógica existente.

Al igual que un puntero variable que se dirige a una variable, un puntero de función se dirige a una función y te permite llamar a esa función indirectamente.

```
Ejemplo19.c
```

#### Pregunta

* Explica el resultado del código anterior y el papel de la función `func_ptr`.

Como puedes ver en el ejemplo anterior, podemos llamar a diferentes funciones para la misma lista de argumentos usando un puntero de función único, y esta es una característica importante. Desde la programación orientada a objetos, se puede pensar en el  polimorfismo y las funciones virtuales y de hecho estás en lo correcto, esta es la única forma de soportar el polimorfismo en C e imitar las funciones virtuales de C ++.

Al igual que los punteros, es importante inicializar los punteros de función correctamente. Para aquellos punteros de función que no se van a inicializar inmediatamente después de la declaración, es obligatorio hacerlos nulos. La anulación de los punteros de función se demuestra en el ejemplo anterior, y es bastante similar a los punteros.

Por lo general, se recomienda definir un nuevo tipo de alias para punteros de función.

```
Ejemplo20.c
```
#### Pregunta

* Explica el  papel de la palabra clave `typedef` y que tiene que ver con los alias en C?

## Estructuras

Cada lenguaje de programación tiene algunos tipos de datos primitivos - Primitive Data Types (PDT). Con estos PDT, puedes diseñar sus estructuras de datos y escribir algoritmos a tu alrededor y no se pueden cambiar ni eliminar.

Las estructuras entran en juego cuando necesitas tener tus propios tipos de datos definidos, y los tipos de datos en el lenguaje no son suficientes. Los tipos definidos por el usuario - User-Defined Types (UDT) son aquellos tipos creados por el usuario y no forman parte del lenguaje.

Ten en cuenta que los UDT son diferentes de los tipos que podría definir usando `typedef`. La palabra clave `typedef` realmente no crea un nuevo tipo, sino que define un alias para un tipo ya definido. Pero las estructuras te permiten introducir UDT totalmente nuevos en tus programas.

Las estructuras encapsulan valores relacionados bajo un solo tipo unificado. Como primer ejemplo, podemos agrupar las variables `rojo`, `verde` y `azul` bajo un nuevo tipo de datos único llamado `color_t`. El nuevo tipo, `color_t`, puede representar un color RGB en varios programas, como una aplicación de edición de imágenes. Podemos definir la estructura C correspondiente de la siguiente manera:

```c
struct color_t {

   int rojo;
   int verde;
   int azul;

};

```

Las estructuras encapsulan. La encapsulación es uno de los conceptos más importasntes en el diseño de software. Se trata de agrupar y encapsular campos relacionados bajo un nuevo tipo. Entonces, podemos usar este nuevo tipo para definir las variables requeridas.

##  Diseño de la memoria

Es importante saber exactamente el diseño de memoria de una variable de estructura. Tener un mal diseño en la memoria podría causar problemas en el rendimiento de ciertas arquitecturas. No olvides que codificamos para producir las instrucciones para la CPU. Los valores se almacenan en la memoria y la CPU debería poder leerlos y escribirlos lo suficientemente rápido.

Conocer el diseño de la memoria ayuda al desarrollador a comprender cómo funciona la CPU y a ajustar su código para obtener un mejor resultado.

Veamos un ejemplo:

```
Ejemplo21.c
```


Podríamos usar typedef para definir un nuevo tipo de alias para la estructura (¿por qué?)

```c
typedef struct {
  char primero;
  char segundo;
  char tercero;
  short cuarto;
}estructura_t ;
```

Ahora, se puede declarar la variable sin usar la palabra clave `struct`:

```c
estructura_t var;
```

El diseño de memoria de una variable de estructura es muy similar a un array. En un array, todos los elementos son adyacentes entre sí en la memoria, y esto es lo mismo para una variable de estructura y sus campos. La diferencia que existe es que, en un array, todos los elementos tienen el mismo tipo y, por lo tanto, el mismo tamaño, pero este no es el caso de una variable de estructura. Cada campo puede tener un tipo diferente y así tener un tamaño diferente. A diferencia de un array cuyo tamaño de memoria se calcula fácilmente, el tamaño de una variable de estructura en la memoria depende de algunos factores y no se puede determinar fácilmente.

#### Pregunta

* Explica el código anterior. ¿Por qué tenemos un byte extra?

La CPU siempre hace todos los cálculos. Para eso necesita cargar los valores de la memoria antes de poder calcular cualquier cosa y necesita almacenar los resultados nuevamente en la memoria después de un cálculo. La computación es súper rápida dentro de la CPU, pero el acceso a la memoria es muy lento. Es importante saber cómo interactúa la CPU con la memoria porque entonces podemos usar esa información para impulsar un programa o depurar un problema.

Generalmente se lee un número específico de bytes en cada acceso a la memoria. Este número de bytes generalmente se denomina palabra (word). Es decir la memoria se divide en palabras y una palabra es una unidad atómica utilizada por la CPU para leer y escribir en la memoria. El número real de bytes en una palabra es un factor dependiente de la arquitectura. Por ejemplo, en la mayoría de las máquinas de 64 bits, el tamaño de la palabra es de `32` bits o `4` bytes.

Con respecto a la  alineación de la memoria, decimos que una variable está alineada en la memoria si su byte inicial está al comienzo de una palabra. De esta manera, la CPU puede cargar su valor en un número optimizado de accesos a la memoria.

#### Pregunta

* Explica el comportamiento de los campos en el código anterior.

El compilador utiliza el `padding` para alinear valores en la memoria. El padding son los bytes adicionales agregados para coincidir con la alineación.

Es posible desactivar la alineación. En terminología C, usamos un término más específico para estructuras alineadas. Decimos que la estructura no está empaquetada. Las estructuras empaquetadas no están alineadas y su uso puede provocar incompatibilidades binarias y problemas de rendimiento. 

Puedes definir fácilmente una estructura que esté empaquetada. En el siguiente ejercicio, que es bastante similar al ejemplo anterior,  `estructura_t` se empaqueta en este ejemplo.

#### Ejercicio

* Completa  y ejecuta el código:

```c
#include <stdio.h>

struct __attribute__((__packed__)) estructura_t {
  char primero;
  char segundo;
  char tercero;
  short cuarto;
} ;

void imprime_tamn(struct estructura_t* var) {
  // ...
}

void imprime_bytes(struct estructura_t* var) {
  // ...
}

int main(int argc, char** argv) {
  // ...
}
```

#### Pregunta

* Explica tus resultados.
* ¿Qué sucede si se tiene un puntero a estructura?.

Las estructuras empaquetadas generalmente se usan en entornos con limitaciones de memoria, pero pueden tener un gran impacto negativo en el rendimiento en la mayoría de las arquitecturas. Solo las nuevas CPU pueden manejar la lectura de un valor no alineado de varias palabras sin exigir un costo adicional. Ten en cuenta que la alineación de la memoria está habilitada de forma predeterminada.

### Estructuras anidadas

En general, tenemos dos tipos de tipos de datos en C. Hay tipos que son primitivos para el lenguaje y hay tipos que los programadores definen mediante la palabra clave `struct`. Los primeros tipos son PDT, y los últimos son UDT.

Los ejemplos de estructura han sido sobre UDT (estructuras) formadas solo por PDT. Vamos a dar un ejemplo de UDT (estructuras) que están hechas de otros UDT (estructuras). Estos se denominan tipos de datos complejos, que son el resultado de anidar algunas estructuras.

Comencemos con el siguiente ejemplo:

```c
typedef struct {
  int x;
  int y;
} punto_t;

typedef struct {
  punto_t centro;
  int radio;
} circulo_t;

typedef struct {
  punto_t inicio;
  punto_t final;
} linea_t;
```

#### Pregunta

* Explica el código anterior.

Es común llamarlos objetos de variables de estructura. Son exactamente análogos a los objetos en la programación orientada a objetos, y pueden encapsular valores y funciones. Por lo tanto, no está mal llamarlos **objetos C**.

### Punteros de estructura

Al igual que los punteros a los PDT, también podemos tener punteros a los UDT. Funcionan exactamente igual que los punteros PDT. Apuntan a una dirección en la memoria, y se puede hacer aritmética en ellos al igual que con los punteros PDT. Los punteros UDT también tienen tamaños de pasos aritméticos equivalentes al tamaño del UDT.

Es importante saber que una variable de estructura apunta a la dirección del primer campo de la variable de estructura.

El siguiente ejemplo muestra que tener tres punteros diferentes de tres tipos diferentes direcccionan el mismo byte en memoria, pero con tipos diferentes.


```
Ejemplo24.c
```

Esto se usa para extender estructuras provenientes de otras bibliotecas agregando más campos. Esta es también la forma en que implementamos la herencia en C.



