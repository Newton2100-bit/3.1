import concurrent.futures
import time
import requests
import threading

# Example 1: Basic ThreadPoolExecutor
def worker_task(name, duration):
    print(f"Task {name} starting...")
    time.sleep(duration)
    print(f"Task {name} completed in {duration} seconds")
    return f"Result from {name}"

print("=== Basic ThreadPoolExecutor ===")
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks
    future1 = executor.submit(worker_task, "A", 1)
    future2 = executor.submit(worker_task, "B", 2)
    future3 = executor.submit(worker_task, "C", 1)
    
    # Get results
    print(f"Result 1: {future1.result()}")
    print(f"Result 2: {future2.result()}")
    print(f"Result 3: {future3.result()}")

# Example 2: Using map() for batch processing
def square_number(n):
    time.sleep(0.1)  # Simulate work
    return n * n

print("\n=== Using map() for Batch Processing ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(square_number, numbers))
    print(f"Squared numbers: {results}")

# Example 3: Handling exceptions
def risky_task(name):
    time.sleep(1)
    if name == "error":
        raise ValueError(f"Error in {name}")
    return f"Success from {name}"

print("\n=== Exception Handling ===")
tasks = ["task1", "error", "task3"]

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(risky_task, task) for task in tasks]
    
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            print(f"Success: {result}")
        except Exception as e:
            print(f"Error: {e}")

# Example 4: Web scraping with timeout
def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)
        return f"{url}: {response.status_code}"
    except Exception as e:
        return f"{url}: Error - {e}"

print("\n=== Web Scraping Example ===")
urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404"
]

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    # Submit all tasks
    futures = [executor.submit(fetch_url, url) for url in urls]
    
    # Process results as they complete
    for future in concurrent.futures.as_completed(futures, timeout=10):
        try:
            result = future.result()
            print(result)
        except Exception as e:
            print(f"Task failed: {e}")

# Example 5: Progress tracking
def long_running_task(task_id):
    steps = 5
    for i in range(steps):
        time.sleep(0.5)
        progress = (i + 1) / steps * 100
        print(f"Task {task_id}: {progress:.0f}% complete")
    return f"Task {task_id} finished"

print("\n=== Progress Tracking ===")
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    tasks = [executor.submit(long_running_task, i) for i in range(3)]
    
    for future in concurrent.futures.as_completed(tasks):
        result = future.result()
        print(f"Completed: {result}")

# Example 6: Context manager vs manual management
print("\n=== Manual Executor Management ===")
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

try:
    future = executor.submit(worker_task, "Manual", 1)
    result = future.result()
    print(f"Manual result: {result}")
finally:
    executor.shutdown(wait=True)  # Important: clean up resources

# Example 7: Combining with other synchronization
print("\n=== Combining with Lock ===")
lock = threading.Lock()
shared_counter = 0

def increment_counter(name):
    global shared_counter
    for i in range(1000):
        with lock:
            shared_counter += 1
    return f"{name} completed increments"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(increment_counter, f"Worker-{i}") for i in range(3)]
    
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)

print(f"Final counter value: {shared_counter}")

# Performance comparison
print("\n=== Performance Comparison ===")
import time

def cpu_bound_task(n):
    return sum(i*i for i in range(n))

def io_bound_task():
    time.sleep(0.1)
    return "IO task completed"

# CPU-bound tasks (not ideal for threading due to GIL)
start_time = time.time()
results = [cpu_bound_task(10000) for _ in range(4)]
sequential_time = time.time() - start_time

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_bound_task, [10000] * 4))
threaded_time = time.time() - start_time

print(f"CPU-bound sequential: {sequential_time:.2f}s")
print(f"CPU-bound threaded: {threaded_time:.2f}s")

# IO-bound tasks (ideal for threading)
start_time = time.time()
results = [io_bound_task() for _ in range(4)]
sequential_io_time = time.time() - start_time

start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(lambda x: io_bound_task(), range(4)))
threaded_io_time = time.time() - start_time

print(f"IO-bound sequential: {sequential_io_time:.2f}s")
print(f"IO-bound threaded: {threaded_io_time:.2f}s")
