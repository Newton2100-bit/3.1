# zip stops at the shortest iterable
short_list = [1, 2, 3]
long_list = ['a', 'b', 'c', 'd', 'e']

# Print out original lists
print('\t','Original lists')
print(short_list,'\n',long_list,sep='')

# Printing the resulatant zip 
print('\t','Final list')
result = list(zip(short_list, long_list))
print(result)  # [(1, 'a'), (2, 'b'), (3, 'c')]
# Note: 'd' and 'e' are ignored
