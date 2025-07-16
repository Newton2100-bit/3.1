def add(x, y):
    return x + y

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Can\'t divide by zero')
    return a / b
def main():
    value1 = add(10, 20)
    value2 = substract(10, 20)
    value3 = multiply(10, 20)
    value4 = divide(10, 20)

    print(f'we have our output as (10 and 20) :{"\n"}add = {value1} {"\n"}substract = {value2}')
    print(f'multiply = {value3}{"\n"}division = {value4}')

if __name__ == '__main__':
    main()
