import threading
import time

lock = threading.Lock()
shared_counter = 0

def increment_with_timeout(thread_name, timeout_seconds):
    global shared_counter
    
    print(f"{thread_name}: Trying to acquire lock...")
    
    # This returns True if lock acquired, False if timeout
    if lock.acquire(timeout=timeout_seconds):
        print(f"{thread_name}: Got lock! Incrementing counter...")
        shared_counter += 1  # Changes ARE applied
        time.sleep(2)
        while True:
            pass
        # Simulate work
        lock.release()
        print(f"{thread_name}: Released lock. Counter is now {shared_counter}")
    else:
        print(f"{thread_name}: TIMEOUT! Could not get lock. Counter unchanged.")
        # Changes are NOT applied - thread continues without touching shared_counter
        print(f"{thread_name}: Continuing with other work...")

# Example usage
lock.acquire()  # Main thread holds the lock

# Start threads that will timeout
t1 = threading.Thread(target=increment_with_timeout, args=("Thread-1", -1))
t2 = threading.Thread(target=increment_with_timeout, args=("Thread-2", 10))

t1.start()
t2.start()

time.sleep(3)  # Let them timeout
lock.release()  # Release the lock

t1.join()
t2.join()

print(f"Final counter value: {shared_counter}")  # Will be 0 - no changes applied
