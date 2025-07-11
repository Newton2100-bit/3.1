import time

def timer(func):
    def wrapper():
        start = time.time()
        result= func()
        end= time.time()
        print(f'{func.__name__} took {end - start:.4f} secs')
        return result
    return wrapper

@timer
def slow_function():
    print('As the slow function i am executing btw!!')
    time.sleep(1)
    print('As the slow funct i am exiting now!!')

slow_function()
