{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d9035a28",
   "metadata": {},
   "source": [
    "### Actividad:  repaso de threading, multiprocessing, asyncio, concurrent.futures"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87f4a495",
   "metadata": {},
   "source": [
    "#### Ejercicio 1: Uso básico de threading\n",
    "\n",
    "Crea un script que inicie 5 hilos. Cada hilo debe imprimir un mensaje que indique su número de identificación (ID) y luego esperar un tiempo aleatorio entre 1 y 5 segundos antes de finalizar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "670436a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading\n",
    "import time\n",
    "import random\n",
    "\n",
    "def worker_thread(thread_id):\n",
    "    # Cada hilo imprime su ID.\n",
    "    print(f\"El hilo {thread_id} esta corriendo.\")\n",
    "    \n",
    "    # Genera un tiempo de espera aleatorio entre 1 y 5 segundos.\n",
    "    sleep_time = random.randint(1, 5)\n",
    "    time.sleep(sleep_time)  # Corrección aquí: eliminación del argumento con nombre\n",
    "    \n",
    "    # Mensaje de finalización del hilo.\n",
    "    print(f\"Hilos {thread_id} a finalizado despues de {sleep_time} segundos.\")\n",
    "\n",
    "# Lista para mantener los hilos.\n",
    "threads = []\n",
    "\n",
    "# Crear y lanzar 5 hilos.\n",
    "for i in range(5):\n",
    "    # Creamos el hilo.\n",
    "    thread = threading.Thread(target=worker_thread, args=(i,))\n",
    "    \n",
    "    # Añadimos el hilo a la lista de hilos.\n",
    "    threads.append(thread)\n",
    "    \n",
    "    # Iniciar el hilo.\n",
    "    thread.start()\n",
    "\n",
    "# Esperar a que todos los hilos terminen.\n",
    "for thread in threads:\n",
    "    thread.join()\n",
    "\n",
    "print(\"Todos los hilos es finalizado.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e62c3704",
   "metadata": {},
   "source": [
    "#### Ejercicio 2: Uso de multiprocessing\n",
    "\n",
    "Escribe un programa que utilice multiprocessing para calcular el factorial de diferentes números de forma paralela. Usa los números 5, 7, y 9."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30bbd94b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import multiprocessing\n",
    "\n",
    "def factorial(number):\n",
    "    if number == 0 or number == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        result = 1\n",
    "        for i in range(2, number + 1):\n",
    "            result *= i\n",
    "        return result\n",
    "\n",
    "def compute_factorial(number, result_dict):\n",
    "    # Calcular el factorial y almacenarlo en un diccionario compartido.\n",
    "    result_dict[number] = factorial(number)\n",
    "    print(f\"El factorial de {number} es {result_dict[number]}\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # Lista de números para los cuales queremos calcular el factorial.\n",
    "    numbers = [5, 7, 9]\n",
    "    \n",
    "    # Diccionario que se usa para almacenar los resultados.\n",
    "    # Utilizamos un Manager dict para permitir el acceso entre procesos.\n",
    "    manager = multiprocessing.Manager()\n",
    "    result_dict = manager.dict()\n",
    "    \n",
    "    # Lista para mantener los procesos.\n",
    "    processes = []\n",
    "    \n",
    "    # Crear y lanzar un proceso por cada número.\n",
    "    for number in numbers:\n",
    "        # Creamos el proceso.\n",
    "        process = multiprocessing.Process(target=compute_factorial, args=(number, result_dict))\n",
    "        \n",
    "        # Añadimos el proceso a la lista de procesos.\n",
    "        processes.append(process)\n",
    "        \n",
    "        # Iniciar el proceso.\n",
    "        process.start()\n",
    "    \n",
    "    # Esperar a que todos los procesos terminen.\n",
    "    for process in processes:\n",
    "        process.join()\n",
    "    \n",
    "    print(\"Todos los procesos terminados.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "681d084c",
   "metadata": {},
   "source": [
    "#### Ejercicio 3: Uso de asyncio\n",
    "\n",
    "Utiliza asyncio para simular la descarga de tres archivos de manera asíncrona. Los tiempos de \"descarga\" deben ser de 3, 5 y 7 segundos respectivamente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e83d2ac9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import asyncio\n",
    "\n",
    "async def download_file(file_name, duration):\n",
    "    # Simula la descarga esperando la cantidad de segundos especificada.\n",
    "    print(f\"Iniciando la descarga de {file_name} (durará {duration} segundos)...\")\n",
    "    await asyncio.sleep(duration)\n",
    "    print(f\"Descarga completada: {file, duration} segundos\")\n",
    "\n",
    "async def main():\n",
    "    # Crear las \"tareas\" para cada descarga simulada.\n",
    "    await asyncio.gather(\n",
    "        download_file(\"archivo1.txt\", 3),\n",
    "        download_file(\"archivo2.txt\", 5),\n",
    "        download_file(\"archivo3.txt\", 7)\n",
    "    )\n",
    "\n",
    "# Ejecutar la función main del programa.\n",
    "asyncio.run(main())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3be8cd64",
   "metadata": {},
   "source": [
    "#### Ejercicio 4: Uso de concurrent.futures con ThreadPoolExecutor\n",
    "\n",
    "Escribe un programa que utilice un ThreadPoolExecutor para realizar un cálculo simple (como la suma de números) en varios hilos. Utiliza un rango de números del 1 al 10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "451cc67f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import concurrent.futures\n",
    "\n",
    "def sum_range(start, end):\n",
    "    total = 0\n",
    "    for number in range(start, end + 1):\n",
    "        total += number\n",
    "    return total\n",
    "\n",
    "def main():\n",
    "    ranges = [(1, 3), (4, 6), (7, 10)]  # Dividiendo el rango de números en tres partes.\n",
    "    results = []\n",
    "    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:\n",
    "        # Crear futuros para cada rango de sumas.\n",
    "        futures = [executor.submit(sum_range, r[0], r[1]) for r in ranges]\n",
    "        \n",
    "        # Recopilar los resultados a medida que se completan.\n",
    "        for future in concurrent.futures.as_completed(futures):\n",
    "            result = future.result()\n",
    "            print(f\"Resultado obtenido: {result}\")\n",
    "            results.append(result)\n",
    "    \n",
    "    # Sumar los resultados parciales para obtener el total final.\n",
    "    total_sum = sum(results)\n",
    "    print(f\"La suma total de 1 a 10 es: {total_sum}\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2956d07c",
   "metadata": {},
   "source": [
    "#### Ejercicio 5: Uso de asyncio con corutinas\n",
    "\n",
    "Implementa un programa con asyncio que simule un reloj, mostrando cada segundo un mensaje que indica cuántos segundos han pasado, hasta un total de 10 segundos.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "319eafdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import asyncio\n",
    "\n",
    "async def clock():\n",
    "    for second in range(1, 11):  # Iterar de 1 a 10 segundos\n",
    "        print(f\"{second} segundo{'s' if second > 1 else ''} han pasado\")\n",
    "        await asyncio.sleep(1)  # Espera un segundo\n",
    "\n",
    "async def main():\n",
    "    await clock()  # Ejecutar la corutina del reloj\n",
    "\n",
    "# Ejecutar la función main utilizando asyncio\n",
    "asyncio.run(main())\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "11710494-cc1a-4c7a-9d95-d16ecdbc8e60",
   "metadata": {},
   "source": [
    "Observación: El error que se experimenta sugiere que se está intentando ejecutar asyncio.run(main()) dentro de un entorno que ya tiene un bucle de eventos en ejecución. Esto es común cuando se utiliza asyncio en un entorno interactivo como Jupyter Notebook o IPython.\n",
    "\n",
    "Para manejar esta situación, puedes modificar la forma en que ejecutas tu programa para trabajar con el bucle de eventos ya existente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65ce06b6-1691-46f7-9532-2798b861de75",
   "metadata": {},
   "outputs": [],
   "source": [
    "import asyncio\n",
    "\n",
    "async def clock():\n",
    "    for second in range(1, 11):  # Iterar de 1 a 10 segundos\n",
    "        print(f\"{second} segundo{'s' if second > 1 else ''} han pasado\")\n",
    "        await asyncio.sleep(1)  # Espera un segundo\n",
    "\n",
    "# Código ajustado para un entorno con bucle de eventos en ejecución\n",
    "async def main():\n",
    "    await clock()  # Ejecutar la corutina del reloj\n",
    "\n",
    "# Utilizar get_event_loop para obtener el bucle de eventos actual\n",
    "loop = asyncio.get_event_loop()\n",
    "\n",
    "# Verificar si el bucle de eventos está en ejecución\n",
    "if loop.is_running():\n",
    "    # Ejecutar la corutina en el bucle de eventos ya existente\n",
    "    asyncio.ensure_future(main())\n",
    "else:\n",
    "    # Iniciar el bucle de eventos y correr la corutina\n",
    "    loop.run_until_complete(main())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1ba7bd3",
   "metadata": {},
   "source": [
    "#### Ejercicio 6: Uso de multiprocessing con Pool\n",
    "\n",
    "Utiliza un Pool de procesos en multiprocessing para aplicar una función que calcule el cuadrado de un número a una lista de números del 1 al 10 de manera paralela."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f2e9d7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import multiprocessing\n",
    "\n",
    "def square_number(n):\n",
    "    return n * n\n",
    "\n",
    "def main():\n",
    "    numbers = range(1, 11)  # Lista de números del 1 al 10\n",
    "    with multiprocessing.Pool() as pool:\n",
    "        # map aplica la función 'square_number' a cada elemento de la lista 'numbers'\n",
    "        results = pool.map(square_number, numbers)\n",
    "        print(results)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # Correr la función main si el script es ejecutado como principal\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9125cb6b",
   "metadata": {},
   "source": [
    "#### Ejercicio 7: Programación funcional con map y reduce\n",
    "\n",
    "Implementa un script que use map para convertir todas las palabras en una lista a mayúsculas, y luego use reduce para concatenarlas en una sola cadena separada por comas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fabf96e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    words = ['hola', 'mundo', 'programación', 'funcional', 'Python']\n",
    "    # Convertir todas las palabras a mayúsculas\n",
    "    upper_words = map(str.upper, words)\n",
    "    \n",
    "    # Concatenar todas las palabras en una cadena separada por comas usando un bucle for\n",
    "    result = \"\"\n",
    "    for word in upper_words:\n",
    "        if result:  # Si result ya tiene contenido, añadimos una coma antes del siguiente elemento\n",
    "            result += \",\"\n",
    "        result += word\n",
    "\n",
    "    print(result)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8581ea0d",
   "metadata": {},
   "source": [
    "#### Ejercicio 8: Crear un microservicio simple con Flask\n",
    "\n",
    "Desarrolla un microservicio básico usando Flask que tenga un endpoint /api/square que acepte un número y devuelva su cuadrado."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57243693-c4bd-4a8a-9959-667d9dd3390a",
   "metadata": {},
   "outputs": [],
   "source": [
    "%%witefile server.py\n",
    "\n",
    "from flask import Flask, request, jsonify\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/api/square', methods=['GET'])\n",
    "def square():\n",
    "    # Obtener el parámetro 'number' de la URL\n",
    "    number = request.args.get('number', default=1, type=int)\n",
    "    \n",
    "    # Calcular el cuadrado del número\n",
    "    result = number ** 2\n",
    "    \n",
    "    # Devolver el resultado en formato JSON\n",
    "    return jsonify({'numero': number, 'cuadrado': result})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, port=5001) # Cambia el puerto si es necesario.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a06cebf1-f837-4c72-bd55-3d5de79812b5",
   "metadata": {},
   "source": [
    "Esto iniciará el servidor Flask, y podrás acceder a él normalmente desde http://localhost:5001.\n",
    "\n",
    "Para probar el endpoint /api/square, puedes usar un navegador o una herramienta como curl para hacer una solicitud GET. Por ejemplo, para calcular el cuadrado de 5:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cdf60f0b-7a55-4a2c-aa16-870d3d53a710",
   "metadata": {},
   "outputs": [],
   "source": [
    "curl \"http://localhost:5001/api/square?number=5\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4c46314b-0185-4092-934e-8f605e180de8",
   "metadata": {},
   "source": [
    "Esto debería devolver una respuesta en JSON como:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2400b4d0-bcc8-448b-aafb-dd9e4b9a37a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "{\n",
    "  \"numero\": 5,\n",
    "  \"cuadrado\": 25\n",
    "}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6425434",
   "metadata": {},
   "source": [
    "#### Ejercicio 9: Uso de asyncio y aiohttp para hacer peticiones HTTP concurrentes\n",
    "\n",
    "Escribe un script que use asyncio y aiohttp para hacer peticiones a tres URLs diferentes de manera concurrente y recolecte sus resultados."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33081ab5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import asyncio\n",
    "import aiohttp\n",
    "\n",
    "async def fetch(session, url):\n",
    "    \"\"\"Petición HTTP asincrónica a la URL dada.\"\"\"\n",
    "    async with session.get(url) as response:\n",
    "        return await response.json()  # Analizar la respuesta JSON\n",
    "\n",
    "async def main():\n",
    "    urls = [\n",
    "        'https://jsonplaceholder.typicode.com/todos/1',\n",
    "        'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true',\n",
    "        'https://httpbin.org/delay/2'  # Este endpoint introduce un retraso de 2 segundos\n",
    "    ]\n",
    "    # Crear una sesión aiohttp\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        tasks = [fetch(session, url) for url in urls]\n",
    "        # Esperar todas las respuestas\n",
    "        responses = await asyncio.gather(*tasks)\n",
    "        for response in responses:\n",
    "            print(response)  # Imprimir cada respuesta JSON\n",
    "\n",
    "# Ejecutar el bucle de eventos\n",
    "asyncio.run(main())\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c231e975-ee94-40d0-96a4-494ac6aef098",
   "metadata": {},
   "source": [
    "Observación: El error indica que ya hay un bucle de eventos de asyncio ejecutándose y estás intentando iniciar uno nuevo con asyncio.run(). Este problema es común cuando intentas ejecutar código asyncio dentro de un entorno como Jupyter Notebook o en el contexto de algunas aplicaciones de servidor que ya manejan su propio bucle de eventos.\n",
    "\n",
    "Para resolver este problema en un entorno como Jupyter Notebook, en lugar de usar asyncio.run(), debes utilizar las funciones get_event_loop() para obtener el bucle de eventos existente y luego run_until_complete() para ejecutar tu corutina principal."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7f88625-6508-4a18-9aa0-d8b78a0d5fa6",
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile asyncio1.py  # utiliza este archivo\n",
    "import asyncio\n",
    "import aiohttp\n",
    "\n",
    "async def fetch(session, url):\n",
    "    async with session.get(url) as response:\n",
    "        return await response.json()  # Parse JSON response\n",
    "\n",
    "async def main():\n",
    "    urls = [\n",
    "        'https://jsonplaceholder.typicode.com/todos/1',\n",
    "        'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true',\n",
    "        'https://httpbin.org/delay/2'  # This endpoint introduces a delay of 2 seconds\n",
    "    ]\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        tasks = [fetch(session, url) for url in urls]\n",
    "        responses = await asyncio.gather(*tasks)\n",
    "        for response in responses:\n",
    "            print(response)  \n",
    "\n",
    "loop = asyncio.get_event_loop()\n",
    "loop.run_until_complete(main())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54e8820d-5eb5-4a46-9083-6d9b24e8ba56",
   "metadata": {},
   "source": [
    "Para solucionar esto en un entorno como Jupyter, puedes utilizar la librería nest_asyncio, que permite anidar bucles de eventos de asyncio.\n",
    "\n",
    "pip install nest_asyncio\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a2f8d9d-902f-4cec-a6d0-a38bb754ed03",
   "metadata": {},
   "source": [
    "Una vez instalado, puedes aplicar nest_asyncio a tu bucle de eventos existente para permitir que se ejecute correctamente en entornos como Jupyter Notebook. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4161b532-7817-4bab-b411-946618e23707",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}\n",
      "{'latitude': 35.7, 'longitude': 139.6875, 'generationtime_ms': 0.0400543212890625, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 40.0, 'current_weather_units': {'time': 'iso8601', 'interval': 'seconds', 'temperature': '°C', 'windspeed': 'km/h', 'winddirection': '°', 'is_day': '', 'weathercode': 'wmo code'}, 'current_weather': {'time': '2024-05-11T18:00', 'interval': 900, 'temperature': 16.4, 'windspeed': 6.5, 'winddirection': 186, 'is_day': 0, 'weathercode': 1}}\n",
      "{'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'Python/3.8 aiohttp/3.8.1', 'X-Amzn-Trace-Id': 'Root=1-663fb59d-03579ec82115402911b7d30c'}, 'origin': '190.238.29.202', 'url': 'https://httpbin.org/delay/2'}\n"
     ]
    }
   ],
   "source": [
    "import asyncio\n",
    "import aiohttp\n",
    "import nest_asyncio\n",
    "\n",
    "# Aplicar nest_asyncio\n",
    "nest_asyncio.apply()\n",
    "\n",
    "async def fetch(session, url):\n",
    "    async with session.get(url) as response:\n",
    "        return await response.json() \n",
    "\n",
    "async def main():\n",
    "    urls = [\n",
    "        'https://jsonplaceholder.typicode.com/todos/1',\n",
    "        'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true',\n",
    "        'https://httpbin.org/delay/2' \n",
    "    ]\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        tasks = [fetch(session, url) for url in urls]\n",
    "        responses = await asyncio.gather(*tasks)\n",
    "        for response in responses:\n",
    "            print(response)  \n",
    "asyncio.run(main())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aef7f3cf-600f-4fae-be9b-022c72403d45",
   "metadata": {},
   "source": [
    "Este enfoque permite ejecutar código asyncio en Jupyter Notebook sin conflictos con el bucle de eventos del entorno."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8307ddb",
   "metadata": {},
   "source": [
    "#### Ejercicio 10: Uso de concurrent.futures para procesamiento distribuido\n",
    "\n",
    "Implementa un script que use concurrent.futures y ThreadPoolExecutor para calcular el resultado de aplicar una función compleja (como el cálculo de la serie Fibonacci) a diferentes entradas de manera distribuida."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a5b9cf2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fibonacci(10) = 55\n",
      "Fibonacci(20) = 6765\n",
      "Fibonacci(30) = 832040\n",
      "Fibonacci(35) = 9227465\n",
      "Fibonacci(40) = 102334155\n"
     ]
    }
   ],
   "source": [
    "import concurrent.futures\n",
    "\n",
    "def fibonacci(n):\n",
    "    \"\"\" Calcula el n-ésimo número de Fibonacci. \"\"\"\n",
    "    if n <= 1:\n",
    "        return n\n",
    "    else:\n",
    "        return fibonacci(n-1) + fibonacci(n-2)\n",
    "\n",
    "def main():\n",
    "    # Lista de números para los cuales calcular la serie Fibonacci\n",
    "    nums = [10, 20, 30, 35, 40]\n",
    "    \n",
    "    # Usar ThreadPoolExecutor para calcular los números de Fibonacci de forma concurrente\n",
    "    with concurrent.futures.ThreadPoolExecutor() as executor:\n",
    "        # Usamos map para aplicar la función a cada elemento en nums\n",
    "        results = executor.map(fibonacci, nums)\n",
    "        \n",
    "        # Imprimir resultados\n",
    "        for num, result in zip(nums, results):\n",
    "            print(f'Fibonacci({num}) = {result}')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57794ad7",
   "metadata": {},
   "source": [
    "#### Ejercicio 11: Uso de asyncio con manejo de excepciones\n",
    "\n",
    "Desarrolla un script utilizando asyncio que realice peticiones HTTP a varios endpoints. Utiliza manejo de excepciones para tratar adecuadamente los errores de conexión y otros errores HTTP."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "de26f182",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error de conexión con http://nonexistent.url\n",
      "Respuesta exitosa de http://example.com: <!doctype html>\n",
      "<html>\n",
      "<head>\n",
      "    <title>Example Domain</title>\n",
      "\n",
      "    <meta charset=\"utf-8\" />\n",
      "    <m...\n",
      "Error 500 desde http://httpbin.org/status/500\n",
      "Error 404 desde http://httpbin.org/status/404\n"
     ]
    }
   ],
   "source": [
    "import aiohttp\n",
    "import asyncio\n",
    "\n",
    "async def fetch_url(session, url):\n",
    "    try:\n",
    "        async with session.get(url) as response:\n",
    "            if response.status == 200:\n",
    "                data = await response.text()\n",
    "                print(f\"Respuesta exitosa de {url}: {data[:100]}...\")  # Imprime los primeros 100 caracteres\n",
    "            else:\n",
    "                print(f\"Error {response.status} desde {url}\")\n",
    "    except aiohttp.ClientConnectionError:\n",
    "        print(f\"Error de conexión con {url}\")\n",
    "    except aiohttp.ClientError as e:\n",
    "        print(f\"Error al realizar la petición a {url}: {e}\")\n",
    "\n",
    "async def main(urls):\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        tasks = [fetch_url(session, url) for url in urls]\n",
    "        await asyncio.gather(*tasks)\n",
    "\n",
    "# Ejecuta directamente la función main con await en Jupyter\n",
    "if __name__ == \"__main__\":\n",
    "    urls = [\n",
    "        \"http://example.com\",\n",
    "        \"http://nonexistent.url\",\n",
    "        \"http://httpbin.org/status/404\",\n",
    "        \"http://httpbin.org/status/500\"\n",
    "    ]\n",
    "    \n",
    "    # Directamente usar await aquí si es una celda de Jupyter\n",
    "    await main(urls)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7efcc045",
   "metadata": {},
   "source": [
    "#### Ejercicio 12: Multiprocessing con uso de Queue para intercambio de datos\n",
    "\n",
    "Implementa un programa que use multiprocessing donde varios procesos productores generan números aleatorios y un consumidor los suma. Usa Queue para la comunicación entre procesos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9addd445",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Producido 58\n",
      "Producido 4\n",
      "Producido 69\n",
      "Consumido 58, la suma total es ahora 58\n",
      "Consumido 4, la suma total es ahora 62\n",
      "Consumido 69, la suma total es ahora 131\n",
      "Producido 93Consumido 93, la suma total es ahora 224\n",
      "\n",
      "Producido 2Consumido 2, la suma total es ahora 226\n",
      "\n",
      "Producido 86Consumido 86, la suma total es ahora 312\n",
      "\n",
      "Producido 85Consumido 85, la suma total es ahora 397\n",
      "\n",
      "Producido 62Consumido 62, la suma total es ahora 459\n",
      "\n",
      "Producido 20Consumido 20, la suma total es ahora 479\n",
      "\n",
      "Producido 89Consumido 89, la suma total es ahora 568\n",
      "\n",
      "Producido 66Consumido 66, la suma total es ahora 634\n",
      "\n",
      "Producido 72Consumido 72, la suma total es ahora 706\n",
      "\n",
      "Producido 14Consumido 14, la suma total es ahora 720\n",
      "\n",
      "Producido 6Consumido 6, la suma total es ahora 726\n",
      "\n",
      "Producido 55Consumido 55, la suma total es ahora 781\n",
      "\n",
      "Producido 88Consumido 88, la suma total es ahora 869\n",
      "\n",
      "Producido 14Consumido 14, la suma total es ahora 883\n",
      "\n",
      "Producido 49Consumido 49, la suma total es ahora 932\n",
      "\n",
      "Producido 27Consumido 27, la suma total es ahora 959\n",
      "\n",
      "Producido 1Consumido 1, la suma total es ahora 960\n",
      "\n",
      "Producido 49Consumido 49, la suma total es ahora 1009\n",
      "\n",
      "Producido 7\n",
      "Consumido 7, la suma total es ahora 1016\n",
      "Producido 75Consumido 75, la suma total es ahora 1091\n",
      "\n",
      "Producido 29Consumido 29, la suma total es ahora 1120\n",
      "\n",
      "Producido 55Consumido 55, la suma total es ahora 1175\n",
      "\n",
      "Producido 70Consumido 70, la suma total es ahora 1245\n",
      "\n",
      "Producido 20Consumido 20, la suma total es ahora 1265\n",
      "\n",
      "Producido 90Consumido 90, la suma total es ahora 1355\n",
      "\n",
      "Producido 22Consumido 22, la suma total es ahora 1377\n",
      "\n",
      "Producido 24Consumido 24, la suma total es ahora 1401\n",
      "\n",
      "La suma final es 1401\n"
     ]
    }
   ],
   "source": [
    "import multiprocessing\n",
    "import random\n",
    "import time\n",
    "\n",
    "def producer(queue):\n",
    "    \"\"\" Función que simula un productor de números aleatorios. \"\"\"\n",
    "    for _ in range(10):\n",
    "        num = random.randint(1, 100)\n",
    "        queue.put(num)\n",
    "        print(f\"Producido {num}\")\n",
    "        time.sleep(random.random())\n",
    "    # Indicar que la producción ha terminado\n",
    "    queue.put(None)\n",
    "\n",
    "def consumer(queue, num_producers):\n",
    "    \"\"\" Función que simula un consumidor que suma los números recibidos. \"\"\"\n",
    "    total_sum = 0\n",
    "    termination_count = 0\n",
    "    \n",
    "    while True:\n",
    "        num = queue.get()\n",
    "        if num is None:\n",
    "            termination_count += 1\n",
    "            if termination_count == num_producers:\n",
    "                break\n",
    "        else:\n",
    "            total_sum += num\n",
    "            print(f\"Consumido {num}, la suma total es ahora {total_sum}\")\n",
    "    \n",
    "    print(f\"La suma final es {total_sum}\")\n",
    "\n",
    "def main():\n",
    "    # Número de procesos productores\n",
    "    num_producers = 3\n",
    "    \n",
    "    # Crear una cola para comunicar números entre productores y consumidor\n",
    "    queue = multiprocessing.Queue()\n",
    "    \n",
    "    # Crear y comenzar los procesos productores\n",
    "    producers = [multiprocessing.Process(target=producer, args=(queue,)) for _ in range(num_producers)]\n",
    "    for p in producers:\n",
    "        p.start()\n",
    "    \n",
    "    # Crear y comenzar el proceso consumidor\n",
    "    consumer_process = multiprocessing.Process(target=consumer, args=(queue, num_producers))\n",
    "    consumer_process.start()\n",
    "    \n",
    "    # Esperar a que todos los procesos productores terminen\n",
    "    for p in producers:\n",
    "        p.join()\n",
    "    \n",
    "    # Esperar a que el proceso consumidor termine\n",
    "    consumer_process.join()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "22e12feb",
   "metadata": {},
   "source": [
    "#### Ejercicio 13: Microservicios con comunicación entre servicios\n",
    "\n",
    "Crea dos microservicios con Flask. El primero genera un número aleatorio. El segundo servicio recibe ese número, lo eleva al cuadrado y devuelve el resultado. Implementa la comunicación entre ambos servicios.\n",
    "\n",
    "Para crear dos microservicios que se comuniquen entre sí usando Flask, podemos definir dos aplicaciones Flask separadas. El primer servicio generará un número aleatorio y el segundo recibirá este número, lo elevará al cuadrado y devolverá el resultado. Vamos a utilizar requests en el segundo servicio para realizar la petición al primero y obtener el número aleatorio.\n",
    "\n",
    "Antes de empezar, asegúrate de tener instalado Flask y Requests. Si no los tienes, puedes instalarlos usando pip:\n",
    "\n",
    "pip install flask requests\n",
    "\n",
    "Servicio 1: Generador de números aleatorios\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7be27cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile service1.py\n",
    "\n",
    "from flask import Flask\n",
    "import random\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/random')\n",
    "def random_number():\n",
    "    \"\"\"Genera un número aleatorio entre 1 y 100.\"\"\"\n",
    "    number = random.randint(1, 100)\n",
    "    return {'number': number}\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(port=5000) ## Cambia de puerto\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46e03796-e2f2-44db-9a6f-ee042c03abca",
   "metadata": {},
   "source": [
    "Este servicio corre en el puerto 5000 y tiene un endpoint /random que devuelve un número aleatorio en formato JSON.\n",
    "\n",
    "Servicio 2: Calculador del cuadrado\n",
    "\n",
    "Guarda este código en un archivo llamado service2.py:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72b56a98-4706-45a2-89d3-056e8b418229",
   "metadata": {},
   "outputs": [],
   "source": [
    "%%writefile service2.py\n",
    "from flask import Flask, jsonify, request\n",
    "import requests\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/square', methods=['GET'])\n",
    "def square():\n",
    "    \"\"\"Obtiene un número aleatorio del servicio 1 y devuelve su cuadrado.\"\"\"\n",
    "    response = requests.get('http://localhost:5000/random')\n",
    "    number = response.json()['number']\n",
    "    squared_number = number ** 2\n",
    "    return jsonify(squared_number=squared_number)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(port=5001)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f79ce94e-c628-4af7-b280-e052345c7827",
   "metadata": {},
   "source": [
    "Para probar la comunicación, puedes usar una herramienta como Postman o simplemente un navegador web o curl para acceder a http://localhost:5001/square. Esto debería darte el cuadrado de un número aleatorio generado por el primer servicio."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37af689d",
   "metadata": {},
   "source": [
    "#### Ejercicio 14: Uso de concurrent.futures para scraping de datos\n",
    "\n",
    "Implementa un programa que utilice concurrent.futures para hacer scraping de datos de varias páginas web de manera concurrente y recolecte datos específicos.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d0906fc-9695-4af3-ad00-db4be64dd415",
   "metadata": {},
   "source": [
    "Para implementar un programa que utiliza concurrent.futures para hacer scraping de datos de varias páginas web de manera concurrente, necesitaremos usar la biblioteca requests para hacer las peticiones HTTP y BeautifulSoup de bs4 para parsear el contenido HTML y extraer los datos necesarios. Primero, asegúrate de tener instaladas ambas bibliotecas, si no, puedes instalarlas con pip:\n",
    "\n",
    "pip install requests beautifulsoup4\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f2a73774-dc25-4b5a-8400-be3c0072af44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "URL: https://www.bbc.com\n",
      "Title: No title found\n",
      "\n",
      "URL: https://www.cnn.com\n",
      "Title: No title found\n",
      "\n",
      "URL: https://www.nytimes.com\n",
      "Title: New York Times - Top Stories\n",
      "\n",
      "URL: https://www.theguardian.com\n",
      "Title: No title found\n",
      "\n",
      "URL: https://www.nbcnews.com\n",
      "Title: No title found\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/c-lara/anaconda3/lib/python3.8/site-packages/bs4/builder/__init__.py:314: RuntimeWarning: coroutine 'main' was never awaited\n",
      "  for attr in list(attrs.keys()):\n",
      "RuntimeWarning: Enable tracemalloc to get the object allocation traceback\n"
     ]
    }
   ],
   "source": [
    "import concurrent.futures\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "def fetch_and_parse(url):\n",
    "    \"\"\"Función que obtiene y parsea el contenido de una URL dada.\"\"\"\n",
    "    try:\n",
    "        response = requests.get(url, timeout=10)\n",
    "        response.raise_for_status()  # Asegura que la respuesta fue exitosa\n",
    "        soup = BeautifulSoup(response.text, 'html.parser')\n",
    "        title = soup.find('h1')  # Buscar el primer <h1> tag, que a menudo es el título principal\n",
    "        if title:\n",
    "            return (url, title.text.strip())\n",
    "        else:\n",
    "            return (url, 'No title found')\n",
    "    except requests.RequestException as e:\n",
    "        return (url, f'Error fetching the page: {e}')\n",
    "\n",
    "def main(urls):\n",
    "    \"\"\"Función principal que ejecuta tareas concurrentes.\"\"\"\n",
    "    with concurrent.futures.ThreadPoolExecutor() as executor:\n",
    "        results = list(executor.map(fetch_and_parse, urls))\n",
    "        \n",
    "        for url, title in results:\n",
    "            print(f'URL: {url}\\nTitle: {title}\\n')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    urls = [\n",
    "        \"https://www.bbc.com\",\n",
    "        \"https://www.cnn.com\",\n",
    "        \"https://www.nytimes.com\",\n",
    "        \"https://www.theguardian.com\",\n",
    "        \"https://www.nbcnews.com\"\n",
    "    ]\n",
    "    main(urls)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bd12f0b",
   "metadata": {},
   "source": [
    "#### Ejercicio 15: Sistema de procesamiento de comandos paralelo\n",
    "\n",
    "Implementa un sistema que utilice concurrent.futures para ejecutar comandos del sistema operativo en paralelo, recolectar sus salidas, y procesar los resultados de forma concurrente.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4872046b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Command: echo Hello, World!\n",
      "Output: Hello, World!\n",
      "\n",
      "\n",
      "Command: ls -la\n",
      "Output: total 452\n",
      "drwxrwxr-x 11 c-lara c-lara   4096 may 11 21:10 .\n",
      "drwxr----- 73 c-lara c-lara   4096 may 11 20:31 ..\n",
      "drwxrwxr-x  2 c-lara c-lara   4096 abr 20 13:06 Actividad0\n",
      "drwxrwxr-x  2 c-lara c-lara   4096 abr 20 13:06 Actividad2\n",
      "drwxrwxr-x  7 c-lara c-lara   4096 may  1 18:19 Actividad4\n",
      "-rw-rw-r--  1 c-lara c-lara  53949 may  6 23:12 Actividad5-C8286.ipynb\n",
      "drwxrwxr-x  2 c-lara c-lara   4096 may 11 21:07 Actividad6\n",
      "-rw-rw-r--  1 c-lara c-lara  40168 may 11 21:10 Actividad6-C8286.ipynb\n",
      "-rw-rw-r--  1 c-lara c-lara  65393 abr 20 13:06 Caso-Refactorizacion.ipynb\n",
      "-rw-rw-r--  1 c-lara c-lara  19869 may  6 12:19 Concurrencia.ipynb\n",
      "drwxrwxr-x  2 c-lara c-lara   4096 abr 20 13:06 Evaluacion2\n",
      "-rw-rw-r--  1 c-lara c-lara  53880 may  6 12:14 Evaluacion5-C8286.ipynb\n",
      "drwxrwxr-x  2 c-lara c-lara   4096 may  3 13:42 Evaluacion6\n",
      "-rw-rw-r--  1 c-lara c-lara 113496 may  6 16:00 Evaluacion7-C8286.ipynb\n",
      "drwxrwxr-x  8 c-lara c-lara   4096 may 11 20:36 .git\n",
      "-rw-rw-r--  1 c-lara c-lara     21 may 11 06:30 .gitignore\n",
      "drwxrwxr-x  2 c-lara c-lara   4096 may 11 11:45 .ipynb_checkpoints\n",
      "drwxrwxr-x  3 c-lara c-lara   4096 may  1 18:19 LenguajeC\n",
      "-rw-rw-r--  1 c-lara c-lara  22073 may  6 12:19 Paralelismo.ipynb\n",
      "-rw-rw-r--  1 c-lara c-lara     19 abr 20 13:06 README.md\n",
      "-rw-rw-r--  1 c-lara c-lara  25415 abr 20 13:06 Repaso.ipynb\n",
      "\n",
      "\n",
      "Command: pwd\n",
      "Output: /home/c-lara/Actividades-C8286\n",
      "\n",
      "\n",
      "Command: invalid_command\n",
      "Error: \n",
      "Return Code: 127\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import concurrent.futures\n",
    "import subprocess\n",
    "\n",
    "def execute_command(command):\n",
    "    \"\"\"Ejecuta un comando del sistema y retorna la salida.\"\"\"\n",
    "    try:\n",
    "        # Ejecutar el comando y capturar la salida estándar y el error estándar\n",
    "        result = subprocess.run(command, shell=True, text=True, capture_output=True)\n",
    "        return (command, result.stdout, result.returncode)\n",
    "    except subprocess.CalledProcessError as e:\n",
    "        # En caso de error en la ejecución del comando\n",
    "        return (command, e.output, e.returncode)\n",
    "\n",
    "def main(commands):\n",
    "    \"\"\"Función principal para ejecutar comandos en paralelo.\"\"\"\n",
    "    with concurrent.futures.ThreadPoolExecutor() as executor:\n",
    "        # Mapa de los comandos a la función execute_command\n",
    "        results = list(executor.map(execute_command, commands))\n",
    "\n",
    "        # Procesar los resultados\n",
    "        for command, output, returncode in results:\n",
    "            if returncode == 0:\n",
    "                print(f\"Command: {command}\\nOutput: {output}\\n\")\n",
    "            else:\n",
    "                print(f\"Command: {command}\\nError: {output}\\nReturn Code: {returncode}\\n\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    # Lista de comandos del sistema para ejecutar\n",
    "    commands = [\n",
    "        'echo Hello, World!',\n",
    "        'ls -la',\n",
    "        'pwd',\n",
    "        'invalid_command'\n",
    "    ]\n",
    "    \n",
    "    main(commands)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79f86b69",
   "metadata": {},
   "source": [
    "#### Ejercicio 16: Plataforma de análisis de datos distribuidos\n",
    "\n",
    "Crea una plataforma de análisis de datos que utilice multiprocessing y concurrent.futures para procesar grandes volúmenes de datos distribuidos entre varios procesos, realizando cálculos estadísticos y generación de reportes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cd904f0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Final Report:\n",
      "           mean   std_dev       max       min\n",
      "count  8.000000  8.000000  8.000000  8.000000\n",
      "mean   0.005696  0.997463  3.576763 -3.215886\n",
      "std    0.036469  0.011213  0.554748  0.433780\n",
      "min   -0.055656  0.978360  2.857251 -3.901841\n",
      "25%   -0.018022  0.991786  3.135587 -3.398615\n",
      "50%    0.014096  0.997752  3.649276 -3.066676\n",
      "75%    0.032760  1.001337  3.967593 -2.916686\n",
      "max    0.047480  1.014811  4.247125 -2.769657\n"
     ]
    }
   ],
   "source": [
    "import concurrent.futures\n",
    "import multiprocessing\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "def analyze_data(data_chunk):\n",
    "    \"\"\"Función que realiza cálculos estadísticos en un fragmento de datos.\"\"\"\n",
    "    result = {\n",
    "        'mean': np.mean(data_chunk),\n",
    "        'std_dev': np.std(data_chunk),\n",
    "        'max': np.max(data_chunk),\n",
    "        'min': np.min(data_chunk)\n",
    "    }\n",
    "    return result\n",
    "\n",
    "def data_distributor(data, num_workers):\n",
    "    \"\"\"Distribuye los datos en fragmentos para cada trabajador.\"\"\"\n",
    "    chunk_size = len(data) // num_workers\n",
    "    return (data[i * chunk_size:(i + 1) * chunk_size] for i in range(num_workers))\n",
    "\n",
    "def main():\n",
    "    # Simulando algunos datos grandes\n",
    "    data = np.random.randn(10000)  # 10,000 puntos de datos aleatorios\n",
    "    \n",
    "    num_workers = multiprocessing.cpu_count()  # Número de procesos a utilizar\n",
    "    \n",
    "    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:\n",
    "        # Distribuir datos\n",
    "        chunks = data_distributor(data, num_workers)\n",
    "        \n",
    "        # Ejecutar análisis en paralelo\n",
    "        results = list(executor.map(analyze_data, chunks))\n",
    "        \n",
    "        # Procesar y combinar resultados\n",
    "        final_report = pd.DataFrame(results)\n",
    "        print(\"Reporte final:\")\n",
    "        print(final_report.describe())  # Genera un reporte estadístico del resumen de resultados\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10327651",
   "metadata": {},
   "source": [
    "#### Ejercicio 17:Descarga de imágenes en paralelo con concurrent.futures\n",
    "\n",
    "Escribe un script que utilice concurrent.futures para descargar imágenes en paralelo. Debes descargar al menos cinco imágenes de URLs especificadas y guardarlas en el disco localmente.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2e99aa29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Error al descargar https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg/320px-Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg: 404 Client Error: Not Found for url: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg/320px-Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg\n",
      "Error al descargar https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg/320px-NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg: 404 Client Error: Not Found for url: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg/320px-NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg\n",
      "Descarga completada: 220px-June_odd-eyed-cat.jpg\n",
      "Error al descargar https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Tulip_-_floriade_canberra.jpg/320px-Tulip_-_floriade_canberra.jpg: 404 Client Error: Not Found for url: https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Tulip_-_floriade_canberra.jpg/320px-Tulip_-_floriade_canberra.jpg\n",
      "Descarga completada: 320px-Lake_mapourika_NZ.jpeg\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import requests\n",
    "from concurrent.futures import ThreadPoolExecutor\n",
    "\n",
    "# Lista de URLs de las imágenes que deseamos descargar\n",
    "image_urls = [\n",
    "    \"https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Lake_mapourika_NZ.jpeg/320px-Lake_mapourika_NZ.jpeg\",\n",
    "    \"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/220px-June_odd-eyed-cat.jpg\",\n",
    "    \"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg/320px-Hawthorne_Bridge%2C_Portland%2C_Oregon_%282018%29_-_2.jpg\",\n",
    "    \"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg/320px-NYC_Midtown_Skyline_at_night_-_Jan_2006_edit1.jpg\",\n",
    "    \"https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Tulip_-_floriade_canberra.jpg/320px-Tulip_-_floriade_canberra.jpg\"\n",
    "]\n",
    "\n",
    "\n",
    "def download_image(url):\n",
    "    \"\"\"Función para descargar una imagen y guardarla localmente.\"\"\"\n",
    "    try:\n",
    "        response = requests.get(url)\n",
    "        response.raise_for_status()  # Asegura que la respuesta fue exitosa\n",
    "\n",
    "        # Extraer nombre de archivo de la URL\n",
    "        file_name = os.path.basename(url)\n",
    "        \n",
    "        # Guardar el archivo en el directorio actual\n",
    "        with open(file_name, 'wb') as f:\n",
    "            f.write(response.content)\n",
    "        print(f\"Descarga completada: {file_name}\")\n",
    "    except requests.RequestException as e:\n",
    "        print(f\"Error al descargar {url}: {e}\")\n",
    "\n",
    "def main():\n",
    "    # Usar un ThreadPoolExecutor para descargar imágenes en paralelo\n",
    "    with ThreadPoolExecutor(max_workers=5) as executor:\n",
    "        executor.map(download_image, image_urls)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89409b3e",
   "metadata": {},
   "source": [
    "#### Ejercicio 18: Asincronía con asyncio\n",
    "\n",
    "Escribe un script que utilice asyncio para realizar peticiones HTTP asincrónicas a tres APIs diferentes y recolecte sus respuestas.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "df8a3f64",
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "asyncio.run() cannot be called from a running event loop",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Input \u001b[0;32mIn [15]\u001b[0m, in \u001b[0;36m<cell line: 25>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[38;5;66;03m# Ejecutar el event loop\u001b[39;00m\n\u001b[1;32m     25\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[0;32m---> 26\u001b[0m     \u001b[43masyncio\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmain\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.8/asyncio/runners.py:33\u001b[0m, in \u001b[0;36mrun\u001b[0;34m(main, debug)\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[38;5;124;03m\"\"\"Execute the coroutine and return the result.\u001b[39;00m\n\u001b[1;32m     10\u001b[0m \n\u001b[1;32m     11\u001b[0m \u001b[38;5;124;03mThis function runs the passed coroutine, taking care of\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[38;5;124;03m    asyncio.run(main())\u001b[39;00m\n\u001b[1;32m     31\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m     32\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m---> 33\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\n\u001b[1;32m     34\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124masyncio.run() cannot be called from a running event loop\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     36\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m coroutines\u001b[38;5;241m.\u001b[39miscoroutine(main):\n\u001b[1;32m     37\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma coroutine was expected, got \u001b[39m\u001b[38;5;132;01m{!r}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;241m.\u001b[39mformat(main))\n",
      "\u001b[0;31mRuntimeError\u001b[0m: asyncio.run() cannot be called from a running event loop"
     ]
    }
   ],
   "source": [
    "import aiohttp\n",
    "import asyncio\n",
    "\n",
    "async def fetch(session, url):\n",
    "    \"\"\"Función asincrónica para realizar una petición HTTP.\"\"\"\n",
    "    async with session.get(url) as response:\n",
    "        return await response.text()\n",
    "\n",
    "async def main():\n",
    "    \"\"\"Función principal que coordina las peticiones HTTP asincrónicas.\"\"\"\n",
    "    urls = [\n",
    "        'https://api.github.com',  # GitHub API para metadatos\n",
    "        'https://api.ipify.org?format=json',  # API para obtener la IP pública\n",
    "        'https://jsonplaceholder.typicode.com/todos/1'  # API de ejemplo de JSONPlaceholder\n",
    "    ]\n",
    "\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        tasks = [fetch(session, url) for url in urls]\n",
    "        responses = await asyncio.gather(*tasks)\n",
    "\n",
    "        for response in responses:\n",
    "            print(response)\n",
    "\n",
    "# Ejecutar el event loop\n",
    "if __name__ == '__main__':\n",
    "    asyncio.run(main())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7ab58ca-1f73-43d9-b9ef-bd18c7e71d38",
   "metadata": {},
   "source": [
    "Modificamos el codigo:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f4607daa-59e8-44a0-8d8c-4317cfe8f0fa",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "asyncio.run() cannot be called from a running event loop",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Input \u001b[0;32mIn [16]\u001b[0m, in \u001b[0;36m<cell line: 26>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     26\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m---> 27\u001b[0m     \u001b[43mloop\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun_until_complete\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmain\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     28\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m:\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.8/asyncio/base_events.py:592\u001b[0m, in \u001b[0;36mBaseEventLoop.run_until_complete\u001b[0;34m(self, future)\u001b[0m\n\u001b[1;32m    591\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_closed()\n\u001b[0;32m--> 592\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_check_running\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    594\u001b[0m new_task \u001b[38;5;241m=\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m futures\u001b[38;5;241m.\u001b[39misfuture(future)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.8/asyncio/base_events.py:552\u001b[0m, in \u001b[0;36mBaseEventLoop._check_running\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    551\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_running():\n\u001b[0;32m--> 552\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mThis event loop is already running\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m    553\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[0;31mRuntimeError\u001b[0m: This event loop is already running",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Input \u001b[0;32mIn [16]\u001b[0m, in \u001b[0;36m<cell line: 26>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     27\u001b[0m     loop\u001b[38;5;241m.\u001b[39mrun_until_complete(main())\n\u001b[1;32m     28\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m:\n\u001b[0;32m---> 29\u001b[0m     \u001b[43masyncio\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmain\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.8/asyncio/runners.py:33\u001b[0m, in \u001b[0;36mrun\u001b[0;34m(main, debug)\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[38;5;124;03m\"\"\"Execute the coroutine and return the result.\u001b[39;00m\n\u001b[1;32m     10\u001b[0m \n\u001b[1;32m     11\u001b[0m \u001b[38;5;124;03mThis function runs the passed coroutine, taking care of\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[38;5;124;03m    asyncio.run(main())\u001b[39;00m\n\u001b[1;32m     31\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m     32\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m---> 33\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\n\u001b[1;32m     34\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124masyncio.run() cannot be called from a running event loop\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     36\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m coroutines\u001b[38;5;241m.\u001b[39miscoroutine(main):\n\u001b[1;32m     37\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124ma coroutine was expected, got \u001b[39m\u001b[38;5;132;01m{!r}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;241m.\u001b[39mformat(main))\n",
      "\u001b[0;31mRuntimeError\u001b[0m: asyncio.run() cannot be called from a running event loop"
     ]
    }
   ],
   "source": [
    "import aiohttp\n",
    "import asyncio\n",
    "\n",
    "async def fetch(session, url):\n",
    "    \"\"\"Función asincrónica para realizar una petición HTTP.\"\"\"\n",
    "    async with session.get(url) as response:\n",
    "        return await response.text()\n",
    "\n",
    "async def main():\n",
    "    \"\"\"Función principal que coordina las peticiones HTTP asincrónicas.\"\"\"\n",
    "    urls = [\n",
    "        'https://api.github.com',  # GitHub API para metadatos\n",
    "        'https://api.ipify.org?format=json',  # API para obtener la IP pública\n",
    "        'https://jsonplaceholder.typicode.com/todos/1'  # API de ejemplo de JSONPlaceholder\n",
    "    ]\n",
    "\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        tasks = [fetch(session, url) for url in urls]\n",
    "        responses = await asyncio.gather(*tasks)\n",
    "\n",
    "        for response in responses:\n",
    "            print(response)\n",
    "\n",
    "# Obtener el bucle de eventos existente y ejecutar la función principal\n",
    "loop = asyncio.get_event_loop()\n",
    "try:\n",
    "    loop.run_until_complete(main())\n",
    "except RuntimeError:\n",
    "    asyncio.run(main())  # Solo para casos donde el primer método falla (como ejecución fuera de notebook)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e7f3dbd-c2d8-45b7-ab9d-347f690ec6db",
   "metadata": {},
   "source": [
    "Usamos nest_asyncio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7dbb549c-55de-4d42-8520-48f561c29ad7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"current_user_url\":\"https://api.github.com/user\",\"current_user_authorizations_html_url\":\"https://github.com/settings/connections/applications{/client_id}\",\"authorizations_url\":\"https://api.github.com/authorizations\",\"code_search_url\":\"https://api.github.com/search/code?q={query}{&page,per_page,sort,order}\",\"commit_search_url\":\"https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}\",\"emails_url\":\"https://api.github.com/user/emails\",\"emojis_url\":\"https://api.github.com/emojis\",\"events_url\":\"https://api.github.com/events\",\"feeds_url\":\"https://api.github.com/feeds\",\"followers_url\":\"https://api.github.com/user/followers\",\"following_url\":\"https://api.github.com/user/following{/target}\",\"gists_url\":\"https://api.github.com/gists{/gist_id}\",\"hub_url\":\"https://api.github.com/hub\",\"issue_search_url\":\"https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}\",\"issues_url\":\"https://api.github.com/issues\",\"keys_url\":\"https://api.github.com/user/keys\",\"label_search_url\":\"https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}\",\"notifications_url\":\"https://api.github.com/notifications\",\"organization_url\":\"https://api.github.com/orgs/{org}\",\"organization_repositories_url\":\"https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}\",\"organization_teams_url\":\"https://api.github.com/orgs/{org}/teams\",\"public_gists_url\":\"https://api.github.com/gists/public\",\"rate_limit_url\":\"https://api.github.com/rate_limit\",\"repository_url\":\"https://api.github.com/repos/{owner}/{repo}\",\"repository_search_url\":\"https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}\",\"current_user_repositories_url\":\"https://api.github.com/user/repos{?type,page,per_page,sort}\",\"starred_url\":\"https://api.github.com/user/starred{/owner}{/repo}\",\"starred_gists_url\":\"https://api.github.com/gists/starred\",\"topic_search_url\":\"https://api.github.com/search/topics?q={query}{&page,per_page}\",\"user_url\":\"https://api.github.com/users/{user}\",\"user_organizations_url\":\"https://api.github.com/user/orgs\",\"user_repositories_url\":\"https://api.github.com/users/{user}/repos{?type,page,per_page,sort}\",\"user_search_url\":\"https://api.github.com/search/users?q={query}{&page,per_page,sort,order}\"}\n",
      "{\"ip\":\"190.238.29.202\"}\n",
      "{\n",
      "  \"userId\": 1,\n",
      "  \"id\": 1,\n",
      "  \"title\": \"delectus aut autem\",\n",
      "  \"completed\": false\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "import aiohttp\n",
    "import asyncio\n",
    "import nest_asyncio\n",
    "\n",
    "nest_asyncio.apply()  # Aplica parche a asyncio para permitir anidamiento de bucles\n",
    "\n",
    "async def fetch(session, url):\n",
    "    \"\"\"Función asincrónica para realizar una petición HTTP.\"\"\"\n",
    "    async with session.get(url) as response:\n",
    "        return await response.text()\n",
    "\n",
    "async def main():\n",
    "    \"\"\"Función principal que coordina las peticiones HTTP asincrónicas.\"\"\"\n",
    "    urls = [\n",
    "        'https://api.github.com',  # GitHub API para metadatos\n",
    "        'https://api.ipify.org?format=json',  # API para obtener la IP pública\n",
    "        'https://jsonplaceholder.typicode.com/todos/1'  # API de ejemplo de JSONPlaceholder\n",
    "    ]\n",
    "\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        tasks = [fetch(session, url) for url in urls]\n",
    "        responses = await asyncio.gather(*tasks)\n",
    "\n",
    "        for response in responses:\n",
    "            print(response)\n",
    "\n",
    "# Ejecutar el script en un entorno con un bucle de eventos ya en ejecución\n",
    "asyncio.run(main())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "032ef48e",
   "metadata": {},
   "source": [
    "#### Ejercicio 19: Uso de corutinas con generadores\n",
    "\n",
    "Implementa una corutina que genere números primos secuencialmente cada vez que se le envíe un valor. Usa el método send() para obtener el siguiente número primo.\n",
    "\n",
    "Podemos hacer uso del método send() para interactuar con el generador y obtener el siguiente número primo cada vez que se envíe un valor."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ed0d2254",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "5\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "def is_prime(num):\n",
    "    \"\"\"Función auxiliar para verificar si un número es primo.\"\"\"\n",
    "    if num <= 1:\n",
    "        return False\n",
    "    if num <= 3:\n",
    "        return True\n",
    "    if num % 2 == 0 or num % 3 == 0:\n",
    "        return False\n",
    "    i = 5\n",
    "    while i * i <= num:\n",
    "        if num % i == 0 or num % (i + 2) == 0:\n",
    "            return False\n",
    "        i += 6\n",
    "    return True\n",
    "\n",
    "def prime_coroutine():\n",
    "    \"\"\"Generador que produce números primos secuencialmente.\"\"\"\n",
    "    num = 2\n",
    "    while True:\n",
    "        if is_prime(num):\n",
    "            received = yield num\n",
    "            if received is not None:\n",
    "                num = received\n",
    "        num += 1\n",
    "\n",
    "# Código para interactuar con la corutina\n",
    "generator = prime_coroutine()  # Crea la corutina\n",
    "print(next(generator))  # Inicia la corutina y obtiene el primer número primo\n",
    "\n",
    "# Obtener los siguientes números primos\n",
    "print(generator.send(None))  # Continuar desde el último número primo\n",
    "print(generator.send(None))  # Continuar desde el último número primo\n",
    "print(generator.send(None))  # Continuar desde el último número primo\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "63ca76d3",
   "metadata": {},
   "source": [
    "#### Ejercicio 20: Programación funcional con map y reduce para procesamiento distribuido\n",
    "\n",
    "Utiliza las funciones map y reduce de la biblioteca functools para encontrar la suma de los cuadrados de una lista de números distribuida entre varios procesos.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1ce7aa69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "La suma de los cuadrados es: 385\n"
     ]
    }
   ],
   "source": [
    "import multiprocessing\n",
    "from functools import reduce\n",
    "\n",
    "def square(n):\n",
    "    \"\"\"Devuelve el cuadrado de un número.\"\"\"\n",
    "    return n * n\n",
    "\n",
    "def add(x, y):\n",
    "    \"\"\"Suma dos números.\"\"\"\n",
    "    return x + y\n",
    "\n",
    "def parallel_sum_of_squares(numbers):\n",
    "    \"\"\"Calcula la suma de los cuadrados de una lista de números distribuidos entre varios procesos.\"\"\"\n",
    "    pool_size = multiprocessing.cpu_count()  # Número de procesos igual al número de núcleos disponibles\n",
    "    with multiprocessing.Pool(processes=pool_size) as pool:\n",
    "        # Distribuir el cálculo del cuadrado de cada número\n",
    "        squares = pool.map(square, numbers)\n",
    "        # Reducir la lista de cuadrados sumándolos\n",
    "        result = reduce(add, squares)\n",
    "    return result\n",
    "\n",
    "# Lista de números\n",
    "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "\n",
    "# Ejecutar la función y mostrar el resultado\n",
    "result = parallel_sum_of_squares(numbers)\n",
    "print(\"La suma de los cuadrados es:\", result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd3aeb2c-0d03-41fb-9553-297da33b283e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
