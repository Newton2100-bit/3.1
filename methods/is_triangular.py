def is_triangular(n):
    """"
    n is an int returns true if n is triangula i.e equalssummation of natural numbers
    """
    total = 0
    for i in range(n+1):
        print(i)
        total += i
        if total == n:
            return True
    return False

print(f' we have 4 triangular {is_triangular(4)}')
print(f' we have 6 triangular {is_triangular(6)}')
print(f' we have 1 triangula {is_triangular(1)}')
