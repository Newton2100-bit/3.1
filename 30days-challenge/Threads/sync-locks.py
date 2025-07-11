import threading
import time
import random

# Shared resource
counter = 0
lock = threading.Lock()

# Without lock (race condition)
def unsafe_increment(name):
    global counter
    for i in range(100000):
        temp = counter
        temp += 1
        counter = temp
    print(f"{name}: Final counter value = {counter}")

# With lock (thread-safe)
def safe_increment(name):
    global counter
    for i in range(100000):
        with lock:  # Context manager - automatically acquires and releases lock
            temp = counter
            temp += 1
            counter = temp
    print(f"{name}: Final counter value = {counter}")

# Alternative lock syntax
def safe_increment_manual(name):
    global counter
    for i in range(100000):
        lock.acquire()
        try:
            temp = counter
            temp += 1
            counter = temp
        finally:
            lock.release()
    print(f"{name}: Final counter value = {counter}")

# Demonstrate race condition
print("=== Race Condition Example (Unsafe) ===")
counter = 0
threads = []

for i in range(3):
    t = threading.Thread(target=unsafe_increment, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Expected: 300000, Got: {counter}")

# Demonstrate thread safety
print("\n=== Thread Safe Example (With Lock) ===")
counter = 0
threads = []

for i in range(3):
    t = threading.Thread(target=safe_increment, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Expected: 300000, Got: {counter}")

# Bank account example
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()
    
    def deposit(self, amount):
        with self.lock:
            current = self.balance
            time.sleep(0.001)  # Simulate processing time
            self.balance = current + amount
    
    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                current = self.balance
                time.sleep(0.001)  # Simulate processing time
                self.balance = current - amount
                return True
            return False
    
    def get_balance(self):
        with self.lock:
            return self.balance

# Test bank account
print("\n=== Bank Account Example ===")
account = BankAccount(1000)

def make_transactions(account, name):
    for i in range(10):
        if random.choice([True, False]):
            account.deposit(random.randint(1, 100))
        else:
            account.withdraw(random.randint(1, 50))
    print(f"{name} completed transactions")

threads = []
for i in range(3):
    t = threading.Thread(target=make_transactions, args=(account, f"Customer-{i}"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final balance: {account.get_balance()}")
