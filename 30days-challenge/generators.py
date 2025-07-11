import time

def counter():
    i = 0
    while i < 4:
        yield i
        i += 1

gen = counter()
#for i in range(4):
# print(next(gen))
#print(next(counter()))

#sample 2
#print('\n','\n')
def multiple_yield():
    print('Start')
    yield 1
    print('Between yields')
    yield 2
    print('End')

gen = multiple_yield()
for i in range(2):
    print(next(gen))
    time.sleep(5)

