import threading
import time
import queue
import random

# 1. Thread-safe Queue for communication
print("=== Producer-Consumer Pattern ===")
task_queue = queue.Queue(maxsize=5)
result_queue = queue.Queue()

def producer(name):
    for i in range(5):
        task = f"Task-{i}-from-{name}"
        task_queue.put(task)
        print(f"Producer {name} added: {task}")
        time.sleep(random.uniform(0.1, 0.5))
    print(f"Producer {name} finished")

def consumer(name):
    while True:
        try:
            task = task_queue.get(timeout=2)
            print(f"Consumer {name} processing: {task}")
            time.sleep(random.uniform(0.2, 0.8))
            result = f"Processed-{task}"
            result_queue.put(result)
            task_queue.task_done()
        except queue.Empty:
            print(f"Consumer {name} timed out, stopping")
            break

# Start producers and consumers
producers = []
consumers = []

for i in range(2):
    p = threading.Thread(target=producer, args=(f"P{i}",))
    producers.append(p)
    p.start()

for i in range(3):
    c = threading.Thread(target=consumer, args=(f"C{i}",))
    consumers.append(c)
    c.start()

# Wait for all producers to finish
for p in producers:
    p.join()

# Wait for all tasks to be processed
task_queue.join()

# Get results
results = []
while not result_queue.empty():
    results.append(result_queue.get())

print(f"Processed {len(results)} tasks")

# 2. Thread Events for synchronization
print("\n=== Thread Events Example ===")
event = threading.Event()

def waiter(name):
    print(f"{name} waiting for event...")
    event.wait()
    print(f"{name} received event!")

def setter():
    time.sleep(2)
    print("Setting event...")
    event.set()

# Start waiter threads
waiters = []
for i in range(3):
    w = threading.Thread(target=waiter, args=(f"Waiter-{i}",))
    waiters.append(w)
    w.start()

# Start setter thread
setter_thread = threading.Thread(target=setter)
setter_thread.start()

# Wait for completion
for w in waiters:
    w.join()
setter_thread.join()

# 3. Thread Semaphore for resource limiting
print("\n=== Semaphore Example ===")
semaphore = threading.Semaphore(2)  # Only 2 threads can access resource

def access_resource(name):
    with semaphore:
        print(f"{name} acquired resource")
        time.sleep(2)
        print(f"{name} released resource")

# Start multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=access_resource, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# 4. Thread-local storage
print("\n=== Thread-Local Storage Example ===")
local_data = threading.local()

def process_data(name):
    # Each thread gets its own copy of this data
    local_data.value = f"Data for {name}"
    time.sleep(1)
    print(f"{name}: {local_data.value}")

threads = []
for i in range(3):
    t = threading.Thread(target=process_data, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# 5. Daemon threads
print("\n=== Daemon Threads Example ===")
def daemon_worker():
    while True:
        print("Daemon thread working...")
        time.sleep(1)

def regular_worker():
    for i in range(3):
        print(f"Regular worker: {i}")
        time.sleep(1)

# Regular thread
regular_thread = threading.Thread(target=regular_worker)
regular_thread.start()

# Daemon thread (will stop when main program ends)
daemon_thread = threading.Thread(target=daemon_worker)
daemon_thread.daemon = True
daemon_thread.start()

regular_thread.join()
print("Main program ending (daemon thread will stop automatically)")
