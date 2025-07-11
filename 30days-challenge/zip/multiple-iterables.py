names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'London', 'Tokyo']

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, lives in {city}")
# Output:
# Alice, 25, lives in New York
# Bob, 30, lives in London
# Charlie, 35, lives in Tokyo

# Create list of tuples
combined = list(zip(names, ages, cities))
print('Raw zippped data','\n🤞\n',zip(names,ages,cities),'\n🤞')
print(combined)
# [('Alice', 25, 'New York'), ('Bob', 30, 'London'), ('Charlie', 35, 'Tokyo')]
