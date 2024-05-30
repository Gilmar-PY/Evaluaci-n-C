#Ejercicio 7: Descarga paralela de páginas Web con aiohttp y asyncio

#Descripción: Implementa un sistema para descargar varias páginas web en paralelo utilizando aiohttp y asyncio.

#Tareas:

 #   Crear una lista de URLs.
  #  Usar aiohttp y asyncio para descargar las páginas web en paralelo.
   # Almacenar el contenido de cada página en un archivo separado.

#Pistas:

 #   Usa aiohttp para realizar solicitudes HTTP de manera asíncrona.
  #  Usa asyncio para gestionar la concurrencia.
import aiohttp
import asyncio

async def fetch_page(session, url):
    async with session.get(url) as response:
        content = await response.text()
        filename = url.replace("https://", "").replace("/", "_") + ".html"
        with open(filename, 'w') as file:
            file.write(content)
        return filename

async def parallel_download(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        return await asyncio.gather(*tasks)

urls = ["https://example.com", "https://example.org", "https://example.net"]
results = asyncio.run(parallel_download(urls))
print(results)
