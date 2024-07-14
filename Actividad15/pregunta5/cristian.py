import time

class CristianServer:
    def __init__(self):
        self.time = time.time()

    def get_time(self):
        return self.time

class CristianClient:
    def __init__(self, server):
        self.server = server
        self.time = time.time()

    def synchronize_clock(self):
        request_time = time.time()
        server_time = self.server.get_time()
        response_time = time.time()
        round_trip_time = response_time - request_time
        self.time = server_time + round_trip_time / 2

# Ejemplo de uso
server = CristianServer()
client = CristianClient(server)
client.synchronize_clock()
print(client.time)

