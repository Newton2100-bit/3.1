from functools import wraps

def decorator(func):
    #@wraps(func)  # Preserves func's metadata
    def wrapper():
        """This is the final doc string"""
        print("Decorator is running!")
        return func()
    return wrapper

@decorator
def fun2():
    """This is fun2."""
    pass

print('This is the original function name',fun2.__name__)  # Output: 'fun2' (correct!)
print('This is the doc string',fun2.__doc__)   # Output: 'This is fun2.' (docstring preserved)
