def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('The output of our program')
            for _ in range(times):
                result = func(*args, **kwargs)
            print(result)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
