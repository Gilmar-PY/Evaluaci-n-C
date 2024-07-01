from app import app
from app.routes import num_worker_threads, queue, threads

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    finally:
        for _ in range(num_worker_threads):
            queue.put((None, None, None, None))
        for t in threads:
            t.join()
