def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling")
        result = func(*args, **kwargs)
        print("After calling")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")


# The beast method 
#slow_function = timer(slow_function)
