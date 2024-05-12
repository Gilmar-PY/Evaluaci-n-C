import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()  # Parse JSON response

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true',
        'https://httpbin.org/delay/2'  # This endpoint introduce un delay de 2 segundos
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response)  

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

