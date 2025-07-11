import random

def random_power():
    def f(x):
        return f'{x} power 2 : {x ** 2}'
    def g(x):
        return f'{x} power 3 : {x ** 3}'
    def h(x):
        return f'{x} power 4 : {x ** 4}'
    functions = [f, g, h]
    return random.choice(functions)

for i in range(2,16):
    option = random_power()
    print(option(3))



# Methods call backs 
def function(f1, f2, data):
   # for i in range(3):
       # f1()
    return f1(f2(data))

print('The lenght of our string is ',end= ' ')
function(print,len,'My name is newton irungu')

