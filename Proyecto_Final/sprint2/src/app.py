
from app import app, num_worker_threads, queue, threads  # Importa la aplicación y los hilos desde el paquete 'app'

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    finally:
        for _ in range(num_worker_threads):
            queue.put((None, None, None, None))
        for t in threads:
            t.join()
