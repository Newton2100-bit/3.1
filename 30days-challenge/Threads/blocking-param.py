import threading
import time

lock = threading.Lock()

def try_nonblocking():
    if lock.acquire(blocking=False):  # Don't wait
        print("Got lock immediately!")
        time.sleep(1)
        lock.release()
    else:
        print("Lock was busy, moving on...")

def try_blocking():
    print("Waiting for lock...")
    lock.acquire(blocking=True)  # Will wait
    print("Finally got the lock!")
    lock.release()
