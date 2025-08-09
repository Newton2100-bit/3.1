# def sum_digits(s: str) -> int:
#     total: int  = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val 
#         except:
#             raise ValueError('String contained a character')
#     return total
#
# input: str = input('Enter a string of digits with no delimeters.')
# total = sum_digits(input)
# print(f'The sum of our input is {total}.')


l1 = [4,5,6]
l2 = [1,0,3]

l3 = zip(l1,l2)
print(list(l3))
print('The type of our zip is ',type(l3))

for x,y in l3:
    print(x,':',y)
