def method_logger(func):
    def wrapper(self, *args, **kwargs):
        print(f"Calling {func.__name__} on {self.__class__.__name__}")
        result = func(self, *args, **kwargs)
        print(f"Finished {func.__name__}")
        a, b = args
       # print(f'a={a} and b={b}')
        print(f'{a} + {b} = {result}')
        return result
    return wrapper

class Calculator:
    @method_logger
    def add(self, a, b):
        return a + b
    
    @method_logger
    def multiply(self, a, b):
        return a * b

calc = Calculator()
result = calc.add(5, 3)
print('The sum of our values is',result)
# Output:
# Calling add on Calculator
# Finished add
