import random

print('________NO SEED HAS BEEN SET___________')
data = [i for i in range(2,100) if i % 3 == 0]
for i in data:
    print(f'Our random data is {random.randint(1,10)}')
print('______END OF OUR UNSEEDED PROGRAM__________')    
