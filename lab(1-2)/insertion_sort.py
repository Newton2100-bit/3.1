import time 
import random
import datetime 
# from type import optional

def insertion_sort(data):

    length: int = len(data)

    for i in range(1, length):

        previous = i - 1 
        key = data[i]

        while previous >= 0 and data[previous] > key:
            data[previous + 1] = data[previous]
            previous -= 1
        data[previous + 1] = key

    return data


data0 = [17, 23, 2, 11, 5, 47, 41, 0, 6, 3]
print(f'unsorted list is {data0}')

sorted_data0 = insertion_sort(data0)
print(f'The sorted data is {sorted_data0}\n')

data1 = [12, 11, 13, 5, 6]
print(f'The unsorted list is {data1}')

sorted_data1 = insertion_sort(data1)
print(f'The sorted list is {sorted_data1}\n')

number = 4
for i in range(number):
    print(f'print the num is {i}')
