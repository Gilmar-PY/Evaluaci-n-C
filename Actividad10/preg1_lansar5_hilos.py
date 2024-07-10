import threading

def print_id(thread_id):
    for _ in range(10):
        print(f"Hilo {thread_id}")

threads = []
for i in range(5):
    thread = threading.Thread(target=print_id, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

