keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Create dictionary from two lists
print('Concept one ( singe person )')
print('List one :',keys)
print('List two :',values)
person = dict(zip(keys, values))
print('Resultant :',person)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Multiple people
print('Concept two ( multiple persons )')
names = ['Alice', 'Bob', 'Charlie']
print('List one :',names)
ages = [25, 30, 35]
print('List two :',ages)
people = {name: age for name, age in zip(names, ages)}
print('Resultant :',people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}
