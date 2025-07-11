def evaluate_string_expression(expression):
    """
    Safely evaluate a string mathematical expression using eval().
    
    Args:
        expression (str): Mathematical expression as a string
        
    Returns:
        float/int: Result of the expression
        
    Example:
        >>> evaluate_string_expression("2 + 3 * 4")
        14
    """
    try:
        # Basic safety: only allow mathematical operations
        allowed_chars = set("0123456789+-*/.() ")
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Expression contains invalid characters")
        
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        return None


# Direct usage examples
print("Using eval() directly:")
print(eval("2 + 3 * 4"))        # 14
print(eval("10 / 2 + 5"))       # 10.0
print(eval("(2 + 3) * 4"))      # 20
print(eval("2 ** 3"))           # 8 (exponentiation)

print("\nUsing the safer wrapper function:")
print(evaluate_string_expression("2 + 3 * 4"))
print(evaluate_string_expression("10 / 2 + 5"))
print(evaluate_string_expression("(2 + 3) * 4"))

# Examples with variables (if needed)
print("\nUsing eval() with variables:")
x = 5
y = 3
print(eval("x + y * 2"))        # 11

# Alternative: using a dictionary for variables
variables = {"a": 10, "b": 20}
print(eval("a + b", {"__builtins__": {}}, variables))  # 30

# More complex expressions
print("\nComplex expressions:")
print(eval("sum([1, 2, 3, 4, 5])"))    # 15
print(eval("max(10, 20, 5)"))          # 20
print(eval("abs(-42)"))                # 42
