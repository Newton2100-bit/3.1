import random, time,timeit

start = time.perf_counter()
value = range(0,100,5)
print(f'The value returned by two is {value}')
print(f'As a list we have {'\n'}{list(value)}')
tm = time.process_time()
print(f'The process time of our proram is {tm:.4f}s')
tkn = time.thread_time()
end = time.perf_counter()
print(f'The main thread took {tkn:.4f}s')
print(f'The total wall clock time taken is {end - start:.4f}s')

