import random

data = [i for i in range(2,100,random.randint(1,100) % 19)]
print('The lenth of our list is',len(data))
print(data)

def iterative_search(data, key):
    length= len(data)
    middle = length / 2
    low = 0

    if key == data[middle]:
        return f'found at the middle'
     elif key < data[middle]:
        iterative_search(data[middle:],key)
    else:
        iterative_search(data[:middle],key)

found = int(input('Enter the value you wanna search '))
print(iterative_search(data, found))




