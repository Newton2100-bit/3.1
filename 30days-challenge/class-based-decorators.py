class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        value = self.func(*args, **kwargs)
        return value

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call #1 to say_hello
say_hello()  # Call #2 to say_hello
