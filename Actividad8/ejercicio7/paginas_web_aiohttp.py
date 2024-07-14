'''Ejercicio 7: Descarga paralela de páginas Web con aiohttp y asyncio
Descripción: Implementa un sistema para descargar varias páginas web en paralelo utilizando aiohttp y asyncio.
Tareas:
   Crear una lista de URLs.
   Usar aiohttp y asyncio para descargar las páginas web en paralelo.
   Almacenar el contenido de cada página en un archivo separado.
Pistas:
  Usa aiohttp para realizar solicitudes HTTP de manera asíncrona.
    Usa asyncio para gestionar la concurrencia.  '''

    
import aiohttp
import asyncio

async def fetch_page(session, url):## descarga asincrona de la pagina
    async with session.get(url) as response:
        content = await response.text()
        filename = url.replace("https://", "").replace("/", "_") + ".html"
        # Abre el archivo en modo de escritura y guarda el contenido de la página
        with open(filename, 'w') as file:
            file.write(content)
        return filename

async def parallel_download(urls):
    async with aiohttp.ClientSession() as session:    # Crea una sesión de cliente aiohttp para gestionar las solicitudes
        tasks = [fetch_page(session, url) for url in urls] # crea lista de tareas
        return await asyncio.gather(*tasks)## ejecucion de tareas en pararlelo

urls = ["https://example.com", "https://example.org", "https://example.net"]
results = asyncio.run(parallel_download(urls))
print(results)
