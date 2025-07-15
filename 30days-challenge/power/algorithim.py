def power(a, b):
    result = 1
    for i in range(b):
        result = result * a 
    return result 
while True:
    a = int(input('Enter your base value '))
    if a == 0:
        break
    b = int(input('Enter your exponent '))
    print('The output is',power(a,b))

    print('TESTING SOMETHING OUT')
    number = list(range(b))
    print(number)

