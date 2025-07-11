from functools import wraps

def debug_metadata(func):
    @wraps(func)
    def wrapper():
        print(f"Metadata for {func.__name__}:")
        print(f"Module: {func.__module__}")
        print(f"File: {func.__code__.co_filename}")  # Actual file path
        return func()
    return wrapper

@debug_metadata
def example():
    """An example function."""
    pass

example()
