my_dict = {'a': 1, 'b': 2, 'c': 3}
print('This is my dictionary',my_dict)
values = my_dict.values()
print('This are the values',values)  # dict_values([1, 2, 3])

## Note that the output o fthe values() method isn't static but rather dynamic
print()
my_dict = {'x': 10, 'y': 20}
values = my_dict.values()
print(values)  # dict_values([10, 20])

my_dict['z'] = 30
print(values)  # dict_values([10, 20, 30]) - automatically updated!

##concert your output to a list to atatin static values
print()
my_dict = {'a': 1, 'b': 2, 'c': 3}
values_list = list(my_dict.values())
print(values_list)  # [1, 2, 3]


##Iterating over the output of the values method
print()
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
print('The original dictionary is ',scores)
for score in scores.values():
    print(f"Score: {score}")

## Usage with if statements
print()
print('Usage with if statement')
if 95 in scores.values():
    print("Someone got a 95!")

##USing it with the sum() method
print()
total = sum(scores.values())
average = sum(scores.values()) / len(scores)
max_score = max(scores.values())
print('The max score was',max_score,'\n','Then we have the total as',total,'\n','And finally we have the average as ',average)


