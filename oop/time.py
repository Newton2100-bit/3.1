import time

now_epoch = time.time()
local_time = time.localtime(now_epoch)
print(f'The local time is {time.ctime(now_epoch)}')
#print(f'The equivalent epoch time is {time.ctime(now_epoch)}')
#print(f'The gmtime is {time.gmtime(now_epoch)}')
mk_local_time = time.ctime(time.mktime(local_time))
print(f'The local time is {mk_local_time}')
gm_time = time.ctime(time.mktime(time.gmtime(now_epoch)))
print(f'The gm method time is {gm_time}')
