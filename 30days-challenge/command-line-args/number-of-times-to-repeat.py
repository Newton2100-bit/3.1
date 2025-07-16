import sys

number = int(sys.argv[1])
count = 0
for i in range(number):
    count += i
    print('Hello world',end = ' ')

print(f'{"\n"}Total values to be output is {count}')
