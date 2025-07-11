import time 
start = time.perf_counter()
print("+" + "-" * 10 + "+" + "-" * 15 + "+")
print("| Header 1 | Header 2      |")
print("+" + "-" * 10 + "+" + "-" * 15 + "+")
time.sleep(34)
print(start)
end = time.perf_counter()
print(end)
time_taken = end - start
print(f'It took {time_taken:.4f}s to execute')

