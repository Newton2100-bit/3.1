def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print("Error:", e)
else:
    print("Result:", result)  # Skipped due to exception
