# import time
#
# start1, start2 = time.time(), time.perf_counter()
# my_list = [i for i in range(1000000)]
# print("LIST :",sum(my_list))
# end1, end2 = time.time(), time.perf_counter()
# print(f"\033[31mTIME:\033[0m {end1 - start1:.4f}")
# print(f"\033[31mPERF:\033[0m {end2 - start2:.4f}")
#
#
# start3, start4 = time.time(), time.perf_counter()
# my_list2 =(i for i in range(1000000))
# # print(my_list , end = " ")
# print('GENERATOR :',sum(my_list2))
# end3, end4 = time.time(), time.perf_counter()
# print(f"\033[31mTIME:\033[0m {end3 - start3:.4f}")
# print(f"\033[31mPERF:\033[0m {end4 - start4:.4f}")

# from collections import Counter 
# my_list = [10,10,30,40,10,20,30,10,40,30,20,30,10]
# count = Counter(my_list)
# # print(type(count))
# print(count.most_common(2))

# print(f"{U+1F34E}")
# print(chr(0x1F34E))
# print('\U0001F34E')
print(f'\033[31;1;4;4mTHIS IS ABOUT MURUGI\nMURUGI WEARS THE FOLLOWING.\033[0m')
for i in range(10):
    print(chr(0x1F459), end = ' ')
print()
