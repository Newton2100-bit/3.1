def is_even(number):
    return number%2 == 0


numbers = 45
print(f'is our value {numbers} an even number {is_even(numbers)}')

def add(x,y):
    return x+y

def mul(x,y):
    result = x * y
    print(f'the value of {x} * {y} is {result}')

num1 = 45
num2 = 89

print(f'The value of adding {num1} and {num2} is {add(num1,num2)}')
mul(num1,num2)
