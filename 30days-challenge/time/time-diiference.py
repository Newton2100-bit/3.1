import time, datetime, subprocess 

start = time.perf_counter()
print(f'Started as {start:.4f}')

greentm = time.gmtime()
localtm = time.localtime()

print(f'The time in greenwitch is {time.asctime(greentm)}')
print(f'The time in local time is {time.asctime(localtm)}')

actual_time = time.time()
print(f'The actual local time is {time.ctime(actual_time)}')

print(f'Total seconds from epoch time is {actual_time:.4f}s')

endtime = time.perf_counter()
print(f'Ended at {endtime:.4f}')
print(f'It took {endtime - start:.4f}s')

print(f'The system ghas been up since')
subprocess.run(['uptime'])
print('This program is executing from the following path')
#subprocess.run(['ls','-al'])
subprocess.run(['pwd'])


