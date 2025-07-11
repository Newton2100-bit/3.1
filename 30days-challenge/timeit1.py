import timeit

# Compare list creation methods
setup = "import random; data = [random.randint(1, 100) for _ in range(1000)]"

# Method 1: List comprehension
time1 = timeit.timeit(
    stmt="[x*2 for x in data]",
    setup=setup,
    number=10000
)

# Method 2: map()
time2 = timeit.timeit(
    stmt="list(map(lambda x: x*2, data))",
    setup=setup,
    number=10000
)

print(f"List comprehension: {time1:.4f}s")
print(f"Map function: {time2:.4f}s")
