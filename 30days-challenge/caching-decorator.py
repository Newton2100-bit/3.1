def cache_method(func):
    def wrapper(self, *args, **kwargs):
        # Create cache attribute if it doesn't exist
        if not hasattr(self, '_cache'):
            self._cache = {}
        
        # Create cache key
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        
        # Check cache
        if key in self._cache:
            print(f"Cache hit for {func.__name__}")
            return self._cache[key]
        
        # Calculate and cache result
        result = func(self, *args, **kwargs)
        self._cache[key] = result
        print(f"Cached result for {func.__name__}")
        return result
    return wrapper

class ExpensiveCalculator:
    @cache_method
    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n-1) + self.fibonacci(n-2)

calc = ExpensiveCalculator()
print(calc.fibonacci(10))  # Calculates and caches
print(calc.fibonacci(10))  # Returns from cache
