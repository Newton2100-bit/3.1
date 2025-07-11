# Mixing different iterable types
numbers = [1, 2, 3, 4]
letters = 'abcd'
boolean_values = (True, False, True, False)

for num, letter, boolean in zip(numbers, letters, boolean_values):
    print(f"{num} - {letter} - {boolean}")
# Output:
# 1 - a - True
# 2 - b - False
# 3 - c - True
# 4 - d - False
# All as a single list
our_list = zip(numbers, letters, boolean_values)
print(list(our_list))

for x in list(our_list):
    print(x)
