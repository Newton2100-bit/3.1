import datetime, time, timeit

start1,start2, start3 = time.perf_counter(),time.process_time(), time.thread_time()
print(f'Our program started to execute at {time.ctime(time.time())}')
name: str =  input('Kindly enter your name ')
age: int = int(input(f'{name.capitalize()} kindly enter your age '))
print(f'Good morning to a {age} years ol dman named {name}, It was nice to meet you.')
print('We are leaving good bye 👋')
end1, end2, end3 = time.perf_counter(), time.process_time(), time.thread_time()
print(f'Took {end1 - start1:.3f}s')
print(f'The process time is {end2 - start2:.6f}s')
print(f'The Thread took {end3 - start3:.6f}s')
