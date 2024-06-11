import threading

def thread_function(name):
    print(f"Thread {name} is running.")

thread = threading.Thread(target=thread_function, args=(1,))
thread.start()
thread.join()
