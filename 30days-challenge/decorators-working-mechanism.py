# Without decorator syntax
def greet():
    print("Hello World")

def add_greeting_decorator(func):
    def wrapper():
        print("--- Start ---")
        func()
        print("--- End ---")
        print()
    return wrapper

# Manual decoration
#decorated_greet = add_greeting_decorator(greet)
#decorated_greet()
greet = add_greeting_decorator(greet)
greet()


# With @ syntax (syntactic sugar)
@add_greeting_decorator
def greet_decorated():
    print("Hello World")

greet_decorated()  # Same result as above
